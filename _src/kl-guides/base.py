import html, json, re

SITE = "https://azai.ca"
BASE = SITE + "/kakeibo-ledger/guides/"
DATE = "2026-11-15"
DATE_TXT = "15 November 2026"
OG = SITE + "/kakeibo-ledger/og.jpg"
ORG = {"@type": "Organization", "name": "Kan Canada Trading Corp."}
PUB = {"@type": "Organization", "name": "Kan Canada Trading Corp.", "url": "https://azai.ca/"}

def play(campaign):
    return ("https://play.google.com/store/apps/details?id=com.kancanada.kakeibo&amp;referrer="
            "utm_source%3Dazai.ca%26utm_medium%3Dguide%26utm_campaign%3D" + campaign)

CSS = """@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&family=Inter:wght@400;500;600&display=swap');
:root{--bg:#F6F1E7;--bg-2:#FFFDF8;--ink:#2B2722;--ink-soft:#6F665B;--ink-faint:#9A8F82;--hairline:#E3D9C7;--accent:#C2452D;--needs:#3F6E9E;--wants:#D0822F;--culture:#5E8C4E;--unexp:#A3536B;--dark:#1E1B17}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Inter,-apple-system,BlinkMacSystemFont,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--accent)}
a:hover{color:var(--accent)}
.wrap{max-width:760px;margin:0 auto;padding:0 22px}
nav{display:flex;justify-content:space-between;align-items:center;padding:24px 0}
.brand{display:flex;align-items:center;gap:12px;font-weight:500;font-size:14px;border:0;color:var(--ink)}
.brand img{width:24px;height:24px;border-radius:6px}
nav .links a{color:var(--ink-soft);border:0;font-size:13px;margin-left:20px}
nav .links a:hover{color:var(--ink)}
.crumbs{font-size:13px;color:var(--ink-faint);margin:18px 0 10px}.crumbs a{color:var(--ink-faint);border:0}
h1{font-family:'Source Serif 4',Georgia,serif;font-size:clamp(34px,5vw,48px);line-height:1.08;letter-spacing:-.02em;font-weight:600;margin-bottom:14px;text-wrap:balance}
.meta{font-size:13px;color:var(--ink-faint);margin-bottom:28px}
.answer{background:var(--bg-2);border:1px solid var(--hairline);border-left:4px solid var(--accent);border-radius:16px;padding:22px 24px;margin:0 0 28px;font-size:17px}
.answer b{display:block;font-size:11px;font-weight:600;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);margin-bottom:6px}
article h2{font-family:'Source Serif 4',Georgia,serif;font-size:30px;font-weight:600;line-height:1.2;letter-spacing:-.01em;margin:44px 0 12px}
article h3{font-size:19px;font-weight:600;margin:28px 0 8px}
article p,article li{font-size:17px;color:#3A342D}
article p{margin:0 0 16px}
article ul,article ol{margin:0 0 18px 22px}article li{margin-bottom:8px}
article strong,article b{color:var(--ink);font-weight:600}
.table{overflow-x:auto;margin:10px 0 24px;background:var(--bg-2);border:1px solid var(--hairline);border-radius:14px}
table{border-collapse:collapse;width:100%;font-size:15px;min-width:560px}
th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--hairline);vertical-align:top}
tr:last-child td{border-bottom:0}
th{font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;color:var(--ink-soft)}
.note{font-size:14px;color:var(--ink-soft)}
.disclose{font-size:15px;color:var(--ink-soft);background:rgba(194,69,45,.07);border-radius:12px;padding:14px 18px;margin:0 0 26px}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:8px;vertical-align:0}
.dot.needs{background:var(--needs)}.dot.wants{background:var(--wants)}.dot.culture{background:var(--culture)}.dot.unexp{background:var(--unexp)}
pre{background:var(--bg-2);border:1px solid var(--hairline);border-radius:14px;padding:18px 20px;overflow-x:auto;font-size:14px;line-height:1.55;margin:10px 0 24px;white-space:pre}
.cta{background:var(--dark);color:#fff;border-radius:22px;padding:30px;margin:44px 0;display:flex;gap:22px;align-items:center;flex-wrap:wrap}
.cta div{flex:1 1 300px}.cta h3{font-family:'Source Serif 4',Georgia,serif;font-size:24px;font-weight:600;margin-bottom:6px;color:#fff}.cta p{color:#D8CFC2;font-size:15px;margin:0}
.cta a{background:var(--accent);color:#fff;border:0;font-weight:500;font-size:15px;border-radius:999px;padding:14px 24px;white-space:nowrap}
.cta a:hover{color:#fff;background:#A93A25}
details{border-top:1px solid var(--hairline);padding:16px 0}details:last-of-type{border-bottom:1px solid var(--hairline)}
summary{cursor:pointer;font-weight:500;font-size:17px}
details p{margin-top:8px;color:var(--ink-soft)}
.sources li{font-size:14px}
.more-h{font-family:'Source Serif 4',Georgia,serif;font-size:26px;font-weight:600;margin:44px 0 0}
.more{display:grid;gap:12px;margin:20px 0 40px}
.more a{display:block;background:var(--bg-2);border:1px solid var(--hairline);border-radius:14px;padding:16px 20px;color:var(--ink);font-weight:600}
.more a:hover{border-color:var(--accent);color:var(--ink)}
.more a span{display:block;font-weight:400;color:var(--ink-soft);font-size:15px}
footer{border-top:1px solid var(--hairline);padding:26px 0 40px;font-size:12px;color:var(--ink-soft)}footer a{color:var(--ink-soft);border:0}
@media (max-width:560px){article h2{font-size:26px}nav .links a{margin-left:14px}.cta{padding:24px}}"""

PRINT_CSS = """
.print-btn{font:inherit;font-size:15px;font-weight:500;background:var(--accent);color:#fff;border:0;border-radius:999px;padding:12px 22px;cursor:pointer;margin:0 0 24px}
.sheet td{height:34px}
@media print{
 body{background:#fff}
 nav,.crumbs,.meta,.answer,.disclose,.cta,.more-h,.more,footer,.print-btn,.no-print,details,.sources,article h2.no-print{display:none!important}
 .table{border:1px solid #999;border-radius:0;break-inside:avoid}
 .sheet{break-inside:avoid}
 article p,article li{font-size:12pt}
 table{font-size:11pt;min-width:0}
 th,td{border-bottom:1px solid #999}
}"""

GUIDES = []  # filled by content modules: dict(slug,title,desc,...)

def esc(s):
    return html.escape(s, quote=True)

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)

def head(title_tag, desc, url, ld, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title_tag)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" href="/kakeibo-ledger/favicon.png">
<link rel="apple-touch-icon" href="/kakeibo-ledger/apple-touch-icon.png">
<meta name="theme-color" content="#F6F1E7">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Kakeibo Ledger">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title_tag)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{OG}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title_tag)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{OG}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
{CSS}{extra_css}
</style>
</head>
<body>
<div class="wrap">
<nav><a class="brand" href="/kakeibo-ledger/"><img src="/kakeibo-ledger/favicon.png" alt="" width="24" height="24">kakeibo ledger</a>
<div class="links"><a href="/kakeibo-ledger/guides/">Guides</a><a href="/kakeibo-ledger/">The app</a></div></nav>
"""

FOOT = """<footer>Kakeibo Ledger is made by Kan Canada Trading Corp., British Columbia, Canada · <a href="/kakeibo-ledger/">The app</a> · <a href="/kakeibo-ledger/guides/">Guides</a> · <a href="/kakeibo-ledger/privacy.html">Privacy policy</a> · <a href="mailto:asoni@kancanada.com">asoni@kancanada.com</a></footer>
</div>
</body>
</html>
"""

CTA_H = "Plan. Write. Reflect. On your phone."
CTA_P = ("Kakeibo Ledger for Android: the four boxes and the month-end questions, with no internet permission, "
         "no account and no ads. Free, or pay once for Pro.")

def cta(campaign, h=CTA_H, p=CTA_P):
    return f'<div class="cta"><div><h3>{esc(h)}</h3><p>{esc(p)}</p></div><a href="{play(campaign)}">Get it on Google Play</a></div>'

def more_list(exclude=None):
    items = "".join(
        f'<a href="{g["slug"]}.html">{esc(g["h1"])}<span>{esc(g["desc"])}</span></a>'
        for g in GUIDES if g["slug"] != exclude)
    return f'<div class="more">{items}</div>'

def words(s):
    return len(strip_tags(s).split())

def render(g):
    url = BASE + g["slug"] + ".html"
    faqs = g["faqs"]
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"],
         "dateModified": DATE, "datePublished": DATE, "mainEntityOfPage": url, "image": OG,
         "author": ORG, "publisher": PUB},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Kakeibo Ledger", "item": SITE + "/kakeibo-ledger/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE},
            {"@type": "ListItem", "position": 3, "name": g["h1"], "item": url}]},
    ]
    body = g["body"]
    faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs)
    src_html = "".join(f'<li><a href="{esc(u)}" rel="nofollow noopener">{esc(t)}</a></li>' for t, u in g["sources"])
    total = words(body) + words(g["answer"]) + sum(len((q + " " + a).split()) for q, a in faqs)
    mins = max(4, round(total / 230))
    g["words"] = total
    out = head(g["title"], g["desc"], url, ld, g.get("extra_css", ""))
    out += ('<div class="crumbs"><a href="/kakeibo-ledger/">Kakeibo Ledger</a> › <a href="/kakeibo-ledger/guides/">Guides</a></div>'
            f'<article><h1>{esc(g["h1"])}</h1><div class="meta">Updated {DATE_TXT} · {mins} min read</div>'
            f'<div class="answer"><b>Short answer</b>{g["answer"]}</div>'
            f'<p class="disclose">{g["disclose"]}</p>\n{body}\n'
            f'{cta(g["slug"], g.get("cta_h", CTA_H), g.get("cta_p", CTA_P))}\n'
            f'<h2>Questions</h2>{faq_html}<h2>Sources</h2><ul class="sources">{src_html}</ul>'
            f'<p class="note">{g.get("source_note", "Prices, plans and app details were checked on " + DATE_TXT + " on each company&#x27;s own pages and change often; check them before you buy.")}</p></article>'
            f'<h2 class="more-h">More guides</h2>{more_list(g["slug"])}\n' + FOOT)
    return out

def render_index():
    url = BASE
    title = "Kakeibo and budgeting guides | Kakeibo Ledger"
    desc = ("Plain-English guides to kakeibo, the Japanese budgeting method: templates, the four categories, "
            "reflection questions, no-spend months and budget apps that don't link to your bank.")
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Kakeibo and budgeting guides", "url": url,
           "publisher": PUB},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Kakeibo Ledger", "item": SITE + "/kakeibo-ledger/"},
              {"@type": "ListItem", "position": 2, "name": "Guides", "item": url}]}]
    out = head(title, desc, url, ld).replace('<meta property="og:type" content="article">', '<meta property="og:type" content="website">')
    out += ('<div class="crumbs"><a href="/kakeibo-ledger/">Kakeibo Ledger</a> › Guides</div>'
            '<article><h1>Kakeibo and budgeting guides</h1>'
            '<p>Practical guides to kakeibo (家計簿), the Japanese household ledger, and to keeping a budget by hand: '
            'how the method works, templates you can print or copy, and honest comparisons with other ways to budget. '
            'They&#x27;re written by the team that makes Kakeibo Ledger for Android. Where another method or app is the '
            'better choice, we say so.</p></article>'
            f'{more_list()}{cta("guides-index")}\n' + FOOT)
    return out
