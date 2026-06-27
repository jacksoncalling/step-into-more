#!/usr/bin/env python3
"""Make the website bilingual (DE default, EN via a nav slider).
Injects data-i18n hooks, a DE/EN toggle, and a translation dictionary.
Idempotent-ish: aborts if already bilingual. Leaves the logo SVGs untouched.
"""
import json
from pathlib import Path

SITE = Path("../../website/index.html")
html = SITE.read_text(encoding="utf-8")

if "data-i18n" in html:
    raise SystemExit("Already bilingual — aborting to avoid double-injection.")

# (anchor substring, i18n key) — attribute is inserted before the anchor's first '>'
INJECT = [
    ('<div class="eyebrow">KI-Beratung', "hero_eyebrow"),
    ('<h1>Ihre KI sollte', "hero_h1"),
    ('<p class="sub">', "hero_sub"),
    ('<a class="btn btn-primary" href="mailto:joshua@stepintomore.co?subject=Gespr%C3%A4ch%20zu%20KI%20%2B%20ICM">Gespräch vereinbaren</a>', "btn_call"),
    ('<a class="btn btn-ghost" href="#wie">Wie es funktioniert</a>', "btn_how"),
    ('<p>Vor 20 Jahren', "sov"),
    ('<div class="eyebrow-d">Worum es geht</div>', "p1_eyebrow"),
    ('<h2 class="s">KI ist schon da. Die Frage ist: wie?</h2>', "p1_h2"),
    ('<p class="lead">\n      Die meisten', "p1_lead"),
    ('<h3>Kein Lock-in</h3>', "c1_h3"),
    ('<p>Eine Methode, keine Plattform. Läuft mit Copilot, ChatGPT oder kommenden Werkzeugen. Ändert sich die Technik, bleibt Ihr System.</p>', "c1_p"),
    ('<h3>Der Mensch entscheidet</h3>', "c2_h3"),
    ('<p>Die KI schlägt vor, Sie prüfen und geben frei. An jedem Schritt eine Kontrollstelle — nichts läuft unbeaufsichtigt durch.</p>', "c2_p"),
    ('<h3>Alles bleibt lesbar</h3>', "c3_h3"),
    ('<p>Anleitungen und Ergebnisse sind Textdateien, die jede*r öffnen und anpassen kann. Volle Transparenz statt versteckter Logik.</p>', "c3_p"),
    ('<div class="eyebrow-d">Geringe Hürde</div>', "al_eyebrow"),
    ('<h2 class="s">Und das Beste: Sie arbeiten bereits so</h2>', "al_h2"),
    ('<h3>Dieselbe Arbeitsweise — nur klüger angeordnet</h3>', "al_h3"),
    ('<p>Organisationen arbeiten seit jeher', "al_p"),
    ("<div class=\"eyebrow-d\">So funktioniert's</div>", "how_eyebrow"),
    ('<h2 class="s">Klein anfangen, risikoarm, kein Vertrag</h2>', "how_h2"),
    ('<h3>Kennenlernen</h3>', "s1_h3"),
    ('<p>Wie arbeiten Sie und Ihr Team heute mit KI? Was nervt, was fehlt?</p>', "s1_p"),
    ('<div class="t">30 Minuten · unverbindlich</div>', "s1_t"),
    ('<h3>Ausprobieren</h3>', "s2_h3"),
    ('<p>Wir richten einen ersten Ordner ein, datenschutzkonform, und testen ihn an echter Arbeit.</p>', "s2_p"),
    ('<div class="t">ein erster Schritt</div>', "s2_t"),
    ('<h3>Auswerten</h3>', "s3_h3"),
    ('<p>Hat es geholfen? Was funktioniert, was fehlt? Sie entscheiden, wie es weitergeht.</p>', "s3_p"),
    ('<div class="t">gemeinsam</div>', "s3_t"),
    ('<div class="eyebrow-d">Für wen</div>', "whom_eyebrow"),
    ('<h2 class="s">Wo viel Wissens- und Dokumentenarbeit anfällt</h2>', "whom_h2"),
    ('<h4>KMU &amp; Mittelstand</h4>', "w1_h4"),
    ('<p>Kanzleien, Agenturen, Beratungen, Ingenieurbüros, Praxen — überall, wo KI bisher nur zufällig genutzt wird.</p>', "w1_p"),
    ('<h4>Öffentliche Verwaltung</h4>', "w2_h4"),
    ('<p>Ämter und Eigenbetriebe, die Digitalisierung sicher und nachvollziehbar angehen wollen.</p>', "w2_p"),
    ('<h4>Bildungs- &amp; Coaching-Träger</h4>', "w3_h4"),
    ('<p>Träger, die ihre Beratungsarbeit mit KI stärken wollen — ohne die Menschen aus dem Blick zu verlieren.</p>', "w3_p"),
    ('<div class="eyebrow-d">Der wichtigste Punkt</div>', "tr_eyebrow"),
    ('<h2 class="s">Datenschutz von Anfang an</h2>', "tr_h2"),
    ('<p class="lead">Gerade bei sensiblen Daten', "tr_lead"),
    ('<h4>Wo liegen die Daten?</h4>', "t1_h4"),
    ('<p>Werkzeuge im kontrollierten Rahmen Ihrer Organisation statt privater Konten — wo Microsoft 365 läuft, im eigenen Tenant mit EU-Datenhaltung.</p>', "t1_p"),
    ('<h4>Nur der nötige Kontext</h4>', "t2_h4"),
    ('<p>In jedem Schritt sieht die KI nur, was dieser Schritt braucht. Weniger Angriffsfläche, weniger Risiko.</p>', "t2_p"),
    ('<h4>Alles nachvollziehbar</h4>', "t3_h4"),
    ('<p>Jeder Schritt ist eine lesbare Datei — keine Blackbox. Gemeinsam mit Ihrer IT bzw. Datenschutzbeauftragten.</p>', "t3_p"),
    ('<div class="eyebrow-d">Wer dahinter steht</div>', "ab_eyebrow"),
    ('<p>Ich baue KI-Werkzeuge', "ab_p1"),
    ('<p>Ich verkaufe keine Software', "ab_p2"),
    ('<h4>Der rote Faden</h4>', "ab_thread"),
    ('<a href="https://portfolio.stepintomore.co">Mehr über meine Arbeit →</a>', "ab_link"),
    ('<h2>Vorschlag, <span class="amber">kein Pitch.</span></h2>', "cta_h2"),
    ('<p>Ein kurzes, unverbindliches Gespräch darüber, wo ein erster Schritt bei Ihnen den größten Unterschied machen würde.</p>', "cta_p"),
]

def add_attr(anchor, key):
    i = anchor.index(">")
    return anchor[:i] + f' data-i18n="{key}"' + anchor[i:]

for anchor, key in INJECT:
    n = html.count(anchor)
    if n != 1:
        raise SystemExit(f"Anchor for '{key}' matched {n} times (expected 1): {anchor[:60]!r}")
    html = html.replace(anchor, add_attr(anchor, key), 1)

# nav: wrap CTA with the language toggle
NAV_OLD = '<a class="nav-cta" href="mailto:joshua@stepintomore.co?subject=Gespr%C3%A4ch%20zu%20KI%20%2B%20ICM">Gespräch vereinbaren</a>'
NAV_NEW = (
    '<div class="nav-right">\n'
    '      <button class="lang-toggle" id="langToggle" type="button" aria-label="Sprache wechseln / Switch language"><span data-lang="de">DE</span><span data-lang="en">EN</span></button>\n'
    '      <a class="nav-cta" data-i18n="nav_cta" href="mailto:joshua@stepintomore.co?subject=Gespr%C3%A4ch%20zu%20KI%20%2B%20ICM">Gespräch vereinbaren</a>\n'
    '    </div>'
)
assert html.count(NAV_OLD) == 1
html = html.replace(NAV_OLD, NAV_NEW, 1)

# default language class so German shows before JS runs
assert "<body>" in html
html = html.replace("<body>", '<body class="lang-de">', 1)

# CSS for the toggle
CSS = """
  /* LANGUAGE TOGGLE */
  .nav-right { display:flex; align-items:center; gap:14px; }
  .lang-toggle { display:inline-flex; border:1.5px solid rgba(255,255,255,0.28); border-radius:8px; overflow:hidden; cursor:pointer; background:transparent; padding:0; font-family:inherit; line-height:1; }
  .lang-toggle span { padding:7px 11px; font-size:12px; font-weight:700; letter-spacing:.5px; color:rgba(255,255,255,0.62); transition:background .15s, color .15s; }
  body.lang-de .lang-toggle span[data-lang="de"],
  body.lang-en .lang-toggle span[data-lang="en"] { background:var(--amber); color:var(--ink); }
  @media (max-width:820px){ .nav-right{ gap:10px; } .nav-cta{ font-size:12px; padding:8px 12px; } }
</style>"""
html = html.replace("</style>", CSS, 1)

DICT = {
  "_title": {"de":"Step Into More — KI, die für Sie arbeitet","en":"Step Into More — AI that works for you"},
  "_desc": {"de":"KI-Beratung mit ICM: Ihre vorhandenen Werkzeuge sinnvoll und sicher nutzen — ohne neue Software, in normaler Sprache, mit dem Menschen an jedem Schritt.","en":"AI consulting with ICM: use the tools you already have sensibly and securely — no new software, in plain language, with a human at every step."},
  "nav_cta": {"de":"Gespräch vereinbaren","en":"Book a call"},
  "hero_eyebrow": {"de":"KI-Beratung · Sie behalten die Kontrolle","en":"AI consulting · You stay in control"},
  "hero_h1": {"de":'Ihre KI sollte <span class="amber">für Sie</span> arbeiten — nicht Sie für sie.',"en":'Your AI should work <span class="amber">for you</span> — not you for it.'},
  "hero_sub": {"de":"Sie haben die Werkzeuge schon: Microsoft 365, ChatGPT. Ich helfe Ihnen, sie <strong>sinnvoll und sicher</strong> zu nutzen — gesteuert über eine durchdachte Ordnerstruktur, in normaler Sprache. <strong>Keine neue Software. Kein Lock-in. Der Mensch entscheidet an jedem Schritt.</strong>","en":"You already have the tools: Microsoft 365, ChatGPT. I help you use them <strong>sensibly and securely</strong> — steered by a well-designed folder structure, in plain language. <strong>No new software. No lock-in. A human decides at every step.</strong>"},
  "btn_call": {"de":"Gespräch vereinbaren","en":"Book a call"},
  "btn_how": {"de":"Wie es funktioniert","en":"How it works"},
  "sov": {"de":"Vor 20 Jahren habe ich Menschen geholfen, <b>ihre eigene Energie</b> zu erzeugen — 400+ Solaranlagen. Bewegt hat mich nicht die Technik, sondern Menschen, die sich ermächtigt fühlten. Heute geht es um dasselbe: <b>Ihre eigene KI.</b>","en":"Twenty years ago I helped people generate <b>their own energy</b> — 400+ solar systems. What moved me wasn't the technology, but people who felt empowered. Today it's the same thing: <b>your own AI.</b>"},
  "p1_eyebrow": {"de":"Worum es geht","en":"What this is about"},
  "p1_h2": {"de":"KI ist schon da. Die Frage ist: wie?","en":"AI is already here. The question is: how?"},
  "p1_lead": {"de":"Die meisten nutzen KI zufällig und unstrukturiert — oder kaufen teure Plattformen mit Lock-in, die nur einen Teil der Arbeit abdecken. <strong>ICM ist anders: eine Methode, keine Plattform.</strong> Eine durchdachte Ordnerstruktur steuert die KI, in normaler Sprache. Das funktioniert mit den Werkzeugen, die Sie schon haben.","en":"Most people use AI randomly and unstructured — or buy expensive platforms with lock-in that cover only part of the work. <strong>ICM is different: a method, not a platform.</strong> A well-designed folder structure steers the AI, in plain language. It works with the tools you already have."},
  "c1_h3": {"de":"Kein Lock-in","en":"No lock-in"},
  "c1_p": {"de":"Eine Methode, keine Plattform. Läuft mit Copilot, ChatGPT oder kommenden Werkzeugen. Ändert sich die Technik, bleibt Ihr System.","en":"A method, not a platform. Runs on Copilot, ChatGPT, or whatever comes next. When the technology changes, your system stays."},
  "c2_h3": {"de":"Der Mensch entscheidet","en":"The human decides"},
  "c2_p": {"de":"Die KI schlägt vor, Sie prüfen und geben frei. An jedem Schritt eine Kontrollstelle — nichts läuft unbeaufsichtigt durch.","en":"The AI proposes, you review and approve. A checkpoint at every step — nothing runs through unsupervised."},
  "c3_h3": {"de":"Alles bleibt lesbar","en":"Everything stays readable"},
  "c3_p": {"de":"Anleitungen und Ergebnisse sind Textdateien, die jede*r öffnen und anpassen kann. Volle Transparenz statt versteckter Logik.","en":"Instructions and results are text files anyone can open and adjust. Full transparency instead of hidden logic."},
  "al_eyebrow": {"de":"Geringe Hürde","en":"Low barrier"},
  "al_h2": {"de":"Und das Beste: Sie arbeiten bereits so","en":"And the best part: you already work this way"},
  "al_h3": {"de":"Dieselbe Arbeitsweise — nur klüger angeordnet","en":"The same way of working — just arranged more intelligently"},
  "al_p": {"de":"Organisationen arbeiten seit jeher mit Ordnern und Dateien. ICM ordnet sie nur so an, dass eine KI mitlesen kann. Keine neue Oberfläche, kein Umlernen. Die Veränderung ist klein, der Effekt ist groß.","en":"Organizations have always worked with folders and files. ICM simply arranges them so an AI can read along. No new interface, nothing to relearn. The change is small, the effect is large."},
  "how_eyebrow": {"de":"So funktioniert's","en":"How it works"},
  "how_h2": {"de":"Klein anfangen, risikoarm, kein Vertrag","en":"Start small, low-risk, no contract"},
  "s1_h3": {"de":"Kennenlernen","en":"Get to know each other"},
  "s1_p": {"de":"Wie arbeiten Sie und Ihr Team heute mit KI? Was nervt, was fehlt?","en":"How do you and your team work with AI today? What's frustrating, what's missing?"},
  "s1_t": {"de":"30 Minuten · unverbindlich","en":"30 minutes · no obligation"},
  "s2_h3": {"de":"Ausprobieren","en":"Try it out"},
  "s2_p": {"de":"Wir richten einen ersten Ordner ein, datenschutzkonform, und testen ihn an echter Arbeit.","en":"We set up a first folder, privacy-compliant, and test it on real work."},
  "s2_t": {"de":"ein erster Schritt","en":"a first step"},
  "s3_h3": {"de":"Auswerten","en":"Evaluate"},
  "s3_p": {"de":"Hat es geholfen? Was funktioniert, was fehlt? Sie entscheiden, wie es weitergeht.","en":"Did it help? What works, what's missing? You decide what happens next."},
  "s3_t": {"de":"gemeinsam","en":"together"},
  "whom_eyebrow": {"de":"Für wen","en":"Who it's for"},
  "whom_h2": {"de":"Wo viel Wissens- und Dokumentenarbeit anfällt","en":"Wherever there's a lot of knowledge and document work"},
  "w1_h4": {"de":"KMU &amp; Mittelstand","en":"SMEs &amp; mid-sized firms"},
  "w1_p": {"de":"Kanzleien, Agenturen, Beratungen, Ingenieurbüros, Praxen — überall, wo KI bisher nur zufällig genutzt wird.","en":"Law firms, agencies, consultancies, engineering offices, medical practices — anywhere AI is so far used only by chance."},
  "w2_h4": {"de":"Öffentliche Verwaltung","en":"Public administration"},
  "w2_p": {"de":"Ämter und Eigenbetriebe, die Digitalisierung sicher und nachvollziehbar angehen wollen.","en":"Public offices and municipal enterprises that want to approach digitalization safely and accountably."},
  "w3_h4": {"de":"Bildungs- &amp; Coaching-Träger","en":"Education &amp; coaching providers"},
  "w3_p": {"de":"Träger, die ihre Beratungsarbeit mit KI stärken wollen — ohne die Menschen aus dem Blick zu verlieren.","en":"Providers who want to strengthen their advisory work with AI — without losing sight of the people."},
  "tr_eyebrow": {"de":"Der wichtigste Punkt","en":"The most important point"},
  "tr_h2": {"de":"Datenschutz von Anfang an","en":"Data protection from the start"},
  "tr_lead": {"de":"Gerade bei sensiblen Daten ist Datenschutz keine Formalie, sondern eine Vertrauensfrage. Deshalb steht er nicht am Ende, sondern am Anfang.","en":"Especially with sensitive data, data protection isn't a formality — it's a question of trust. That's why it comes at the beginning, not the end."},
  "t1_h4": {"de":"Wo liegen die Daten?","en":"Where does the data live?"},
  "t1_p": {"de":"Werkzeuge im kontrollierten Rahmen Ihrer Organisation statt privater Konten — wo Microsoft 365 läuft, im eigenen Tenant mit EU-Datenhaltung.","en":"Tools within your organization's controlled environment instead of private accounts — where Microsoft 365 runs, in your own tenant with EU data residency."},
  "t2_h4": {"de":"Nur der nötige Kontext","en":"Only the context needed"},
  "t2_p": {"de":"In jedem Schritt sieht die KI nur, was dieser Schritt braucht. Weniger Angriffsfläche, weniger Risiko.","en":"At each step the AI sees only what that step needs. Less attack surface, less risk."},
  "t3_h4": {"de":"Alles nachvollziehbar","en":"Everything traceable"},
  "t3_p": {"de":"Jeder Schritt ist eine lesbare Datei — keine Blackbox. Gemeinsam mit Ihrer IT bzw. Datenschutzbeauftragten.","en":"Every step is a readable file — no black box. Done together with your IT or data protection officer."},
  "ab_eyebrow": {"de":"Wer dahinter steht","en":"Who's behind it"},
  "ab_p1": {"de":"Ich baue KI-Werkzeuge an der Schnittstelle von Mensch, Organisation und Technologie — und ich kenne den beruflichen Übergang aus eigener Erfahrung. Vom Dach zur Plattform zur KI ist es für mich immer dieselbe Frage: <strong>wie geben wir Menschen die Kontrolle über die Systeme zurück, von denen ihr Leben abhängt?</strong>","en":"I build AI tools at the intersection of people, organizations, and technology — and I know what career transition feels like from my own experience. From the rooftop to the platform to AI, for me it's always the same question: <strong>how do we give people back control over the systems their lives depend on?</strong>"},
  "ab_p2": {"de":"Ich verkaufe keine Software, die Sie danach allein lässt. Ich arbeite mit Ihren Leuten, an Ihren Abläufen, mit Ihrem Datenschutz — bis es trägt. Vorschlag, kein Pitch.","en":"I don't sell software that leaves you on your own afterward. I work with your people, on your processes, with your data protection — until it holds. A proposal, not a pitch."},
  "ab_thread": {"de":"Der rote Faden","en":"The golden thread"},
  "ab_link": {"de":"Mehr über meine Arbeit →","en":"More about my work →"},
  "cta_h2": {"de":'Vorschlag, <span class="amber">kein Pitch.</span>',"en":'A proposal, <span class="amber">not a pitch.</span>'},
  "cta_p": {"de":"Ein kurzes, unverbindliches Gespräch darüber, wo ein erster Schritt bei Ihnen den größten Unterschied machen würde.","en":"A short, no-obligation conversation about where a first step would make the biggest difference for you."},
}

SCRIPT = """
<script>
const I18N = %s;
function setLang(lang){
  document.documentElement.lang = lang;
  document.body.classList.remove('lang-de','lang-en');
  document.body.classList.add('lang-' + lang);
  document.querySelectorAll('[data-i18n]').forEach(function(el){
    var k = el.getAttribute('data-i18n');
    if (I18N[k] && I18N[k][lang] != null) el.innerHTML = I18N[k][lang];
  });
  if (I18N._title && I18N._title[lang]) document.title = I18N._title[lang];
  var d = document.querySelector('meta[name="description"]');
  if (d && I18N._desc && I18N._desc[lang]) d.setAttribute('content', I18N._desc[lang]);
  try { localStorage.setItem('sim_lang', lang); } catch(e) {}
}
(function(){
  var lang = 'de';
  try { var s = localStorage.getItem('sim_lang'); if (s === 'en' || s === 'de') lang = s; } catch(e) {}
  setLang(lang);
  var btn = document.getElementById('langToggle');
  if (btn) btn.addEventListener('click', function(){
    setLang(document.documentElement.lang === 'de' ? 'en' : 'de');
  });
})();
</script>
</body>""" % json.dumps(DICT, ensure_ascii=False)

html = html.replace("</body>", SCRIPT, 1)

SITE.write_text(html, encoding="utf-8")
print(f"bilingual site written: {len(INJECT)+1} i18n hooks, toggle + dictionary added")
