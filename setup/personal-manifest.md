# Personal manifest: what setup resets vs keeps

> The line between the reusable engine and the original owner's personal layer. Setup replaces the
> PERSONAL files with blanks (from `setup/templates/`) and leaves the ENGINE untouched.

## Personal (replace with your own)
| File or folder | What it holds | How to reset |
|---|---|---|
| `brief.md` | The client brief (you, as the client) | copy `setup/templates/brief.template.md` |
| `positioning-canon/README.md` | Facts, voice, hook, golden thread, segments at a glance | copy `setup/templates/positioning-canon.README.template.md` |
| `marketing/voice/voice-charter.md` | What you stand for, how it sounds, what you never do | copy `setup/templates/voice-charter.template.md` |
| `marketing/voice/voice-de.md`, `voice-en.md`, `tone-references.md` | Registers + your real tone anchors | clear; the Guide rebuilds from the charter |
| `marketing/narratives/*`, `marketing/offers/*` | Your story and offers | one `setup/templates/offer.template.md` per offer |
| `marketing/assets/*`, `marketing/content/*` | Your flyers, pages, posts | clear; regenerate with the Marketing Maker after voice + canon exist |
| `business-dev/lead-research/segments/*` | Your target segments | one `setup/templates/segment.template.md` per segment |
| `business-dev/CONTEXT.md` | Your pipeline overview | clear to a blank pipeline |
| `commons/roundtable.md` | The shared log | copy `setup/templates/roundtable.template.md` (empty log, protocol kept) |
| `first-client-coach/brief.md` | The founder brief the Coach reads | the Guide writes this with you (step 1) |
| `first-client-coach/reference/the-terroir-read.md` | The evaluative read of the practice | clear; optional to regenerate if you use Terroir |
| `business-dev/warm-network/ergebnisse/*` | Your warm contacts | use the existing `trust-ledger-vorlage.md` |
| `README.md`, `CLAUDE.md` (personal facts only) | Front door + map | rewrite the personal facts once the canon exists; keep the structure |

## Engine (keep, do not change)
- The four agents: `first-client-coach/`, `marketing/specialist/`, `business-dev/lead-research/`,
  `business-dev/warm-network/` (their `identity.md`, `rules.md`, `examples.md`, `tools.md`)
- `.claude/agents/*` (the callable subagents, including this setup Guide)
- The lead-research loop: `01_finden` through `05_termin` ANLEITUNGs, `rubrik.md`,
  `compliance-checklist.md`, `follow-up-cadence.md`, `kontakt-karte-vorlage.md`
- `commons/README.md` (the protocol)
- `business-dev/warm-network/CLAUDE.md`, `freie-pilotprojekte.md`, `trust-ledger-vorlage.md`
- `bausteine/*` (generic building blocks)
- the `CLAUDE.md` map skeleton (structure stays; only the personal facts inside it change)
