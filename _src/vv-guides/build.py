"""Builds azai.ca/voicevault/guides/ from the fragments here: python3 build.py
Folders starting with "_" aren't published by GitHub Pages, so this source stays private to the repo."""
import json, os, re, html
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "voicevault", "guides")
SITE = "https://azai.ca/voicevault/guides/"
PLAY = "https://play.google.com/store/apps/details?id=com.azai.voicevault&amp;referrer=utm_source%3Dazai.ca%26utm_medium%3Dguide%26utm_campaign%3D{slug}"
UPDATED = "2026-10-31"
import datetime
def nice(d): return datetime.date.fromisoformat(d).strftime("%-d %B %Y")

CSS = """
@font-face{font-family:Geist;src:url(../geist.ttf);font-weight:100 900;font-display:swap}
:root{--bg:#F4F2FA;--ink:#121214;--ink2:#4A4A57;--ink3:#8A8A98;--violet:#6D4AFF;--line:rgba(18,18,20,.1)}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Geist,-apple-system,BlinkMacSystemFont,sans-serif;color:var(--ink);line-height:1.65;-webkit-font-smoothing:antialiased;
 background:radial-gradient(1000px 700px at 0% 0%,#E4DCFF 0%,transparent 65%),var(--bg) no-repeat}
a{color:var(--violet)}
.wrap{max-width:760px;margin:0 auto;padding:0 22px}
nav{display:flex;justify-content:space-between;align-items:center;padding:22px 0}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:17px;text-decoration:none;color:var(--ink)}
.brand img{width:30px;height:30px;border-radius:8px}
nav .links a{color:var(--ink2);text-decoration:none;font-size:14px;margin-left:18px}
.crumbs{font-size:14px;color:var(--ink3);margin:18px 0 10px}.crumbs a{color:var(--ink3)}
h1{font-size:clamp(34px,5vw,48px);line-height:1.08;letter-spacing:-.03em;font-weight:700;margin-bottom:14px}
.meta{font-size:14px;color:var(--ink3);margin-bottom:28px}
.answer{background:#fff;border-radius:20px;padding:22px 24px;margin:0 0 30px;border-left:4px solid var(--violet)}
.answer b{display:block;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--violet);margin-bottom:6px}
article h2{font-size:28px;line-height:1.2;letter-spacing:-.02em;margin:42px 0 12px}
article h3{font-size:20px;margin:28px 0 8px}
article p,article li{font-size:18px;color:#26262e}
article p{margin:0 0 16px}
article ul,article ol{margin:0 0 18px 22px}article li{margin-bottom:8px}
.table{overflow-x:auto;margin:10px 0 24px;background:#fff;border-radius:16px}
table{border-collapse:collapse;width:100%;font-size:15px;min-width:560px}
th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:13px;letter-spacing:.04em;text-transform:uppercase;color:var(--ink2)}
.note{font-size:15px;color:var(--ink2)}
.disclose{font-size:15px;color:var(--ink2);background:rgba(109,74,255,.07);border-radius:14px;padding:14px 18px;margin:0 0 26px}
.cta{background:#121214;color:#fff;border-radius:26px;padding:30px;margin:44px 0;display:flex;gap:22px;align-items:center;flex-wrap:wrap}
.cta div{flex:1 1 300px}.cta h3{font-size:22px;margin-bottom:6px;color:#fff}.cta p{color:#C9C9D6;font-size:16px;margin:0}
.cta a{background:#E5392F;color:#fff;text-decoration:none;font-weight:700;border-radius:999px;padding:14px 26px;white-space:nowrap}
details{border-top:1px solid var(--line);padding:16px 0}details:last-of-type{border-bottom:1px solid var(--line)}
summary{cursor:pointer;font-weight:600;font-size:18px}
details p{margin-top:8px}
.sources li{font-size:15px}
.more{display:grid;gap:12px;margin:20px 0 40px}
.more a{display:block;background:#fff;border-radius:16px;padding:16px 20px;text-decoration:none;color:var(--ink);font-weight:600}
.more a span{display:block;font-weight:400;color:var(--ink2);font-size:15px}
footer{border-top:1px solid var(--line);padding:26px 0 40px;font-size:14px;color:var(--ink3)}footer a{color:var(--ink3)}
"""

def page(title, description, canonical, body, schema):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="../icon.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="VoiceVault">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:image" content="https://azai.ca/voicevault/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(description)}">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<nav><a class="brand" href="/voicevault/"><img src="../icon.png" alt="">VoiceVault</a>
<div class="links"><a href="/voicevault/guides/">Guides</a><a href="/voicevault/">The app</a></div></nav>
{body}
<footer>VoiceVault is made by Kan Canada Trading Corp., British Columbia, Canada · <a href="/voicevault/privacy.html">Privacy policy</a> · <a href="mailto:asoni@kancanada.com">asoni@kancanada.com</a></footer>
</div>
</body>
</html>
"""

def load(path):
    text = open(path).read()
    m = re.match(r"<!--(.*?)-->\s*", text, re.S)
    meta = json.loads(m.group(1)); meta["body"] = text[m.end():]
    meta["slug"] = os.path.splitext(os.path.basename(path))[0]
    return meta

guides = sorted((load(os.path.join(HERE, f)) for f in os.listdir(HERE) if f.endswith(".html")), key=lambda g: g["order"])
os.makedirs(OUT, exist_ok=True)

def cta(slug):
    return (f'<div class="cta"><div><h3>Every meeting, written up. Right on your phone.</h3>'
            f'<p>VoiceVault for Android: transcripts, summaries and to-dos with no account, no servers and no subscription. 30 days free, then pay once.</p></div>'
            f'<a href="{PLAY.format(slug=slug)}">Get it on Google Play</a></div>')

for g in guides:
    # Google cuts titles around 60 characters and descriptions around 155.
    if len(g["title"]) > 60 or len(g["description"]) > 155:
        print(f'too long: {g["slug"]} (title {len(g["title"])}, description {len(g["description"])})')
    url = SITE + g["slug"] + ".html"
    faq = "".join(f"<details><summary>{html.escape(q)}</summary><p>{a}</p></details>" for q, a in g["faq"])
    sources = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(l)}</a></li>' for l, u in g["sources"])
    others = "".join(f'<a href="{o["slug"]}.html">{html.escape(o["h1"])}<span>{html.escape(o["description"])}</span></a>' for o in guides if o is not g)
    body = (f'<div class="crumbs"><a href="/voicevault/">VoiceVault</a> › <a href="/voicevault/guides/">Guides</a></div>'
            f'<article><h1>{html.escape(g["h1"])}</h1><div class="meta">Updated {nice(g.get("updated", UPDATED))} · {g["minutes"]} min read</div>'
            f'<div class="answer"><b>Short answer</b>{g["answer"]}</div>'
            + (f'<p class="disclose">{g["disclose"]}</p>' if g.get("disclose") else "")
            + g["body"].replace("<!--CTA-->", cta(g["slug"]))
            + f'<h2>Questions</h2>{faq}'
            + (f'<h2>Sources</h2><ul class="sources">{sources}</ul><p class="note">{g.get("note", "Prices and features were checked on 31 October 2026 and change often; check each provider before you buy.")}</p>' if sources else "")
            + f'</article><h2 style="font-size:24px;margin-top:40px">More guides</h2><div class="more">{others}</div>')
    schema = [{"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["description"],
               "dateModified": g.get("updated", UPDATED), "datePublished": g.get("updated", UPDATED), "mainEntityOfPage": url, "image": "https://azai.ca/voicevault/og.jpg",
               "author": {"@type": "Organization", "name": "Kan Canada Trading Corp."},
               "publisher": {"@type": "Organization", "name": "Kan Canada Trading Corp.", "url": "https://azai.ca/"}},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                  {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in g["faq"]]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "VoiceVault", "item": "https://azai.ca/voicevault/"},
                  {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE},
                  {"@type": "ListItem", "position": 3, "name": g["h1"], "item": url}]}]
    open(os.path.join(OUT, g["slug"] + ".html"), "w").write(page(g["title"], g["description"], url, body, schema))

items = "".join(f'<a href="{g["slug"]}.html">{html.escape(g["h1"])}<span>{html.escape(g["description"])}</span></a>' for g in guides)
index_body = (f'<div class="crumbs"><a href="/voicevault/">VoiceVault</a> › Guides</div><article><h1>Meeting notes guides</h1>'
              f'<p>Practical guides to recording, transcribing and writing up meetings on Android, from the team that makes VoiceVault. '
              f'Where we compare other apps, we say where they\'re the better choice.</p></article><div class="more">{items}</div>{cta("guides-index")}')
open(os.path.join(OUT, "index.html"), "w").write(page("Meeting notes guides for Android | VoiceVault",
     "Guides to recording, transcribing and writing up meetings on Android: offline transcription, Otter and Fireflies alternatives, and more.",
     SITE, index_body, {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Meeting notes guides", "url": SITE}))
print("built", len(guides), "guides")
