import json, re, html, os, glob, importlib.util

OUT = "/Users/anujsoni/Documents/Business/CEO/Open Projects/AZAI 4/azai-website/daily-oracle/guides"
HERE = os.path.dirname(os.path.abspath(__file__))
DATE = "2026-11-15"
DATE_H = "15 November 2026"
BASE = "https://azai.ca/daily-oracle/guides/"
PLAY = "https://play.google.com/store/apps/details?id=com.kancanada.dailyoracle"
OG = "https://azai.ca/daily-oracle/og.jpg"

CSS = """@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=swap');
:root{--bg:#0F0E17;--bg-2:#17152A;--ink:#F3EBDD;--ink-soft:#A9A1B8;--ink-faint:#6E6880;--hairline:#2A2740;--gold:#D9B26F;--phone:#05050A}
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:var(--bg);color:var(--ink)}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased;
 background:radial-gradient(1200px 700px at 20% -10%,#2D2750 0%,var(--bg) 60%) no-repeat,var(--bg)}
a{color:var(--gold);text-decoration:none;border-bottom:1px solid rgba(217,178,111,.35)}
a:hover{border-bottom-color:var(--gold)}
img{display:block;max-width:100%;height:auto}
.wrap{max-width:760px;margin:0 auto;padding:0 22px}
nav{display:flex;justify-content:space-between;align-items:center;padding:24px 0}
.brand{display:flex;align-items:center;gap:12px;font-weight:500;font-size:14px;color:var(--ink);border:0}
.brand img{width:24px;height:24px;border-radius:6px}
nav .links a{color:var(--ink-soft);border:0;font-size:13px;margin-left:22px}
nav .links a:hover{color:var(--ink)}
.crumbs{font-size:13px;color:var(--ink-faint);margin:18px 0 12px}.crumbs a{color:var(--ink-soft);border:0}
h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(38px,6vw,56px);line-height:1.05;letter-spacing:-.3px;font-weight:500;margin-bottom:14px;text-wrap:balance}
.meta{font-size:13px;color:var(--ink-faint);margin-bottom:28px}
.answer{background:var(--bg-2);border-radius:18px;padding:22px 24px;margin:0 0 26px;border-left:3px solid var(--gold);font-size:17px}
.answer b{display:block;font-size:11px;font-weight:500;letter-spacing:1.6px;text-transform:uppercase;color:var(--gold);margin-bottom:8px}
article h2{font-family:'Cormorant Garamond',Georgia,serif;font-size:34px;font-weight:500;line-height:1.15;letter-spacing:-.2px;margin:46px 0 12px}
article h3{font-size:19px;font-weight:600;margin:28px 0 8px}
article p,article li{font-size:17px;color:#E2DACB}
article p{margin:0 0 16px}
article ul,article ol{margin:0 0 18px 22px}article li{margin-bottom:8px}
article strong,article b{color:var(--ink);font-weight:600}
blockquote{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:24px;line-height:1.35;color:var(--ink);border-left:2px solid var(--gold);padding-left:20px;margin:22px 0 6px}
.cite{font-size:14px;color:var(--ink-soft);padding-left:22px;margin-bottom:12px}
.table{overflow-x:auto;margin:10px 0 24px;background:var(--bg-2);border-radius:16px;border:1px solid var(--hairline)}
table{border-collapse:collapse;width:100%;font-size:15px;min-width:560px}
th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--hairline);vertical-align:top;color:#E2DACB}
tr:last-child td{border-bottom:0}
th{font-size:11px;font-weight:500;letter-spacing:1.2px;text-transform:uppercase;color:var(--ink-soft)}
.note{font-size:14px;color:var(--ink-soft)}
.disclose{font-size:15px;color:var(--ink-soft);background:rgba(217,178,111,.08);border-radius:14px;padding:14px 18px;margin:0 0 26px}
.shot{float:right;width:220px;margin:6px 0 18px 26px}
.shot div{border-radius:30px;border:6px solid var(--phone);background:var(--phone);overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.5),0 0 0 1px var(--hairline)}
.shot img{border-radius:24px}
.shot figcaption{font-size:13px;color:var(--ink-soft);margin-top:10px;line-height:1.5}
.arcana{background:var(--bg-2);border:1px solid var(--hairline);border-radius:16px;padding:18px 20px;margin:0 0 14px}
.arcana h3{margin:0 0 4px;font-family:'Cormorant Garamond',Georgia,serif;font-size:26px;font-weight:500}
.arcana .kw{font-size:13px;letter-spacing:.6px;color:var(--gold);margin-bottom:8px}
.arcana p{margin:0 0 8px}.arcana p:last-child{margin:0}
.arcana .q{font-style:italic;color:var(--ink-soft)}
.cta{background:var(--phone);border:1px solid var(--hairline);border-radius:26px;padding:30px;margin:46px 0;display:flex;gap:22px;align-items:center;flex-wrap:wrap;clear:both}
.cta div{flex:1 1 300px}.cta h3{font-family:'Cormorant Garamond',Georgia,serif;font-size:28px;font-weight:500;margin:0 0 6px;color:var(--ink)}.cta p{color:var(--ink-soft);font-size:15px;margin:0}
.cta a{background:var(--gold);color:var(--bg);border:0;font-weight:600;font-size:15px;border-radius:999px;padding:14px 24px;white-space:nowrap}
details{border-top:1px solid var(--hairline);padding:16px 0}details:last-of-type{border-bottom:1px solid var(--hairline)}
summary{cursor:pointer;font-weight:500;font-size:17px;list-style:none}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";float:right;color:var(--ink-soft);font-weight:400}
details[open] summary::after{content:"\\2013"}
details p{margin-top:10px;font-size:16px;color:var(--ink-soft)}
.sources li{font-size:15px}
.more{display:grid;gap:12px;margin:20px 0 40px}
.more a{display:block;background:var(--bg-2);border:1px solid var(--hairline);border-radius:16px;padding:16px 20px;color:var(--ink);font-weight:500}
.more a:hover{border-color:var(--gold)}
.more a span{display:block;font-weight:400;color:var(--ink-soft);font-size:14px;margin-top:2px}
h2.more-h{font-family:'Cormorant Garamond',Georgia,serif;font-size:30px;font-weight:500;margin-top:40px}
footer{border-top:1px solid var(--hairline);padding:28px 0 48px;font-size:12px;color:var(--ink-soft)}footer a{color:var(--ink-soft);border:0}footer a:hover{color:var(--ink)}
@media (max-width:600px){.wrap{padding:0 16px}.shot{float:none;width:200px;margin:8px auto 22px}article h2{font-size:29px}nav .links a{margin-left:16px}.cta{padding:24px}}"""

def esc(s):
    return html.escape(s, quote=True)

def strip(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()

def load():
    arts = []
    for f in sorted(glob.glob(os.path.join(HERE, "a_*.py"))):
        ns = {}
        exec(open(f, encoding="utf-8").read(), ns)
        arts.append(ns["A"])
    arts.sort(key=lambda a: a["order"])
    return arts

def head(title, desc, url, ld, ogtype="article"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" href="/daily-oracle/favicon.png">
<link rel="apple-touch-icon" href="/daily-oracle/apple-touch-icon.png">
<meta name="theme-color" content="#0F0E17">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="Daily Oracle">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{OG}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{OG}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
{CSS}
</style>
</head>
<body>
<div class="wrap">
<nav aria-label="Main"><a class="brand" href="/daily-oracle/"><img src="/daily-oracle/favicon.png" alt="" width="24" height="24"><span>daily oracle</span></a>
<div class="links"><a href="/daily-oracle/guides/">Guides</a><a href="/daily-oracle/">The app</a></div></nav>
"""

FOOT = """<footer>Daily Oracle is made by Kan Canada Trading Corp., British Columbia, Canada · <a href="/daily-oracle/">The app</a> · <a href="/daily-oracle/guides/">Guides</a> · <a href="/daily-oracle/privacy.html">Privacy policy</a> · <a href="mailto:asoni@kancanada.com">asoni@kancanada.com</a></footer>
</div>
</body>
</html>
"""

def cta(campaign, h, p):
    return (f'<div class="cta"><div><h3>{h}</h3><p>{p}</p></div>'
            f'<a href="{PLAY}&amp;referrer=utm_source%3Dazai.ca%26utm_medium%3Dguide%26utm_campaign%3D{campaign}">Get it on Google Play</a></div>')

CTA_H = "One card, one line, and the real moon."
CTA_P = "Daily Oracle for Android: a tarot card from the 1909 Rider-Waite-Smith deck, a Stoic quote, one small action and tonight's moon, calculated offline. Free with ads, no account."

def more_list(arts, exclude=None):
    out = []
    for a in arts:
        if a["slug"] == exclude:
            continue
        out.append(f'<a href="{a["slug"]}.html">{esc(a["h1"])}<span>{esc(a["desc"])}</span></a>')
    return '<div class="more">' + "".join(out) + "</div>"

def words(a):
    txt = strip(a["answer"] + " " + a["body"] + " " + " ".join(q + " " + ans for q, ans in a["faq"]))
    return len(txt.split())

def build(a, arts):
    url = BASE + a["slug"] + ".html"
    wc = words(a)
    mins = max(4, round(wc / 230))
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": a["h1"], "description": a["desc"],
         "dateModified": DATE, "datePublished": DATE, "mainEntityOfPage": url, "image": OG,
         "author": {"@type": "Organization", "name": "Kan Canada Trading Corp."},
         "publisher": {"@type": "Organization", "name": "Kan Canada Trading Corp.", "url": "https://azai.ca/"}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(ans)}} for q, ans in a["faq"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Daily Oracle", "item": "https://azai.ca/daily-oracle/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE},
            {"@type": "ListItem", "position": 3, "name": a["h1"], "item": url}]},
    ]
    body = a["body"].replace("{{CTA}}", cta(a["slug"], a.get("cta_h", CTA_H), a.get("cta_p", CTA_P)))
    if "{{CTA}}" not in a["body"]:
        raise SystemExit("no CTA in " + a["slug"])
    faq = "".join(f"<details><summary>{q}</summary><p>{ans}</p></details>" for q, ans in a["faq"])
    src = "".join(f'<li><a href="{esc(u)}" rel="nofollow noopener">{t}</a></li>' for t, u in a["sources"])
    page = head(a["title"], a["desc"], url, ld)
    page += (f'<div class="crumbs"><a href="/daily-oracle/">Daily Oracle</a> › <a href="/daily-oracle/guides/">Guides</a></div>'
             f'<article><h1>{a["h1"]}</h1><div class="meta">Updated {DATE_H} · {mins} min read</div>'
             f'<div class="answer"><b>Short answer</b>{a["answer"]}</div>'
             f'<p class="disclose">{a["disclose"]}</p>\n{body}\n'
             f'<h2>Questions</h2>{faq}<h2>Sources</h2><ul class="sources">{src}</ul>'
             f'<p class="note">{a.get("srcnote", "Sources were checked on " + DATE_H + ".")}</p></article>'
             f'<h2 class="more-h">More guides</h2>{more_list(arts, a["slug"])}\n')
    page += FOOT
    open(os.path.join(OUT, a["slug"] + ".html"), "w", encoding="utf-8").write(page)
    return wc

def build_index(arts):
    url = BASE
    title = "Tarot, Moon and Stoic Guides | Daily Oracle"
    desc = "Guides to a daily tarot practice, the Rider-Waite-Smith deck, Major Arcana meanings, moon phases and moon signs, and Stoic quotes for reflection."
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Daily Oracle guides", "url": url,
           "description": desc, "publisher": {"@type": "Organization", "name": "Kan Canada Trading Corp.", "url": "https://azai.ca/"}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Daily Oracle", "item": "https://azai.ca/daily-oracle/"},
              {"@type": "ListItem", "position": 2, "name": "Guides", "item": url}]}]
    page = head(title, desc, url, ld, ogtype="website")
    page += ('<div class="crumbs"><a href="/daily-oracle/">Daily Oracle</a> › Guides</div><article>'
             '<h1>Guides to a daily reflection practice</h1>'
             '<p>Practical guides to tarot as a tool for reflection, the history of the Rider-Waite-Smith deck, the moon as astronomers measure it, and the Stoic writers worth reading each morning. They\'re written by the team that makes Daily Oracle. We treat tarot and astrology as prompts for thinking, not predictions, and where another app or a paper deck suits you better, we say so.</p>'
             '</article>' + more_list(arts) +
             cta("guides-index", CTA_H, CTA_P) + "\n" + FOOT)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    arts = load()
    for a in arts:
        print(a["slug"], build(a, arts), "words", "| title len", len(a["title"]), "| desc len", len(a["desc"]))
    build_index(arts)
