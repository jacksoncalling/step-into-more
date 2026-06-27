# Setup: make this system yours

This repository is a working consulting practice (Step Into More) built as a folder system. The
**engine** (the four agents, the method, the structure) is reusable. The **personal layer** (the
voice, facts, offers, contacts, the read) belongs to the original owner. Setup swaps the personal
layer for yours and leaves the engine untouched.

## What you keep, what you replace
The exact line is in [`personal-manifest.md`](personal-manifest.md). In short:
- **Keep:** the four agents, the lead-research loop, the Commons protocol, the building blocks, the map skeleton.
- **Replace:** your brief, your canon (facts and voice), your offers, your segments, your contacts, your read.

## Recommended path: the Onboarding Guide (guided, over several sessions)
1. **Archive the original owner's personal files.** Until a reset script exists, do this by hand:
   move the files listed in `personal-manifest.md` into a new `_archive/` folder. This never
   destroys anything, it just sets them aside.
2. **Lay down the blanks.** Copy the skeletons from [`setup/templates/`](templates/) into their real
   locations (the manifest says which goes where).
3. **Open Claude at the repo root** and say: **"use the setup subagent"** (or "start onboarding").
4. The Guide reads [`onboarding-checklist.md`](onboarding-checklist.md) and interviews you, one step
   at a time. It drafts, you approve, it writes the file and checks the box. Stop anytime and resume
   next session, it picks up where you left off.

## By hand (no agent)
Work through [`onboarding-checklist.md`](onboarding-checklist.md) yourself, filling each template as you go.

## Notes worth reading first
- **Archive, never destroy.** Setup sets the originals aside; it does not hard-delete them.
- **The four agents stay as they are.** Their `examples.md` are reference calibration from the
  original build (they show how each agent behaves). You do not need to rewrite them.
- **The landing page lives outside this repo** (it was built in Lovable). Setup gives you the words;
  the hosted page is yours to rebuild separately.
- **Voice is built by conversation, not by filling blanks fast.** Let the Guide interview you. The
  point is to surface your real voice, the same way good discovery surfaces a client's.
