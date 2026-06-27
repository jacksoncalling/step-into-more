# Bewerbungstool — Anleitung (Ebene 2)
> Werkzeug-Ordner-Skelett. Schneidet Lebenslauf & Anschreiben auf eine konkrete Stelle zu.
> Prinzip: aus einem Stamm-Profil + einer Geschichten-Sammlung; ehrlich, nichts erfunden.

## Was dieser Ordner tut
Hilft, Bewerbungsunterlagen auf eine konkrete Stellenanzeige zuzuschneiden — Anschreiben
zuerst, story-getragen, dann der passende Lebenslauf-Zuschnitt.

## Inputs (was die KI liest)
- `Vorlagen/stamm-profil.md` — vollständiger Werdegang der Person (Ebene 3, bleibt stabil)
- `Vorlagen/storybank.md` — Geschichten mit Ergebnis-Bezug (Ebene 3)
- `Vorlagen/anschreiben-stil.md` — Tonalität: spielerisch, story-geführt (Ebene 3)
- `Ergebnisse/[stelle]/stellenanzeige.md` — die konkrete Anzeige (Ebene 4, pro Fall)

## Process (was die KI tut)
1. Stellenanzeige lesen, Kernanforderungen herausziehen.
2. Aus Stamm-Profil + Storybank die passenden Belege wählen — **nur Vorhandenes**.
3. Anschreiben entwerfen (Geschichte zuerst). Lücken benennen und umdeuten, nicht kaschieren.
4. Lebenslauf auf die Stelle zuschneiden (Reihenfolge, Schwerpunkte).

## Outputs (was die KI schreibt)
- `Ergebnisse/[stelle]/anschreiben.md`
- `Ergebnisse/[stelle]/lebenslauf-zuschnitt.md`

## Regel
Niemals Qualifikationen, Daten oder Erfahrungen erfinden. Lücken ehrlich benennen und als
Stärke oder Lernschritt rahmen.
