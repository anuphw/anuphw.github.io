---
layout: post
title: "All You Need Is, Attention!"
description: "On when attention is the right tool — and when it isn't"
date: 2026-02-25 00:00:00 +0530
tags: [attention, transformers, multimodal, deep-learning]
categories: machine-learning
math: true
giscus_comments: true
---

{% include figure.liquid path="/assets/img/posts/attention-hero.png" alt="Two feature sets of different shapes connected by dynamic lines of light" class="img-fluid" %}

The title is borrowed, obviously. But the argument here is not about transformers replacing everything. It is about a narrower and more useful question: **when is attention the right tool?**

Not always. But there is one class of problems where it is almost always the right answer — when you have two sets of features with different shapes that need to share information with each other. This post is about that class of problems.

---

## The Problem

Suppose you are building a model that takes an image and a question about it, and produces an answer. You run the image through a CNN backbone and get a grid of feature vectors. You embed the question tokens and get a sequence of vectors. Now you need these two representations to inform each other — the image features need to know what the question is asking, and the question tokens need to know where to look in the image.

The trouble is that these two feature sets look nothing alike:

- Image features: 49 spatial patches, each with a 512-dimensional vector → shape `(49 × 512)`
- Question tokens: 12 word embeddings, each with a 256-dimensional vector → shape `(12 × 256)`

Different number of elements. Different dimensionality. No natural alignment between them.

How do you get them to talk to each other?

---

## The Obvious Approaches, and Their Shortcomings

Three approaches come to mind immediately.

**Pad and concatenate.** Pad the shorter sequence to match the length of the longer one, then concatenate along the feature dimension. This forces a positional alignment that does not exist — image patch 7 has no inherent relationship to question token 7. The padding is also meaningless signal that the model has to learn to ignore.

**Global pooling.** Collapse each feature set into a single fixed-size vector using average or max pooling, then concatenate or add them. This is simple and it works up to a point. But a single vector cannot represent which parts of the image are relevant to which parts of the question. You have discarded all spatial and sequential structure in the process of making the shapes compatible.

**Linear projection.** Project both feature sets into a shared dimension, then combine with addition or elementwise multiplication. Better — but the projection weights are fixed after training. They do not adapt based on what the inputs actually are. A projection learned for questions about color is the same projection used for questions about location.

{% include figure.liquid path="/assets/img/posts/attention-static-bridges.png" alt="The three failing approaches — pad and concat, global pooling, linear projection" class="img-fluid" %}

The failure mode all three share is the same: **the bridge between the two feature sets is static.** It is decided at training time and does not change based on the content of the inputs at inference time.

---

## What Attention Does Differently

Attention builds a dynamic bridge. The key idea, stated in one line:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V$$

The dynamism lives in $$QK^T$$ — a matrix of dot products between actual input vectors at inference time, not learned parameters. The weights that determine how much each image patch contributes to each question token are recomputed fresh for every new image-question pair. That is what makes this different from a projection. What matters here is what it does to the shapes.

Take the image-question example from above. Using cross-attention:

- Project question tokens into queries: $$Q$$ of shape `(12 × 64)`
- Project image patches into keys and values: $$K$$ of shape `(49 × 64)`, $$V$$ of shape `(49 × 64)`
- Compute $$QK^T$$: shape `(12 × 49)` — each of the 12 question tokens gets a score over each of the 49 image patches
- After softmax and multiplying by $$V$$: output shape `(12 × 64)` — same structure as the query, but now each token carries information drawn from the image patches it found most relevant

{% include figure.liquid path="/assets/img/posts/attention-matrix-shapes.png" alt="Matrix shape transformation through Q, K, V" class="img-fluid" %}

The output has the same shape as the thing asking the questions, regardless of the shape of what it is querying. The image had 49 elements; the question had 12; the output has 12 — because the question is in the driver's seat. It gets to decide, based on its own content, how much of each image patch to pull in.

This is what none of the three approaches above can do.

---

## When This Actually Matters

The image-question example is a special case of a more general pattern. Here are four situations where that pattern appears, along with the models that exploited it.

{% include figure.liquid path="/assets/img/posts/attention-use-cases.png" alt="Four use cases of attention" class="img-fluid" %}

### Variable-Length Sequences

This is the degenerate case of the pattern — self-attention, where queries and keys come from the same sequence. There is only one feature set, and it attends to itself. The "two sets with different shapes" framing still applies, just with both sets being the same sequence at the same step.

You have a sequence of arbitrary length — a sentence, an audio clip, a time series — and you need each element to gather context from every other element. RNNs do this by passing a fixed-size hidden state forward one step at a time; by step 100, whatever was at step 1 has been compressed through 99 nonlinearities. Long-range dependencies are difficult to preserve.

Attention has no concept of distance. Every token computes relevance scores against every other token in a single step, and those scores are derived from content, not position.

**[BERT](https://github.com/google-research/bert)** (Devlin et al., 2019) made this the foundation of language understanding — bidirectional self-attention over the full sequence, allowing every token to be influenced by every other token simultaneously. **[Wav2Vec 2.0](https://arxiv.org/abs/2006.11477)** (Baevski et al., 2020) applied the same idea to raw audio, where the "sequence" is a stream of audio frames of arbitrary length.

### Cross-Modal Fusion

This is the image-question case generalized. Two modalities — image and text, audio and video, sensor readings and language instructions — each with its own structure, needing to inform each other.

Projecting each modality to a shared space and adding them loses the relational structure between them. A model that can ask "which image regions are most relevant to this specific word?" cannot be built with a fixed projection — it needs attention.

**[CLIP](https://github.com/openai/CLIP)** (Radford et al., 2021) learns a joint embedding space for images and text using contrastive learning, with attention operating within each modality. **[Flamingo](https://arxiv.org/abs/2204.14198)** (Alayrac et al., 2022) goes further, interleaving cross-attention layers that let language tokens directly attend to visual features at multiple scales. **[DALL-E 2](https://arxiv.org/abs/2204.05862)** and the family of diffusion models use cross-attention to condition image generation on text embeddings, where each spatial region of the image attends to the text tokens that are relevant to it.

### Irregular Spatial Structures

CNNs are built around grids. Every convolution assumes that neighboring pixels are spatially close and that the input has a fixed, regular structure. This assumption breaks down for graphs, point clouds, and molecules — structures where the number of neighbors is variable and there is no canonical ordering of elements.

In a graph, a node needs to aggregate information from its neighbors, but different nodes have different numbers of neighbors. A point cloud representing a 3D object has no fixed spatial grid — the number of points varies, and there is no notion of "the pixel to the right."

Attention handles this naturally. Given a set of elements and a way to compute pairwise relevance, it can aggregate information across any set of neighbors without requiring a fixed structure.

**[Graph Attention Networks](https://github.com/PetarV-/GAT)** (Veličković et al., 2018) apply attention over graph neighborhoods — each node attends to its neighbors, with learned weights that depend on the content of both the node and its neighbor, not just the graph topology. **[AlphaFold2](https://github.com/google-deepmind/alphafold)** (Jumper et al., 2021) uses a form of attention operating over pairs of amino acid residues to propagate structural constraints through a protein's contact map, a structure that has no fixed spatial grid.

### Dynamic Feature Relationships

In standard detection and segmentation pipelines, the features used to recognize an object are determined by the architecture — a specific region proposal, a fixed anchor, a particular feature pyramid level. These are reasonable heuristics, but they are fixed.

Cross-attention allows the model to dynamically route information based on content. A query representing "the object I am trying to detect" can attend over the full feature map and pull in exactly the regions that are relevant — without the model needing to know in advance where those regions will be.

**[DETR](https://github.com/facebookresearch/detr)** (Carion et al., 2020) replaced the traditional detection pipeline with a set of learned object queries, each attending over the full image feature map to find the object it is responsible for. There are no anchors, no non-maximum suppression — the attention mechanism handles the assignment. In [diffusion-based image generation models](https://github.com/CompVis/latent-diffusion) (Rombach et al., 2022), each spatial position in the noisy image attends to text condition tokens at every denoising step, dynamically adjusting which text tokens it draws from as the image structure emerges.

---

## The Unifying Principle

Across all four cases, the same structure appears: two sets of features, different shapes, needing to exchange information in a way that depends on the content of both.

The common thread is that **the routing of information is itself a function of the data.** Which image patches are relevant to a question token depends on the question. Which graph neighbors should dominate depends on the node's features. Which text tokens should influence a spatial position in a generated image depends on what is being generated there.

When that condition holds — when you cannot decide at training time how information should flow between two feature sets, because it depends on what the inputs actually are — attention is the right tool.

The alternative approaches all assume the routing can be fixed. Attention does not.

---

## When It Is Not Worth It

Dynamic routing has a cost. The $$QK^T$$ matrix has shape $$(n \times m)$$ where $$n$$ and $$m$$ are the sizes of the two feature sets. Memory and compute scale quadratically with sequence length, which means full cross-attention becomes prohibitive when both sets are large — a high-resolution image feature map attended to by a long document, for instance.

In practice, this is why most large-scale systems that use cross-attention introduce some form of approximation: pooling the queries down before attending, using sparse attention patterns, or chunking the sequence. The full dynamic bridge is expensive; the question is always whether the routing actually needs to be that dynamic, or whether a cheaper approximation captures most of the benefit.

If the relationship between two feature sets is mostly stable across inputs — the same parts of the image are almost always relevant regardless of the question — a fixed projection might close most of the gap at a fraction of the cost. Attention is the right default when you do not know that in advance.
