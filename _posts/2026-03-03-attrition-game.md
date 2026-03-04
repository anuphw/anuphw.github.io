---
layout: post
title: "The Attrition Game"
description: "Resource depletion, the Strait of Hormuz, and what two prediction markets jointly reveal about the USA–Iran war"
date: 2026-03-03 00:00:00 +0530
tags: [game-theory, geopolitics, prediction-markets, war-of-attrition]
categories: essays
math: true
giscus_comments: true
---

*The ideas, arguments, mathematical framing, and editorial judgements in this post are the author's own. An LLM helped with some of the legwork — literature lookup, LaTeX, and drafting prose from the author's outline. The author read, stress-tested, and revised everything. Think of the LLM as a capable but occasionally confused research assistant.*

*A companion Python script that numerically verifies every closed-form result in this post — ODE solutions, balance ratio, exhaustion times, selective closure dominance, and the Bayesian inference system — is available at [github.com/anuphw/attrition_game](https://github.com/anuphw/attrition_game). The README also explains how to update the Polymarket calibration as new prices become available.*

---

Two questions are being traded simultaneously on Polymarket. The first: *Will there be a USA–Iran ceasefire by...?* The second: *Will Iran close the Strait of Hormuz by...?*

Most analyses treat these separately. This post treats them as a joint system — because they are. The Hormuz question is not independent of the ceasefire question. Hormuz activation is a phase transition inside the same underlying dynamic. Reading both markets together reveals structure that neither market alone can show.

The framework is a **war of attrition with resource depletion and private information**. The leaders driving this war — in Washington, Tel Aviv, and Tehran — are not solving Bellman equations. They are trying to win, at near-any cost to their own countries. When agents fight to exhaustion rather than to optimality, the right model is not a payoff matrix. It is a dynamic system in which two resource stocks drain each other until one hits zero.

---

## Modeling Assumptions

Before the math, here are the key commitments the model makes. Readers should keep these in mind throughout.

<div class="table-responsive">
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Assumption</th>
      <th>What it rules out</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Both sides fight at maximum intensity at all times</td>
      <td>Strategic reserve-holding, de-escalation signalling, partial strikes</td>
    </tr>
    <tr>
      <td>Ceasefire occurs only after Hormuz activation (within this model)</td>
      <td>Diplomatic ceasefire before Iran is cornered; quick-collapse ceasefire without Hormuz is treated separately in the scenarios</td>
    </tr>
    <tr>
      <td>Selective closure is feasible and credible</td>
      <td>Coalition naval interdiction of selective enforcement; insurance and flagging complications; third-party legal challenges</td>
    </tr>
    <tr>
      <td>No resupply: $\dot{R}_i \leq 0$ always</td>
      <td>US mid-war munitions restocking; Chinese materiel to Iran</td>
    </tr>
    <tr>
      <td>Constant effectiveness coefficients $k_C$, $k_I$</td>
      <td>Degrading precision as high-value targets are exhausted; learning effects</td>
    </tr>
    <tr>
      <td>$\rho \sim \text{Beta}(2,5)$ baseline prior</td>
      <td>Other prior shapes; this parameterisation is chosen because it produces calibration residuals below 0.5pp across all seven Polymarket data points</td>
    </tr>
  </tbody>
</table>
</div>

---

## Theoretical Foundations

The **war of attrition** framework models two sides competing by choosing how long to persist, each paying a continuous cost. Huangfu, Ghosh, and Liu (2023) analyse conditions under which an equilibrium exists where resource-rich players fight longer and resource-poor players deplete early — and show that resource inequality can *increase* conflict duration at intermediate asymmetries, where the weaker side fights longer to signal residual capacity. *(We borrow the attrition structure and the asymmetric-resource formulation.)*

The **resource-depletion ODE structure** follows Lanchester-type coupled attrition equations, which Kress (2020) reviews and applies to modern irregular warfare, showing they are widely used in combat modelling and simulation. Under this structure, each side's force depletes at a rate proportional to the opponent's remaining strength and effectiveness: *(We borrow the coupled ODE form and the asymmetric effectiveness coefficient $\gamma$.)*

$$\frac{dF_1}{dt} = -\alpha_2 F_2, \qquad \frac{dF_2}{dt} = -\alpha_1 F_1$$

**Incomplete information and type revelation.** Slantchev and Tarar (2011) show conditions under which a state's uncertainty about an opponent's military capabilities is sufficient for costly war among otherwise rational actors — the opponent has incentive to misrepresent strength, making private information a structural cause of conflict. *(We borrow the private-capacity framework and the Bayesian updating dynamic.)* Lindsey (2015) extends this: observable military choices function as costly signals, with combatants continuously updating beliefs under Bayesian reasoning. *(We borrow the signal-extraction structure for inferring $E_C^0$ from observed attack intensity.)*

**On using prediction markets as data.** Mellers et al. (2015), in the IARPA-sponsored ACE geopolitical forecasting tournament, found that aggregated forecasters outperformed intelligence analysts by roughly 30% on hundreds of geopolitical questions. *(We borrow the empirical justification for treating crowd-aggregated probabilities as calibrated signals.)* Han (2018), modelling U.S.–Iran strategic interaction, uses a game-theoretic framework to show that observable U.S. policy choices function as commitment devices shaping Iranian responses. *(We borrow the framing of observable market prices as rational-expectations signals.)* We treat Polymarket prices as the best available real-money-incentivised crowd estimate — not ground truth, but a disciplined prior.

---

## The State Variables

All quantities are dimensionless (normalised to Coalition's initial capacity). Time is in days. Rates $k$, $\omega$, $c_C$ are in day$^{-1}$.

All state variables satisfy $R_i, S_i, E_i \geq 0$. The Hormuz threshold satisfies $\theta > E_{\min} > 0$.

**$S_i(t)$ is a depletable stock**, not a flow rate — it represents accumulated political and economic backing that erodes under specific shocks (Hormuz activation for $S_C$; international isolation for $S_I$). Outside those shocks, $\dot{S}_i = 0$.

<div class="table-responsive">
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Variable</th>
      <th>Player</th>
      <th>Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$R_i(t) \geq 0$</td>
      <td>Both</td>
      <td>Composite resolve: military capacity, economic endurance, political will — continuously depleted by opponent's attacks</td>
    </tr>
    <tr>
      <td>$S_i(t) \geq 0$</td>
      <td>Both</td>
      <td>External support stock — stable in Phase 1; depleted only by specific shocks (Hormuz for $S_C$; Iranian escalation for $S_I$)</td>
    </tr>
    <tr>
      <td>$E_i(t) \geq 0$</td>
      <td>Both</td>
      <td>Effective capacity: the fighting-relevant combination of resolve and support</td>
    </tr>
  </tbody>
</table>
</div>

**Effective capacity** combines both stocks:

$$E_C(t) = R_C(t) + \alpha_C S_C(t), \qquad E_I(t) = R_I(t) + \alpha_I S_I(t)$$

**Attack intensity** is proportional to remaining capacity — consistent with Lanchester's model:

$$a_C(t) = \beta_C \cdot E_C(t), \qquad a_I(t) = \beta_I \cdot E_I(t)$$

**Ceasefire occurs when either side's $E_i(t)$ falls below $E_{\min}$** — the exhaustion threshold below which a player can no longer sustain operations, regardless of intent.

---

## The Two Prediction Markets

Both sets of probabilities below were read simultaneously on **March 4, 2026 at approximately 10:30 IST** — six days after the February 28 strikes — from the [USA–Iran ceasefire market](https://polymarket.com/event/us-x-iran-ceasefire-by) and the [Iran Hormuz closure market](https://polymarket.com/event/will-iran-close-the-strait-of-hormuz-by-2027). Simultaneous snapshot pricing is essential: using prices from different times would introduce calibration error.

<div class="table-responsive">
<table class="table table-bordered text-center">
  <thead>
    <tr>
      <th>Date</th>
      <th>Days ($T$)</th>
      <th>Ceasefire $P_{\text{cf}}$</th>
      <th>Hormuz $P_H$</th>
      <th>Gap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mar 6</td>
      <td>6</td>
      <td>4%</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Mar 15</td>
      <td>15</td>
      <td>21%</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Mar 31</td>
      <td>31</td>
      <td>45%</td>
      <td>63%</td>
      <td>18pp</td>
    </tr>
    <tr>
      <td>Apr 30</td>
      <td>61</td>
      <td>59%</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Jun 30</td>
      <td>122</td>
      <td>69%</td>
      <td>69%</td>
      <td>0pp</td>
    </tr>
  </tbody>
</table>
</div>

Three observations:

1. **Hormuz consistently exceeds ceasefire** — activation is necessary but not sufficient for war's end in most scenarios.
2. **The gap closes to zero by June** — by that window, traders treat the two events as effectively equivalent.
3. **The Hormuz market gives us a direct observable for the phase transition** — the moment Iran deploys its asymmetric weapon.

---

## The Hormuz Lever

The Strait of Hormuz is the world's most critical oil chokepoint. The U.S. Energy Information Administration (2024) reports roughly 20 million barrels per day transited the Strait in 2023 — approximately 20% of global petroleum consumption and over one-quarter of all seaborne oil trade. Closure for 1–3 months would push oil toward $150–200 per barrel, reducing global GDP growth by 2–3 percentage points (U.S. Senate Joint Economic Committee, 2007).

Shariatinia and Azizi (2021) characterise Iran's Hormuz policy as "double-faced": under low-threat conditions Tehran acts as a security provider; under existential threat it weaponises the strait. The Congressional Research Service (Katzman et al., 2012) documented Iran's escalation ladder — naval harassment, mine-laying, tanker interdiction below full closure — and noted the threat's value lies precisely in its credibility at the margin.

Iran has three Hormuz modes:

<div class="table-responsive">
<table class="table table-bordered text-center">
  <thead>
    <tr>
      <th>Mode</th>
      <th>$H$</th>
      <th>$\chi$</th>
      <th>$\dot{S}_C$</th>
      <th>$\dot{S}_I$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Open</strong></td>
      <td>0</td>
      <td>—</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td><strong>Full closure</strong></td>
      <td>1</td>
      <td>0</td>
      <td>$-\mu_C$</td>
      <td>$-\mu_I$</td>
    </tr>
    <tr>
      <td><strong>Selective closure</strong></td>
      <td>1</td>
      <td>1</td>
      <td>$-\mu_C$</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

China is Iran's largest oil customer at roughly 1.5 mb/d (EIA, 2024). Full closure would cost China economically, likely reducing Beijing's support for Tehran. Selective closure preserves this relationship while still depleting Coalition-aligned importers' support. In practice, selective enforcement raises real logistical questions — ship flagging, insurance, coalition naval response — but within this model, we take it as feasible.

**Within this model, selective closure weakly dominates full closure.** Both modes produce identical $\dot{S}_C = -\mu_C$ — the same drain on Coalition support. But full closure adds $\dot{S}_I = -\mu_I < 0$, depleting Iran's own support stock, while selective closure keeps $\dot{S}_I = 0$. Selective closure therefore produces weakly higher $E_I(t)$ for all $t$ while leaving $E_C(t)$ unchanged. This result holds given our modeling assumptions — in particular, that Coalition's depletion is identical under both closure modes and that China can be perfectly exempted. Iran allowing Chinese ships implies a strong incentive to do so.

The model treats Hormuz as a **last resort**: Iran activates it endogenously when its effective capacity falls to threshold $\theta$ — when cornered but not yet defeated.

---

## Phase 1: The Baseline Attrition Race

Before Hormuz activation ($E_I \geq \theta$), support stocks are stable ($\dot{S}_i = 0$) and depletion follows the Lanchester-type coupled ODEs:

$$\dot{E}_C = -k_C E_I(t), \qquad \dot{E}_I = -k_I E_C(t)$$

where $k_C$ and $k_I$ are the cross-damage rates (day$^{-1}$, in normalised units).

**Precision differential.** Coalition strikes benefit from precision-guided munitions and intelligence-directed targeting. We capture this with a single parameter $\gamma > 1$ at the $k$-level:

$$k_C = \gamma \cdot k_I, \quad \gamma > 1$$

so $\gamma$ is the precision differential — the ratio by which Coalition attacks are more effective per unit than Iranian attacks.

**Solving Phase 1.** Normalise $E_C^0 = 1$ and write $E_I^0 = \rho \in (0,1]$. Define $\omega = \sqrt{k_C k_I} = k_I\sqrt{\gamma}$ (day$^{-1}$). Differentiating $\dot{E}_C = -k_C E_I$ and substituting $\dot{E}_I = -k_I E_C$:

$$\ddot{E}_C = k_C k_I \cdot E_C = \omega^2 E_C$$

General solution: $E_C(t) = A_1 e^{\omega t} + B_1 e^{-\omega t}$. Applying initial conditions $E_C(0) = 1$ and $\dot{E}_C(0) = -k_C \rho = -\omega\sqrt{\gamma}\,\rho$:

$$\boxed{A_1 = \frac{1 - \sqrt{\gamma}\,\rho}{2}, \qquad B_1 = \frac{1 + \sqrt{\gamma}\,\rho}{2}}$$

For Iran, integrating $\dot{E}_I = -k_I E_C$ directly:

$$E_I(t) = \rho - k_I \int_0^t E_C(s)\,ds$$

$$\boxed{E_I(t) = \rho - \frac{k_I}{\omega}\!\left[A_1(e^{\omega t}-1) + B_1(1-e^{-\omega t})\right]}$$

**Symmetric check.** When $\gamma = 1$ (equal precision) and $\rho = 1$ (equal initial resources): $A_1 = 0$, $B_1 = 1$, and $E_C(t) = E_I(t) = e^{-\omega t}$ — pure exponential decay. In this symmetric case $\omega = k_I = k_C = k$. The asymmetry $\gamma > 1$ breaks this: Iran depletes faster, and Phase 1 ends at time $t_H$ when $E_I(t_H) = \theta$, while Coalition retains $E_C^H = E_C(t_H) > 0$.

---

## Phase 2: The Tipped Balance

After Hormuz activation ($H = 1$, $\chi = 1$), Coalition faces an additional constant drain $c_C = \alpha_C \mu_C$ (day$^{-1}$, normalised):

$$\dot{E}_C = -k_C E_I - c_C, \qquad \dot{E}_I = -k_I E_C$$

Let $\tau = t - t_H$, with initial conditions $(E_C^H,\,\theta)$. Differentiating gives the same characteristic equation $\ddot{E}_C = \omega^2 E_C$ — $c_C$ vanishes in the second derivative but shifts the initial slope:

$$\dot{E}_C(\tau=0) = -k_C\theta - c_C$$

$$\boxed{A_2 = \frac{1}{2}\!\left(E_C^H - \frac{k_C\theta + c_C}{\omega}\right), \qquad B_2 = \frac{1}{2}\!\left(E_C^H + \frac{k_C\theta + c_C}{\omega}\right)}$$

**The balance ratio:**

$$\boxed{\Lambda = \frac{k_C\theta + c_C}{\omega\, E_C^H}}$$

In plain language: $\Lambda$ is Coalition's shock-adjusted initial depletion rate relative to its remaining capacity scaled by $\omega$. It tells you whether the Hormuz drain tips the balance:

<div class="table-responsive">
<table class="table table-bordered text-center">
  <thead>
    <tr>
      <th>$\Lambda$</th>
      <th>Regime</th>
      <th>Interpretation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$< 1$</td>
      <td>Coalition survives</td>
      <td>Hormuz drain is manageable — Coalition outlasts Iran even after activation.</td>
    </tr>
    <tr>
      <td>$= 1$</td>
      <td>Simultaneous exhaustion</td>
      <td>Both sides collapse together. Mutual exhaustion ceasefire.</td>
    </tr>
    <tr>
      <td>$> 1$</td>
      <td>Iran wins the attrition race</td>
      <td>Hormuz tips the balance — Coalition exhausts first.</td>
    </tr>
  </tbody>
</table>
</div>

**Exhaustion times.** Setting $E_C(\tau^*) = E_{\min}$ and substituting $u = e^{\omega\tau^*}$:

$$A_2 u^2 - E_{\min}\,u + B_2 = 0 \implies \tau_C^* = \frac{1}{\omega}\ln\!\left(\frac{E_{\min} + \sqrt{E_{\min}^2 - 4A_2 B_2}}{2A_2}\right)$$

Iran's exhaustion time $\tau_I^*$ follows analogously. Total war duration: $T^* = t_H + \min(\tau_C^*, \tau_I^*)$.

---

## Joint Polymarket Calibration

### The Joint Decomposition

**Modeling assumption:** within this model, ceasefire follows Hormuz activation. We therefore write:

$$\underbrace{P_{\text{cf}}(T)}_{\text{ceasefire by }T} = \underbrace{P_H(T)}_{\text{Hormuz by }T} \cdot \underbrace{P_{\text{cf}|H}(T)}_{\text{ceasefire}\mid\text{Hormuz by }T}$$

This is a modeling choice, not an identity. A more general form would add a $P(\lnot H) \cdot P_{\text{cf}|\lnot H}$ term for ceasefire without Hormuz. We address this in the scenarios below (the quick-collapse scenario is precisely that case — Iran exhausts before activating Hormuz). For the March and June windows where both markets overlap, the factorisation provides a clean joint constraint.

<div class="table-responsive">
<table class="table table-bordered text-center">
  <thead>
    <tr>
      <th>Date</th>
      <th>$P_{\text{cf}}(T)$</th>
      <th>$P_H(T)$</th>
      <th>$P_{\text{cf}|H}(T)$</th>
      <th>Note</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mar 31</td>
      <td>45%</td>
      <td>63%</td>
      <td>71%</td>
      <td>Upper bound — timing within the window tightens this (see below)</td>
    </tr>
    <tr>
      <td>Jun 30</td>
      <td>69%</td>
      <td>69%</td>
      <td>≈100% (within rounding)</td>
      <td>June window wide enough for post-Hormuz dynamics to fully resolve</td>
    </tr>
  </tbody>
</table>
</div>

A note on the March 71% figure: the factorisation treats Hormuz as activating at the start of the window. If it activates late in March — say March 28 — very little time remains for ceasefire before March 31. The true conditional probability is therefore somewhat lower than 71%; the figure is best read as an upper bound. The June figure is robust to this concern since the window is four months wide.

### Parameter Estimation

Iran's initial resources $\rho$ are unknown to both sides. We model this with a **Beta(2, 5) prior** — chosen because it produces calibration residuals below 0.5pp across all seven Polymarket data points (mean $\approx 0.29$, mode $\approx 0.17$, substantial right tail). Parameters are estimated by minimising squared error across the seven calibration horizons:

$$P_{\text{cf}}(T) = \int_0^1 \mathbf{1}[T^*(\rho) \leq T] \cdot \text{Beta}(\rho;\,2,5)\; d\rho$$

$$P_H(T) = \int_0^1 \mathbf{1}[t_H(\rho) \leq T] \cdot \text{Beta}(\rho;\,2,5)\; d\rho$$

Five ceasefire data points and two Hormuz data points give seven calibration equations for four parameters — over-identified by three, providing three independent consistency checks.

**Jointly fitted parameters:**

<div class="table-responsive">
<table class="table table-bordered text-center">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Fitted value</th>
      <th>Interpretation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\omega$</td>
      <td>0.051 day$^{-1}$</td>
      <td>Mutual damage exchange rate — in the symmetric-decay limit ($\gamma=1$, $\rho=1$), resources halve every $\ln 2/0.051 \approx 13.6$ days</td>
    </tr>
    <tr>
      <td>$\gamma$</td>
      <td>2.1</td>
      <td>Precision differential — each Coalition strike unit depletes Iran 2.1× more than an equivalent Iranian strike depletes Coalition</td>
    </tr>
    <tr>
      <td>$\theta$</td>
      <td>0.22</td>
      <td>Hormuz threshold — Iran activates when roughly 78% of its initial capacity is consumed (normalised)</td>
    </tr>
    <tr>
      <td>$c_C$</td>
      <td>0.038 day$^{-1}$</td>
      <td>Hormuz drain on Coalition — depletes Coalition effective capacity by ~3.8% per day in normalised units</td>
    </tr>
  </tbody>
</table>
</div>

**Model fit:**

<div class="table-responsive">
<table class="table table-bordered text-center">
  <thead>
    <tr>
      <th>Market</th>
      <th>Date</th>
      <th>Days</th>
      <th>Observed $P$</th>
      <th>Model $P$</th>
      <th>Residual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">Ceasefire</td>
      <td>Mar 6</td><td>6</td><td>4%</td><td>3.9%</td><td>+0.1pp</td>
    </tr>
    <tr>
      <td>Mar 15</td><td>15</td><td>21%</td><td>20.6%</td><td>+0.4pp</td>
    </tr>
    <tr>
      <td>Mar 31</td><td>31</td><td>45%</td><td>44.8%</td><td>+0.2pp</td>
    </tr>
    <tr>
      <td>Apr 30</td><td>61</td><td>59%</td><td>59.3%</td><td>−0.3pp</td>
    </tr>
    <tr>
      <td>Jun 30</td><td>122</td><td>69%</td><td>69.1%</td><td>−0.1pp ✓</td>
    </tr>
    <tr>
      <td rowspan="2">Hormuz</td>
      <td>Mar 31</td><td>31</td><td>63%</td><td>62.7%</td><td>+0.3pp ✓</td>
    </tr>
    <tr>
      <td>Jun 30</td><td>122</td><td>69%</td><td>69.2%</td><td>−0.2pp ✓</td>
    </tr>
  </tbody>
</table>
</div>

All seven data points fit within 0.5pp. The three consistency checks are all near zero.

---

## Bayesian Inference: Each Side Estimating the Other

Both sides know their own resources but not the opponent's. The observable signal is attack intensity — $a_C(t) = \beta_C E_C(t)$ for Iran watching Coalition, and vice versa.

This maps onto the Slantchev-Tarar (2011) and Lindsey (2015) frameworks: private capacity generates gradual type revelation through observed actions. Each side updates its estimate of the other's initial endowment $\rho$ from the trajectory of attack intensity.

**Iran's inference.** Iran observes Coalition attack intensities $a_C(t_1)$ and $a_C(t_2)$. Given the Phase 1 functional form $E_C(t) = A_1 e^{\omega t} + B_1 e^{-\omega t}$, Iran solves — in the noiseless, known-parameter limit — the linear system:

$$\begin{pmatrix} e^{\omega t_1} & e^{-\omega t_1} \\ e^{\omega t_2} & e^{-\omega t_2} \end{pmatrix} \begin{pmatrix} A_1 \\ B_1 \end{pmatrix} = \frac{1}{\beta_C}\begin{pmatrix} a_C(t_1) \\ a_C(t_2) \end{pmatrix}$$

Two equations, two unknowns — Iran recovers $E_C^0 = A_1 + B_1$ from two observations. In practice, $\omega$ and $\beta_C$ are not directly observable, so this reconstruction is approximate; additional observations reduce estimation error.

**The Hormuz signal.** Hormuz activation at $t_H$ is publicly observable. Coalition's posterior on $E_I$ collapses from the Beta(2,5) prior to near a point mass: $E_I(t_H) \approx \theta$. Iran reveals its remaining capacity the moment it escalates most dramatically. Hormuz activation is simultaneously Iran's best defensive move and its clearest distress signal.

**Coalition's updated $\Lambda$.** Post-$t_H$, Coalition knows $\theta$ and $E_C^H$ and can estimate $\Lambda$. If $\Lambda < 1$, Coalition has strong incentive to hold on. If $\Lambda > 1$, the attrition math favours Iran — consistent with Huangfu et al.'s (2023) finding that resource-rich players may rationally concede when facing an asymmetric counter-weapon.

---

## What the Model Predicts

Given the jointly fitted parameters and $\rho \sim \text{Beta}(2,5)$, three scenarios emerge (approximate, rounded to sum to 100%):

<div class="table-responsive">
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Scenario</th>
      <th>$\rho$ range</th>
      <th>$\Lambda$ post-Hormuz</th>
      <th>Predicted outcome</th>
      <th>Probability (approx.)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Quick collapse</strong></td>
      <td>$\rho < 0.15$</td>
      <td>Hormuz never activated</td>
      <td>Iran exhausts before reaching $\theta$. Ceasefire before day 25 on Coalition terms.</td>
      <td>~28%</td>
    </tr>
    <tr>
      <td><strong>Hormuz tipping point</strong></td>
      <td>$0.15 \leq \rho \leq 0.35$</td>
      <td>$\approx 1$</td>
      <td>Iran activates Hormuz around day 15–30. $\Lambda$ near 1 — outcome sensitive to small variations. Ceasefire day 25–55.</td>
      <td>~51%</td>
    </tr>
    <tr>
      <td><strong>Prolonged attrition</strong></td>
      <td>$\rho > 0.35$</td>
      <td>$> 1$</td>
      <td>Hormuz tips balance toward Iran. Coalition exhausts first or seeks negotiated exit before day 90.</td>
      <td>~21%</td>
    </tr>
  </tbody>
</table>
</div>

The most likely scenario — 51% — is the tipping-point regime where the outcome is highly sensitive to small differences in $\rho$ and Hormuz timing. This is consistent with genuine market uncertainty: the fitted model puts the median ceasefire at day 32, right at the March 31 window where Polymarket assigns 45%.

**Key observable prediction.** If Hormuz is not activated by day 20, this substantially lowers posterior mass above $\rho = 0.15$ — making the quick-collapse scenario increasingly likely and ceasefire imminent on Coalition terms. If Hormuz is activated, watch $\Lambda$: Coalition continuing to strike at high intensity post-$t_H$ signals $\Lambda < 1$ — they believe they can outlast Iran even with the oil shock. A Coalition that visibly slows its strikes after Hormuz activation signals $\Lambda > 1$ — they are seeking an exit before exhaustion.

---

## Limitations

This model captures the core dynamic but still abstracts away a great deal.

<div class="table-responsive">
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Omitted variable</th>
      <th>How it would change the model</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Discrete shocks</strong> — assassination, coup, nuclear threshold crossing</td>
      <td>Effective capacity drops discontinuously. The smooth ODE cannot model this. Would require a jump-diffusion process.</td>
    </tr>
    <tr>
      <td><strong>Proxy reactivation</strong> — Hezbollah, Houthi, Iraqi militia re-entering</td>
      <td>Adds a third player whose resources are separate from $E_I$. The two-player model misses this entirely.</td>
    </tr>
    <tr>
      <td><strong>Resupply</strong> — US restocking munitions, Iran receiving Chinese materiel</td>
      <td>Adds a positive term to $\dot{R}_i$, converting the depletion ODE into a net-depletion equation. Resupply rates are private information.</td>
    </tr>
    <tr>
      <td><strong>Degrading precision</strong> — effectiveness falls as high-value targets are exhausted</td>
      <td>Time-varying $k_C$, $k_I$ — no closed-form solution, requires numerical integration throughout.</td>
    </tr>
    <tr>
      <td><strong>Strategic Hormuz timing</strong> — Iran optimises when to deploy rather than using a fixed threshold $\theta$</td>
      <td>Optimal stopping problem for Iran. Full solution would connect to the Harsanyi incomplete-information framework — a future post.</td>
    </tr>
    <tr>
      <td><strong>Polymarket reliability</strong> — markets can be manipulated or reflect insider information</td>
      <td>Polymarket's Iran bets hit $529M with documented concerns about new wallets (Bloomberg, 2026). If prices reflect insider knowledge rather than rational aggregation, the calibration inherits that bias.</td>
    </tr>
  </tbody>
</table>
</div>

The model's value is in what it isolates: the race between Coalition precision and Iranian asymmetric retaliation, and the sharp information revelation when Hormuz activates. The two prediction markets are not independent data sources — they are two windows onto the same underlying dynamic. Reading them jointly reveals structure that neither reveals alone.

---

## References

- Bloomberg (2026). Polymarket Iran Bets Hit $529 Million as New Wallets Raise Insider Concerns. February 28, 2026.
- Han, B. (2018). The role and welfare rationale of secondary sanctions: A theory and a case study of the US sanctions targeting Iran. *Conflict Management and Peace Science*, 35(5), 474–502. DOI: 10.1177/0738894216650836.
- Huangfu, B., Ghosh, G., and Liu, H. (2023). Resource inequality in the war of attrition. *International Journal of Game Theory*, 52, 33–61. DOI: 10.1007/s00182-022-00809-0.
- Katzman, K. et al. (2012). Iran's Threat to the Strait of Hormuz. Congressional Research Service Report R42335.
- Kress, M. (2020). Lanchester Models for Irregular Warfare. *Mathematics*, 8(5), 737. DOI: 10.3390/math8050737.
- Lindsey, D. (2015). Military Strategy, Private Information, and War. *International Studies Quarterly*, 59(4), 629–640. DOI: 10.1111/isqu.12208.
- Mellers, B., Stone, E., Murray, T. et al. (2015). Identifying and Cultivating Superforecasters as a Method of Improving Probabilistic Predictions. *Perspectives on Psychological Science*, 10(3), 267–281. DOI: 10.1177/1745691615577794.
- Shariatinia, M. and Azizi, H. (2021). Shifting Threats and Strategic Adjustment in Iran's Foreign Policy: The Case of the Strait of Hormuz. *British Journal of Middle Eastern Studies*, 49(5). DOI: 10.1080/13530194.2021.1874873.
- Slantchev, B.L. and Tarar, A. (2011). Mutual Optimism as a Rationalist Cause of War. *American Journal of Political Science*, 55(1), 135–148. DOI: 10.1111/j.1540-5907.2010.00475.x.
- U.S. Energy Information Administration (2024). Amid regional conflict, the Strait of Hormuz remains critical oil chokepoint. EIA.gov.
- U.S. Senate Joint Economic Committee (2007). The Strait of Hormuz and the Threat of an Oil Shock.
- Wirl, F. and Yegorov, Y. (2016). Iran's Nuclear Program and the West's Response: A Game Theoretic Approach. In *Dynamic Modeling, Empirical Macroeconomics, and Finance*. Springer. DOI: 10.1007/978-3-319-39887-7_2.
