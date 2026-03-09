---
layout: post
title: "The Evolving Game: 30 Years of AI Education Dynamics"
description: "What happens when the AI education game runs for 30 years — institutional inertia, a mid-game breakthrough shock, and diverging trajectories for high- and low-resource families."
date: 2026-03-09 00:00:00 +0530
tags: [game-theory, education, llm, ai-policy]
categories: llm-education
series: "LLM Impact on Education"
series_index: 2
math: true
giscus_comments: true
related_posts: true
---

> **Series: LLM Impact on Education** — [Post 0: Parent Guide](/blog/2026/llm-education-0-parent-guide/) · [Post 1: The Classroom Game](/blog/2026/llm-education-1-classroom-game/) · **[Post 2: The Evolving Game](/blog/2026/llm-education-2-evolving-game/)** · [Post 3: The Continuous Theory](/blog/2026/llm-education-3-continuous-theory/) · [Post 4: The Full Picture](/blog/2026/llm-education-4-full-picture/)

What if we let the game run — not just once, but for 30 years?

[Post 1](/blog/2026/llm-education-1-classroom-game/) mapped the basic structure: four players, their strategies, their payoffs, and the Nash Equilibrium that results when everyone plays rationally. That equilibrium is real and meaningful. But it's a snapshot. Education systems don't jump instantly to equilibrium — they adapt, year by year, in response to what other actors are doing and what the environment demands.

And halfway through any 30-year window for a child starting school today, something might happen that resets the board entirely.

---

## Institutional Inertia: Why Actors Move Slowly

The first thing to understand about real systems is that actors don't leap to their optimal strategy overnight. When new information arrives — a government shifts its AI policy, a competitor school achieves better outcomes with a different approach — real institutions adjust gradually.

Our model captures this with an **inertia parameter of 0.3**: actors move 30% of the way toward their best response each year, not 100%. This is not a modeling convenience. It reflects something true about institutions.

A school that decides to fully integrate AI into its pedagogy faces a multi-year process: teacher retraining, assessment redesign, infrastructure acquisition, parent communication, regulatory approval. Even a motivated, well-resourced institution takes years. A government changing education policy faces legislative processes, budget cycles, and the need to build political coalitions. A parent who decides to change their child's learning environment faces constraints on time and money.

The 30% adjustment rate means the system has memory. What was true last year still shapes what's true this year. Equilibria are approached slowly, and sometimes actors are still converging on the last equilibrium when the environment changes and a new one becomes relevant.

---

## The Punctuated Equilibrium

The LLM breakthrough is the central event in our simulation.

AI capability does not grow smoothly. The historical record shows periods of rapid advance followed by periods of consolidation — what biologists call punctuated equilibrium when they observe it in species evolution. We are, by most accounts, currently in a consolidation period. Models are getting incrementally better; they are not getting transformatively better.

Our model represents this as:

1. **Convergence phase (years 1–14):** All actors are adjusting toward the Nash Equilibrium we described in Post 1. Governments settle on moderate regulation, moderate subsidy. Schools gradually integrate AI tools. High-resource parents supplement significantly; low-resource parents supplement less. Students adjust their delegation level accordingly.

2. **Plateau (year ~14):** The system approaches stability. Not full equilibrium — institutional inertia prevents that — but a relatively settled state where the pace of change has slowed and actors' strategies are near their best responses.

3. **Shock (year 15):** A breakthrough. A new architecture, a qualitative leap in capability, a sudden expansion of what AI can and cannot do. The shock changes the payoff functions for all actors simultaneously. The strategies that were near-optimal yesterday are suddenly not.

4. **Re-equilibration (years 15–30):** The system adjusts again, but now from a starting point shaped by 15 years of prior adaptation. The question is not just where the new equilibrium is, but which actors adapt fastest and whether the shock widens or narrows the gaps between them.

---

## What the Simulation Shows

### Convergence before the shock

In the pre-shock period, the simulation shows characteristic convergence paths. Regulation ($r$) starts high in most government starting positions — the political default when AI is new and parents are worried — and drifts toward a moderate equilibrium as the evidence base accumulates and as peer-country comparisons create normative pressure.

School pedagogy (*p*) lags regulation by roughly 3–5 simulation years. Schools wait for regulatory clarity before making costly infrastructure investments. This lag is realistic: it matches the historical pattern of technology adoption in education.

Parent supplementation (*x*) diverges early. High-resource parents begin supplementing almost immediately, while low-resource parents wait for school-provided access. By year 10, the supplementation gap has already opened up significantly, even before the shock.

### Strategy stability and cycling

Most actor strategies stabilize before the shock. But one strategy tends to cycle: government subsidy (*s*) oscillates as governments respond to emerging equity data. When the supplementation gap becomes visible in outcome data (typically year 6–8 in the simulation), governments increase subsidy. This narrows the gap. The political pressure for subsidy then decreases. Subsidy drifts down. The gap reopens. The cycle repeats.

This cycling behavior is not a bug in the model — it reproduces a recognizable pattern in real education policy. Equity initiatives get funded, show results, lose political salience, get defunded, produce new inequities, regenerate political will.

### The shock and re-equilibration

The year-15 shock disrupts everything simultaneously. Several dynamics emerge:

**Regulation initially spikes.** When capability expands rapidly, the political default is precautionary restriction. Governments that had settled on moderate regulation $r \approx 0.4$ jump toward $r \approx 0.7$–$0.8$. This is the observable pattern: every major AI advance has been followed by a wave of calls for restriction.

**Schools pause investment.** The uncertainty about what AI will look like in 18 months makes it rational to delay infrastructure decisions. Schools that had been gradually integrating AI tools freeze their pedagogy at pre-shock levels while waiting for the dust to settle.

**The parent gap widens.** High-resource parents, facing uncertainty, increase private supplementation. They can afford to bet on multiple approaches. Low-resource parents, who were more dependent on school-provided access, experience a relative deterioration as school AI integration pauses and they lack private alternatives.

**Re-equilibration is slower than initial convergence.** The system that re-stabilizes after year 20 is generally at a higher average human capital level than the pre-shock equilibrium — the breakthrough is broadly beneficial. But the distribution is worse. The shock that raises the mean tends to widen the variance.

---

## How Population Composition Changes Everything

The simulation above assumes a fixed mix of high-resource and low-resource parents. But that mix — what we call $\pi_P$, the proportion of high-resource parents in the population — is itself a parameter that varies across districts, cities, and countries.

The results are striking:

- In a district where $\pi_P$ is high (say, 0.7 — most parents are high-resource), the pre-shock equilibrium has lower government subsidy (private supplementation substitutes for public investment), moderate regulation (high-resource parents are comfortable with AI tools), and a smaller equity gap (because most families are on the high-resource side).

- In a district where $\pi_P$ is low (say, 0.3), the equilibrium has higher subsidy demands, more pressure for regulation as a proxy for protection, and a larger equity gap even with higher subsidy.

- The shock affects these differently. In high $\pi_P$ districts, the shock accelerates divergence within the existing distribution. In low $\pi_P$ districts, the shock can be democratizing if government response is robust (rapid subsidy of the new tools) or devastating if government response is slow.

This finding has a policy implication: the same national policy will produce different outcomes in different districts depending on the initial population composition. A one-size-fits-all subsidy regime is suboptimal. Districts with lower $\pi_P$ need higher subsidy rates just to arrive at the same equity outcome.

---

## What the 30-Year View Reveals

Running the game out over time reveals things the snapshot equilibrium misses:

1. The equity gap opens early and compounds. Interventions are more effective in years 1–5 than in years 10–15, because the gap is smaller and institutions are still in flux.

2. Institutional inertia is protective against shocks but costly in terms of optimal response speed. Societies with more flexible institutions adapt faster post-shock but are also more volatile pre-shock.

3. The political cycling of subsidy is a real cost. Resources spent, withdrawn, and re-spent on equity programs produce worse outcomes than the same total resources spent consistently.

4. The shock does not affect all actors equally. Students are affected immediately — through changes in what their school does and what their parents provide. Governments respond over 2–3 years. Schools respond over 3–7 years. The gap between student exposure and institutional response is where most of the post-shock harm concentrates.

---

## Where the Math Gets Richer

Our simulation treats actors as belonging to two types: high-resource or low-resource, progressive or conservative, equity-focused or efficiency-focused. This is a useful simplification. But real populations are not bimodal. Every parent is slightly different. Every school has its own culture. The range of actual variation is continuous, not categorical.

What does the math look like when we relax the two-type assumption and model the full spectrum of actor variation?

[Post 3: The Continuous Theory — what happens when actors exist on a full spectrum](/blog/2026/llm-education-3-continuous-theory/)

---

*How this series was made: The questions driving this research, the editorial judgment, and the final decisions about what to include or exclude are human. The analysis, modeling, writing, and simulation code are largely AI-generated, guided by human prompts and reviewed by human editors. This series is itself an experiment in human-AI collaboration.*
