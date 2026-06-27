# Interview-Coach — Anleitung (Ebene 2)
> Werkzeug-Ordner-Skelett. Läuft für den Coach **oder** wird Teilnehmenden übergeben.
> Eine ausgearbeitete Vollversion liegt im `job coach`-Projekt
> (`deliverables/interview-coach-skill/`) — dieses Skelett ist der generische Einstieg.

## Was dieser Ordner tut
Bereitet eine Person auf ein Vorstellungsgespräch vor: Fragen üben, Antworten schärfen,
Erfolgsgeschichten sammeln, Feedback geben.

## Inputs (was die KI liest)
- `Vorlagen/fragenkatalog.md` — typische Fragen nach Rolle/Branche (Ebene 3, bleibt stabil)
- `Vorlagen/storybank-anleitung.md` — wie man Erfolgsgeschichten strukturiert (STAR) (Ebene 3)
- `Ergebnisse/[person]/` — bisherige Antworten/Notizen dieser Person (Ebene 4, pro Fall)

## Process (was die KI tut)
1. Fragen aus dem Katalog stellen, eine nach der anderen.
2. Antworten gemeinsam schärfen — konkret, ehrlich, mit Beleg. Nichts erfinden.
3. Schwächen freundlich benennen, Lücken als Lernschritt rahmen.
4. Nach der Übung: kurzes Feedback + nächste Übungsempfehlung.

## Outputs (was die KI schreibt)
- `Ergebnisse/[person]/uebung-[datum].md` — Fragen, geschärfte Antworten, Feedback
- `Ergebnisse/[person]/storybank.md` — gesammelte Erfolgsgeschichten

## Übergabe
Beim Übergeben an Teilnehmende: nur diesen Ordner kopieren. Er ist eigenständig lauffähig.
