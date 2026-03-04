# Blog Post Design: The Attrition Game

**Date:** 2026-03-03
**Status:** Approved — ready for implementation

---

## Title

*The Attrition Game: Resource Depletion, Hormuz, and the Mathematics of War Exhaustion*

---

## Model Choices

| Choice | Value | Rationale |
|---|---|---|
| $\rho$ distribution | Beta(2,5) | Iran likely has 20–40% of Coalition capacity, long right tail |
| Exchange asymmetry | $k_C = \gamma k_I$, $\gamma > 1$ | Coalition strikes more precise per unit |
| Hormuz trigger | Endogenous at $E_I < \theta$ | Last resort weapon, not deployed from day one |
| Support interaction | Additive $E = R + \alpha S$ | Tractable, linear ODEs |
| China floor | $S_I \geq S_{\min}$ | China won't fully abandon Iran |
| Ceasefire condition | Resource exhaustion $E_i < E_{\min}$ | Leaders want to win, not optimise |

---

## Two-Phase ODE System

### Phase 1 (no Hormuz, $E_I \geq \theta$)

$$\dot{E}_C = -k_C E_I, \quad \dot{E}_I = -k_I E_C$$

Solution with $E_C^0 = 1$, $E_I^0 = \rho$, $\omega = \sqrt{k_C k_I} = k_I\sqrt{\gamma}$:

$$E_C(t) = A_1 e^{\omega t} + B_1 e^{-\omega t}$$

$$A_1 = \frac{1 - \sqrt{\gamma}\rho}{2}, \quad B_1 = \frac{1 + \sqrt{\gamma}\rho}{2}$$

$$E_I(t) = \rho - \frac{1}{\sqrt{\gamma}}\left[A_1(e^{\omega t}-1) + B_1(1-e^{-\omega t})\right]$$

Phase ends at $t_H$: $E_I(t_H) = \theta$

### Phase 2 (Hormuz active, $E_I < \theta$)

$$\dot{E}_C = -k_C E_I - c_C, \quad \dot{E}_I = -k_I E_C$$

Solution with $\tau = t - t_H$, ICs $(E_C^H, \theta)$:

$$E_C(\tau) = A_2 e^{\omega\tau} + B_2 e^{-\omega\tau}$$

$$A_2 = \frac{1}{2}\left(E_C^H - \frac{k_C\theta + c_C}{\omega}\right), \quad B_2 = \frac{1}{2}\left(E_C^H + \frac{k_C\theta + c_C}{\omega}\right)$$

---

## Key Quantities

**Balance ratio (Phase 2):**

$$\Lambda = \frac{k_C\theta + c_C}{\omega E_C^H}$$

- $\Lambda < 1$: Coalition outlasts Iran
- $\Lambda > 1$: Hormuz tips balance, Iran wins the attrition race

**Exhaustion times:** Solved from $Au^2 - E_{\min}u + B = 0$ where $u = e^{\omega t}$

**Ceasefire:** $\tau = \min(t_C^*, t_I^*)$

---

## Selective Closure Dominance

Proof: selective closure ($\chi=1$) gives same $\dot{S}_C$ as full closure but preserves $S_I$.
Therefore $E_I$ is strictly higher under selective closure for all $t > t_H$.
Selective closure weakly dominates full closure. QED.

---

## Polymarket Calibration

$$P(\text{ceasefire by }T) = \int_0^1 \mathbf{1}[\tau(\rho) \leq T] \cdot \text{Beta}(\rho; 2, 5)\, d\rho$$

4 free parameters: $(\omega, \gamma, \theta, c_C)$. 5 Polymarket data points. Over-identified by 1.

---

## Bayesian Inference

Iran observes $a_C(t) = \beta_C E_C(t)$. Two observations solve:

$$\begin{pmatrix} e^{\omega t_1} & e^{-\omega t_1} \\ e^{\omega t_2} & e^{-\omega t_2} \end{pmatrix} \begin{pmatrix} A_1 \\ B_1 \end{pmatrix} = \frac{1}{\beta_C}\begin{pmatrix} a_C(t_1) \\ a_C(t_2) \end{pmatrix}$$

Then $E_C^0 = A_1 + B_1$.

Hormuz activation at $t_H$ is publicly observable — collapses Coalition's uncertainty about Iran's resource level to $E_I(t_H) = \theta$.

---

## Post Structure

1. Opening — same war, different question: not when does it end, but how
2. Section 1: State variables and the two-resource model
3. Section 2: Phase 1 — the baseline attrition race
4. Section 3: Phase transition — Iran reaches for Hormuz
5. Section 4: Selective closure dominance proof
6. Section 5: Phase 2 — the tipped balance
7. Section 6: Polymarket calibration
8. Section 7: Bayesian inference
9. Section 8: Predictions and limitations

---

## Tags & Category

- Tags: `game-theory`, `geopolitics`, `prediction-markets`, `war-of-attrition`, `iran`
- Category: `essays`
