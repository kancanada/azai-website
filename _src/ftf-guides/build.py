"""Builds Flip to Focus guide pages into the azai-website repo."""
import html, json, re, sys, importlib.util, pathlib

HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path("/Users/anujsoni/Documents/Business/CEO/Open Projects/AZAI 4/azai-website/flip-to-focus/guides")
DATE = "2026-11-15"
DATE_LONG = "15 November 2026"
BASE = "https://azai.ca/flip-to-focus/guides/"
OG = "https://azai.ca/flip-to-focus/og.jpg"
PLAY = "https://play.google.com/store/apps/details?id=com.kancanada.fliptofocus&amp;referrer=utm_source%3Dazai.ca%26utm_medium%3Dguide%26utm_campaign%3D"
ORG = {"@type": "Organization", "name": "Kan Canada Trading Corp."}
PUB = {"@type": "Organization", "name": "Kan Canada Trading Corp.", "url": "https://azai.ca/"}

ORDER = [
    "pomodoro-technique",
    "how-long-to-study-before-a-break",
    "stop-checking-phone-while-studying",
    "phone-presence-and-attention-research",
    "best-study-timer-apps-android",
    "forest-app-alternative",
    "flora-app-alternative",
    "exam-study-plan-template",
    "study-schedule-template",
    "deep-work-for-students",
]

CSS = """
:root{--bg:#F4F2EE;--ink:#1A1A1A;--ink2:#4A4A4A;--ink3:#6B6B6B;--faint:#B5B3AE;--line:#DDDAD3;--accent:#3C8F6E;--accent2:#8FD6B4;--phone:#0E0F12;--card:#FFFFFF}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Inter,-apple-system,BlinkMacSystemFont,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-underline-offset:2px}
.wrap{max-width:760px;margin:0 auto;padding:0 22px}
nav{display:flex;justify-content:space-between;align-items:center;padding:24px 0}
.brand{display:flex;align-items:center;gap:12px;font-weight:500;font-size:14px;text-decoration:none;color:var(--ink)}
.brand img{width:24px;height:24px;border-radius:6px}
nav .links a{color:var(--ink3);text-decoration:none;font-size:13px;margin-left:22px}
nav .links a:hover{color:var(--ink)}
.crumbs{font-size:13px;color:var(--ink3);margin:18px 0 12px}.crumbs a{color:var(--ink3)}
.eyebrow{font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.8px;color:var(--accent);margin-bottom:12px}
h1{font-size:clamp(32px,5vw,46px);line-height:1.08;letter-spacing:-.025em;font-weight:500;margin-bottom:14px;text-wrap:balance}
.meta{font-size:13px;color:var(--ink3);margin-bottom:28px}
.answer{background:var(--card);border-radius:18px;padding:22px 24px;margin:0 0 26px;border-left:4px solid var(--accent)}
.answer b{display:block;font-size:11px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;color:var(--accent);margin-bottom:6px}
article h2{font-size:27px;line-height:1.2;letter-spacing:-.015em;font-weight:500;margin:44px 0 12px}
article h3{font-size:19px;font-weight:600;margin:28px 0 8px}
article p,article li{font-size:17.5px;color:#262626}
article p{margin:0 0 16px}
article ul,article ol{margin:0 0 18px 22px}article li{margin-bottom:8px}
.table{overflow-x:auto;margin:10px 0 24px;background:var(--card);border-radius:16px}
table{border-collapse:collapse;width:100%;font-size:15px;min-width:560px}
th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:11px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;color:var(--ink3)}
tr:last-child td{border-bottom:0}
.note{font-size:14px;color:var(--ink3)}
.disclose{font-size:15px;color:var(--ink2);background:rgba(60,143,110,.09);border-radius:14px;padding:14px 18px;margin:0 0 26px}
.template{background:var(--card);border:1px dashed var(--faint);border-radius:16px;padding:18px 20px;margin:10px 0 24px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:14px;line-height:1.6;white-space:pre-wrap;overflow-x:auto;color:#262626}
.cta{background:var(--phone);color:#fff;border-radius:26px;padding:30px;margin:44px 0;display:flex;gap:22px;align-items:center;flex-wrap:wrap}
.cta div{flex:1 1 300px}.cta h3{font-size:21px;font-weight:500;margin-bottom:6px;color:#fff}.cta p{color:#C4C6C9;font-size:15.5px;margin:0}
.cta a{background:var(--accent2);color:var(--phone);text-decoration:none;font-weight:600;border-radius:999px;padding:14px 26px;white-space:nowrap}
.cta a:hover{background:#fff}
details{border-top:1px solid var(--line);padding:16px 0}details:last-of-type{border-bottom:1px solid var(--line)}
summary{cursor:pointer;font-weight:500;font-size:17.5px}
details p{margin-top:8px}
.sources li{font-size:15px}
.more{display:grid;gap:12px;margin:20px 0 40px}
.more a{display:block;background:var(--card);border-radius:16px;padding:16px 20px;text-decoration:none;color:var(--ink);font-weight:500}
.more a:hover{box-shadow:0 0 0 1px var(--accent)}
.more a span{display:block;font-weight:400;color:var(--ink3);font-size:15px;margin-top:2px}
h2.more-h{font-size:22px;font-weight:500;margin-top:40px}
footer{border-top:1px solid var(--line);padding:26px 0 44px;font-size:13px;color:var(--ink3)}footer a{color:var(--ink3)}
@media (max-width:600px){nav .links a{margin-left:16px}.cta{padding:24px}article p,article li{font-size:17px}}
""".strip()


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def load(slug):
    spec = importlib.util.spec_from_file_location(slug.replace("-", "_"), HERE / "articles" / f"{slug}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.ART


def head(title, desc, url, ldjson, og_type="article"):
    t = esc(title)
    d = esc(desc)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" href="/flip-to-focus/favicon.png">
<link rel="apple-touch-icon" href="/flip-to-focus/apple-touch-icon.png">
<meta name="theme-color" content="#3C8F6E">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Flip to Focus">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{OG}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{OG}">
<script type="application/ld+json">{json.dumps(ldjson, ensure_ascii=False)}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<div class="wrap">
<nav aria-label="Main"><a class="brand" href="/flip-to-focus/"><img src="/flip-to-focus/favicon.png" alt="" width="24" height="24">flip to focus</a>
<div class="links"><a href="/flip-to-focus/guides/">Guides</a><a href="/flip-to-focus/">The app</a></div></nav>
"""


FOOT = """<footer>Flip to Focus is made by Kan Canada Trading Corp., British Columbia, Canada · <a href="/flip-to-focus/privacy.html">Privacy policy</a> · <a href="mailto:asoni@kancanada.com">asoni@kancanada.com</a></footer>
</div>
</body>
</html>
"""


def cta(slug, h3, p):
    return f'<div class="cta"><div><h3>{h3}</h3><p>{p}</p></div><a href="{PLAY}{slug}">Get it on Google Play</a></div>'


DEFAULT_CTA = ("Phone face down. Timer running.",
               "Flip to Focus for Android: a study timer that stops the moment you pick up your phone. No ads, no account. 7 days free, then pay once for life.")


def more_list(arts, exclude=None):
    out = []
    for a in arts:
        if a["slug"] == exclude:
            continue
        out.append(f'<a href="{a["slug"]}.html">{esc(a["h1"])}<span>{esc(a["desc"])}</span></a>')
    return '<div class="more">' + "".join(out) + "</div>"


def build_article(a, arts):
    slug = a["slug"]
    url = f"{BASE}{slug}.html"
    title = f'{a["title"]} | Flip to Focus'
    faq_ld = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(ans)}} for q, ans in a["faq"]]
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": a["h1"], "description": a["desc"],
         "dateModified": DATE, "datePublished": DATE, "mainEntityOfPage": url, "image": OG, "author": ORG, "publisher": PUB},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_ld},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Flip to Focus", "item": "https://azai.ca/flip-to-focus/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE},
            {"@type": "ListItem", "position": 3, "name": a["h1"], "item": url}]},
    ]
    words = len(strip_tags(a["intro"] + a["body"] + a["answer"] + "".join(x for f in a["faq"] for x in f)).split())
    mins = max(3, round(words / 230))
    body = a["body"].replace("{{CTA}}", cta(slug, *a.get("cta", DEFAULT_CTA)))
    if "{{CTA}}" not in a["body"]:
        body += cta(slug, *a.get("cta", DEFAULT_CTA))
    faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{ans}</p></details>" for q, ans in a["faq"])
    src_html = "".join(f'<li><a href="{esc(u)}" rel="nofollow noopener">{esc(label)}</a></li>' for label, u in a["sources"])
    page = head(title, a["desc"], url, ld)
    page += f'<div class="crumbs"><a href="/flip-to-focus/">Flip to Focus</a> › <a href="/flip-to-focus/guides/">Guides</a></div>'
    page += f'<article><div class="eyebrow">{esc(a["eyebrow"])}</div><h1>{esc(a["h1"])}</h1><div class="meta">Updated {DATE_LONG} · {mins} min read</div>'
    page += f'<div class="answer"><b>Short answer</b>{a["answer"]}</div>'
    page += f'<p class="disclose">{a["disclose"]}</p>'
    page += a["intro"] + "\n" + body
    page += f"\n<h2>Questions</h2>{faq_html}<h2>Sources</h2><ul class=\"sources\">{src_html}</ul>"
    page += f'<p class="note">{a.get("sources_note", "Sources were checked on " + DATE_LONG + ". App prices, features and store listings change often; check them before you buy.")}</p></article>'
    page += '<h2 class="more-h">More guides</h2>' + more_list(arts, slug)
    page += FOOT
    (OUT / f"{slug}.html").write_text(page, encoding="utf-8")
    return words


def build_index(arts):
    url = BASE
    title = "Study and focus guides | Flip to Focus"
    desc = "Practical guides to studying with fewer phone distractions: the Pomodoro technique, break lengths, exam plans, study schedules, focus apps and the research."
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Study and focus guides", "url": url,
           "publisher": PUB,
           "hasPart": [{"@type": "Article", "headline": a["h1"], "url": f'{BASE}{a["slug"]}.html'} for a in arts]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Flip to Focus", "item": "https://azai.ca/flip-to-focus/"},
              {"@type": "ListItem", "position": 2, "name": "Guides", "item": url}]}]
    page = head(title, desc, url, ld, og_type="website")
    page += '<div class="crumbs"><a href="/flip-to-focus/">Flip to Focus</a> › Guides</div>'
    page += ('<article><div class="eyebrow">Guides</div><h1>Study and focus guides</h1>'
             '<p>Practical guides to studying with fewer phone distractions, from the team that makes Flip to Focus. '
             'We cite the research and the original sources, say where the evidence is weaker than its reputation, '
             'and when we compare other apps, we say where they are the better choice.</p></article>')
    page += more_list(arts)
    page += cta("guides-index", *DEFAULT_CTA)
    page += FOOT
    (OUT / "index.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    arts = [load(s) for s in ORDER]
    for a in arts:
        w = build_article(a, arts)
        print(f'{a["slug"]}: {w} words | {a["title"]} ({len(a["title"]) + 16} chars) | desc {len(a["desc"])}')
    build_index(arts)
