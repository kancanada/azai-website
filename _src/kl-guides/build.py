import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import base, a1, a2, a3
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
for g in base.GUIDES:
    if g.get("extra_css") == "PRINT": g["extra_css"] = base.PRINT_CSS
    open(os.path.join(OUT, g["slug"] + ".html"), "w").write(base.render(g))
    print(g["slug"], g["words"], len(base.strip_tags(g["body"]).split()))
open(os.path.join(OUT, "index.html"), "w").write(base.render_index())
