---
layout: post
title: "The Full Picture: What the Simulation Tells Us"
description: "An agent-based model with 1,250 individual agents confirms the theoretical predictions — and reveals which policy regimes are most resilient when the breakthrough arrives."
date: 2026-03-09 00:00:00 +0530
tags: [game-theory, education, llm, ai-policy]
categories: llm-education
series: "LLM Impact on Education"
series_index: 4
math: true
giscus_comments: true
related_posts: true
---

> **Series: LLM Impact on Education** — [Post 0: Parent Guide](/blog/2026/llm-education-0-parent-guide/) · [Post 1: The Classroom Game](/blog/2026/llm-education-1-classroom-game/) · [Post 2: The Evolving Game](/blog/2026/llm-education-2-evolving-game/) · [Post 3: The Continuous Theory](/blog/2026/llm-education-3-continuous-theory/) · **[Post 4: The Full Picture](/blog/2026/llm-education-4-full-picture/)**

Everything we've built so far — the two-type model, the repeated game, the continuous theory — leads here.

[Post 1](/blog/2026/llm-education-1-classroom-game/) established the basic game: four players, their strategies, their payoffs, the Nash Equilibrium where nobody wants to deviate, and the 7% welfare loss from self-interest. [Post 2](/blog/2026/llm-education-2-evolving-game/) let the game run for 30 years, adding institutional inertia, a mid-game breakthrough shock, and the divergent trajectories of high-resource and low-resource populations. [Post 3](/blog/2026/llm-education-3-continuous-theory/) replaced the two-type assumption with a full spectrum of actor variation, discovered phase transitions and threshold effects, and showed how policy works as a lever on the distribution itself.

Each piece was analytically clean but incomplete. The equilibrium analysis assumed rational actors but ignored adaptation. The simulation assumed two types but ignored the full range of variation. The continuous theory captured the spectrum but remained largely static.

The agent-based model brings it all together.

---

## The Agent-Based Model

Instead of modeling "the government" and "the schools" as single actors with averaged-out strategies, the agent-based model populates the simulation with **hundreds of individual agents** — each with their own parameters, their own histories, and their own response functions.

- 200 parent agents, each with a resource level drawn from a beta distribution (calibrated to approximate real income distributions in OECD countries)
- 50 school agents, each with their own institutional culture parameter (inertia, risk tolerance, baseline pedagogy)
- A government agent that observes aggregate outcomes and adjusts policy in response to political pressure weighted by the parent distribution
- 1000 student agents, each assigned to a school and family, with delegation behavior that responds to the assessment environment their school creates and the supplementation their parents provide

The agents interact each simulation period (representing one academic year). Parents observe school quality and adjust supplementation. Schools observe regulatory environment and peer school behavior and adjust pedagogy and assessment. The government observes aggregate human capital and equity outcomes and adjusts regulation and subsidy. Students adjust delegation in response to assessment design and parental oversight.

This is a richer world than our earlier models. It's also harder to analyze cleanly. That's the point: the real world is messy, and we want to know whether the clean theoretical predictions survive in a messy environment.

---

## Confirming the Theoretical Predictions

The agent-based simulation broadly confirms the theoretical results from the earlier posts — but with important texture.

**The Price of Anarchy result holds but varies.** The aggregate welfare cost of self-interested play (relative to a coordinated social optimum) is approximately 5–9% across different calibrations, consistent with our theoretical estimate of 7%. But in scenarios with high population heterogeneity — where the variance of the parent resource distribution is high — the PoA can reach 12–13%. Heterogeneous populations have more trouble coordinating than homogeneous ones.

**Phase transitions are real.** The regulatory flip predicted by the continuous theory appears in the simulation. When the proportion of high-resource parents crosses approximately 0.50–0.58 (depending on the specific calibration), the government's equilibrium regulation drops discontinuously. This is not an artifact of the continuous theory — it emerges organically from hundreds of agents' individual political pressure and school adoption decisions.

**The school adoption cascade is visible.** In most simulation runs, adoption of AI tools in schools stays below 35–40% for the first 8–10 years, then accelerates sharply. The acceleration is triggered when a critical mass of school agents observes that peer schools with AI integration are achieving better outcome metrics. Below the threshold, each school's adoption decision is driven by its own calculation. Above the threshold, imitation becomes the dominant driver.

---

## The LLM Breakthrough in a Continuous Simulation

The breakthrough shock in the agent-based simulation is more complex than in the two-type model.

In the two-type model, the shock hits a stylized world and we can track which type does better. In the agent-based model, the shock hits 1,250 individual agents, each of whom responds differently based on their specific parameters. The results are striking:

**Which equilibria are resilient?** Not all pre-shock equilibria are equally fragile. Systems that had achieved high **assessment integrity** — where school assessment was genuinely diagnostic of learning rather than gameable by AI — prove more resilient to the shock. The logic: when assessment integrity is high, schools and students have accurate information about what is actually being learned. When the shock arrives and the definition of "what AI can do" expands, systems with high assessment integrity can quickly identify which skills are affected and adjust. Systems with low assessment integrity are operating with corrupted information and take much longer to re-equilibrate.

**The heterogeneity premium post-shock.** In the simulation, the populations that adapt fastest post-shock are those with high internal heterogeneity — a mix of early adopters and laggards among both parents and schools. The early adopters explore the new capability landscape quickly; the laggards observe and adopt what works. Fully homogeneous populations — everyone adopts at the same speed — explore the landscape less efficiently and arrive at the post-shock equilibrium more slowly.

**High-resource parents gain disproportionately from the shock, regardless of its nature.** This is the most robust result in the simulation. Whether the breakthrough makes AI dramatically better at instruction, at assessment, at content creation, or at tutoring — in every scenario, the gap between high-resource and low-resource student outcomes widens in the immediate post-shock period (years 1–4 after the shock). The mechanism is always the same: high-resource parents respond faster, supplement more aggressively with new tools, and absorb early-adoption costs that low-resource parents cannot afford.

---

## Policy Experiment Results

We run three policy regimes through the full agent-based simulation and compare outcomes across three dimensions: aggregate human capital (H), equity (E, measured as the inverse of the Gini coefficient of human capital outcomes), and credential signal integrity (S, how well credentials predict actual capability).

**Regime 1: High regulation + low subsidy**

Regulation $r = 0.75$, subsidy $s = 0.15$, teacher investment $t = 0.30$.

Outcome profile: moderate H (regulation slows adoption, moderating the average gains from AI tools), high E in the pre-shock period (restricted access means less supplementation gap), steep equity deterioration post-shock (low subsidy means low-resource families can't access the new tools, while high-resource families find workarounds to the regulation), moderate S (schools maintain assessment integrity under regulatory pressure, but cannot use AI tools to genuinely enhance diagnosis).

**Regime 2: Low regulation + high subsidy**

Regulation $r = 0.25$, subsidy $s = 0.70$, teacher investment $t = 0.45$.

Outcome profile: high H pre-shock (adoption is fast and broad), moderate E (subsidy narrows the gap but high-resource parents also supplement aggressively, so the gap doesn't close fully), lower S (without regulatory pressure, schools allow AI-gameable assessments to persist; the credential drifts from the underlying skill), high H post-shock (low regulation means the system can rapidly incorporate the new capability), equity largely determined by the subsidy level relative to the supplementation advantage.

**Regime 3: Moderate regulation + moderate subsidy + high teacher investment**

Regulation $r = 0.45$, subsidy $s = 0.45$, teacher investment $t = 0.75$.

Outcome profile: slightly lower H than Regime 2 (adoption is slower), better S than Regime 2 (teacher investment supports genuine assessment design rather than AI-gameable shortcuts), better equity than Regime 1 post-shock (subsidy is sufficient to provide some post-shock access), most resilient to the shock (teacher investment builds human capacity that the shock cannot immediately obsolete).

**No single policy dominates across all three outcome dimensions.**

This is the honest result. Regime 2 maximizes H. Regime 3 maximizes S and equity resilience. Regime 1 achieves moderate equity pre-shock but deteriorates sharply post-shock. The trade-off between aggregate performance, equity, and credential integrity is real and unavoidable. Governments must choose which outcome they weight most — and must live with the consequences for the other dimensions.

---

## What Governments Can Actually Do

The simulation clarifies what is and isn't in governments' control.

**Choose which outcome dimension to prioritize** — and be honest with the public that prioritizing one dimension has costs in others. A government promising high human capital AND high equity AND credential integrity from a single policy regime is either very lucky or not being truthful.

**Understand that the political payoff term shapes even welfare-motivated policy.** In the simulation, governments in high-$\pi_P$ jurisdictions (wealthy parent populations) tend to converge on low-regulation, moderate-subsidy regimes — not because this is optimal for aggregate welfare but because the political cost of restricting high-resource parents' AI access is higher than the political benefit of the equity gains from restriction. This is not corruption. It is the equilibrium of democratic institutions responding to the distribution of political pressure.

**Use phase transitions intentionally.** Near regulatory or equity tipping points, small policy changes have large effects. A government that understands where its jurisdiction sits relative to these tipping points can achieve large systemic effects with targeted, modest interventions. A government ignoring these tipping points may spend large resources achieving small effects in the wrong region of the parameter space.

**Invest in teacher capacity early, before shocks arrive.** The simulation shows that the regimes that weather the breakthrough shock best are those that invested heavily in teacher training and assessment design in the pre-shock period. This investment looks inefficient when things are stable — why train teachers for a tool landscape that might be obsolete in 18 months? — but is what determines post-shock resilience.

---

## The Series Closer

The breakthrough hasn't happened yet. When it does, which equilibrium will your society be in?

The answer depends on choices being made right now — by governments deciding whether to invest in teacher training or just regulate AI access, by schools deciding whether to design genuinely diagnostic assessments or let the credential drift, by parents deciding how to supplement and what skills they're actually investing in, and occasionally, by students themselves who choose to develop genuine judgment rather than optimized output.

The game doesn't wait for the players to understand it. It runs regardless.

What we've tried to do in this series is make the game visible — its structure, its players, its equilibria, its phase transitions, and its resilience properties. Not to prescribe an outcome, but to show the map of possibilities clearly enough that people navigating it can do so consciously.

The breakthrough is coming. The question is what we'll have built before it arrives.

---

*How this series was made: The questions driving this research, the editorial judgment, and the final decisions about what to include or exclude are human. The analysis, modeling, writing, and simulation code are largely AI-generated, guided by human prompts and reviewed by human editors. This series is itself an experiment in human-AI collaboration.*
