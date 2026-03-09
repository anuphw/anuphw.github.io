---
layout: post
title: "The Classroom Game: A Game-Theoretic Model of AI in Education"
description: "A formal four-player game model showing why every country is having the same confused AI-in-schools debate — and what the Nash Equilibrium looks like."
date: 2026-03-09 00:00:00 +0530
tags: [game-theory, education, llm, ai-policy]
categories: llm-education
series: "LLM Impact on Education"
series_index: 1
math: true
giscus_comments: true
related_posts: true
---

> **Series: LLM Impact on Education** — [Post 0: Parent Guide](/blog/2026/llm-education-0-parent-guide/) · **[Post 1: The Classroom Game](/blog/2026/llm-education-1-classroom-game/)** · [Post 2: The Evolving Game](/blog/2026/llm-education-2-evolving-game/) · [Post 3: The Continuous Theory](/blog/2026/llm-education-3-continuous-theory/) · [Post 4: The Full Picture](/blog/2026/llm-education-4-full-picture/)

Why does every country seem to be having the same confused debate about AI in schools at the same time? The United States is banning, then unbanning, then cautiously re-banning phones and AI tools. The UK is commissioning reports. Singapore is building AI literacy into its national curriculum. France is worried about equity. Each country has its own context, its own politics, its own educational culture — and yet the structure of the debate is almost identical everywhere.

That's a signal. When the same argument recurs across wildly different contexts, it usually means the argument is driven by the structure of the situation, not by local idiosyncrasies. Game theory is the tool we use to understand the structure of situations.

---

## The Game-Theoretic Lens

Think of this as a game with four players: government, schools, parents, and students. Each player has goals. Each player makes choices. And each player's choices affect everyone else's outcomes.

This is not a metaphor. It is a formal claim: the confusion and contradiction you see in AI education policy is exactly what you'd predict from a multi-player game where each actor is rationally pursuing their own interests in an environment where the rules are still being written.

Let's meet the players and their choices.

---

## The Actors and Their Strategies

### Government

Government sets three key parameters:

- **Regulation** ($r \in [0,1]$): How tightly it controls AI use in schools. Zero means anything goes; one means complete prohibition.
- **Subsidy** ($s \in [0,1]$): How much public funding flows to AI infrastructure and access programs.
- **Teacher investment** ($t \in [0,1]$): How much it invests in training teachers to work effectively with AI tools.

These three levers interact. High regulation without high teacher investment just means schools struggle to comply. High subsidy without regulation might accelerate inequality rather than reduce it, as schools that are already well-resourced use the funds most effectively.

### Schools

Schools make three key choices:

- **Pedagogy** ($p$): How much they integrate AI tools into actual instruction versus treating AI as an out-of-school phenomenon to be managed.
- **Assessment** ($a$): Whether assessments are designed to detect and reward genuine learning, or whether they can be gamed with AI assistance.
- **Resource split** ($\rho$): How they allocate resources between AI infrastructure and traditional instruction.

Schools face a genuine dilemma. An assessment system that AI can defeat is a system that's providing false signals about whether students are learning. But changing assessment is expensive, politically fraught, and requires teacher retraining. Many schools rationally choose to lag.

### Parents

Parents make two key choices:

- **Supplementation** ($x$): How much they invest in additional AI tools, tutoring, or educational resources outside what school provides.
- **Credential signaling** ($\sigma$): Which credentials they push their child toward — and whether they believe the credential actually reflects the underlying skill.

High-resource parents can supplement aggressively. This matters because it means the overall distribution of educational AI access is determined not just by policy but by the private decisions of thousands of households.

### Students

Students' key variable is **delegation** ($e$): how much of their cognitive work they delegate to AI versus doing themselves.

Here's the uncomfortable truth: *e* is mostly determined by the environment everyone else creates. A student who over-delegates isn't necessarily lazy — they may be rationally responding to an assessment system that doesn't distinguish between their work and AI's work, a parent who is satisfied with output rather than learning, and a school that hasn't thought hard about where the line should be. The minority of students who actively choose a different path despite their environment — who develop genuine curiosity and judgment regardless of incentives — are real, but they're the exception.

---

## What Each Actor Is Trying to Maximize

### Student Payoff

A student accumulates skill from effort — the harder problems they genuinely wrestle with, the more they develop. They also benefit from AI assistance, which lets them access explanations and feedback they wouldn't otherwise have. But over-delegation creates **atrophy** — the more cognitive work is outsourced, the less the underlying capacity develops.

$$U_S = \alpha \cdot H(e, \text{LLM}) - \beta \cdot D(e) + \gamma \cdot C$$

Where $H$ is human capital accumulation, $D$ is the atrophy penalty from over-delegation, and $C$ is the credential value. $\alpha$, $\beta$, $\gamma$ are weights reflecting how much each matters to the student's situation.

In plain English: there's a trade-off between getting things done with AI and actually developing the capacity to do them yourself. The optimal point depends on what the student is trying to become.

### Parent Payoff

Parents care about two things: their child's actual human capital (will they be capable?) and the credential signal (will it be recognized?). They pay costs to supplement.

$$U_P = w_H \cdot H - w_S \cdot x + v \cdot \sigma(\text{credentials})$$

Where $x$ is supplementation cost and $\sigma$ captures how much the credential is expected to signal in the future labor market. The problem is that w_H and σ may diverge — a credential might become a weaker signal of actual capability if AI has made it easier to obtain. Parents betting on credential value alone may be optimizing for the wrong thing.

### School Payoff

Schools want reputation (which depends on measurable outcomes), compliance (which protects them from regulatory risk), and efficiency (which keeps them solvent). They pay costs when teachers leave — and teachers leave at higher rates when institutions change rapidly without adequate support.

$$U_{Sc} = \lambda_R \cdot \text{Reputation} - \lambda_T \cdot \text{TeacherAttrition} + \lambda_C \cdot \text{Compliance} - \lambda_E \cdot \text{ResourceCost}$$

This explains why schools tend toward conservative adoption: the downside risks (teacher attrition, reputational damage from a policy that backfires) are immediate and concrete, while the upside (better learning outcomes from AI integration) is diffuse and delayed.

### Government Payoff

Governments care about aggregate outcomes (the average skill level of the population they're governing), equity (the distribution of those outcomes, not just the mean), and fiscal sustainability. They also respond to political pressure — the **political payoff** term.

$$U_G = \mu_A \cdot \text{AggregateH} + \mu_E \cdot \text{Equity} - \mu_F \cdot \text{FiscalCost} + \mu_P \cdot \text{PoliticalPayoff}$$

The political payoff term is not a corruption of governance — it's a recognition that democratic governments respond to what voters want. And what voters want from education policy is often contradictory: more AI, but safer; better outcomes, but cheaper; more equity, but no new taxes.

---

## Nash Equilibrium: Where Everyone Stops Changing

A Nash Equilibrium is the point where nobody wants to change their strategy unilaterally — given what everyone else is doing, each player is already playing their best response.

In this model, we can characterize the Nash Equilibrium as a set of choices $(r^*, s^*, t^*, p^*, a^*, x^*, e^*)$ where each actor is best-responding to the others. A key result:

**The Price of Anarchy (PoA) ≈ 1.07**

The Price of Anarchy measures how much welfare society loses because each actor pursues self-interest rather than coordinating on a social optimum. A PoA of 1.07 means the Nash Equilibrium produces about 7% less aggregate welfare than the socially optimal outcome everyone could achieve with perfect coordination.

That 7% gap doesn't sound dramatic. But compounded over a generation of students, across an entire national education system, the gap between "each actor rationally pursuing their interest" and "a well-coordinated system" is substantial.

---

## What Government Policy Can Do

The gap between Nash Equilibrium and social optimum is not fixed. Government policy is precisely the mechanism by which societies try to close it.

Regulation shapes the feasible strategy space — it changes what schools and students can do. Subsidies change the cost-benefit calculation for schools and parents. Teacher investment changes what schools can actually implement rather than just what they're permitted to do.

The formal result: a well-designed policy triplet $(r, s, t)$ can move the system from its $\text{PoA} \approx 1.07$ equilibrium toward the social optimum. The challenge is that governments are themselves players in the game — the political payoff term means even well-intentioned policy is shaped by electoral incentives.

This is not cynicism. It is the structure of the problem.

---

## What Comes Next

We've just found equilibrium assuming everyone plays rationally once. But real institutions don't choose once and lock in — they observe what others do, update their beliefs, and adjust. A government that sees high-resource parents massively supplementing will update its equity calculus. A school that sees peer institutions successfully integrating AI will update its adoption strategy.

What happens when we let the game run for 30 years, with actors learning and adapting along the way? And what happens when, partway through that 30-year window, AI has a breakthrough that makes today's equilibrium obsolete?

The stable world we just described might not stay stable for long.

[Post 2: The Evolving Game — what happens when the game runs for 30 years](/blog/2026/llm-education-2-evolving-game/)

---

*How this series was made: The questions driving this research, the editorial judgment, and the final decisions about what to include or exclude are human. The analysis, modeling, writing, and simulation code are largely AI-generated, guided by human prompts and reviewed by human editors. This series is itself an experiment in human-AI collaboration.*
