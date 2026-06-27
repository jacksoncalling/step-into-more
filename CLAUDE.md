# Step Into More — Consulting HQ
**Joshua Baker · joshua@stepintomore.co · +49 151 59057395**

---

## What is This?

The home of my **consulting practice**: guiding organizations—starting with educational providers like the DAA—to leverage their **existing AI tools** (Microsoft 365 Copilot, ChatGPT, Claude) through ICM (Interpretable Context Methodology, by Jake van Clief). No new software, utilizing natural language, keeping humans at every decision point.

**Identity & Focus:** I am a native English speaker operating primarily in the German market. All my internal system routing, planning, and agent instructions are in English, while the client-facing deliverables and marketing assets are generated in German. 

**The Core Challenge:** "Step Into More" is an early-stage venture currently focused on breaking through the initial hurdle: landing the **very first paying customer** and securing that crucial first positive feedback loop. 

**Offer in one sentence:** I accompany organizations using ICM and their existing software suite as a foundation to create real, tangible value for employees and their end customers. Lets make it two, the people or workers need to be a central part of this transformation,
this means I meat them where they are leadership and the workers. Feelings of uncertainty, anxiety (FOMO ie) curiosity are all a part of this transition that we are experiencing in the world andin our companies.
Education, transperancy and respect are essential components of a successful transformation. I am the guide at the edge which understands the complexity of people and the potential of the tools. 

---

## The Model: Three Things That Are Never Mixed

1. **Business / Consulting** (this folder) — how I sell and consult: reusable `bausteine/` (building blocks: ICM explanations, templates, tools) + client relationships managed in `clients/`.
2. **Products** — what I *deliver*, generic and versioned. These are **separate top-level repositories** referenced here but never copied directly into this directory (to prevent tightly coupled code):
   - **Sensing System** → `~/sensing-system/` (Coach/Researcher/Commons/Coachee, ICM sensor network)
   - **Limina** → `~/Documents/Limina/` (AI orientation for participants)
3. **Clients** — active and prospective engagements. **DAA is designated as Client #1**. Every client folder holds its specific pitch, reference documents, and product deployment details.

> Originating from the legacy `~/job coach/` folder (Skool competition, first build). The original DAA pitch is now located in `clients/daa/`, and outdated product duplicates reside in `job coach/_archiv/` (superseded by `sensing-system`).

---

## Active Clients & Pipeline

- `clients/daa/` — DAA Talentcenter Aachen. ICM + AI Consulting. Phase: Initial Contact / Proposal. See `business-dev/CONTEXT.md` for active pipeline status.
- **Target Pipeline:** Actively pursuing the first official conversion via three core channels:
  1. *Warm Network:* Approaching self-employed contacts and local business owners within my personal network to run test pilots and gain initial validation.
  2. *Physical Ground Game:* Direct local outreach via physical cold drops—visiting offices, handing out flyers, and distributing business cards.
  3. *Digital Outreach:* Target-specific cold email campaigns.

## Routing

| If I want to… | Go to | Read |
|-------------|---------|------|
| Edit reusable building blocks | `bausteine/` | `bausteine/README.md` |
| Work on client DAA | `clients/daa/` | `clients/daa/CLAUDE.md` |
| Explain ICM (Letters/Slides/Conversations) | `bausteine/icm-erklaert/` | — |
| Be coached toward the first client | `first-client-coach/` | `identity.md` |
| Access Voice/Story/Asset/Content for marketing | `marketing/` | `marketing/CONTEXT.md` |
| Research & qualify leads (cold outreach) | `business-dev/lead-research/` | its local `CLAUDE.md` |
| Work the warm network (trust, free pilots) | `business-dev/warm-network/` | its local `CLAUDE.md` |
| See the live pipeline at a glance (the cockpit) | `business-dev/lead-research/output/` | `pipeline-board.html` |
| See the whole team's state + open handoffs | `commons/` | `roundtable.md` |
| See what tools/skills an agent has | each agent's folder | its `tools.md` |
| Build the Sensing System product | `~/sensing-system/` | its local `README.md` |
| Access Limina product design | `~/Documents/Limina/` | — |
| Find new clients / manage sales pipeline | `business-dev/` | `business-dev/CONTEXT.md` |
| Onboard a new client | Copy `clients/client-template/` → rename | its local `CLAUDE.md` |

---

## Architecture
step-into-more/
├── CLAUDE.md                     ← This file (Map: Business · Products · Clients)
├── brief.md                      ← The client brief (me, treated as a real client)
├── first-client-coach/           ← Founder-facing Coach (agent): two minds (Joe Hudson + operator), warm-first
├── commons/                      ← The round table: agents post handoffs + learn each other's work (roundtable.md)
├── bausteine/                    ← Reusable, generic blocks (≈ Jake's templates/)
│   ├── README.md
│   ├── builders-paper.md         ← ICM / competition messaging
│   ├── icm-erklaert/             ← In-depth ICM material (MD + visual HTML)
│   ├── vorlagen/                 ← Empty ICM frameworks (CLAUDE.md/CONTEXT.md, tool skeletons)
│   └── werkzeuge/                ← Functional tools (interview-coach-skill)
├── marketing/                    ← Asset & content engine: WHAT we say/show
│   ├── CONTEXT.md                ← Strategy (Short/Long Play · 3 Doors · DE/EN)
│   ├── voice/                    ← voice-charter + voice-de + voice-en (one soul, two registers)
│   ├── narratives/               ← icm-wedge (short) · socio-technical (long) · origin-story
│   ├── offers/                   ← icm-consulting (leads) · limina (expand) · coaching (soul)
│   ├── assets/                   ← decks/ · html/ · one-pagers/ · templates/
│   └── content/                  ← substack/ (long game) · social/
├── business-dev/                 ← Outreach engine: WHOM we contact (internal)
│   ├── CONTEXT.md
│   ├── lead-research/            ← ICM Workspace: Finding & qualifying targets (cold) + the cockpit (output/pipeline-board.html)
│   ├── warm-network/             ← Warm trust channel: trust ledger, warm loop, free pilots
│   ├── outreach/                 ← email-templates/ (cold-de · cold-en)
│   ├── pipeline/   └── case-studies/
└── clients/
├── client-template/          ← Onboarding template for copying
│   ├── CLAUDE.md
│   ├── intake/   ├── deliverables/   └── communications/
└── daa/                      ← Client #1
├── CLAUDE.md             ← DAA context (Contacts, funding, sales approach)
├── intake/               ← Original DAA PDFs (Flyers, minutes, TCAK)
├── deliverables/         ← icm methodology (HTML+PDF), icm pitch, limina flyer
├── communications/       ← Meeting notes, email drafts
└── templates/            ← DAA program: minutes + modules 01–05

---

## Critical Rules

- **NEVER reference information from one client inside another client’s folder.** If there is any doubt regarding confidentiality, ask first.
- **Building blocks (`bausteine/`) must remain entirely generic.** No client names or specific identifying details are allowed in this directory. All client-specific work lives strictly inside `clients/<client_name>/`.
- **Everything initializes from templates.** Base new clients on `clients/client-template/`. Tailor deliverables inside the specific client's folder. Never modify original templates in `bausteine/` or `client-template/` directly—always work on a copy.
- **Do not copy product code into this repo.** `sensing-system` and `Limina` remain in their own independent repositories; only reference them here and set paths per deployment.
- **Keep data privacy representations honest.** Avoid sweeping legal/compliance guarantees. Frame conversations around: "Ask these questions + here is how this methodology helps." An authentic pilot project must actively involve the client’s Data Protection Officer (DSB). Do not assume or state that DAA runs Copilot in their own tenant yet—this is unverified.
- **Execution Strategy Priority:** All active workflows must align with the primary milestone of moving a warm contact or cold lead into a signed, paid engagement to generate a strong testimonial.
- Run `/wrap-up` at the conclusion of every session.

## Naming Conventions

- Pitch/Proposal: `client_proposal_YYYY-MM.md`
- Deliverable: `client_deliverable-type_v1.md`
- Meeting Notes: `client_YYYY-MM-DD_topic.md`
- Email Draft: `client_recipient_topic.md`
- Case Study: `YYYY_industry_result.md` (Always entirely anonymized)