---
layout: post
title: "The Ceasefire Equation"
description: "Game theory, prediction markets, and what the math says about the USA–Iran war"
date: 2026-03-03 00:00:00 +0530
tags: [game-theory, geopolitics, prediction-markets, nash-equilibrium]
categories: essays
math: true
giscus_comments: true
---

On February 28, 2026, the United States and Israel launched coordinated strikes on Iran — the largest US military operation in the Middle East since 2003. Iran retaliated within hours. Gulf states are under fire. Oil is at record highs.

Everyone has an opinion on who is right. Fewer people have a framework for predicting what happens next.

Prediction markets do. Polymarket currently assigns a 45% probability of an official ceasefire by March 31, rising to 69% by June 30. These numbers are not arbitrary — they are the aggregate of thousands of traders putting real money on their beliefs.

Game theory can explain where those numbers come from. And if you trust both the math and the market, it can tell you when this ends.

---

## The Game

Strip away the politics. Two players: the **Coalition** (USA and Israel, treated as a single actor) and **Iran**. Each round, both independently choose one of two actions:

- **Continue** — keep fighting
- **Ceasefire** — signal willingness to stop

An official ceasefire requires *both* players to choose Ceasefire simultaneously. One side stopping unilaterally is not a ceasefire — it is a concession.

The payoffs from each combination of choices can be written as a matrix. Call Coalition's payoffs the first entry in each cell, Iran's the second:

<div class="table-responsive">
<table class="table table-bordered text-center">
  <thead>
    <tr>
      <th></th>
      <th><strong>Iran: Continue</strong></th>
      <th><strong>Iran: Ceasefire</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Coalition: Continue</strong></td>
      <td>$(a,\ e)$</td>
      <td>$(b,\ f)$</td>
    </tr>
    <tr>
      <td><strong>Coalition: Ceasefire</strong></td>
      <td>$(c,\ g)$</td>
      <td>$(d,\ h)$</td>
    </tr>
  </tbody>
</table>
</div>

Each symbol represents a concrete real-world quantity:

<div class="table-responsive">
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Player</th>
      <th>Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$a$</td>
      <td>Coalition</td>
      <td>Ongoing war: military costs (casualties, logistics, oil shock to allies) offset by the probability of destroying Iran's nuclear program and weakening the regime</td>
    </tr>
    <tr>
      <td>$b$</td>
      <td>Coalition</td>
      <td>Iran accepts while Coalition continues striking — maximum strategic gain, full objectives achieved</td>
    </tr>
    <tr>
      <td>$c$</td>
      <td>Coalition</td>
      <td>Coalition offers ceasefire while Iran keeps fighting — strategic humiliation, worst outcome</td>
    </tr>
    <tr>
      <td>$d$</td>
      <td>Coalition</td>
      <td>Mutual ceasefire — partial objectives, stability, alliance relationships preserved</td>
    </tr>
    <tr>
      <td>$e$</td>
      <td>Iran</td>
      <td>Absorbs strikes and retaliates — maximum physical damage, but signals regime survival and resolve to domestic and regional audiences</td>
    </tr>
    <tr>
      <td>$f$</td>
      <td>Iran</td>
      <td>Accepts ceasefire while strikes continue — humiliation, physical damage, no guarantees</td>
    </tr>
    <tr>
      <td>$g$</td>
      <td>Iran</td>
      <td>Coalition blinks while Iran continues — best outcome: survival signalled, no concessions required</td>
    </tr>
    <tr>
      <td>$h$</td>
      <td>Iran</td>
      <td>Mutual ceasefire — partial survival, some concessions required, but physical damage stops</td>
    </tr>
  </tbody>
</table>
</div>

The assumed preference orderings are:

$$\text{Coalition: } b > d > a > c$$

$$\text{Iran: } g > e > h > f$$

Neither side has a dominant pure strategy. If Iran is continuing, Coalition prefers to continue ($a > c$). But if Iran is offering ceasefire, Coalition also prefers to continue ($b > d$). So Coalition always wants to Continue — except that if Coalition always continues, Iran should Continue too (since $e > f$). And if both always Continue, neither achieves a ceasefire, and the expected costs of the war accumulate indefinitely.

This is the structure that produces a **mixed strategy Nash equilibrium**.

---

## The Nash Equilibrium

In a mixed strategy Nash equilibrium, each player randomises over their actions in a way that makes the *other* player indifferent between their own choices. The logic: if your opponent could strictly prefer one action, they would play it with certainty — which you would then exploit. Equilibrium requires you to keep them guessing.

Let $p$ = probability that Coalition plays Continue, and $q$ = probability that Iran plays Continue.

**Coalition's indifference condition** — Iran mixes only if its strategy $q$ makes Coalition indifferent between Continue and Ceasefire. Using Coalition's payoffs:

$$\underbrace{q \cdot a + (1-q) \cdot b}_{\text{Coalition's EU from Continue}} = \underbrace{q \cdot c + (1-q) \cdot d}_{\text{Coalition's EU from Ceasefire}}$$

The left side is Coalition's expected utility from playing Continue: with probability $q$ Iran also continues (Coalition gets $a$), with probability $1-q$ Iran ceases (Coalition gets $b$). The right side is the same calculation if Coalition plays Ceasefire instead.

Solving for $q$:

$$\boxed{q^* = \frac{d - b}{a - b - c + d}}$$

**Iran's indifference condition** — Coalition mixes only if its strategy $p$ makes Iran indifferent between Continue and Ceasefire. Using Iran's payoffs:

$$\underbrace{p \cdot e + (1-p) \cdot g}_{\text{Iran's EU from Continue}} = \underbrace{p \cdot f + (1-p) \cdot h}_{\text{Iran's EU from Ceasefire}}$$

The left side is Iran's expected utility from continuing: with probability $p$ the Coalition also continues (Iran gets $e$), with probability $1-p$ the Coalition ceases (Iran gets $g$). The right side is Iran's expected utility from offering ceasefire.

Solving for $p$:

$$\boxed{p^* = \frac{h - g}{e - f - g + h}}$$

Two things are worth noting. First, $p^{\ast}$ — Coalition's mixing probability — depends only on **Iran's** payoffs ($e, f, g, h$), not Coalition's. And $q^{\ast}$ — Iran's mixing probability — depends only on **Coalition's** payoffs ($a, b, c, d$), not Iran's. This is the classic result in mixed strategy equilibria: your opponent's mixing probability is pinned by your payoffs, not theirs. The intuition: your opponent mixes to keep you indifferent, so their mixing rate must be calibrated to your costs and benefits. Second, both expressions are ratios — the equilibrium probabilities are determined entirely by the relative sizes of costs and benefits, not their absolute values.

---

## Connecting to Prediction Markets

An official ceasefire requires both players to simultaneously choose Ceasefire. In the mixed strategy equilibrium, this happens with per-round probability:

$$r = (1 - p^*)(1 - q^*)$$

If we model the conflict as a sequence of discrete decision rounds — think of each round as a week of diplomacy — then ceasefire is a geometrically distributed waiting time. The probability that ceasefire has occurred by round $T$ is:

$$\boxed{P(\text{ceasefire by } T) = 1 - (1 - r)^T}$$

This is exactly what a prediction market is pricing. Polymarket's ceasefire contracts resolve to "Yes" if an official, mutually agreed ceasefire is announced by the stated date. The market price is the probability $P(\text{ceasefire by } T)$.

Given $P$ and $T$, we can invert to recover the implied per-round ceasefire probability:

$$r = 1 - (1 - P)^{1/T}$$

Plugging in the Polymarket data (with $T$ measured in days from February 28):

<div class="table-responsive">
<table class="table table-bordered text-center">
  <thead>
    <tr>
      <th>Ceasefire by</th>
      <th>Days ($T$)</th>
      <th>Market probability ($P$)</th>
      <th>Implied daily $r$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>March 6</td>
      <td>6</td>
      <td>4%</td>
      <td>0.68%</td>
    </tr>
    <tr>
      <td>March 15</td>
      <td>15</td>
      <td>21%</td>
      <td>1.56%</td>
    </tr>
    <tr>
      <td>March 31</td>
      <td>31</td>
      <td>45%</td>
      <td>1.90%</td>
    </tr>
    <tr>
      <td>April 30</td>
      <td>61</td>
      <td>59%</td>
      <td>1.46%</td>
    </tr>
    <tr>
      <td>June 30</td>
      <td>122</td>
      <td>69%</td>
      <td>0.93%</td>
    </tr>
  </tbody>
</table>
</div>

If the game were truly static — fixed payoffs, fixed strategies — $r$ would be constant across all windows. It is not. It rises sharply from 0.68% to 1.90%, then falls back to 0.93%. That variation is the signal.

---

## Bayesian Updating

A static game assumes both players have complete information about each other's payoffs. In reality, each side's true cost tolerance — how much damage they can absorb before their calculus shifts — is private information. What we observe from the outside is each side's *actions*, from which we infer their types.

This is the Bayesian updating component. Each day of continued fighting is a signal. Both sides are revising their estimates of the other's resolve. And as those estimates change, so do $p^{\ast}$ and $q^{\ast}$ — and therefore $r$.

<div class="table-responsive">
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Window</th>
      <th>Implied $r$</th>
      <th>What both sides are learning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Week 1 (Mar 1–6)</td>
      <td>0.68%</td>
      <td>Both sides signalling maximum resolve. No material updating off priors. Coalition strikes are landing but Iran is retaliating visibly against Gulf infrastructure — neither has flinched.</td>
    </tr>
    <tr>
      <td>Weeks 2–4 (Mar 7–31)</td>
      <td>peaks at 1.90%</td>
      <td>Damage accumulating on both sides. Iran's cost of continuing ($e$) is being revealed as higher than initially priced — strikes on energy infrastructure are showing real economic effect. Coalition's cost of continuing ($a$) is also rising: oil above $130, Gulf allies under domestic pressure, US approval ratings slipping. Both $p^{\ast}$ and $q^{\ast}$ fall as the cost of continuing rises relative to the cost of stopping. $r = (1-p^{\ast})(1-q^{\ast})$ rises.</td>
    </tr>
    <tr>
      <td>April onward</td>
      <td>falling to 0.93%</td>
      <td>War fatigue without resolution. Both sides have absorbed the initial shock and repriced it as the new normal. Neither has a dominant new reason to stop. Resolve has been demonstrated on both sides. $r$ falls — not because the war is going well for anyone, but because both sides have updated toward believing the other will not back down.</td>
    </tr>
  </tbody>
</table>
</div>

The rising $r$ in weeks 2–4 is not a sign that ceasefire is inevitable. It is a sign that *this is the window*. Both sides' cost functions are in flux. Bargaining is most likely when the marginal cost of the next day of fighting is highest relative to the value of continuing.

After April, if no ceasefire has occurred, the market is telling you something important: both sides have revealed their types as high-resolve. The game shifts character — it is no longer a question of whether the other side will fold, but of who can endure longer. That is a different, and much worse, game.

---

## The Prediction

The model yields a concrete prediction. The per-day ceasefire probability peaks around March 15–31. Using the implied $r$ values, the conditional probability of ceasefire in each remaining window — given no ceasefire has occurred yet — can be computed as:

$$P(\text{ceasefire in window} \mid \text{no ceasefire yet}) = 1 - (1 - r_{\text{window}})^{\Delta T}$$

<div class="table-responsive">
<table class="table table-bordered text-center">
  <thead>
    <tr>
      <th>Window</th>
      <th>$\Delta T$ (days)</th>
      <th>Window $r$</th>
      <th>Conditional probability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mar 1 – Mar 6</td>
      <td>6</td>
      <td>0.68%</td>
      <td>4%</td>
    </tr>
    <tr>
      <td>Mar 7 – Mar 31</td>
      <td>25</td>
      <td>1.90%</td>
      <td>38%</td>
    </tr>
    <tr>
      <td>Apr 1 – Apr 30</td>
      <td>30</td>
      <td>1.46%</td>
      <td>36%</td>
    </tr>
    <tr>
      <td>May 1 – Jun 30</td>
      <td>61</td>
      <td>0.93%</td>
      <td>43%</td>
    </tr>
  </tbody>
</table>
</div>

The highest per-day probability of ceasefire is in mid-to-late March. If March passes without a deal, the window does not close — but it narrows. The conditional probability of ceasefire in any given month falls, and the expected duration of the conflict grows.

The model's prediction: **if a ceasefire happens, the most likely time is before the end of March**. Every day past April 30 without an agreement is evidence that both sides have revealed sufficiently high resolve that the game has entered a new phase — one where the geometric model breaks down and something more like a war of attrition takes over.

---

## What This Model Does Not See

This is an academic exercise. The two-player strategic form game is a useful lens, but the real world has far more moving parts than any 2×2 matrix can hold. Here are the variables this model deliberately ignores — and why each of them matters.

<div class="table-responsive">
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Variable</th>
      <th>Why it matters</th>
      <th>How it would change the model</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>China's leverage on Iran</strong></td>
      <td>China is Iran's largest oil buyer and a major economic lifeline. If Beijing signals that continued fighting threatens its economic interests — or privately tells Tehran that support has limits — Iran's cost of continuing ($e$) rises sharply without a single additional strike landing.</td>
      <td>Would reduce $q^{\ast}$ (Iran's probability of continuing) independently of Coalition actions. Ceasefire probability $r$ rises even if Coalition payoffs are unchanged.</td>
    </tr>
    <tr>
      <td><strong>International diplomatic pressure</strong></td>
      <td>UN Security Council resolutions, EU sanctions threats, Arab League positioning, and backchannel mediation by Qatar or Oman all affect the political cost of continuing for both sides. A credible ceasefire framework offered by a neutral third party changes the payoff for mutual ceasefire ($d$ and $h$) without either side having to concede directly.</td>
      <td>Raises $d$ and $h$ simultaneously — makes the mutual ceasefire cell more attractive for both players, pushing both $p^{\ast}$ and $q^{\ast}$ down. $r$ rises.</td>
    </tr>
    <tr>
      <td><strong>Domestic politics</strong></td>
      <td>US Congressional pressure, Israeli public opinion after casualties, and Iranian regime legitimacy under protest conditions all affect each player's effective payoffs in ways that can shift faster than the battlefield. A leader's political survival constraint is not in the payoff matrix.</td>
      <td>Effectively changes $a$ and $c$ for Coalition and $e$ and $g$ for Iran in real time — makes the model non-stationary in ways that a fixed payoff matrix cannot capture.</td>
    </tr>
    <tr>
      <td><strong>Nuclear threshold dynamics</strong></td>
      <td>If strikes bring Iran close to — or over — a nuclear breakout threshold, the entire payoff structure changes discontinuously. The value of Coalition's objective ($b$) could collapse if Iran weaponises before the conflict ends. This is a non-linear event that a smooth payoff function cannot model.</td>
      <td>Would require a jump process or regime-switching model, not a static 2×2 game.</td>
    </tr>
    <tr>
      <td><strong>Coalition unity</strong></td>
      <td>The model treats USA and Israel as a single player. In practice, their objectives diverge: the US may prioritise nuclear dismantlement and regional stability; Israel may prioritise regime change. Disagreement within the Coalition effectively reduces $p^{\ast}$ — the Coalition is less able to credibly commit to continuing.</td>
      <td>Would require a three-player game or a principal-agent model within the Coalition. This is precisely what Option C (Harsanyi incomplete information game) begins to address.</td>
    </tr>
    <tr>
      <td><strong>Iranian proxy network</strong></td>
      <td>Hezbollah, Houthi, and Iraqi militia activity gives Iran instruments of retaliation that are not direct military action — and that impose costs on the Coalition without formally escalating. The model has no concept of asymmetric or indirect moves.</td>
      <td>Would require an extensive-form game with a richer action space, not a binary Continue/Ceasefire choice.</td>
    </tr>
  </tbody>
</table>
</div>

The model's value is not in its completeness — it is in its clarity. By stripping the conflict down to two players and two choices, we can isolate the pure logic of deterrence and see exactly what the prediction market is implying about costs and resolve. Every variable in the table above is real and consequential. Each one is also a reason why the ceasefire could come sooner than the model predicts — or not at all.

---

The model does not know what any individual leader will decide. What it does is take the market's aggregate judgment seriously and ask: if rational actors with these payoffs are generating these probabilities, what must be true about the underlying costs and incentives?

The math already has an answer. We are just reading it.
