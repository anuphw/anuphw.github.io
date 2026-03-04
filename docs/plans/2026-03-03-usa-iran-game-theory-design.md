# Blog Post Design: The Ceasefire Equation

**Date:** 2026-03-03
**Status:** Approved — ready for implementation
**Future extension:** Harsanyi incomplete information game (Option C) — separate post

---

## Title

*The Ceasefire Equation: Game Theory, Prediction Markets, and the USA–Iran War*

---

## Audience & Tone

Rigorous. Assumes familiarity with probability and basic algebra. Full game-theoretic
treatment with formal notation. Tables with borders throughout. No hand-waving on the math.

---

## Players

- **Coalition** = USA + Israel (treated as single player)
- **Iran**

---

## The Game (Strategic Form)

Simultaneous-move game. Each round both players choose **Continue** or **Ceasefire**.
Official ceasefire requires both to choose Ceasefire simultaneously.

### Payoff Matrix (Coalition, Iran)

|                          | **Iran: Continue**  | **Iran: Ceasefire** |
|--------------------------|---------------------|---------------------|
| **Coalition: Continue**  | $(a,\ e)$           | $(b,\ f)$           |
| **Coalition: Ceasefire** | $(c,\ g)$           | $(d,\ h)$           |

### Payoff Definitions

| Symbol | Player    | Meaning                                                                 |
|--------|-----------|-------------------------------------------------------------------------|
| $a$    | Coalition | Ongoing war: military cost offset by probability of achieving objectives |
| $b$    | Coalition | Iran folds unilaterally while Coalition continues — maximum gain        |
| $c$    | Coalition | Coalition offers ceasefire while Iran continues — strategic humiliation  |
| $d$    | Coalition | Mutual ceasefire — partial objectives achieved, stability restored      |
| $e$    | Iran      | Absorbs strikes, retaliates — maximum damage but regime survival signal |
| $f$    | Iran      | Accepts while strikes continue — humiliation + physical damage          |
| $g$    | Iran      | Coalition blinks while Iran continues — best outcome (survival + no deal)|
| $h$    | Iran      | Mutual ceasefire — partial survival, some concessions required          |

### Payoff Ordering (assumed)

- Coalition: $b > d > a > c$
- Iran: $g > e > h > f$

---

## Mixed Strategy Nash Equilibrium

Let $p$ = probability Coalition plays Continue, $q$ = probability Iran plays Continue.

Indifference conditions:

$$p^* = \frac{d - c}{(a - b - c + d)}, \quad q^* = \frac{h - f}{(e - f - g + h)}$$

---

## Connecting to Polymarket

Per-round ceasefire probability (both play Ceasefire simultaneously):

$$r = (1 - p^*)(1 - q^*)$$

Cumulative ceasefire probability by day $T$ (geometric waiting time):

$$P(\text{ceasefire by } T) = 1 - (1 - r)^T$$

Inverse (back-calculate $r$ from market data):

$$r = 1 - (1 - P)^{1/T}$$

---

## Polymarket Data & Implied r

| Date       | Days (T) | Cumulative P | Implied r (per day) |
|------------|----------|--------------|---------------------|
| Mar 6      | 6        | 4%           | 0.68%               |
| Mar 15     | 15       | 21%          | 1.56%               |
| Mar 31     | 31       | 45%          | 1.90%               |
| Apr 30     | 61       | 59%          | 1.46%               |
| Jun 30     | 122      | 69%          | 0.93%               |

---

## Bayesian Updating Narrative

$r$ is not constant — it rises then falls. Interpretation by window:

| Window       | Implied r | What both sides are learning                                         |
|--------------|-----------|----------------------------------------------------------------------|
| Week 1       | 0.68%     | Maximum resolve signalling. No updating off priors yet.              |
| Weeks 2–4    | peaks 1.9%| Damage accumulating. Iranian costs $e$ revealed higher than priced.  |
|              |           | Coalition costs $a$ rising (oil shock, Gulf allies pressured).       |
|              |           | Both $p^*$ and $q^*$ fall → $r$ rises.                              |
| April onward | falling   | War fatigue without resolution. Costs absorbed as new normal.        |
|              |           | Neither side has dominant reason to stop. $r$ falls back.            |

---

## The Prediction

- Peak $r$ ≈ 1.9% is around day 15–31 (mid–late March) — highest per-day ceasefire probability
- Conditional on no ceasefire by March 31 (55% chance), $r$ declining → entrenchment
- Each day past April 30 without agreement makes near-term ceasefire significantly less likely
- Model predicts: **highest-probability ceasefire window is mid-to-late March 2026**

---

## Post Structure

1. **Opening** — Feb 28 strikes, active war, one question: when does it stop?
2. **Section 1: The Game** — players, strategies, payoff matrix (bordered table)
3. **Section 2: Nash Equilibrium** — derive $p^*$ and $q^*$, indifference conditions
4. **Section 3: Connecting to Polymarket** — introduce $r$, geometric formula, Polymarket data table
5. **Section 4: Bayesian Updating** — $r$ time series table, week-by-week narrative
6. **Section 5: The Prediction** — conditional probabilities, entrenchment scenario
7. **Closing** — the math already has an answer; we just have to read it

---

## Tags & Category

- Tags: `game-theory`, `geopolitics`, `prediction-markets`, `nash-equilibrium`, `iran`, `usa`
- Category: `essays`

---

## Future Post (Option C)

Harsanyi incomplete information game:
- Each player has private type (resolve level: high vs low)
- Prior beliefs over opponent types
- Polymarket probabilities as posteriors over types
- Derive Bayesian Nash Equilibrium
- Show how type uncertainty changes equilibrium strategies vs the complete information case
