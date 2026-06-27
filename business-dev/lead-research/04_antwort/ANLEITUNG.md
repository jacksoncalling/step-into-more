# Stage 04 — Reply Triage (Antwort)

Classify an incoming reply and update the contact's state. The agent reads and
classifies; **Josh decides and sends.** No automatic replies, ever.

## Inputs
- The incoming reply — pasted by Josh, or later fetched via the Gmail MCP `[MCP: gmail read]`
- The contact card in `../03_ansprache/ergebnisse/<kunde>_<person>_<thema>.md`
  (what we proposed, which door, the hook)

## Process
1. Read the reply against the contact card — what did we offer, and how did they respond?
2. Classify intent into exactly one:
   - **INTERESTED** — wants to talk / meet / learn more
   - **QUESTION** — positive but needs info before committing
   - **NOT NOW** — friendly, wrong timing
   - **NO** — declines
   - **UNSUBSCRIBE** — asks to stop / objects to contact
3. Update the contact card: set `Status`, append a dated note with the reply gist + your classification + reasoning.
4. Update `../output/pipeline-board.html` — move the card to **Replied**; `NOT NOW` → nurture; `NO`/`UNSUBSCRIBE` → declined.
5. Recommend the next action and **draft** it — but send nothing:
   - INTERESTED → hand to `05_termin/` (scheduling).
   - QUESTION → draft a short German answer; Josh reviews & sends.
   - NOT NOW → set a nurture date on the card; no further action now.
   - NO → optional one-line German thank-you draft; close gracefully.
   - UNSUBSCRIBE → **stop all contact immediately**, record it on the card (UWG/DSGVO duty).

## Human gate
The agent classifies and drafts. **Josh confirms the classification and sends.**

## Output
- Updated contact card (Status + dated reply note)
- Updated `../output/pipeline-board.html`
- A drafted reply where applicable (German, client-facing)

## Übergabe
INTERESTED → `05_termin/`. QUESTION → back to Josh to send. NOT NOW → nurture.
NO / UNSUBSCRIBE → closed, logged.
