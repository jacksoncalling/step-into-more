# Narrative: Die Infrastruktur ist eine Datei (Wedge Story)

> Die Geschichte, die ein Gespräch über *Orchestrierung über Silos hinweg* öffnet — ohne
> teure Plattform, ohne Datenteam. Quelle für Erstgespräche mit KMU, Produkt-/CS-Teams,
> Trägern, die Kontext zum Fließen bringen wollen. Geschwister-Narrativ zu `icm-wedge.md`.
> **Entwurf — Boden für Variationen.**

## Kernbotschaft (eine Zeile)
**„Das größte Problem in jeder Organisation ist nicht zu wenig KI — es ist, dass Kontext
nicht über Silos hinweg fließt. Diese Infrastruktur muss keine Plattform sein. Sie kann
eine Ordnerstruktur sein, die Menschen noch lesen und steuern."**

## Woher das kommt (der Anlass)
Scott Brinker (martech-Vordenker) beschreibt, wie Databricks mit *CustomerLake* die
Anwendungs- in die Infrastrukturschicht zieht. Sein Kernsatz: *„He who integrates the data
integrates the universe."* Das eigentliche Problem in der martech-Welt war nie zu wenig
Software — es war **Integration von Kontext über die Silos hinweg.** Der ganze historische
Bogen, den er zeichnet — Punkt-zu-Punkt → Hub-and-Spoke → composable → embedded — ist die
Geschichte von Organisationen, die Kontext fließen lassen wollen, ohne im n²-Chaos zu ersaufen.

**Der Dreh:** Databricks beantwortet diese Frage mit Milliarden Datenzeilen, Agenten-Schwärmen
und Echtzeit. ICM beantwortet *dieselbe Frage* mit Ordnern und Markdown-Dateien. Es ist nicht
die kleine, billige Version — es ist die **andere Achse**: Interpretierbarkeit und menschliches
Urteil statt Skalierung und Geschwindigkeit.

## Der Bogen (60 Sekunden)
1. **Wo du stehst:** Dein Wissen über Kund*innen, Markt, „wie wir hier arbeiten" sitzt in
   Köpfen und E-Mail-Postfächern. Punkt-zu-Punkt. Silo City.
2. **Das Problem:** Nicht zu wenig KI — sondern dass Kontext nicht *über* die Teams hinweg
   fließt. Produkt weiß nicht, was Vertrieb hört. Coach A lernt nicht, was Coach B entdeckt.
3. **Die übliche Antwort:** Eine teure Plattform kaufen (Lock-in, Datenteam nötig, deckt nur
   einen Teil ab). Für die meisten Organisationen mit Kanonen auf Spatzen.
4. **Der Dreh (ICM):** Ein gemeinsamer Ordner als *Bus*. Jedes Team schreibt einmal hinein —
   und ist mit allen verbunden. Hub-and-Spoke für **Bedeutung**, nicht für Datenzeilen.
   In normaler Sprache, lesbar, der Mensch entscheidet an jedem Gate.
5. **Der Beweis:** Das Sensing System — ein Coaching-Netz, in dem eine Beobachtung „nach oben
   und quer" fließt, ohne dass je persönliche Daten den geschützten Ordner verlassen. Die
   Laufwerksgrenzen *sind* der Datenschutz. DSGVO durch Architektur, nicht durch Policy.
6. **Der Einstieg:** Der eine Ordner, der den größten Silo aufbricht. Klein, risikoarm,
   keine neue Software.

## Die ehrliche Linie (nicht überverkaufen)
Eine Datei *ist* die richtige Infrastruktur — aber nicht immer. Wann sie gewinnt:
- **Wenig Datenvolumen, viel Kontext-Reichtum.** Ein Träger hat kein Datenproblem, er hat ein
  *Bedeutungsproblem*.
- Der Engpass ist **menschliche Interpretation und Vertrauen**, nicht Rechenleistung.
- Regulierung/Einwilligung macht „Daten nicht bewegen" zum *Feature*.
- Kein Datenteam — und nie eines geben wird. Die Organisation muss ihre eigene
  Integrationsschicht **lesen und besitzen** können.

Wann eine Datei *bricht* (und man es sagen muss):
- Viele gleichzeitige Schreibende, Echtzeit → Konflikte, Veraltetes.
- Sobald man **quer über tausende Dateien** abfragen muss, braucht es einen Index / Graph
  darüber. (Das ist der Punkt, an dem ein Graph wie Terroir die Datei ablöst — die meisten
  Organisationen erreichen ihn nie, und das ist in Ordnung.)

## Das Diagnose-Werkzeug (im Erstgespräch)
Brinkers Komplexitätskurve, auf *Bedeutung* statt *Daten* angewandt:

> **„Wie bewegt sich heute Kontext zwischen euren Teams?"**
> 90 % antworten: *in Köpfen und per E-Mail* = Silo City, Punkt-zu-Punkt, n².
> → ICM-als-Datei gibt ihnen Hub-and-Spoke für Kontext, zu nahezu null Kosten, ohne neues Tool.

Eine konkrete, verkaufbare Diagnose — und ein klarer erster Auftrag.

## Beide Schichten — die Reife-Geschichte
Wir besitzen *beide* Enden von Brinkers „composable canvas":
- **Dateien (Sensing System)** = das governte Fundament, der Kern.
- **Graph (Terroir)** = die semantische Schicht für den Tag, an dem „quer abfragen" zum
  Engpass wird — unser Unity-Catalog / unsere Genie-Ontology.

Der Weg, den wir anbieten: **als Datei starten → zum Graph reifen, wenn der Engpass es
verlangt.** Nicht vorher. Das ist die ehrliche Version des Versprechens.

## Was wir NIE behaupten
- Dass wir „Databricks für Kleine" sind. Wir sind die andere Achse, nicht die billige Kopie.
- Pauschale Rechtssicherheit. Ein echter Pilot bezieht die/den Datenschutzbeauftragte*n ein.
- Dass eine Datei jedes Problem löst. Sie löst das *Kontext-fließt-nicht*-Problem für
  Organisationen, deren Engpass Bedeutung und Vertrauen ist — nicht Volumen.

## Wohin es führt
Wedge-Gespräch → bei Trägern Sensing System + später Limina (`limina.md`);
bei KMU / Produkt- & CS-Teams tiefere ICM-Systeme. Langes Spiel: Substack-Essay aus der
Brinker-Achse (Datei vs. Plattform · Mensch-am-Gate vs. Agenten-Schwarm).

---
*Quelle des Anlasses: Scott Brinker, „The day infrastructure marched on the martech
application layer", 22. Juni 2026 (chiefmartec). Extern, nur als Aufhänger — kein Zitat ohne
Kontext.*
