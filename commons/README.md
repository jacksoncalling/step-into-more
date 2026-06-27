# The Commons: where the agents meet

> The canon is what the agents all READ (shared beliefs: facts, voice, positioning). The Commons is
> where they WRITE to each other (shared awareness: what just happened, what's needed, who is handing
> what to whom). It is the round table. Without it, the three specialists run as isolated stage gates
> and never learn about each other's work.

## What lives here
- `roundtable.md`: a rolling shared log plus the open-handoffs list. This is the one file every agent
  reads first and posts to last.

## How it relates to the other shared surfaces
| Surface | What it is | Who it is for |
|---|---|---|
| **Positioning Canon** (`../positioning-canon/`) | Shared beliefs, read-only by agents | the team's shared mind |
| **The Commons** (this folder) | Shared awareness and handoffs, read and write | agent to agent (and humans) |
| **Pipeline board** (`../business-dev/lead-research/output/pipeline-board.html`) | Live view of pipeline STATE | humans, at a glance |
| **Coach's Pattern Ledger** (`../first-client-coach/`) | The founder's private patterns | the Coach only |

The board shows *where each contact is*. The Commons shows *what each agent did and needs*, the
narrative the board cannot hold.

## The protocol (every agent follows this)
1. **Read first.** Before starting, read the last few entries in `roundtable.md` and the Open Handoffs.
2. **Do your work.**
3. **Post one entry** at the end: date, agent, Did / Changed / Need / Handoff. Newest on top.
4. **Handoffs are explicit.** If your work creates work for another agent, add a checkbox line under
   Open Handoffs naming that agent. The receiving agent checks it off when it picks it up.
5. **Humans read here too.** One place to see the whole team's state in plain language.

## Where this goes next (not built today)
The Commons is a plain-text file on purpose: every agent can read and write it reliably, and it ships
in the repo. Two natural evolutions, when there is a reason to build them:
- **A dashboard tab** next to the cockpit that renders the roundtable and open handoffs visually.
- **A Slack (or chat) bridge** so agents post to a channel and humans reply in the same place: agent
  to agent to human, one thread. The file stays the source of truth; Slack becomes a view onto it.
