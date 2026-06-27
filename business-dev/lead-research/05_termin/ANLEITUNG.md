# Stage 05 — Schedule (Termin)

Turn an interested reply into a proposed meeting. The agent reads availability and
drafts the proposal; **Josh reviews and sends.** Booking a slot is a gated write.

## Inputs
- An **INTERESTED** contact handed over from `04_antwort/` + their reply
- Calendar availability:
  - `[MCP later: gmail/calendar read]` — read Google Calendar free/busy for ~2 weeks
  - `[Now: manual]` — Josh pastes 2–3 open slots
- The contact card

## Process
1. Get availability (MCP read, or Josh's pasted slots).
2. Choose 2–3 candidate slots — spread across days and times; for a cold-ish contact,
   favour the mid-day sweet spot (≈13:00 local). Offer video or phone.
3. Draft a short German reply proposing the slots — warm, concrete, low-friction
   ("Vorschlag, kein Pitch"), easy to confirm with one line.
4. Update the contact card: `Next Step` = proposed slots + date. `Status` stays
   **Replied** until Josh actually sends.

## Human gate
**Josh reviews and sends the proposal.** When the meeting is confirmed (the
confirmation reply runs back through `04_antwort/`), set `Status` → **Meeting Scheduled**.
`[MCP later: create the calendar event — also a gated write, Josh confirms.]`

## Output
- A drafted German scheduling reply in `ergebnisse/<kunde>_<person>_termin.md`
- Updated contact card + `../output/pipeline-board.html`

## Übergabe
On confirmation → card `Status` = Meeting Scheduled (board column **Meeting Set**),
log to `../../pipeline/`. If an engagement begins → new client folder from
`../../../clients/client-template/`.
