---
layout: post
title: "The Continuous Theory: When Populations Exist on a Spectrum"
description: "Replacing the two-type model with beta distributions reveals phase transitions, threshold effects, and a surprising principle for where policy intervention has the most leverage."
date: 2026-03-09 00:00:00 +0530
tags: [game-theory, education, llm, ai-policy]
categories: llm-education
series: "LLM Impact on Education"
series_index: 3
math: true
giscus_comments: true
related_posts: true
---

> **Series: LLM Impact on Education** — [Post 0: Parent Guide](/blog/2026/llm-education-0-parent-guide/) · [Post 1: The Classroom Game](/blog/2026/llm-education-1-classroom-game/) · [Post 2: The Evolving Game](/blog/2026/llm-education-2-evolving-game/) · **[Post 3: The Continuous Theory](/blog/2026/llm-education-3-continuous-theory/)** · [Post 4: The Full Picture](/blog/2026/llm-education-4-full-picture/)

When we model the world as binary — two types of parents, two types of schools — we're making a useful simplification. Useful, because it makes the math tractable and the intuitions clear. But a simplification nonetheless.

Real populations are not bimodal. Parents aren't "high-resource" or "low-resource" — they're spread across a continuous distribution of incomes, educational attainment, access to social capital, time, and willingness to engage with AI tools. Schools aren't "progressive adopters" or "conservative laggards" — they're distributed across a spectrum of institutional cultures, leadership philosophies, and resource constraints. Government officials aren't purely equity-focused or purely efficiency-focused — they're balancing shifting coalitions with shifting priorities.

What happens to our model when we relax the two-type assumption?

---

## Beta Distributions: A Flexible Tool for Real Populations

The mathematical tool we reach for is the **beta distribution** — a flexible family of distributions defined on the interval [0,1], making it natural for modeling proportions, probabilities, and continuous parameters that live between two extremes.

The beta distribution is parameterized by two shape parameters, $\alpha$ and $\beta$:

- When $\alpha = \beta = 1$, you get a uniform distribution: every value between 0 and 1 is equally likely.
- When $\alpha > \beta$, the distribution skews toward 1 — most of the population is toward the high end.
- When $\alpha < \beta$, it skews toward 0.
- When both $\alpha$ and $\beta$ are large, the distribution concentrates — most of the population is near the mean, with little spread.
- When both are small (less than 1), the distribution is U-shaped — the population is polarized toward the extremes.

Why does this matter? Because the shape of the parent population distribution — not just its mean — changes the equilibrium the system reaches.

A society where parents are mostly clustered near the middle (high $\alpha$ and $\beta$, similar values) behaves differently from a society where parents are polarized between a high-resource elite and a low-resource majority (U-shaped beta), even if the two societies have the same average resource level. Policy designed for one will misfire in the other.

---

## From Equilibrium Points to Equilibrium Correspondences

In the two-type model, we asked: "What is THE equilibrium?" A specific set of strategies that nobody wants to deviate from.

In the continuous model, we ask a different question: "How does equilibrium shift as the population distribution shifts?" This is an **equilibrium correspondence** — a mapping from population parameters to equilibrium outcomes.

Let $\pi_P$ parameterize the parent resource distribution (think of it as the mean of the beta distribution, with shape parameters capturing the spread). As $\pi_P$ varies:

**Government regulation ($r^*$):** As $\pi_P$ increases (more high-resource parents), optimal government regulation drifts lower. High-resource parents are more comfortable with AI tools, more likely to provide oversight at home, and less dependent on school-provided guardrails. They also exert more political pressure, and their pressure is in the direction of access rather than restriction. The result: districts and countries with wealthier parent populations tend toward lower AI regulation, not because regulation is worse for them but because the political equilibrium supports lower regulation.

**Government subsidy ($s^*$):** More surprisingly, subsidy is non-monotone in $\pi_P$. Low $\pi_P$ → high subsidy demand (equity pressure is high). Medium $\pi_P$ → subsidy pressure is lower (enough private supplementation that public pressure eases). High $\pi_P$ → subsidy may increase again, but now oriented toward capability amplification rather than equity catch-up. The shape of the distribution matters: a more polarized (U-shaped) parent population produces more extreme swings in subsidy pressure than a concentrated distribution with the same mean.

**School pedagogy adoption ($p^*$):** School adoption of AI tools increases with $\pi_P$, but not linearly. There's a threshold effect: below a critical proportion of engaged, high-resource parents (~0.35 in our calibration), schools face little pressure to adopt and do so slowly. Above that threshold, parental pressure becomes a significant driver. This threshold behavior is important because it means moderate increases in the high-resource parent proportion can produce large changes in school behavior.

---

## Phase Transitions: When Small Changes Have Large Effects

This threshold behavior in school adoption is an example of a **phase transition** — a point where the system's behavior changes qualitatively, not just quantitatively.

Think of water at 99°C versus water at 101°C. These temperatures are close. The change in temperature is small. But the state of the water is fundamentally different: liquid versus gas. The physics near the transition point is different from the physics far from it.

Education systems have analogous transition points:

**The regulatory flip.** In our model, there is a critical $\pi_P$ value (~0.55 in the baseline calibration) above which the government's equilibrium regulation drops sharply — from moderate-to-high restriction to moderate-to-low restriction. Below this point, the political coalition favoring restriction is larger than the coalition favoring access; above it, the balance reverses. A jurisdiction hovering near this threshold will be politically volatile: small demographic shifts produce large policy swings.

**The equity tipping point.** There is a critical subsidy level below which equity gaps compound (high-resource parents' advantage grows faster than subsidies compensate) and above which equity gaps narrow. Near this tipping point, small changes in subsidy produce large changes in equity trajectory. The implication: trying to save money near the equity tipping point by reducing subsidy slightly can trigger a much larger equity deterioration than the cost saving justifies.

**The school adoption cascade.** When school adoption of AI tools crosses approximately 40% of schools in a district, the remaining schools face qualitatively different pressure: their students are now visibly behind students from AI-integrated schools in ways that are hard to ignore. This creates cascade dynamics: adoption accelerates once it reaches the threshold, not because conditions changed but because adoption itself changed conditions.

Phase transitions have a property that makes them particularly important for policy: **small changes in policy near the transition point have large effects; the same changes far from the transition point have small effects.** This means the leverage of policy is highly non-uniform. A subsidy increase that does little in a high-π_P jurisdiction may be transformative in a jurisdiction hovering near the equity tipping point.

---

## Government Policy as a Lever on the Distribution

Here's the key insight from the continuous model: **government policy doesn't just change outcomes directly — it changes the effective distribution of the parent population, which changes the equilibrium the system settles into.**

A subsidy program doesn't just give low-resource families money. It shifts *their effective position* in the resource distribution. A family that was at the 20th percentile of resource access, effectively a low-resource family for all strategic purposes, may move to the 45th percentile with subsidy. This doesn't just help that family — it changes the shape of the distribution, potentially moving the system closer to (or further from) a phase transition.

Formally: a subsidy $s$ applied to the lower tail of the parent resource distribution transforms the effective beta distribution from $\text{Beta}(\alpha, \beta)$ to $\text{Beta}(\alpha', \beta')$ with the same mean but lower variance and less weight in the lower tail. This transformed distribution may sit on the other side of a regulatory or equity tipping point.

The policy implication is subtle but important: **it may be more effective to design policy based on where in the distribution subsidy achieves the most impact (near phase transitions) rather than where need is highest (the very bottom).** This is counterintuitive — it says don't just help the most disadvantaged, help the people who are on the edge of a threshold. But it's what the mathematics implies if the goal is to shift which equilibrium the entire system inhabits, not just to improve outcomes for specific individuals.

This is not an argument against helping the most disadvantaged. It is an argument for thinking about population-level equilibrium effects alongside individual-level outcome effects when designing policy.

---

## The Limits of Theory

The continuous model is richer than the two-type model. It captures threshold effects, phase transitions, and the policy implications of distribution shape rather than just distribution mean. It also makes stronger demands on the data: calibrating a beta distribution requires more information than categorizing parents as high or low resource.

More importantly: the continuous model is still a model. It makes assumptions about how actors behave, what they maximize, and how they respond to each other. These assumptions are reasonable and defended — but they are not facts.

The hardest question is empirical: do real education systems actually exhibit the phase transitions and threshold effects the model predicts? Do we see the regulatory flip at high $\pi_P$ values? Do we see the school adoption cascade?

Answering these questions requires not just theory but simulation — running thousands of agents through these dynamics and seeing whether the aggregate behavior matches the theoretical predictions.

[Post 4: The Full Picture — running the simulation with thousands of agents](/blog/2026/llm-education-4-full-picture/)

---

*How this series was made: The questions driving this research, the editorial judgment, and the final decisions about what to include or exclude are human. The analysis, modeling, writing, and simulation code are largely AI-generated, guided by human prompts and reviewed by human editors. This series is itself an experiment in human-AI collaboration.*
