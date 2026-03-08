---
layout: post
title: "U.S.–Iran War 2026 — Strategic Analysis Dashboard (Day 9)"
description: "Day 9 — Evidence-based strategic modeling: military capabilities, Hormuz scenarios, escalation paths, economic consequences, and probabilistic forecasting."
date: 2026-03-08 09:00:00 +0000
tags: [geopolitics, iran, us-iran-war, conflict-analysis, military-strategy, middle-east, hormuz, strategic-analysis]
categories: analysis
---

<style>
/* ── Reset & variables ──────────────────────────────────── */
:root{
  --bg:#0a0e1a;--panel:#111827;--border:#1f2d45;
  --red:#e63946;--blue:#3b82f6;--gold:#f59e0b;
  --green:#10b981;--orange:#f97316;--purple:#8b5cf6;
  --text:#e2e8f0;--muted:#94a3b8;--card:#1a2540;
}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;font-size:14px;line-height:1.6;margin:0;padding:0;}
/* override Cayman theme defaults */
.page-header{display:none}
.main-content{max-width:100%!important;padding:0!important;margin:0!important;font-size:inherit!important;}
.main-content h1,.main-content h2,.main-content h3,.main-content h4,.main-content p,.main-content ul,.main-content ol,.main-content table{all:revert;}
.site-footer{background:#060a12;border-top:1px solid var(--border);color:var(--muted);font-size:11px;padding:12px 24px;}
*{box-sizing:border-box;}

/* ── Header ─────────────────────────────────────────────── */
.dash-header{background:linear-gradient(135deg,#0f1b2d,#1a0a0a);border-bottom:2px solid var(--red);padding:16px 28px;display:flex;align-items:center;gap:14px;flex-wrap:wrap;}
.dash-header h1{font-size:19px;font-weight:700;color:var(--text);margin:0;}
.dash-header .sub{color:var(--muted);font-size:12px;margin-top:3px;}
.badge{background:var(--red);color:#fff;font-size:10px;font-weight:700;padding:2px 7px;border-radius:3px;letter-spacing:1px;animation:blink 2s infinite;}
.badge.gold{background:var(--gold);color:#000;}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.55}}
.datestamp{margin-left:auto;color:var(--gold);font-size:12px;font-weight:600;}

/* ── Nav tabs ────────────────────────────────────────────── */
.dash-nav{background:var(--panel);border-bottom:1px solid var(--border);display:flex;overflow-x:auto;padding:0 14px;gap:2px;position:sticky;top:0;z-index:100;}
.dash-nav button{background:none;border:none;color:var(--muted);padding:11px 14px;font-size:11px;font-weight:700;cursor:pointer;border-bottom:3px solid transparent;white-space:nowrap;transition:.2s;text-transform:uppercase;letter-spacing:.5px;}
.dash-nav button:hover{color:var(--text);}
.dash-nav button.active{color:var(--red);border-bottom-color:var(--red);}

/* ── Layout ──────────────────────────────────────────────── */
.dash-main{max-width:1380px;margin:0 auto;padding:22px 22px;}
.tab-pane{display:none}.tab-pane.active{display:block}

/* ── Typography ──────────────────────────────────────────── */
.dash-main h2{font-size:17px;font-weight:700;color:var(--text);display:flex;align-items:center;gap:8px;margin:0 0 16px;}
.dash-main h2::before{content:'';display:block;width:4px;height:20px;background:var(--red);border-radius:2px;flex-shrink:0;}
.dash-main h3{font-size:13px;font-weight:700;color:var(--gold);text-transform:uppercase;letter-spacing:.5px;margin:0 0 8px;}
.dash-main p{color:var(--muted);margin:0 0 9px;}
.dash-main ul,.dash-main ol{color:var(--muted);padding-left:18px;margin:0 0 9px;}
.dash-main li{margin-bottom:3px;}

/* ── Grid ────────────────────────────────────────────────── */
.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-bottom:14px;}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:14px;}
@media(max-width:860px){.g2,.g3,.g4{grid-template-columns:1fr;}}

/* ── Cards ───────────────────────────────────────────────── */
.card{background:var(--card);border:1px solid var(--border);border-radius:7px;padding:15px;}
.card.cl-r{border-left:4px solid var(--red)}.card.cl-b{border-left:4px solid var(--blue)}
.card.cl-g{border-left:4px solid var(--gold)}.card.cl-gr{border-left:4px solid var(--green)}
.card.cl-o{border-left:4px solid var(--orange)}.card.cl-p{border-left:4px solid var(--purple)}

/* ── Stats row ───────────────────────────────────────────── */
.stats{display:flex;gap:13px;margin-bottom:18px;flex-wrap:wrap;}
.stat{background:var(--card);border:1px solid var(--border);border-radius:7px;padding:13px 16px;flex:1;min-width:130px;}
.stat .v{font-size:24px;font-weight:800;line-height:1;}
.stat .l{font-size:10px;color:var(--muted);margin-top:4px;text-transform:uppercase;letter-spacing:.5px;}
.s-r .v{color:var(--red)}.s-g .v{color:var(--gold)}.s-b .v{color:var(--blue)}
.s-gr .v{color:var(--green)}.s-o .v{color:var(--orange)}.s-p .v{color:var(--purple)}

/* ── Alerts ──────────────────────────────────────────────── */
.alert{border-radius:6px;padding:11px 15px;margin-bottom:14px;font-size:13px;display:flex;gap:9px;align-items:flex-start;}
.alert.a-r{background:rgba(230,57,70,.1);border:1px solid rgba(230,57,70,.3);}
.alert.a-g{background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.3);}
.alert.a-b{background:rgba(59,130,246,.1);border:1px solid rgba(59,130,246,.3);}
.alert .ic{font-size:15px;flex-shrink:0;}

/* ── Tables ──────────────────────────────────────────────── */
.dash-main table{width:100%;border-collapse:collapse;margin-bottom:18px;font-size:12px;}
.dash-main th{background:#1f2d45;color:var(--text);padding:9px 11px;text-align:left;font-size:10px;text-transform:uppercase;letter-spacing:.5px;}
.dash-main td{padding:8px 11px;border-bottom:1px solid var(--border);color:var(--muted);vertical-align:top;}
.dash-main tr:hover td{background:#1a2540;color:var(--text);}
td.actor{color:var(--text);font-weight:600;}
td.hi{color:var(--red);font-weight:600;}td.med{color:var(--gold);font-weight:600;}td.lo{color:var(--green);font-weight:600;}

/* ── Probability bars ────────────────────────────────────── */
.pb{display:flex;align-items:center;gap:9px;margin-bottom:7px;}
.pb .pl{width:210px;font-size:12px;color:var(--muted);flex-shrink:0;}
.pb .bg{flex:1;background:var(--border);border-radius:4px;height:9px;}
.pb .fill{height:9px;border-radius:4px;}
.pb .pct{width:36px;text-align:right;font-size:11px;font-weight:700;}

/* ── Scenario cards ──────────────────────────────────────── */
.sc{background:var(--card);border:1px solid var(--border);border-radius:7px;padding:15px;margin-bottom:12px;}
.sc-head{display:flex;align-items:center;gap:11px;margin-bottom:9px;}
.sc-tag{background:var(--red);color:#fff;font-size:10px;font-weight:700;padding:2px 7px;border-radius:3px;letter-spacing:1px;flex-shrink:0;}
.sc-tag.b{background:var(--blue)}.sc-tag.g{background:var(--gold);color:#000}
.sc-tag.gr{background:var(--green);color:#000}.sc-tag.o{background:var(--orange);color:#000}
.sc-tag.p{background:var(--purple)}
.sc-meta{display:flex;gap:14px;margin-top:9px;flex-wrap:wrap;}
.sc-meta .mk{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;}
.sc-meta .mv{color:var(--text);font-weight:600;font-size:12px;}

/* ── Ladder / timeline ───────────────────────────────────── */
.ladder{position:relative;padding-left:22px;}
.ladder-line{position:absolute;left:5px;top:6px;bottom:6px;width:1px;background:var(--border);}
.ladder-item{display:flex;gap:14px;align-items:flex-start;margin-bottom:0;}
.ladder-dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px;position:relative;z-index:1;}
.ladder-body{flex:1;padding-bottom:12px;border-bottom:1px solid var(--border);}
.ladder-item:last-child .ladder-body{border-bottom:none;}
.ladder-step{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;}
.ladder-desc{font-size:13px;color:var(--text);}

/* ── Tags ────────────────────────────────────────────────── */
.tag{display:inline-block;font-size:10px;font-weight:700;padding:2px 6px;border-radius:3px;margin:0 3px 3px 0;}
.tag.r{background:rgba(230,57,70,.2);color:var(--red);border:1px solid var(--red);}
.tag.b{background:rgba(59,130,246,.2);color:var(--blue);border:1px solid var(--blue);}
.tag.g{background:rgba(245,158,11,.2);color:var(--gold);border:1px solid var(--gold);}
.tag.gr{background:rgba(16,185,129,.2);color:var(--green);border:1px solid var(--green);}
.tag.o{background:rgba(249,115,22,.2);color:var(--orange);border:1px solid var(--orange);}
.tag.p{background:rgba(139,92,246,.2);color:var(--purple);border:1px solid var(--purple);}

/* ── Code/tree ───────────────────────────────────────────── */
.tree{font-family:monospace;font-size:12px;color:var(--muted);background:#0f1622;border:1px solid var(--border);border-radius:6px;padding:15px;overflow-x:auto;line-height:2;}
.tk{color:var(--gold)}.tv{color:var(--green)}.tw{color:var(--red)}.tm{color:var(--orange)}

/* ── Advantage pill ──────────────────────────────────────── */
.adv{font-size:10px;padding:2px 5px;border-radius:3px;font-weight:700;}
.adv-us{background:rgba(96,165,250,.2);color:#60a5fa;}
.adv-ir{background:rgba(248,113,113,.2);color:#f87171;}
.adv-eq{background:rgba(148,163,184,.2);color:#94a3b8;}

/* ── Sources ─────────────────────────────────────────────── */
.sources{margin-top:28px;padding-top:14px;border-top:1px solid var(--border);}
.sources p{font-size:11px;color:var(--muted);margin-bottom:4px;}
.sources a{color:var(--blue);font-size:11px;text-decoration:none;}
.sources a:hover{text-decoration:underline;}
</style>

<!-- ═══ HEADER ═══════════════════════════════════════════ -->
<div class="dash-header">
  <div>
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px;">
      <span class="badge">LIVE CONFLICT — DAY 9</span>
      <span class="badge gold">ANALYSIS</span>
    </div>
    <h1>U.S.–Iran War 2026 — Strategic Analysis Dashboard</h1>
    <div class="sub">Evidence-based strategic modeling &nbsp;|&nbsp; Conflict began 28 February 2026</div>
  </div>
  <div class="datestamp">8 March 2026 · 09:00 UTC</div>
</div>

<!-- ═══ NAV ═══════════════════════════════════════════════ -->
<nav class="dash-nav" id="dashNav">
  <button class="active" onclick="showTab('overview',this)">Overview</button>
  <button onclick="showTab('objectives',this)">Strategic Objectives</button>
  <button onclick="showTab('military',this)">Military Capability</button>
  <button onclick="showTab('hormuz',this)">Hormuz Scenarios</button>
  <button onclick="showTab('dynamics',this)">War Dynamics</button>
  <button onclick="showTab('iran',this)">Iran's Strategy</button>
  <button onclick="showTab('escalation',this)">Escalation Paths</button>
  <button onclick="showTab('economic',this)">Economic Impact</button>
  <button onclick="showTab('historical',this)">Historical Analogies</button>
  <button onclick="showTab('forecast',this)">Forecast</button>
  <button onclick="showTab('unknowns',this)">Key Unknowns</button>
</nav>

<div class="dash-main">

<!-- ════════════════════════════════ TAB: OVERVIEW ══════ -->
<div id="tab-overview" class="tab-pane active">

<h2>Situation Overview — Day 9</h2>

<div class="alert a-r"><span class="ic">🔴</span><div><strong>Critical development:</strong> Supreme Leader Ali Khamenei confirmed killed in the opening US strike, 28 Feb. IRGC commander Pakpour and security adviser Shamkhani also killed. Iran operating under an Interim Leadership Council (constitution Article 111). Strait of Hormuz effectively closed — tanker traffic near zero. WTI crude up 35.6% in one week — the largest weekly gain in the contract's history (since 1983).</div></div>

<div class="stats">
  <div class="stat s-r"><div class="v">1,332+</div><div class="l">Killed in Iran (military + civilian)</div></div>
  <div class="stat s-g"><div class="v">~2,000</div><div class="l">US/Israeli strikes conducted</div></div>
  <div class="stat s-o"><div class="v">2,500+</div><div class="l">Iranian missiles & drones fired</div></div>
  <div class="stat s-b"><div class="v">+35.6%</div><div class="l">WTI crude — record weekly gain</div></div>
  <div class="stat s-gr"><div class="v">~0</div><div class="l">Tanker transits/day thru Hormuz</div></div>
  <div class="stat s-p"><div class="v">Day 9</div><div class="l">No ceasefire reached</div></div>
</div>

<div class="g2">
<div class="card cl-r">
<h3>US / Israel Actions</h3>
<ul>
<li>~900 strikes in first 12 hours; ~2,000 total by Day 3</li>
<li>Targets: Tehran, Isfahan, Qom, Karaj, Kermanshah</li>
<li>Killed: Khamenei, IRGC chief Pakpour, adviser Shamkhani</li>
<li>IAEA: nuclear installations <em>not</em> confirmed hit as of March 2</li>
<li>Israel expanding strikes to Beirut from March 2</li>
<li>Trump demands "unconditional surrender" (March 6)</li>
<li>Senate war powers vote failed — strikes continue</li>
</ul>
</div>
<div class="card cl-o">
<h3>Iran's Response</h3>
<ul>
<li>500+ ballistic/naval missiles + ~2,000 drones by Day 5</li>
<li>Targets: Israel, US bases in Qatar, Bahrain, UAE, Kuwait, Iraq, Jordan, Saudi Arabia</li>
<li>Hormuz closed — 150+ tankers anchored outside strait</li>
<li>Energy facilities in Gulf attacked</li>
<li>Interim Leadership Council formed; IRGC pushing Mojtaba Khamenei as successor</li>
<li>Iran vows: <strong>no unconditional surrender</strong></li>
<li>Hezbollah entered March 2 — limited anti-tank fire on northern Israel</li>
</ul>
</div>
</div>

<div class="g3">
<div class="card cl-b">
<h3>Great Power Reactions</h3>
<ul>
<li><strong>China:</strong> Condemned strikes, called ceasefire — not intervening militarily</li>
<li><strong>Russia:</strong> Expressed condolences; called strikes illegal — not intervening</li>
<li><strong>UN Security Council:</strong> Emergency meeting; no binding resolution</li>
<li><strong>Oman:</strong> Attempted mediation — "active negotiations abandoned"</li>
</ul>
</div>
<div class="card cl-g">
<h3>Regional Actors</h3>
<ul>
<li><strong>Hezbollah:</strong> Entered March 2 (limited); Lebanon govt banning Hezbollah military activities</li>
<li><strong>Gulf states:</strong> US bases being struck; airspace closures in UAE/Qatar/Kuwait</li>
<li><strong>Iraq:</strong> US base hit by drones; Shia militias active</li>
<li><strong>Saudi Arabia:</strong> US bases on territory targeted</li>
</ul>
</div>
<div class="card cl-p">
<h3>Economic Shockwaves</h3>
<ul>
<li>WTI +35.63% — largest weekly gain in futures history</li>
<li>Brent crude ~$84/barrel (+15% from pre-conflict)</li>
<li>Analysts: $100+ if disruption persists beyond 4 weeks</li>
<li>Dow fell 400+ points on March 2</li>
<li>Thousands of flights grounded (Emirates, Gulf carriers)</li>
<li>Global inflation risk: +0.8% if Hormuz closure sustained</li>
</ul>
</div>
</div>

</div><!-- /tab-overview -->

<!-- ════════════════════════════ TAB: OBJECTIVES ════════ -->
<div id="tab-objectives" class="tab-pane">

<h2>Strategic Objectives of Each Actor</h2>

<div class="alert a-g"><span class="ic">⚠️</span><div>Stated goals vs. true objectives often diverge sharply. This section models underlying strategic logic, not press releases.</div></div>

| Actor | True Primary Objective | Acceptable Outcome | Unacceptable Outcome | Escalation Tolerance | Key Constraints |
|-------|----------------------|-------------------|---------------------|---------------------|-----------------|
| 🇺🇸 **United States** | Permanent neutralisation of Iran's nuclear capability; reassert regional hegemony | Regime change or verified denuclearisation; US-friendly successor | Iran achieves nuclear breakout; prolonged attrition; $150+ oil; domestic political backlash | **Moderate** — 2026 midterms constrain prolonged war | Public opinion, energy prices, Senate war-powers dispute, allied cohesion |
| 🇮🇱 **Israel** | Permanent elimination of Iranian nuclear/missile threat; Hezbollah disarmament | Iranian military dismantled; no nuclear programme; Hezbollah neutralised | Iran survives with nuclear capability; Hezbollah stays armed; mounting home-front casualties | **High** — existential framing sustains domestic tolerance | IDF capacity strain after 2024–25 campaigns; US dependency; war-economy pressure |
| 🇮🇷 **Iran** | Regime survival; prevent full military defeat; maximise adversary cost | Ceasefire that preserves Islamic Republic structure, even under new leadership | Regime collapse; occupation; forced nuclear dismantlement | **High** asymmetric; **low** conventional | Decapitated leadership; depleting missile stocks; economy in freefall; pre-existing protests |
| 🇸🇦 **Saudi Arabia** | Iranian strategic defeat without destabilisation threatening Saudi territory | Iran weakened, Houthis ended, Hormuz reopened, oil stability | Iran striking Saudi oil infrastructure at scale; Shia unrest in Eastern Province | **Low** — prefers proxy distance | Oil revenue dependency; US bases on soil = liability; Vision 2030 exposure |
| 🇦🇪 **Gulf States** (UAE/Qatar/Kuwait/Bahrain) | Preserve economic stability; protect US umbrella; avoid becoming battlefield | Fast US victory; Hormuz reopened; Iran cannot strike Gulf again | Prolonged strikes on energy/financial infrastructure; tourism collapse | **Very Low** — hosting bases they didn't want targeted | Massive exposure (Dubai/Abu Dhabi financial hubs); airspace crisis; tanker insurance |
| 🇨🇳 **China** | Preserve Iran as strategic partner; benefit from US overstretch; buy discounted Iranian oil | Negotiated ceasefire that preserves Iranian state; weakens US regional position | US-friendly regime in Tehran; long-term Hormuz disruption | **Very Low** — will not intervene militarily | Taiwan priority; $750B+ in US Treasuries; SWIFT exposure; export dependency |
| 🇷🇺 **Russia** | US distracted from Ukraine; high oil prices boost Kremlin revenues | Prolonged US-Iran conflict; Iran survives; West divided | Quick US victory that frees US strategic bandwidth for Europe/Ukraine | **Very Low** — no capacity or strategic interest to intervene | Ukraine war absorbs resources; Su-35 deal to Iran in doubt; Western sanctions |

<div class="g2" style="margin-top:14px;">
<div class="card cl-g">
<h3>Alignment Analysis</h3>
<p>The US–Israel alignment is the tightest. But sub-objectives diverge: the US prioritises nuclear dismantlement and regional order; Israel prioritises Hezbollah and permanent Iranian military incapacitation. This creates risk of Israel overreaching into Lebanon beyond US comfort zone.</p>
<p>Russia benefits from high oil and US distraction but has <strong>no viable intervention pathway</strong> after Ukraine attrition. China is similarly constrained by Western economic interdependence.</p>
</div>
<div class="card cl-r">
<h3>Iran's Strategic Paradox</h3>
<p>Iran faces the classic decapitation dilemma: the regime's core objective is <em>survival of the system</em>, but the leader and top commanders are already dead. The IRGC now functions as primary decision-maker — shifting Iran's objective from defending Khamenei's legacy to <strong>ensuring IRGC institutional survival</strong>.</p>
<p>This makes the IRGC simultaneously the last coherent fighting force AND a potential political actor seeking its own accommodation — a dangerous combination for escalation control.</p>
</div>
</div>

</div><!-- /tab-objectives -->

<!-- ════════════════════════════ TAB: MILITARY ══════════ -->
<div id="tab-military" class="tab-pane">

<h2>Military Capability Assessment</h2>

| Capability | 🇺🇸 United States | 🇮🇷 Iran | 🇮🇱 Israel | Advantage |
|------------|-----------------|---------|-----------|-----------|
| **Air Power** | B-2 bombers, F-22/F-35, 2 carrier strike groups in theatre. Unmatched penetration vs. hardened sites. | Aged F-14/MiG-29/Su-24 — mostly non-combat-ready. Air defence degraded Day 1. Russian Su-35 deal incomplete. | F-35I Adir, F-15I, F-16I (~600 combat aircraft). Proven long-range strike (2024–25). | <span class="adv adv-us">US/IL overwhelming</span> |
| **Missile Inventory** | Tomahawk (1,000+ km), JASSM-ER, precision PGMs. Near-unlimited magazine from sea/air. | Pre-war: 3,000+ ballistic missiles (Shahab, Emad, Fattah hypersonic). 500+ fired by Day 5. Rebuilding toward 2,000 stock — dispersed underground. | Jericho III (nuclear-capable), Delilah, Rocks. Iron Dome/Arrow/David's Sling layered defence. | <span class="adv adv-ir">Iran quantity; US precision</span> |
| **Naval Strength** | 2 carrier strike groups (Truman + Vinson). Aegis destroyers. Nuclear submarines. 5th Fleet Bahrain (under attack). | No blue-water navy. Fast attack boats, midget submarines, naval mines, anti-ship missiles. Asymmetric harassment doctrine. | Dolphin-class subs (nuclear-capable cruise missiles), corvettes. Regional only. | <span class="adv adv-us">US strategic; Iran asymmetric in Gulf</span> |
| **Drone Capability** | Reaper, Global Hawk (ISR + strike). Limited swarm doctrine. | **Most significant asymmetric asset.** Shahed-136/131 loitering munitions. ~2,000 fired in 5 days. ~$20K/unit. Mass-producible. | Heron, Hermes-900 ISR. Limited offensive drone vs. Iran. | <span class="adv adv-ir">Iran dominates in volume/cost</span> |
| **Cyber Warfare** | NSA/Cyber Command — elite offensive capability. Stuxnet precedent. Disrupting Iranian C2. | Significant offensive capacity; attacks on Gulf SCADA + Israeli infrastructure. Defensive cyber vulnerable to US intrusion. | Unit 8200 — world-class offensive cyber. Coordinating with US on Iranian networks. | <span class="adv adv-us">US/IL — but Iran's Gulf energy attacks are consequential</span> |
| **Space & Surveillance** | Full-spectrum ISR: satellites, AWACS, RC-135, P-8. Total battlespace awareness over Iran. | Limited — Qaem reconnaissance satellite (2023). Reliant on terrain masking + concealment. | Ofek satellite constellation. Excellent regional ISR. | <span class="adv adv-us">US decisive advantage</span> |
| **Logistics & Sustainment** | Prepositioned stocks; Diego Garcia, Al Udeid, Bahrain. But bases now under Iranian missile attack — logistics vulnerability. | Interior lines. Mountain dispersal. Domestic drone/missile production. Fuel/food imports challenged by sanctions. | Dependent on US for precision munition resupply. Short interior lines. | <span class="adv adv-us">US overall; Iran resilient via interior lines</span> |

<div class="g3" style="margin-top:6px;">
<div class="card cl-r">
<h3>Can Iran sustain damage on Israel?</h3>
<p><strong>Limited but real.</strong> 500+ missiles fired at Israel by Day 5. Israel's layered defence intercepts ~85–90% of threats. Saturation attacks can penetrate — 11 killed in Israel by Day 9. Hezbollah's entry (March 2) adds a second front with 150,000+ rockets. Iran <em>can</em> impose costs — it cannot destroy Israel militarily.</p>
<p><strong>Critical constraint:</strong> At 100/day burn rate, Iran's pre-war 3,000-missile stock depletes in ~30 days. The rate must slow.</p>
</div>
<div class="card cl-b">
<h3>Can Iran strike US bases effectively?</h3>
<p><strong>Partially, limited strategic effect.</strong> Iran struck Bahrain 5th Fleet HQ, Ali al-Salem (Kuwait), Al Udeid (Qatar), Iraq bases. Most intercepted by Patriot/THAAD. 6 US soldiers killed to date. Politically significant (triggering domestic debate) but US military capability not meaningfully degraded.</p>
<p><strong>Risk:</strong> A mass salvo defeating point defence and killing 50+ Americans would dramatically alter US escalation calculus.</p>
</div>
<div class="card cl-o">
<h3>Can Iran sustain long-term war?</h3>
<p><strong>2–4 months maximum before critical degradation.</strong> Key bottlenecks: missile production (~50–100/month), drone production (higher but component-constrained), fuel for military ops, food imports under blockade, decapitated leadership reducing IRGC coherence. Historical precedent (Iran–Iraq War) shows Iran can absorb enormous punishment — but that was a structurally different moment.</p>
</div>
</div>

</div><!-- /tab-military -->

<!-- ════════════════════════════ TAB: HORMUZ ════════════ -->
<div id="tab-hormuz" class="tab-pane">

<h2>Strait of Hormuz Scenarios</h2>

<div class="alert a-r"><span class="ic">🔴</span><div><strong>Current status (Day 9):</strong> Strait of Hormuz effectively closed. 150+ tankers anchored outside. Traffic near zero. 20% of global oil supply + significant LNG volumes disrupted. WTI recorded its largest single-week gain in futures history.</div></div>

<div class="g2">
<div class="card">
<h3>Iran's Closure Toolkit</h3>
<ul>
<li><strong>Naval mines:</strong> Thousands available; deployed rapidly by fast boats and Ghadir-class midget submarines in the 33-mile-wide strait</li>
<li><strong>Anti-ship missiles:</strong> C-802, Noor, Qader — shore-based and mobile; range covers entire strait</li>
<li><strong>Fast attack craft (IRGC Navy):</strong> Swarming harassment, boarding, damage to tankers</li>
<li><strong>Shahed drones (anti-ship config):</strong> Demonstrated against commercial vessels since 2023</li>
<li><strong>Coastal artillery:</strong> Deployed along Bandar Abbas and Qeshm Island</li>
</ul>
</div>
<div class="card">
<h3>US Counter-Measures</h3>
<ul>
<li><strong>MCM vessels:</strong> Avenger-class mine countermeasures — slow (weeks per cleared corridor)</li>
<li><strong>Carrier air power:</strong> F/A-18s suppressing shore-based missile batteries</li>
<li><strong>Aegis destroyers:</strong> Anti-ship missile defence escort for tanker convoys</li>
<li><strong>P-8 Poseidon:</strong> Sub-hunting aircraft to neutralise IRGC submarine threat</li>
<li><strong>Historical precedent:</strong> Operation Praying Mantis (Apr 1988) destroyed ~half of Iran's operational navy in a single day</li>
</ul>
</div>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag gr">SCENARIO A</span><h3>Harassment Only — Ships Still Moving</h3></div>
<p>Iran conducts intermittent missile threats, drone harassment, and fast-boat shadowing. No mines in main channel. Insurance premiums spike but tankers transit under armed escort.</p>
<div class="sc-meta">
<div><div class="mk">Probability</div><div class="mv" style="color:var(--green)">15% (already past this stage)</div></div>
<div><div class="mk">Oil Price Impact</div><div class="mv">+$10–20/bbl ($85–95 Brent)</div></div>
<div><div class="mk">Escalation Level</div><div class="mv" style="color:var(--gold)">Medium</div></div>
</div>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag g">SCENARIO B</span><h3>Partial Disruption — Mining + Tanker Damage</h3></div>
<p>Iran mines approaches, damages 2–3 VLCCs. 50–70% volume reduction sustained for weeks. US mine clearance underway but slow. Gulf states face enormous economic pressure to push for ceasefire.</p>
<div class="sc-meta">
<div><div class="mk">Probability</div><div class="mv" style="color:var(--gold)">25%</div></div>
<div><div class="mk">Duration</div><div class="mv">4–8 weeks</div></div>
<div><div class="mk">Oil Price Impact</div><div class="mv">+$30–50/bbl ($110–130 Brent)</div></div>
<div><div class="mk">Escalation Level</div><div class="mv" style="color:var(--orange)">High</div></div>
</div>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag">SCENARIO C</span><h3>Attempted Full Closure — <em>Current Situation</em></h3></div>
<p><strong>Active as of March 8, 2026.</strong> Mines, missile threats, and drone swarms make transit uninsurable. 150+ ships anchored outside. Traffic near zero.</p>
<div class="sc-meta">
<div><div class="mk">Probability continues 2+ wks</div><div class="mv" style="color:var(--red)">60%</div></div>
<div><div class="mk">Duration estimate</div><div class="mv">2–6 weeks from start; max ~6–8 weeks</div></div>
<div><div class="mk">Oil Price Impact</div><div class="mv">$120–160+ Brent if sustained 4+ weeks</div></div>
<div><div class="mk">Escalation Level</div><div class="mv" style="color:var(--red)">Severe</div></div>
</div>
<p style="margin-top:10px;"><strong>Escalation timeline from full closure:</strong></p>
<div class="ladder" style="margin-top:10px;">
<div class="ladder-line"></div>
<div class="ladder-item"><div class="ladder-dot" style="background:var(--gold)"></div><div class="ladder-body"><div class="ladder-step">Week 1–2</div><div class="ladder-desc">Oil price shock. SPR releases (US, IEA). Tanker insurance suspended. Gulf states push for talks.</div></div></div>
<div class="ladder-item"><div class="ladder-dot" style="background:var(--orange)"></div><div class="ladder-body"><div class="ladder-step">Week 2–4</div><div class="ladder-desc">US begins active mine-clearance. Strikes on Iranian naval assets + Bandar Abbas. Escort convoys form. China/India apply ceasefire pressure.</div></div></div>
<div class="ladder-item"><div class="ladder-dot" style="background:var(--red)"></div><div class="ladder-body"><div class="ladder-step">Week 4–6</div><div class="ladder-desc">$120–150 oil. Global recession risk. Europe energy emergency. Iran running low on naval mines and missiles.</div></div></div>
<div class="ladder-item"><div class="ladder-dot" style="background:var(--purple)"></div><div class="ladder-body"><div class="ladder-step">Week 6+</div><div class="ladder-desc">Either: Iran forced to reopen by naval defeat, OR political resolution under international pressure, OR US strikes Kharg Island (Iran's main oil terminal).</div></div></div>
</div>
<div class="alert a-g" style="margin-top:12px;"><span class="ic">⚡</span><div><strong>Physical constraint:</strong> Iran cannot sustain a closure against US Navy power projection indefinitely. The US can force the strait open — the question is political will and tolerable escalation cost. In Operation Praying Mantis (April 1988), the US destroyed roughly half of Iran's operational navy in a single day.</div></div>
</div>

</div><!-- /tab-hormuz -->

<!-- ════════════════════════════ TAB: DYNAMICS ══════════ -->
<div id="tab-dynamics" class="tab-pane">

<h2>War Dynamics Model</h2>

<div class="g2">
<div class="card cl-b">
<h3>Game Theory Framework</h3>
<p>This conflict is an <strong>asymmetric attrition game</strong> with incomplete information. The US-Israel coalition has overwhelming conventional superiority but faces a <em>cost-imposition problem</em>: Iran's rational strategy is to make winning too expensive, not to win outright.</p>
<ul>
<li><strong>Deterrence failure:</strong> The war itself signals pre-war deterrence collapsed — Iran's nuclear ambiguity no longer restrained US/Israel</li>
<li><strong>Commitment problem:</strong> Trump's "unconditional surrender" demand creates mutual lock-in — Iran cannot surrender without regime collapse; US cannot back down without political damage</li>
<li><strong>Information asymmetry:</strong> US doesn't know Iran's true missile reserves; Iran doesn't know US redlines for WMD use</li>
<li><strong>Audience costs:</strong> Both leaders face domestic audiences that make concessions costly</li>
</ul>
</div>
<div class="card cl-g">
<h3>Escalation Ladder</h3>
<div class="ladder">
<div class="ladder-line"></div>
<div class="ladder-item"><div class="ladder-dot" style="background:var(--green)"></div><div class="ladder-body"><div class="ladder-step">Level 1 — Pre-war</div><div class="ladder-desc">Sanctions, proxy conflict, nuclear pressure — status quo pre-Feb 28</div></div></div>
<div class="ladder-item"><div class="ladder-dot" style="background:var(--gold)"></div><div class="ladder-body"><div class="ladder-step">Level 2 — Day 1–3</div><div class="ladder-desc">Conventional air/missile strikes; leadership decapitation; Iran conventional retaliation — <strong>current base</strong></div></div></div>
<div class="ladder-item"><div class="ladder-dot" style="background:var(--orange)"></div><div class="ladder-body"><div class="ladder-step">Level 3 — Day 3–14</div><div class="ladder-desc">Hormuz closed; energy facilities attacked; Hezbollah entry; US bases under sustained fire — <strong>current trajectory</strong></div></div></div>
<div class="ladder-item"><div class="ladder-dot" style="background:var(--red)"></div><div class="ladder-body"><div class="ladder-step">Level 4</div><div class="ladder-desc">Iran strikes Saudi/UAE oil infrastructure (Abqaiq); $150+ oil; Gulf states demand ceasefire; US strikes Kharg Island</div></div></div>
<div class="ladder-item"><div class="ladder-dot" style="background:var(--purple)"></div><div class="ladder-body"><div class="ladder-step">Level 5 — Nuclear threshold</div><div class="ladder-desc">Iran nuclear breakout attempt OR regime collapse OR chemical weapon use → existential US/Israel response</div></div></div>
</div>
</div>
</div>

<h3 style="color:var(--text);font-size:15px;margin:14px 0 10px;">Feedback Loop Model</h3>
<div class="tree">
<div><span class="tk">US-ISRAEL PRESSURE CAMPAIGN</span></div>
<div>│</div>
<div>├── Strike Iranian leadership + nuclear/missile sites</div>
<div>│       └── <span class="tv">✓ Achieved: Khamenei dead, IRGC chief dead, sites struck</span></div>
<div>│</div>
<div>├── Expected: Iran capitulates or regime collapses</div>
<div>│       └── <span class="tw">✗ Actual: IRGC takes control — more militant, nationalist</span></div>
<div>│</div>
<div>└── IRAN RESPONSE LOOP</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Close Hormuz → <span class="tw">Global economic damage → pressure on US allies</span></div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Strike US bases → <span class="tm">US domestic debate (war powers) → political constraint</span></div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Activate Hezbollah → <span class="tw">Israel two-front war → Israeli public pressure</span></div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Missile/drone attrition → <span class="tv">Deplete US/Israel air defence magazine (costly to replace)</span></div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── ESCALATION RISK FEEDBACK</div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── If Iran approaches nuclear breakout → <span class="tw">Immediate Israeli nuclear threat</span></div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── If oil hits $150 → <span class="tm">China/India/Europe demand ceasefire → US isolated</span></div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── If US soldiers killed at scale → <span class="tw">US escalation to ground forces</span></div>
<div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── If IRGC fractures → <span class="tv">Negotiated end becomes possible</span></div>
</div>

<div class="g3" style="margin-top:14px;">
<div class="card cl-r">
<h3>Resource Depletion</h3>
<p><strong>Iran:</strong> ~100 missiles/day. Pre-war stock ~3,000 → depleted in ~30 days at this rate. Drone production partially compensates.</p>
<p><strong>US:</strong> Tomahawk ~$2M each. 2,000 strikes = ~$4B+. Congressional appropriations debate begins Week 3.</p>
<p><strong>Israel:</strong> Iron Dome interceptors ~$50K; Arrow-3 ~$1M+. Magazine depth a genuine concern within 4–6 weeks of sustained saturation attacks.</p>
</div>
<div class="card cl-g">
<h3>Deterrence Signalling</h3>
<ul>
<li><strong>US:</strong> "4 weeks" Trump statement = limited war framing, not open-ended commitment</li>
<li><strong>Iran:</strong> Hormuz closure = "we can hurt the world economy"</li>
<li><strong>Israel:</strong> Lebanon strikes = willingness to expand, deterring full Hezbollah mobilisation</li>
<li><strong>China:</strong> Ceasefire calls without action = pressure without commitment</li>
</ul>
</div>
<div class="card cl-p">
<h3>Domestic Political Constraints</h3>
<p><strong>US:</strong> Senate war powers vote already close. Midterms Nov 2026. Gas prices = political liability.</p>
<p><strong>Iran:</strong> Nationwide protests erupted Dec 2025 — regime already fragile. War may temporarily unify population (nationalism) or accelerate collapse (economic suffering). Highly uncertain.</p>
<p><strong>Israel:</strong> War-weary after 2024–25. But nuclear threat = existential justification sustaining high domestic tolerance.</p>
</div>
</div>

</div><!-- /tab-dynamics -->

<!-- ════════════════════════════ TAB: IRAN STRATEGY ═════ -->
<div id="tab-iran" class="tab-pane">

<h2>Iran's Likely Strategy</h2>

<div class="alert a-r"><span class="ic">🎯</span><div><strong>Core assumption:</strong> Iran's IRGC leadership knows it cannot defeat the US conventionally. Regime survival — specifically <em>IRGC institutional survival</em> — is the primary objective, replacing ideological continuity after Khamenei's death.</div></div>

| Strategy Option | Description | Probability | Assessment |
|----------------|-------------|-------------|------------|
| **1. Global Economic Disruption** | Close Hormuz, attack Gulf energy infrastructure — make war too costly for everyone to tolerate | <span style="color:var(--red);font-weight:700">ACTIVE — 85%</span> | Already deployed. Most rational play. Forces third-party pressure on US. Iran's most powerful lever. |
| **2. Proxy Escalation** | Activate Hezbollah, Iraq militias, Houthis simultaneously — open multiple fronts, stretch US-Israel capacity | <span style="color:var(--gold);font-weight:700">PARTIAL — 65%</span> | Hezbollah activated March 2 (limited). Iraq militias hitting US bases. Lebanon govt complicates full activation. |
| **3. Diplomatic Wedge** | Accept ceasefire mediation via China/Russia/Oman to split US-European-Gulf coalition | <span style="color:var(--gold);font-weight:700">40%</span> | Oman attempted (US rejected). Best diplomatic card: offer to negotiate to split Gulf states from US. |
| **4. War of Attrition** | Survive, preserve forces, bleed adversaries over months — wait for domestic politics to shift | <span style="color:var(--gold);font-weight:700">35%</span> | Historical model (Iran-Iraq War). Requires population willingness to absorb suffering. IRGC has capacity for this. |
| **5. Nuclear Breakout** | Race to assemble nuclear device as last-resort deterrent or ceasefire-forcing mechanism | <span style="color:var(--green);font-weight:700">15%</span> | Very high risk. Nuclear sites reportedly NOT struck (IAEA March 2). Iran retains ~400kg of 60%-enriched uranium. Israeli/US red line would trigger immediate catastrophic escalation. |
| **6. Full Regional Escalation** | Full Hezbollah rocket campaign + attack Saudi oil (Abqaiq) + draw regional powers in | <span style="color:var(--green);font-weight:700">20%</span> | High risk of triggering overwhelming US response. Saudi Arabia joining against Iran would be decisive. Most destabilising for Iran itself. |

<div class="g2" style="margin-top:14px;">
<div class="card cl-r">
<h3>Most Probable Strategy Package</h3>
<p>Iran is most likely pursuing a <strong>combined 1+2+3 strategy</strong> simultaneously:</p>
<ol>
<li>Maintain Hormuz closure as long as militarily possible (economic leverage)</li>
<li>Activate Hezbollah in limited mode (pain without full-war risk)</li>
<li>Keep diplomatic channels open (Oman, China) for an exit ramp</li>
<li>Signal willingness to negotiate to split Gulf states from US</li>
<li>Use nationalist rally-effect to consolidate IRGC power during leadership transition</li>
</ol>
</div>
<div class="card cl-g">
<h3>Iran's Key Vulnerabilities</h3>
<ul>
<li><strong>Missile magazine exhaustion:</strong> ~30-day window before conventional deterrence degrades sharply</li>
<li><strong>Leadership vacuum:</strong> IRGC-by-committee is slower and less coherent than single-leader decision-making</li>
<li><strong>Population:</strong> December 2025 protests showed deep dissatisfaction — Hormuz closure hurts Iranian fishermen and imports too</li>
<li><strong>No nuclear deterrent:</strong> The one thing that would have stopped this war is absent</li>
<li><strong>China won't save them:</strong> Beijing values US trade more than Iran alliance — a critical miscalculation Iran may have made</li>
</ul>
</div>
</div>

</div><!-- /tab-iran -->

<!-- ════════════════════════════ TAB: ESCALATION ════════ -->
<div id="tab-escalation" class="tab-pane">

<h2>Escalation Scenarios — Five War Trajectories</h2>

<div class="sc">
<div class="sc-head"><span class="sc-tag gr">TRAJECTORY 1</span><h3>Rapid Ceasefire (2–4 weeks)</h3></div>
<p><strong>Trigger:</strong> IRGC signals willingness to negotiate as missile stocks deplete. Oman or China brokers back-channel deal. US accepts face-saving "victory" — Iran agrees to nuclear freeze, Hormuz reopens, ceasefire declared.</p>
<div class="sc-meta">
<div><div class="mk">Probability</div><div class="mv" style="color:var(--green)">20%</div></div>
<div><div class="mk">Timeline</div><div class="mv">Week 2–4 from now</div></div>
<div><div class="mk">Oil Impact</div><div class="mv">Retreats to $85–95</div></div>
</div>
<p style="margin-top:8px;"><strong>Key obstacle:</strong> Trump's "unconditional surrender" demand makes any negotiated ceasefire politically toxic — requires reframing as "Iran capitulated."</p>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag b">TRAJECTORY 2</span><h3>Limited Regional War (1–3 months) — Most Probable</h3></div>
<p><strong>Trigger:</strong> No ceasefire in first 2 weeks. US strikes continue but slow. Iran reduced to lower-intensity harassment — drones and sporadic missiles. Hezbollah limited engagement. War becomes a managed slow burn.</p>
<div class="sc-meta">
<div><div class="mk">Probability</div><div class="mv" style="color:var(--blue)">35%</div></div>
<div><div class="mk">Timeline</div><div class="mv">1–3 months</div></div>
<div><div class="mk">Oil Impact</div><div class="mv">$100–120 sustained; global inflation +1.5%</div></div>
</div>
<p style="margin-top:8px;">Ends with negotiated arrangement when Iran's military capability degrades sufficiently to force concessions. <strong>Current most likely trajectory.</strong></p>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag g">TRAJECTORY 3</span><h3>Gulf Shipping War (2–6 months)</h3></div>
<p><strong>Trigger:</strong> Iran successfully mines Hormuz approaches; tanker damaged or sunk; US Navy in extended mine-clearance operation. Iran strikes Saudi/UAE oil facilities. $150+ oil triggers global recession fears.</p>
<div class="sc-meta">
<div><div class="mk">Probability</div><div class="mv" style="color:var(--gold)">25%</div></div>
<div><div class="mk">Timeline</div><div class="mv">2–6 months</div></div>
<div><div class="mk">Oil Impact</div><div class="mv">$130–160; shipping insurance crisis</div></div>
</div>
<p style="margin-top:8px;">Historical parallel: 1987–88 Tanker War. Operation Praying Mantis destroyed Iran's operational naval forces in a single day. Likely endpoint: Iran's naval capacity destroyed, strait forced open.</p>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag o">TRAJECTORY 4</span><h3>Regime Destabilisation (2–6 months)</h3></div>
<p><strong>Trigger:</strong> Khamenei's death + economic collapse + IRGC power struggle + resumed popular protests combine to fracture the Islamic Republic. IRGC factions compete; reformist elements reach out to US via back-channels. Regime fragments rather than surrenders.</p>
<div class="sc-meta">
<div><div class="mk">Probability</div><div class="mv" style="color:var(--orange)">20%</div></div>
<div><div class="mk">Timeline</div><div class="mv">3–6 months if war continues</div></div>
<div><div class="mk">Oil Impact</div><div class="mv">Volatile; uncertainty premium $110–140</div></div>
</div>
<p style="margin-top:8px;"><strong>Warning:</strong> Regime collapse without a prepared successor = Libya/Iraq 2003 scenario. IRGC has 190,000 armed personnel controlling missile arsenal — a collapsing IRGC with WMD access is an extreme proliferation risk.</p>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag">TRAJECTORY 5</span><h3>Large Regional War — Hezbollah Full Entry (10% probability, catastrophic)</h3></div>
<p><strong>Trigger:</strong> Israel expands Lebanon strikes significantly; Hezbollah launches full 150,000+ rocket campaign; Syria's new government collapses; Iraq enters via Shia militias at scale. US casualties reach politically intolerable level.</p>
<div class="sc-meta">
<div><div class="mk">Probability</div><div class="mv" style="color:var(--red)">10%</div></div>
<div><div class="mk">Timeline</div><div class="mv">6–18 months</div></div>
<div><div class="mk">Oil Impact</div><div class="mv">$160–200+; global recession confirmed</div></div>
</div>
<p style="margin-top:8px;"><strong>Positive signal:</strong> Lebanon's government is publicly calling for Hezbollah disarmament (March 2) — an unprecedented political moment that reduces Trajectory 5 probability. If Israel's Lebanon strikes kill Lebanese civilians at scale, this dynamic reverses rapidly.</p>
</div>

</div><!-- /tab-escalation -->

<!-- ════════════════════════════ TAB: ECONOMIC ══════════ -->
<div id="tab-economic" class="tab-pane">

<h2>Economic Consequences</h2>

<div class="stats">
  <div class="stat s-g"><div class="v">+35.6%</div><div class="l">WTI crude weekly gain (record)</div></div>
  <div class="stat s-o"><div class="v">~$84</div><div class="l">Brent crude (March 8)</div></div>
  <div class="stat s-r"><div class="v">~0</div><div class="l">Tanker transits/day through Hormuz</div></div>
  <div class="stat s-b"><div class="v">150+</div><div class="l">Tankers anchored outside strait</div></div>
  <div class="stat s-r"><div class="v">–400pts</div><div class="l">Dow Jones drop (March 2)</div></div>
</div>

| Duration | Oil Price (Brent) | Global Inflation | Shipping Impact | Financial Markets |
|----------|------------------|-----------------|----------------|------------------|
| **1 Month** | $90–110 | +0.5–0.8% | Hormuz closed; Cape route adds 2–3 weeks + $2–3M/voyage | S&P –5–10%; gold/USD safe-haven rally |
| **3 Months** | $120–140 | +1.0–1.5% | Shipping insurance crisis; Suez-only for non-Hormuz flows | S&P –15–20%; recession pricing begins; credit spreads widen |
| **6 Months** | $140–180 | +2.0–3.0% | Sustained crunch; LNG spot 3–5× normal; global supply chain reorder | Global bear market; recession confirmed; EM debt crisis |

| Duration | 🇺🇸 United States | 🇪🇺 Europe | 🇨🇳 China | 🇮🇳 India |
|----------|-----------------|-----------|---------|---------|
| **1 Month** | Gas +$0.40–0.80/gal; SPR releases; GDP –0.2% | LNG crisis developing; winter reserves buffer; GDP –0.3% | Russian pipeline partially insulates; GDP –0.3% | Iranian oil disrupted; scramble for alternatives; GDP –0.4% |
| **3 Months** | Gas +$1.20–1.80/gal; midterm political crisis; GDP –0.8% | IEA emergency release; Russia gas debate revived; GDP –0.6–1.0% | Reroutes via Russia; insulated but not immune; GDP –0.5% | Severe — 14% from Iran + Gulf; food inflation spike; GDP –0.8–1.2% |
| **6 Months** | Recession risk; Fed forced to cut despite inflation; unemployment +1–2% | Recession confirmed; energy rationing in Germany; political crisis | Structural advantage (pipelines) but global recession hits exports | Stagflation; currency pressure; potential balance of payments crisis |

<div class="g2" style="margin-top:6px;">
<div class="card cl-g">
<h3>The US Economic Paradox</h3>
<p>The US is simultaneously causing the disruption AND the world's largest oil producer. High oil prices benefit US shale producers (ExxonMobil, Chevron) while hurting US consumers. This creates a strange political economy: energy sector profits fund campaigns while consumers revolt at the pump. The SPR was largely depleted in 2022 (Biden) and partially refilled — a limited buffer is available.</p>
</div>
<div class="card cl-b">
<h3>China's Strategic Oil Position</h3>
<p>China imported ~900,000 barrels/day from Iran. This supply is now at risk from US interdiction. However: China has 90-day SPR coverage, Russia pipeline (Power of Siberia) bypasses Hormuz, and China will attempt to purchase discounted distressed cargoes. High oil prices hurt China's manufacturing competitiveness — China has strong economic incentive to push for ceasefire, but not strong enough to risk US sanctions by breaking ranks openly.</p>
</div>
</div>

<h3 style="color:var(--text);font-size:15px;margin:14px 0 10px;">Alternative Route Economics (While Hormuz Is Closed)</h3>

| Route | Additional Distance | Cost Premium | Capacity |
|-------|-------------------|--------------|----------|
| **Hormuz (normal)** | Baseline | Baseline | 21 mb/d (20% of global) |
| **Cape of Good Hope** | +6,000–10,000 nm | +$2–4M/voyage; +2–3 weeks | Unlimited theoretically; fleet-constrained |
| **Sumed Pipeline (Egypt)** | N/A | Modest premium | 2.8 mb/d — already at capacity |
| **Saudi East–West Pipeline** | N/A | Transit fee | 5 mb/d — partial substitute; Saudi under attack too |
| **Russian Pipeline** | N/A | Russia negotiating leverage | ~2–3 mb/d additional |

<div class="alert a-g" style="margin-top:8px;"><span class="ic">⚡</span><div>Alternative routes can cover <strong>~40–50%</strong> of Hormuz volume with weeks-long delays and massive cost increases. A sustained 6-month closure would not be fully compensated — a global recession would be nearly certain.</div></div>

</div><!-- /tab-economic -->

<!-- ════════════════════════════ TAB: HISTORICAL ════════ -->
<div id="tab-historical" class="tab-pane">

<h2>Historical Analogies</h2>

<div class="g2">
<div class="card cl-g">
<h3>1987–88 Iran–Iraq Tanker War <span class="tag g">MOST RELEVANT</span></h3>
<p><strong>What happened:</strong> Iran attacked neutral shipping in the Gulf. US intervened with Operation Earnest Will (convoy escort) and Operation Praying Mantis (April 1988), destroying roughly half of Iran's operational naval fleet in a single day.</p>
<p><strong>Key lessons for 2026:</strong></p>
<ul>
<li>Iran backed down when faced with direct US military action against its navy</li>
<li>The US can physically destroy Iran's ability to threaten the strait relatively quickly</li>
<li>Political will — not capability — is the limiting factor</li>
<li>Iran sustained the tanker war for ~2 years before backing down under military and economic pressure</li>
</ul>
<p><strong>Key difference 2026:</strong> Iran now has vastly more sophisticated anti-ship missiles and drones than in 1988. But US naval technology has also advanced dramatically (Aegis, directed energy, CIWS).</p>
</div>
<div class="card cl-r">
<h3>2003 Iraq Invasion <span class="tag r">CAUTIONARY</span></h3>
<p><strong>What happened:</strong> US rapidly destroyed Iraqi military but failed catastrophically at post-war stabilisation. "Mission Accomplished" declared while insurgency was just beginning.</p>
<p><strong>Relevance to 2026:</strong></p>
<ul>
<li>Decapitating a regime (Khamenei dead, like Saddam captured) does NOT automatically produce a stable successor</li>
<li>IRGC = Republican Guard equivalent, but more ideologically coherent and deeply embedded in economy/society</li>
<li>Iran has 90 million people — far larger and more complex than Iraq's 25 million in 2003</li>
<li>No US ground invasion planned — limiting the Iraq parallel somewhat</li>
</ul>
<p><strong>Key lesson:</strong> Define the end-state <em>before</em> achieving military success, or you own the chaos.</p>
</div>
<div class="card cl-o">
<h3>1973 Yom Kippur War / Oil Embargo <span class="tag o">ECONOMIC PARALLEL</span></h3>
<p><strong>What happened:</strong> OPEC embargo cut oil supply to US/Europe; oil quadrupled in price; global recession followed.</p>
<p><strong>Similarities:</strong> Sudden supply disruption → price shock → global economic consequences. US credibility tied to Israeli survival.</p>
<p><strong>Key difference:</strong> In 1973, Arab states were oil exporters using oil as a weapon. In 2026, Iran is closing a <em>transit route</em> that also hurts its Gulf Arab neighbours — a strategically self-damaging move that limits its sustainability.</p>
<p>Also: In 1973, the US was a net oil importer. In 2026, the US is the world's #1 producer — reducing domestic political pressure from high prices.</p>
</div>
<div class="card cl-p">
<h3>US–Iran Proxy Conflicts 2019–2025 <span class="tag p">RECENT PRECEDENT</span></h3>
<p><strong>What happened:</strong> Tanker attacks (2019), Soleimani killing (Jan 2020), drone/missile tit-for-tats, proxy warfare through Houthis/Hezbollah — each time managed de-escalation below direct war threshold.</p>
<p><strong>Why the old pattern broke down in 2026:</strong></p>
<ul>
<li>Each prior escalation had an "exit" — this time, the US/Israel committed to destroying leadership with no exit short of regime change</li>
<li>Iran's nuclear programme reached near-breakout status (May 2025 IAEA) — removing the deterrence ambiguity that kept Iran safe</li>
<li>The Khamenei killing is categorically different: no established playbook for what happens next</li>
</ul>
</div>
</div>

<div class="card cl-gr" style="margin-top:6px;">
<h3>Most Useful Analogy</h3>
<p><strong>Primary:</strong> The <strong>1987–88 Tanker War</strong> for the Hormuz/naval dimension — Iran knows it can impose costs but ultimately cannot win a direct naval confrontation with the US. This gives a rational basis for Iran to eventually open the strait in exchange for something.</p>
<p><strong>Secondary:</strong> The <strong>2003 Iraq invasion</strong> for the regime-change dimension — the danger of "winning" the war but losing the peace. If Iran's government collapses without an organised successor, the region faces a catastrophic power vacuum with IRGC armed factions, nuclear materials, and 90 million people in chaos.</p>
<p><strong>Least useful:</strong> Yom Kippur War — too different in structure (Iran is not an oil exporter using oil as a weapon; it's a transit-state closing a route that hurts its neighbours too).</p>
</div>

</div><!-- /tab-historical -->

<!-- ════════════════════════════ TAB: FORECAST ══════════ -->
<div id="tab-forecast" class="tab-pane">

<h2>Strategic Forecast — Probabilistic Assessment</h2>

<div class="alert a-b"><span class="ic">📊</span><div>All probabilities reflect assessments as of Day 9 (March 8, 2026). Confidence intervals are wide given the unprecedented nature of leadership decapitation and ongoing leadership transition.</div></div>

<div class="g2">
<div class="card">
<h3>War Duration Probabilities</h3>
<div class="pb"><div class="pl">Ends within 30 days (by April 8)</div><div class="bg"><div class="fill" style="width:25%;background:var(--green)"></div></div><div class="pct" style="color:var(--green)">25%</div></div>
<div class="pb"><div class="pl">Ends within 90 days (by June 8)</div><div class="bg"><div class="fill" style="width:65%;background:var(--gold)"></div></div><div class="pct" style="color:var(--gold)">65%</div></div>
<div class="pb"><div class="pl">Ends within 1 year</div><div class="bg"><div class="fill" style="width:88%;background:var(--orange)"></div></div><div class="pct" style="color:var(--orange)">88%</div></div>
<div class="pb"><div class="pl">Drags beyond 1 year</div><div class="bg"><div class="fill" style="width:12%;background:var(--red)"></div></div><div class="pct" style="color:var(--red)">12%</div></div>
<p style="margin-top:12px;">Iran's missile stocks will exhaust within 4–6 weeks at current burn rates, forcing either military capitulation or negotiation. Trump has signalled a 4-week war framing. Gulf states' economic pain creates ceasefire pressure. Most likely endpoint: ceasefire by late April 2026.</p>
</div>
<div class="card">
<h3>Key Event Probabilities</h3>
<div class="pb"><div class="pl">Hormuz disruption continues 30+ days</div><div class="bg"><div class="fill" style="width:60%;background:var(--red)"></div></div><div class="pct" style="color:var(--red)">60%</div></div>
<div class="pb"><div class="pl">Iran regime collapse / fragmentation</div><div class="bg"><div class="fill" style="width:20%;background:var(--orange)"></div></div><div class="pct" style="color:var(--orange)">20%</div></div>
<div class="pb"><div class="pl">Hezbollah full-scale rocket campaign</div><div class="bg"><div class="fill" style="width:25%;background:var(--red)"></div></div><div class="pct" style="color:var(--red)">25%</div></div>
<div class="pb"><div class="pl">Iran nuclear breakout attempt</div><div class="bg"><div class="fill" style="width:15%;background:var(--purple)"></div></div><div class="pct" style="color:var(--purple)">15%</div></div>
<div class="pb"><div class="pl">Saudi/UAE oil infrastructure attack</div><div class="bg"><div class="fill" style="width:30%;background:var(--orange)"></div></div><div class="pct" style="color:var(--orange)">30%</div></div>
<div class="pb"><div class="pl">Oil hits $130+ Brent</div><div class="bg"><div class="fill" style="width:40%;background:var(--gold)"></div></div><div class="pct" style="color:var(--gold)">40%</div></div>
<div class="pb"><div class="pl">Ceasefire brokered by China/Oman</div><div class="bg"><div class="fill" style="width:35%;background:var(--blue)"></div></div><div class="pct" style="color:var(--blue)">35%</div></div>
<div class="pb"><div class="pl">US/China direct confrontation</div><div class="bg"><div class="fill" style="width:5%;background:var(--red)"></div></div><div class="pct" style="color:var(--red)">5%</div></div>
<div class="pb"><div class="pl">Nuclear weapon use (any actor)</div><div class="bg"><div class="fill" style="width:3%;background:var(--purple)"></div></div><div class="pct" style="color:var(--purple)">3%</div></div>
</div>
</div>

<div class="card cl-g" style="margin-top:8px;">
<h3>Base Case Outcome — 45% Probability</h3>
<p>A <strong>negotiated ceasefire within 45–75 days</strong>, brokered via Oman or China, under the following conditions:</p>
<ol>
<li>Iran's missile stocks deplete to the point where continued resistance is militarily unsustainable</li>
<li>Hormuz reopened under US Navy escort — partially forced, partially traded for a ceasefire signal</li>
<li>IRGC negotiates institutional survival in exchange for nuclear freeze (not dismantlement)</li>
<li>Trump declares victory ("Iran destroyed its missiles, nuclear programme set back decades, Khamenei dead")</li>
<li>Islamic Republic survives in weakened form under IRGC leadership — more hardline, less ideological</li>
<li>The underlying nuclear question is deferred, not resolved</li>
</ol>
<p><strong>This outcome satisfies no one completely but is the equilibrium that avoids catastrophic escalation.</strong></p>
</div>

</div><!-- /tab-forecast -->

<!-- ════════════════════════════ TAB: UNKNOWNS ══════════ -->
<div id="tab-unknowns" class="tab-pane">

<h2>Key Unknowns — Variables That Could Reshape Everything</h2>

<div class="sc">
<div class="sc-head"><span class="sc-tag">UNKNOWN 1</span><h3>Iran's True Missile Reserve Depth</h3></div>
<p>We know Iran fired 500+ missiles in the first 5 days. Pre-war estimates put stock at 3,000+ ballistic missiles. But Iran has been covertly rebuilding after June 2025 strikes and may have dispersed reserves in hardened underground facilities that US surveillance has not fully mapped. If Iran has 5,000+ missiles dispersed in mountain bunkers, the attrition timeline changes dramatically — potentially extending the conflict by months.</p>
<div class="sc-meta">
<div><div class="mk">If reserves larger than estimated</div><div class="mv" style="color:var(--red)">War extends 3–6 months; US forced to accept negotiated deal</div></div>
<div><div class="mk">If reserves deplete faster</div><div class="mv" style="color:var(--green)">Ceasefire within 3–4 weeks</div></div>
</div>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag b">UNKNOWN 2</span><h3>IRGC Internal Power Struggle</h3></div>
<p>Khamenei is dead. Top commanders Pakpour and Shamkhani are dead. An Interim Leadership Council is functioning but the IRGC is reportedly pressuring the Assembly of Experts to name Mojtaba Khamenei (the son) as successor. If a significant IRGC faction rejects the chosen successor or seeks accommodation with the US in exchange for institutional survival, the war ends rapidly. Conversely, if hardliners completely dominate, expect maximum escalation.</p>
<div class="sc-meta">
<div><div class="mk">If IRGC fractures</div><div class="mv" style="color:var(--green)">Rapid ceasefire; regime transformation possible</div></div>
<div><div class="mk">If hardliners dominate</div><div class="mv" style="color:var(--red)">Maximum escalation: Hormuz + Hezbollah + oil infrastructure attacks</div></div>
</div>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag g">UNKNOWN 3</span><h3>Hezbollah's Strategic Decision</h3></div>
<p>Hezbollah has 150,000+ rockets and missiles. So far it has engaged only limitedly (anti-tank fire, small barrages). Lebanon's government is publicly calling for Hezbollah disarmament — an unprecedented political moment. The question is whether Nasrallah's successors (assassinated 2024) decide that Iran's survival requires Hezbollah's full commitment, or whether they conserve capacity given Lebanon's fragile political situation.</p>
<div class="sc-meta">
<div><div class="mk">If Hezbollah stays limited</div><div class="mv" style="color:var(--gold)">War remains bilateral Iran-US/Israel; manageable</div></div>
<div><div class="mk">If Hezbollah goes full</div><div class="mv" style="color:var(--red)">Trajectory 5; Israeli civilian crisis; massive escalation; Lebanon collapse risk</div></div>
</div>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag o">UNKNOWN 4</span><h3>Iran's Nuclear Breakout Decision</h3></div>
<p>The IAEA confirmed on March 2 that nuclear installations were NOT struck in the first wave. Iran retains ~400kg of 60%-enriched uranium and scientific knowledge to enrich to weapons grade. The theoretical "dash time" to a first device is weeks to months. If the IRGC concludes regime collapse is certain, a nuclear breakout attempt — not a usable weapon, but a political signal — becomes rational as last resort. This would be the most dangerous decision in the conflict.</p>
<div class="sc-meta">
<div><div class="mk">Current probability</div><div class="mv" style="color:var(--orange)">15% (rises to 35%+ if regime faces imminent collapse)</div></div>
<div><div class="mk">If attempted</div><div class="mv" style="color:var(--red)">Immediate Israeli preventive strike; potential use of Jericho III; catastrophic escalation</div></div>
</div>
</div>

<div class="sc">
<div class="sc-head"><span class="sc-tag p">UNKNOWN 5</span><h3>Chinese Economic Coercion of the United States</h3></div>
<p>China holds ~$750–800 billion in US Treasury securities. If China concludes the Iran war is fundamentally damaging Chinese interests (long Hormuz closure, global recession, Iranian ally destroyed), it has economic levers it has never deployed: Treasury selling, yuan-denominated oil contracts, halting exports of critical minerals (rare earths, semiconductor inputs). China has strong incentive NOT to use these weapons (mutual assured economic destruction) — but if the war extends 3–6 months and Beijing concludes the US is restructuring the entire Middle East, this calculus could change.</p>
<div class="sc-meta">
<div><div class="mk">Probability if war &lt; 60 days</div><div class="mv" style="color:var(--purple)">10%</div></div>
<div><div class="mk">Probability if war &gt; 90 days + Iran regime collapse imminent</div><div class="mv" style="color:var(--orange)">25%</div></div>
<div><div class="mk">If deployed</div><div class="mv" style="color:var(--red)">Global financial crisis; US-China relations rupture; new Cold War threshold crossed</div></div>
</div>
</div>

<div class="card cl-g" style="margin-top:8px;">
<h3>Bonus Unknown: US Domestic Politics</h3>
<p>The Senate already voted on war powers (failed to stop Trump, but close). A single mass-casualty event at a US base — say 50+ American soldiers killed in a mass salvo on Al Udeid — would trigger a domestic political crisis that could either force rapid escalation ("he must avenge them") or rapid de-escalation ("this war is killing Americans"). The direction depends entirely on political framing in the 48 hours after such an event. This is the <strong>highest-impact, least-predictable variable of all.</strong></p>
</div>

</div><!-- /tab-unknowns -->

</div><!-- /dash-main -->

<!-- ═══ SOURCES ════════════════════════════════════════════ -->
<div class="sources" style="max-width:1380px;margin:0 auto;padding:0 22px 28px;">
<h3>SOURCES — Live reporting as of March 8, 2026</h3>
<p><a href="https://en.wikipedia.org/wiki/2026_Iran_war">Wikipedia: 2026 Iran War</a></p>
<p><a href="https://commonslibrary.parliament.uk/research-briefings/cbp-10521/">UK House of Commons Library: US-Israel Strikes on Iran Feb/Mar 2026</a></p>
<p><a href="https://www.aljazeera.com/news/2026/3/1/us-israel-attacks-on-iran-death-toll-and-injuries-live-tracker">Al Jazeera: Death toll live tracker</a></p>
<p><a href="https://www.aljazeera.com/news/2026/3/1/how-us-israel-attacks-on-iran-threaten-the-strait-of-hormuz-oil-markets">Al Jazeera: Strait of Hormuz threat analysis</a></p>
<p><a href="https://www.cnbc.com/2026/03/07/not-slowing-down-one-week-on-us-israeli-strikes-on-iran-continue.html">CNBC: One week on — strikes continue</a></p>
<p><a href="https://www.npr.org/2026/03/06/nx-s1-5738448/iran-us-israel-war">NPR: Israel strikes Beirut and Tehran; Trump demands unconditional surrender</a></p>
<p><a href="https://www.washingtonpost.com/world/2026/03/01/iran-succession-supreme-leader-khamenei/">Washington Post: Iran succession after Khamenei</a></p>
<p><a href="https://www.rand.org/pubs/commentary/2026/03/who-or-what-will-replace-irans-supreme-leader-ali-khamenei.html">RAND: Who will replace Khamenei?</a></p>
<p><a href="https://www.bloomberg.com/news/articles/2026-03-05/iran-war-how-oil-prices-are-surging-as-hormuz-shipping-production-disrupted">Bloomberg: Oil prices and Hormuz disruption</a></p>
<p><a href="https://www.morganstanley.com/insights/articles/iran-war-oil-inflation-stock-market-2026">Morgan Stanley: Oil, inflation, and market analysis</a></p>
<p><a href="https://www.oxfordeconomics.com/resource/the-2026-iran-war-an-initial-take-and-implications/">Oxford Economics: 2026 Iran War implications</a></p>
<p><a href="https://www.cnbc.com/2026/03/02/iran-china-russia-strikes-assistance-alliance-weapons-missiles-geopolitics-oil-prices-ukraine.html">CNBC: Why Iran should not count on Russia and China</a></p>
<p><a href="https://www.britannica.com/event/2026-Iran-Conflict">Britannica: 2026 Iran Conflict explained</a></p>
</div>

<script>
function showTab(name, btn) {
  document.querySelectorAll('.tab-pane').forEach(function(el){ el.classList.remove('active'); });
  document.querySelectorAll('.dash-nav button').forEach(function(el){ el.classList.remove('active'); });
  document.getElementById('tab-' + name).classList.add('active');
  btn.classList.add('active');
  window.scrollTo({top: 0, behavior: 'smooth'});
}
</script>
