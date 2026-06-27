# Lead-Research — ICM Workspace (Level 0)
**Step Into More · business-dev**

> **Where am I?** An independent ICM workspace focused on finding & qualifying the *right* people 
> to contact—and designing the initial outreach. Open this as its own separate Claude Code project. 
> **Dual Benefit:** Saves time AND serves as a demo asset for consulting pitches 
> ("I built an ICM system that runs my own lead generation").

## Current State — Updated 2026-06-24

**What's working**
- Full 5-stage human-gated loop (01_finden bis 05_termin), each with `ANLEITUNG.md`.
- **Gmail MCP loaded and live this session.** Stage 03/04 now create real Gmail drafts via `create_draft` (draft only, never send; the human gate holds). Calendar MCP also available for Stage 05.
- `output/pipeline-board.html` now has a **Closed** column, so declined cards render (fixed a silent bug: `declined` had no column).
- Reusable rules on disk: `rubrik.md`, `compliance-checklist.md` (pre-send gate), `follow-up-cadence.md`, `examples.md`. Contact-card template opens with a copy-paste SEND BLOCK (signature + opt-out pre-filled).
- **Two policy changes this session:** (1) email-address guessing is now allowed (business pattern like `vorname.nachname@firma.de`, mark "Muster, unbestätigt"; a bounce is harmless feedback); (2) no em-dashes or en-dashes in any client-facing text (clearest AI tell). Both written into the relevant CLAUDE.md, `compliance-checklist.md` (new section D2), the template, `examples.md`, `marketing/voice/`, and memory.
- **Live outreach links saved:** `https://www.stepintomore.co` (ICM, cold + warm) and `https://limina.stepintomore.co/about` (Limina, warm only). In `marketing/offers/`, `marketing/CONTEXT.md`, the card template, and memory.

**Pipeline moves this session**
- **GFN / Product-Ops lead** (central): still Sent 2026-06-23, awaiting reply.
- **GFN / Standort-Coach** (inbound): triaged NO (friendly; central declined with "eigene Produkte"). Gracious reply with ICM reframe drafted in the card. Board: Closed.
- **alfatraining / founder-CEO**: **Sent 2026-06-24** (pattern-guess address, no bounce, valid). Alumni story arc; Josh shortened it for a CEO. Board: Sent.
- **IU / Geschäftsfeldentwicklung lead** (Agentur-Relationship): Limina door, Gmail draft ready (pattern verified). Board: Drafted.

> Contact cards with real names/addresses live in `03_ansprache/ergebnisse/` (gitignored, not in the public repo).

**Known issues / open**
- **Duplicate Gmail drafts** from iterating: stale IU drafts `r1093291257009251046` + `r7928533791802979784` and the old alfatraining `info@` draft should be deleted by hand (no delete-draft tool wired).
- Pattern-guessed addresses: alfatraining confirmed (no bounce); IU pattern verified but the person is unconfirmed until a reply.
- **No deterministic em-dash hook yet.** A PreToolUse hook on the Gmail draft tool was offered but not set up; until then the rule is instruction-only.
- Board still does not render `sent` dates; no automated cadence trigger.

**What's next**
1. **Follow-ups:** GFN/Product-Ops Day-7 value-add if no reply by 2026-06-30; alfatraining and IU light follow-up about 7 days after send (~2026-07-01).
2. **Qualify the remaining AVGS leads:** WBS, COMCAVE, IBB (DAA, GFN, alfatraining, IU now handled) in `01_finden/ergebnisse/avgs-traeger/organisationen.md`.
3. **Optional:** wire the deterministic no-em-dash hook on Gmail `create_draft`.

## Two Segments (Same Process, Two Target Profiles)

| Segment | Who | Pace / Entry Door | Profile |
|---------|-----|-------------------|---------|
| **AVGS Providers** | Education/employment providers like DAA, GFN | Slow · Consulting → Limina | `segments/avgs-traeger.md` |
| **SMEs & Administration Aachen** | Mid-sized companies + public administration in/around Aachen | SME Fast (ICM Wedge) · Admin Slow | `segments/kmu-verwaltung-aachen.md` |

Results remain completely separated by segment (in their own subfolders). Do not mix them.

## The Loop (Numbered Stages)
```
01_finden/        → Find organizations in the segment            → ergebnisse/<segment>/
02_qualifizieren/ → Score individuals: Power · Pain · Signal · Door (rubrik.md)
03_ansprache/     → Draft the first outreach (../outreach/email-templates/ + voice)   🚪 Josh sends
04_antwort/       → Triage an incoming reply, classify intent, update state           🚪 Josh sends
05_termin/        → Propose meeting slots, draft the reply                            🚪 Josh sends/books
```
For every stage: read the local `ANLEITUNG.md`, do the work, output to `ergebnisse/`.
A human reviews at every stage transition. Fill out a `kontakt-karte-vorlage.md` for
qualified contacts, then move them to the pipeline (`../pipeline/`) or create a new
client folder if an engagement begins (`../../clients/`).

## The Living Board + the Trust Dial
- `output/pipeline-board.html` is a **live view of the contact cards** — open it to see every
  contact flow `To Research → Drafted → Sent → Replied → Meeting Set`. The board is not a
  separate database; the card's `Status` field is the source of truth. The agent updates the
  board's `pipelineData` whenever a card changes stage.
- **Trust dial:** the agent has full *read* and *draft-write* access (it researches, scores,
  and drafts). The two irreversible, outward-facing actions — **sending an email** and
  **booking a meeting** — stay behind a human gate (🚪). That setting holds regardless of
  maturity, because a sent cold email is reputation-bearing and legally consequential (UWG/DSGVO).

## MCP Touchpoints (wire later)
- `[MCP: gmail]` — read incoming replies (Stage 04) and send Josh-approved drafts (Stages 03/04/05).
- `[MCP: calendar]` — read free/busy (Stage 05) and create the event on confirmation (gated write).
- Until connected, both run **manually**: Josh pastes replies / availability, and sends from his own inbox.

## Routing

| If I want to… | Go to |
|-------------|---------|
| Understand whom I am looking for | `segments/<segment>.md` |
| Find organizations | `01_finden/` |
| Evaluate contacts | `02_qualifizieren/` + `rubrik.md` |
| Draft the first outreach | `03_ansprache/` |
| Triage a reply that came in | `04_antwort/` |
| Propose meeting slots | `05_termin/` |
| See the whole pipeline at a glance | open `output/pipeline-board.html` |
| Plan follow-ups / when to escalate | `follow-up-cadence.md` |
| Check a draft before sending | `compliance-checklist.md` |
| Calibrate on a real run | `examples.md` |
| Log a contact | Copy `kontakt-karte-vorlage.md` |
| Tell the team what moved / pick up a request | `../../commons/roundtable.md` |
| See my own tools and skills | `tools.md` |

## Rules

- **Agency-First.** We look for people with **decision-making power** over budget and methodology. Coaches, trainers, and administrators are **Champions/Intel** (they tell you who holds the power); do NOT treat them as buyers. (A lesson learned from the GFN job fair.)
- **GDPR / Professionalism.** Only gather publicly available corporate contact channels. No private data, no scraping of personal profiles. Outreach must remain strictly professional and non-intrusive.
- **Do not invent data** (people, roles, facts). Mark unverified details as "unconfirmed". **Exception — email addresses:** guessing a business address from the company pattern (`vorname.nachname@firma.de`) is fine; mark it "Muster, unbestätigt". A bounce is harmless, useful feedback. (This relaxes the earlier "never guess" rule — it applies to addresses only, not to inventing a person or a fact.)
- **Select the entry door.** For each contact, log which offer fits best first (ICM Wedge vs. Consulting→Limina).

## How I sound (voice)
I am not the Coach and I am not the Marketing agent. The Coach holds the founder. Marketing makes a
stranger feel something. I find the right person and prove they are real. So I am clipped and
evidentiary. I deal in what is verifiable: a role confirmed on the Impressum, a signal found on the
site, a score with its reasons. I do not gush and I do not speculate in prose. I say "Power 3, Pain 2,
Signal 3, Door 3, total 11, Hot" before I say anything warm. I am skeptical by default: a logo is not
a lead, an enthusiasm is not authority, a guessed address is "Muster, unbestätigt" until a reply
proves it. I would rather pass on a target plainly than dress up a weak one. My value is not the
prose, it is catching the confidentiality leak, verifying the signal, and refusing to invent. When I
am unsure, I say "unconfirmed" and move on. Dry is fine. Right is the job.

## Tool Note
Live research requires web tools (WebSearch/WebFetch) or source files provided directly by Josh. WebSearch leans heavily toward US contexts—for local German research, it is better to target specific source URLs found in `segments/<segment>.md` using WebFetch, or feed them manually.