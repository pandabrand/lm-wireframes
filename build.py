#!/usr/bin/env python3
"""Builds Las Mujeres low-fi wireframes as standalone HTML files (Paper Wireframe Kit style).

Each screen is self-contained (inline CSS + SVG) so it can be imported into Figma with
html.to.design at 1440 (desktop) and 375 (mobile) widths.

Run: python3 build.py   -> writes screens into ./screens and an index.html
"""
from pathlib import Path

OUT = Path(__file__).parent
SCREENS = OUT / "screens"

# ---------- icons (simple line icons, 24px grid) ----------
def svg(path, size=24):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="#000" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg>')

I = {
    "image": svg('<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="M21 15l-5-5L5 21"/>', 40),
    "menu": svg('<path d="M3 6h18M3 12h18M3 18h18"/>'),
    "chev_r": svg('<path d="M9 18l6-6-6-6"/>'),
    "chev_d": svg('<path d="M6 9l6 6 6-6"/>'),
    "chev_l": svg('<path d="M15 18l-6-6 6-6"/>'),
    "pin": svg('<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>'),
    "pin_big": svg('<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>', 32),
    "cal": svg('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 11h18"/>'),
    "user": svg('<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>'),
    "search": svg('<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>'),
    "check": svg('<path d="M5 12l5 5 9-10"/>'),
    "x": svg('<path d="M6 6l12 12M18 6L6 18"/>'),
    "lock": svg('<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'),
    "download": svg('<path d="M12 3v12M7 10l5 5 5-5M4 21h16"/>'),
    "insta": svg('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5"/>'),
    "fb": svg('<path d="M15 3h-3a4 4 0 0 0-4 4v3H6v4h2v7h4v-7h3l1-4h-4V7a1 1 0 0 1 1-1h2z"/>'),
    "info": svg('<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>'),
    "bed": svg('<path d="M3 18V7M3 13h18v5M21 13a4 4 0 0 0-4-4h-7v4"/><circle cx="7" cy="10.5" r="1.5"/>'),
    "glass": svg('<path d="M8 3h8l-1 7a3 3 0 0 1-6 0zM12 13v8M8 21h8"/>'),
    "list": svg('<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>'),
    "map": svg('<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>'),
}

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Patrick Hand',cursive;color:#000;background:#fff;font-size:20px;line-height:1.35}
a{color:inherit;text-decoration:none}
.note{display:flex;gap:16px;align-items:flex-start;background:#E9FBF4;border-bottom:2px solid #2BD4A4;padding:12px 64px;font-family:Inter,Arial,sans-serif;font-size:14px;line-height:1.4}
.note b{display:block;font-size:12px;letter-spacing:.06em;text-transform:uppercase}
.note .screen{margin-left:auto;white-space:nowrap;color:#3a3a3a}
.note .back{white-space:nowrap;color:#000;font-weight:600;text-decoration:underline}
header.site{display:flex;justify-content:space-between;align-items:center;padding:20px 64px;border-bottom:2px solid #000;background:#fff}
.logo{font-size:32px;letter-spacing:.1em}
header nav{display:flex;gap:36px;font-size:22px}
header nav a.on{text-decoration:underline;text-underline-offset:6px}
header .menu{display:none}
.wrap{max-width:1440px;margin:0 auto;padding:0 64px}
section{padding:72px 0}
section.tight{padding:40px 0}
section.soft{background:#F4F4F4;border-top:2px solid #000;border-bottom:2px solid #000}
h1{font-size:64px;line-height:1.05;font-weight:400}
h2{font-size:42px;line-height:1.1;font-weight:400}
h3{font-size:28px;line-height:1.15;font-weight:400}
h4{font-size:22px;font-weight:400}
p{max-width:680px}
.muted{color:#5a5a5a}
.small{font-size:16px}
.eyebrow{font-size:16px;letter-spacing:.12em;text-transform:uppercase;color:#5a5a5a}
.stack{display:flex;flex-direction:column;gap:16px}
.stack.lg{gap:24px}
.row{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.between{justify-content:space-between}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:12px 24px;border:2px solid #000;border-radius:8px;background:#000;color:#fff;font:inherit;font-size:20px;white-space:nowrap}
.btn.outline{background:#fff;color:#000}
.btn.ghost{background:transparent;border-color:transparent;color:#000;padding-left:8px;padding-right:8px}
.btn.sm{padding:6px 14px;font-size:18px}
.btn.lg{padding:16px 32px;font-size:22px}
.btn.block{width:100%}
.btn svg{stroke:currentColor}
.img{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;background:#F0F0F0;border:2px solid #000;border-radius:8px;color:#555;text-align:center;padding:16px;min-height:240px;width:100%}
.img svg{stroke:#555}
.grid{display:grid;gap:32px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.split{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.split.wide{grid-template-columns:2fr 1fr;align-items:start}
.card{display:flex;flex-direction:column;gap:10px}
.card .link{display:inline-flex;align-items:center;gap:4px;text-decoration:underline;text-underline-offset:4px}
.box{border:2px solid #000;border-radius:8px;padding:24px;background:#fff}
.box.soft{background:#F4F4F4}
.box.selected{box-shadow:6px 6px 0 #000}
.field{display:flex;flex-direction:column;gap:6px;width:100%}
.field label{font-size:16px;text-transform:uppercase;letter-spacing:.04em}
.field .hint{font-size:16px;color:#5a5a5a}
.field.error .input{border-color:#C62828}
.field.error .hint{color:#C62828}
.field.success .hint{color:#1B7F4B}
.input{display:flex;align-items:center;justify-content:space-between;gap:8px;border:2px solid #000;border-radius:8px;padding:10px 16px;min-height:52px;background:#fff;color:#5a5a5a}
.input.area{min-height:120px;align-items:flex-start}
.input.filled{color:#000}
.check{display:flex;gap:12px;align-items:center}
.check i{display:inline-flex;width:24px;height:24px;border:2px solid #000;border-radius:4px;flex:none;align-items:center;justify-content:center}
.check i.on{background:#000}
.check i.on svg{stroke:#fff;width:16px;height:16px}
.radio i{border-radius:50%}
.radio i.on{background:#fff;box-shadow:inset 0 0 0 5px #000}
.tags{display:flex;gap:10px;flex-wrap:wrap}
.tag{display:inline-flex;align-items:center;gap:6px;border:2px solid #000;border-radius:999px;padding:4px 16px;font-size:18px;background:#fff}
.tag.on{background:#000;color:#fff}
.badge{display:inline-block;white-space:nowrap;border:2px solid #000;border-radius:6px;padding:0 8px;font-size:16px}
.badge.dark{background:#000;color:#fff}
.tabs{display:flex;border-bottom:2px solid #000;gap:0}
.tabs span{padding:12px 24px;border:2px solid transparent;border-bottom:none;border-radius:8px 8px 0 0;margin-bottom:-2px}
.tabs span.on{border-color:#000;background:#fff}
.steps{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:18px}
.steps .s{display:flex;align-items:center;gap:8px;color:#5a5a5a}
.steps .s b{display:inline-flex;width:30px;height:30px;border:2px solid #5a5a5a;border-radius:50%;align-items:center;justify-content:center;font-weight:400}
.steps .s.on{color:#000}.steps .s.on b{border-color:#000;background:#000;color:#fff}
.steps .s.done{color:#000}.steps .s.done b{border-color:#000}
.steps .line{width:40px;height:2px;background:#000}
.crumbs{display:flex;gap:8px;align-items:center;font-size:18px;color:#5a5a5a}
.acc{border-top:2px solid #000}
.acc>div{display:flex;justify-content:space-between;align-items:center;padding:18px 0;border-bottom:2px solid #000}
table{width:100%;border-collapse:collapse;border:2px solid #000;border-radius:8px;font-size:19px}
th,td{text-align:left;padding:14px 16px;border-bottom:2px solid #000}
th{background:#F4F4F4;font-weight:400;font-size:16px;text-transform:uppercase;letter-spacing:.04em}
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;text-align:center;font-size:18px}
.cal span{padding:8px 0;border-radius:50%}
.cal .h{color:#5a5a5a;font-size:16px}
.cal .off{color:#bbb;text-decoration:line-through}
.cal .sel{background:#000;color:#fff}
.cal .range{background:#E2E2E2;border-radius:0}
.slots{display:flex;gap:10px;flex-wrap:wrap}
.summary{display:flex;flex-direction:column;gap:12px}
.summary .line{display:flex;justify-content:space-between}
.summary .total{border-top:2px solid #000;padding-top:12px;font-size:24px}
.divider{height:2px;background:#000;width:100%}
.toast{display:flex;align-items:center;gap:12px;border:2px solid #000;border-radius:8px;padding:14px 18px;background:#000;color:#fff}
.toast svg{stroke:#fff}
.toast.light{background:#fff;color:#000}.toast.light svg{stroke:#000}
.modal-bg{background:rgba(0,0,0,.45);padding:80px 0;display:flex;justify-content:center}
.modal{background:#fff;border:2px solid #000;border-radius:12px;padding:32px;width:560px;max-width:calc(100% - 32px);display:flex;flex-direction:column;gap:16px;box-shadow:8px 8px 0 #000}
.list-row{display:flex;gap:16px;align-items:center;justify-content:space-between;padding:16px 0;border-bottom:2px solid #000}
.hotspot{position:absolute;display:inline-flex;width:40px;height:40px;border:2px solid #000;border-radius:50%;background:#fff;align-items:center;justify-content:center;font-size:18px}
.rel{position:relative}
footer.site{background:#F4F4F4;border-top:2px solid #000;padding:64px 64px 32px;display:flex;flex-direction:column;gap:48px}
footer .top{display:flex;justify-content:space-between;gap:48px}
footer .cols{display:flex;gap:72px}
footer .cols div{display:flex;flex-direction:column;gap:8px}
footer .legal{display:flex;justify-content:space-between;align-items:center;font-size:16px;color:#5a5a5a}
footer .signup{display:flex;gap:12px;margin-top:8px}
footer .signup .input{width:360px}
.center{text-align:center;align-items:center;margin-left:auto;margin-right:auto}
.grid>*,.split>*,.stack>*{min-width:0}
.img span{overflow-wrap:anywhere}
@media (max-width:700px){
  html,body{overflow-x:hidden}
  .input[style*="min-width"]{min-width:0 !important;width:100%}
  .row>.btn{flex:0 1 auto}
  .row.stack-m>.btn{width:100%}
  body{font-size:18px}
  .note{padding:10px 16px;flex-direction:column;gap:4px}.note .screen{margin-left:0}
  header.site{padding:16px}
  .logo{font-size:26px}
  header nav{display:none}
  header .menu{display:block}
  .wrap{padding:0 16px}
  section{padding:40px 0}
  h1{font-size:40px}h2{font-size:30px}h3{font-size:24px}
  .g2,.g3,.g4,.split,.split.wide{grid-template-columns:1fr;gap:24px}
  .g4.m2,.g3.m2{grid-template-columns:1fr 1fr;gap:16px}
  .img{min-height:200px}
  .tabs{overflow:hidden}
  .steps .line{width:16px}.steps .s em{display:none}
  table{font-size:16px}th,td{padding:10px 8px}
  .hide-m{display:none}
  .row.stack-m{flex-direction:column;align-items:stretch}
  footer.site{padding:40px 16px 24px;gap:32px}
  footer .top{flex-direction:column;gap:32px}
  footer .cols{flex-direction:column;gap:28px}
  footer .signup{flex-direction:column}footer .signup .input{width:100%}
  footer .legal{flex-direction:column;align-items:flex-start;gap:12px}
}
"""

NAV = [("Wines & Ciders", "04-products.html"), ("The Farm", "02-about-farm.html"), ("Visit", "10-visit.html"),
       ("Stay", "13-cabin.html"), ("Club", "17-club.html"), ("Stockists", "23-stockists.html")]

# ---------- building blocks ----------
def img(label, h=320, extra=""):
    return f'<div class="img" style="min-height:{h}px;{extra}">{I["image"]}<span>{label}</span></div>'

def btn(t, kind="", href="#", icon=""):
    return f'<a class="btn {kind}" href="{href}">{t}{icon}</a>'

def card(label, title, body, link="Learn more", h=260, meta=""):
    m = f'<span class="eyebrow">{meta}</span>' if meta else ""
    return (f'<div class="card">{img(label, h)}{m}<h3>{title}</h3><p class="muted">{body}</p>'
            f'<a class="link" href="#">{link} {I["chev_r"]}</a></div>')

def field(label, ph, icon="", state="", hint="", filled=False, area=False):
    h = f'<span class="hint">{hint}</span>' if hint else ""
    cls = "input" + (" filled" if filled else "") + (" area" if area else "")
    return f'<div class="field {state}"><label>{label}</label><div class="{cls}"><span>{ph}</span>{icon}</div>{h}</div>'

def select(label, val):
    return field(label, val, I["chev_d"], filled=True)

def check(t, on=False, radio=False):
    return f'<div class="check{" radio" if radio else ""}"><i class="{"on" if on else ""}">{I["check"] if on and not radio else ""}</i><span>{t}</span></div>'

def steps(names, cur):
    out = []
    for i, n in enumerate(names, 1):
        cls = "on" if i == cur else ("done" if i < cur else "")
        mark = "✓" if i < cur else str(i)
        out.append(f'<div class="s {cls}"><b>{mark}</b><em>{n}</em></div>')
    return '<div class="steps">' + '<span class="line"></span>'.join(out) + "</div>"

def crumbs(*items):
    return '<div class="crumbs">' + f' {I["chev_r"]} '.join(items) + "</div>"

def acc(items):
    return '<div class="acc">' + "".join(f'<div><span>{q}</span>{I["chev_d"]}</div>' for q in items) + "</div>"

def summary(lines, total):
    rows = "".join(f'<div class="line"><span>{a}</span><span>{b}</span></div>' for a, b in lines)
    return f'<div class="summary">{rows}<div class="line total"><span>Total</span><span>{total}</span></div></div>'

def cal(sel=(), rng=(), off=()):
    days = "".join(f'<span class="h">{d}</span>' for d in "SMTWTFS")
    cells = '<span></span>' * 3
    for d in range(1, 31):
        c = "sel" if d in sel else "range" if d in rng else "off" if d in off else ""
        cells += f'<span class="{c}">{d}</span>'
    return (f'<div class="box"><div class="row between" style="margin-bottom:12px">{I["chev_l"]}<h4>June 2027</h4>{I["chev_r"]}</div>'
            f'<div class="cal">{days}{cells}</div></div>')

def header(active=""):
    links = "".join(f'<a href="{h}" class="{"on" if n == active else ""}">{n}</a>' for n, h in NAV)
    return (f'<header class="site"><a class="logo" href="01-home.html">LAS MUJERES</a><nav>{links}</nav>'
            f'<span class="menu">{I["menu"]}</span></header>')

FOOTER = f"""<footer class="site">
<div class="top">
  <div class="stack" style="gap:12px">
    <h3>Get farm news &amp; new releases</h3>
    <p class="muted">Harvest updates, events and club releases. About once a month.</p>
    <div class="signup"><div class="input"><span>Email address</span></div>{btn("Subscribe")}</div>
  </div>
  <div class="cols">
    <div><span class="eyebrow">Explore</span><a href="04-products.html">Wines &amp; Ciders</a><a href="02-about-farm.html">The Farm</a><a href="06-artists.html">Label Artists</a><a href="08-growers.html">Growers</a></div>
    <div><span class="eyebrow">Visit</span><a href="10-visit.html">Tours &amp; Tastings</a><a href="03-farm-tour.html">Farm Tour</a><a href="13-cabin.html">Stay in the Cabin</a></div>
    <div><span class="eyebrow">Find our wines</span><a href="17-club.html">Wine &amp; Cider Club</a><a href="23-stockists.html">Find a Stockist</a><a href="20-trade-login.html">Trade Availability</a></div>
  </div>
</div>
<div class="legal"><span>© Las Mujeres · Farm address · Tasting room hours</span><span class="row">{I["insta"]}{I["fb"]}</span></div>
</footer>"""

PAGES = []  # (slug, title, story, group)

def page(slug, title, story, body, active="", group="", footer=True):
    PAGES.append((slug, title, story, group))
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>LM · {title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body>
<div class="note"><div><b>User story</b>{story}</div><span class="screen">{slug.split('-')[0]} · {title}</span><a class="back" href="../index.html">← All wireframes</a></div>
{header(active)}
<main>{body}</main>
{FOOTER if footer else ""}
</body></html>"""
    (SCREENS / f"{slug}.html").write_text(html)


# ---------- copy shorthands ----------
S_CLUB = "As a B2C customer of LM, I want to join the wine and cider club."
S_B2B = "As a B2B customer of LM, I want to know the current availability of ciders and wines."
S_FARM = "As a visitor to the LM website, I want to find out more about the farm."
S_PROD = "As a visitor to the LM website, I want to learn more about the products they make."
S_ART = "As a visitor to the LM website, I want to learn more about the artists they work with for labels."
S_GROW = "As a visitor to the LM website, I want to learn more about the farmers they work with."
S_TOUR = "As a visitor to the LM website, I want to take a visual tour of the farm."
S_BOOK = "As a visitor to the LM website, I want to book a tour or tasting."
S_NEWS = "As a visitor to the LM website, I want to sign up for the newsletter."
S_CABIN = "As a visitor to the LM website, I want to book a stay in the LM cabin (promo codes for special guests needed)."
S_STOCK = "As a visitor to the LM website, I want to find a stockist."
S_HOME = "Entry point for all stories: farm, products, visit, stay, club, stockists, newsletter."


def build():
    SCREENS.mkdir(parents=True, exist_ok=True)

    # 01 Home
    page("01-home", "Home", S_HOME, f"""
<section class="tight"><div class="wrap stack lg">
  {img("Hero image: orchard, vineyard or cellar", 560)}
  <div class="row between stack-m"><h1>Wine &amp; cider from<br>our family farm</h1>
  <div class="row">{btn("Explore wines & ciders", "", "04-products.html")}</div></div>
</div></section>
<section><div class="wrap split">
  {img("Photo: the farm / founders", 420)}
  <div class="stack"><span class="eyebrow">The farm</span><h2>Short intro to Las Mujeres: who we are, where we farm, how we make.</h2>
  <p class="muted">Two or three sentences on the land, the people and the approach. Links through to the full story.</p>
  {btn("Our story", "outline", "02-about-farm.html")}</div>
</div></section>
<section class="soft"><div class="wrap stack lg">
  <div class="row between"><h2>Wines &amp; ciders</h2>{btn("See all", "ghost", "04-products.html", I["chev_r"])}</div>
  <div class="grid g4 m2">
    {card("Bottle shot", "Product name", "Cider · Vintage · Style", "View", 300)}
    {card("Bottle shot", "Product name", "Wine · Vintage · Style", "View", 300)}
    {card("Bottle shot", "Product name", "Cider · Vintage · Style", "View", 300)}
    {card("Bottle shot", "Product name", "Wine · Vintage · Style", "View", 300)}
  </div>
</div></section>
<section><div class="wrap grid g3">
  {card("Photo: tasting room", "Tours &amp; tastings", "Walk the orchard and taste the current releases with us.", "Request a visit")}
  {card("Photo: the cabin", "Stay in the cabin", "Wake up on the farm. Book a night or a weekend.", "Check dates")}
  {card("Photo: club shipment", "Wine &amp; cider club", "Seasonal shipments, member pricing and events.", "Join the club")}
</div></section>
<section class="soft"><div class="wrap split">
  <div class="stack"><span class="eyebrow">Meet the makers</span><h2>The artists behind our labels and the growers behind our fruit.</h2>
  <div class="row">{btn("Label artists", "outline", "06-artists.html")}{btn("Our growers", "outline", "08-growers.html")}</div></div>
  <div class="grid g2">{img("Label art", 260)}{img("Grower portrait", 260)}</div>
</div></section>
<section><div class="wrap split">
  <div class="stack"><h2>Where to find Las Mujeres</h2><p class="muted">Shops, restaurants and bars that pour our wines and ciders.</p>
  <div class="row">{btn("See all stockists", "", "23-stockists.html")}</div></div>
  <div class="img" style="min-height:300px">{I["pin_big"]}<span>Map preview</span></div>
</div></section>""")

    # 02 About the farm
    page("02-about-farm", "About the Farm", S_FARM, f"""
<section class="tight"><div class="wrap stack lg">{img("Hero photo: wide landscape of the farm", 520)}
<div class="stack"><span class="eyebrow">Our story</span><h1>About the farm</h1><p class="muted">Intro paragraph: where the farm is, how it started, what it means to the family.</p></div></div></section>
<section><div class="wrap split">{img("Archive / founders photo", 420)}
<div class="stack"><h2>How it started</h2><p class="muted">History of the land and the people. Two or three short paragraphs.</p></div></div></section>
<section class="soft"><div class="wrap stack lg"><h2>How we farm</h2><div class="grid g3">
  {card("Photo: orchard", "The orchard", "Varieties, practices, organic / regenerative notes.", "Meet the growers")}
  {card("Photo: vineyard", "The vineyard", "Grapes, soils, climate.", "See the wines")}
  {card("Photo: cellar", "The cellar", "Low-intervention methods, fermentation, aging.", "See the ciders")}
</div></div></section>
<section><div class="wrap stack lg"><h2>The people</h2><div class="grid g4 m2">
  {card("Portrait", "Name", "Role on the farm", "Read more", 260)}{card("Portrait", "Name", "Role on the farm", "Read more", 260)}
  {card("Portrait", "Name", "Role on the farm", "Read more", 260)}{card("Portrait", "Name", "Role on the farm", "Read more", 260)}
</div></div></section>
<section class="soft"><div class="wrap split"><div class="stack"><h2>See it for yourself</h2>
<p class="muted">Take the visual tour online, or come and walk the farm with us.</p>
<div class="row">{btn("Take the farm tour", "", "03-farm-tour.html")}{btn("Book a visit", "outline", "10-visit.html")}</div></div>
{img("Photo: visitors in the orchard", 340)}</div></section>""", "The Farm")

    # 03 Visual farm tour
    spots = [(18, 30), (42, 55), (65, 25), (80, 62), (30, 75)]
    hs = "".join(f'<span class="hotspot" style="left:{x}%;top:{y}%">{n}</span>' for n, (x, y) in enumerate(spots, 1))
    page("03-farm-tour", "Visual Farm Tour", S_TOUR, f"""
<section class="tight"><div class="wrap stack">{crumbs("The Farm", "Farm tour")}<h1>Take a tour of the farm</h1>
<p class="muted">Click a numbered stop on the map, or step through the tour in order.</p></div></section>
<section class="tight"><div class="wrap split wide">
  <div class="rel"><div class="img" style="min-height:560px">{I["map"]}<span>Illustrated farm map (drone photo or drawn map)</span></div>{hs}</div>
  <div class="box stack"><span class="eyebrow">Stop 2 of 5</span>{img("Photo: the cider house", 240)}<h3>The cider house</h3>
  <p class="muted">Short caption about this stop.</p>
  <div class="row between">{btn("Previous", "outline sm", "#", "")}{btn("Next stop", "sm", "#", I["chev_r"])}</div></div>
</div></section>
<section><div class="wrap stack lg"><h2>The farm through the year</h2><div class="grid g4 m2">{img("Photo: spring blossom", 260)}{img("Photo: summer orchard", 260)}{img("Photo: harvest", 260)}{img("Photo: winter pruning", 260)}</div></div></section>
<section class="soft"><div class="wrap stack lg"><h2>All stops</h2><div class="grid g4 m2">
  {card("Photo", "1 · The orchard", "Caption", "View", 200)}{card("Photo", "2 · The cider house", "Caption", "View", 200)}
  {card("Photo", "3 · The vineyard", "Caption", "View", 200)}{card("Photo", "4 · The cabin", "Caption", "View", 200)}
</div><div class="row">{btn("Book an in-person tour", "", "10-visit.html")}</div></div></section>""", "The Farm")

    # 04 Products index
    prods = "".join(card("Bottle shot", "Product name", f"{t} · 2025 · Style notes", "View", 320, t.upper())
                    for t in ["Cider", "Wine", "Cider", "Wine", "Cider", "Wine", "Cider", "Wine"])
    page("04-products", "Wines & Ciders", S_PROD, f"""
<section class="tight"><div class="wrap stack"><h1>Wines &amp; ciders</h1><p class="muted">Intro: what we make and why.</p></div></section>
<section class="tight"><div class="wrap stack lg">
  <div class="grid g4 m2">{prods}</div>
</div></section>
<section class="soft"><div class="wrap split"><div class="stack"><h2>Get new releases first</h2><p class="muted">Club members get first access and member pricing.</p>
{btn("Join the club", "", "17-club.html")}</div>{img("Photo: club shipment", 300)}</div></section>""", "Wines & Ciders")

    # 05 Product detail
    page("05-product-detail", "Product Detail", S_PROD, f"""
<section class="tight"><div class="wrap">{crumbs("Wines &amp; Ciders", "Ciders", "Product name")}</div></section>
<section class="tight"><div class="wrap split" style="align-items:start">
  <div class="stack">{img("Bottle shot", 520)}<div class="grid g3">{img("Label detail", 120)}{img("In the glass", 120)}{img("Orchard", 120)}</div></div>
  <div class="stack lg"><span class="eyebrow">Cider · 2025</span><h1>Product name</h1>
  <p class="muted">Tasting notes: aroma, palate, finish. One short paragraph.</p>
  <div class="tags"><span class="tag">Dry</span><span class="tag">Sparkling</span><span class="tag">6.5% ABV</span><span class="tag">750 ml</span></div>
  <div class="box soft stack"><h3>Where to find it</h3>
  <div class="row">{I["pin"]}<span>Shops, restaurants and bars</span></div>
  <div class="row">{I["glass"]}<span>The farm tasting room</span></div>
  <div class="row">{I["cal"]}<span>Club shipments</span></div>
  <div class="row">{btn("Find a stockist", "", "23-stockists.html")}{btn("Join the club", "outline", "17-club.html")}</div></div>
  {acc(["Making notes", "Food pairing", "Technical sheet (PDF)"])}</div>
</div></section>
<section class="soft"><div class="wrap grid g2">
  <div class="box row" style="align-items:flex-start;gap:24px">{img("Label artwork", 180, "max-width:180px")}<div class="stack"><span class="eyebrow">The label</span><h3>Artist name</h3><p class="muted">Line about the label art.</p><a class="link" href="07-artist-detail.html">Meet the artist</a></div></div>
  <div class="box row" style="align-items:flex-start;gap:24px">{img("Grower portrait", 180, "max-width:180px")}<div class="stack"><span class="eyebrow">The fruit</span><h3>Grower / orchard name</h3><p class="muted">Line about where the fruit comes from.</p><a class="link" href="09-grower-detail.html">Meet the grower</a></div></div>
</div></section>
<section><div class="wrap stack lg"><h2>You might also like</h2><div class="grid g4 m2">
  {card("Bottle shot", "Product name", "Wine · 2025", "View", 260)}{card("Bottle shot", "Product name", "Cider · 2025", "View", 260)}
  {card("Bottle shot", "Product name", "Wine · 2024", "View", 260)}{card("Bottle shot", "Product name", "Cider · 2024", "View", 260)}
</div></div></section>""", "Wines & Ciders")

    # 06 Artists index
    arts = "".join(card("Artist portrait / label art", "Artist name", "Medium · Location · Labels: Product A, Product B", "Meet the artist", 300) for _ in range(6))
    page("06-artists", "Label Artists", S_ART, f"""
<section class="tight"><div class="wrap split"><div class="stack"><span class="eyebrow">Our labels</span><h1>The artists behind our labels</h1>
<p class="muted">Why we commission a different artist for each label, and how we pick them.</p></div>{img("Collage of labels", 360)}</div></section>
<section><div class="wrap grid g3">{arts}</div></section>""", "Wines & Ciders")

    # 07 Artist detail
    page("07-artist-detail", "Artist Detail", S_ART, f"""
<section class="tight"><div class="wrap">{crumbs("Label Artists", "Artist name")}</div></section>
<section class="tight"><div class="wrap split" style="align-items:start">{img("Artist portrait", 480)}
<div class="stack lg"><h1>Artist name</h1><div class="tags"><span class="tag">Medium</span><span class="tag">City</span></div>
<p class="muted">Bio: background, practice, how they approached the label.</p>
<div class="row">{I["insta"]}<a class="link" href="#">Artist website</a></div></div></div></section>
<section class="soft"><div class="wrap stack lg"><h2>Labels by this artist</h2><div class="grid g3">
  {card("Label artwork + bottle", "Product name", "Cider · 2025 · Story behind the artwork", "View the product")}
  {card("Label artwork + bottle", "Product name", "Wine · 2024 · Story behind the artwork", "View the product")}
  {card("Process sketch", "From sketch to label", "Optional process photos", "View")}
</div></div></section>
<section><div class="wrap row between">{btn("Previous artist", "outline", "#")}{btn("Next artist", "outline", "#", I["chev_r"])}</div></section>""", "Wines & Ciders")

    # 08 Growers index
    grows = "".join(card("Grower portrait / orchard", "Grower or farm name", "Location · Fruit: apples / grapes · Since 20XX", "Meet the grower", 300) for _ in range(6))
    page("08-growers", "Growers", S_GROW, f"""
<section class="tight"><div class="wrap split"><div class="stack"><span class="eyebrow">Our growers</span><h1>The farmers we work with</h1>
<p class="muted">Our own fruit plus partner growers. How we choose them and work together.</p></div>
<div class="img" style="min-height:360px">{I["pin_big"]}<span>Map of grower locations</span></div></div></section>
<section><div class="wrap grid g3">{grows}</div></section>""", "The Farm")

    # 09 Grower detail
    page("09-grower-detail", "Grower Detail", S_GROW, f"""
<section class="tight"><div class="wrap">{crumbs("Growers", "Grower name")}</div></section>
<section class="tight"><div class="wrap stack lg">{img("Hero: grower in their orchard / vineyard", 460)}
<div class="split" style="align-items:start"><div class="stack"><h1>Grower name</h1><p class="muted">Their story, the land, how long we have worked together.</p></div>
<div class="box soft stack"><div class="row">{I["pin"]}<span>Location</span></div><div class="row">{I["glass"]}<span>Fruit: varieties</span></div><div class="row">{I["info"]}<span>Practices: organic, dry-farmed…</span></div></div></div></div></section>
<section class="soft"><div class="wrap stack lg"><h2>Made with their fruit</h2><div class="grid g4 m2">
  {card("Bottle shot", "Product name", "Cider · 2025", "View", 260)}{card("Bottle shot", "Product name", "Wine · 2025", "View", 260)}
  {card("Bottle shot", "Product name", "Cider · 2024", "View", 260)}{card("Bottle shot", "Product name", "Wine · 2024", "View", 260)}
</div></div></section>""", "The Farm")

    # 10 Visit
    page("10-visit", "Visit: Tours & Tastings", S_BOOK, f"""
<section class="tight"><div class="wrap stack lg">{img("Hero: tasting room / guests in the orchard", 460)}
<div class="row between stack-m"><div class="stack"><h1>Visit the farm</h1><p class="muted">Hours, location and what to expect.</p></div>{btn("Request a visit", "lg", "11-visit-request.html")}</div></div></section>
<section><div class="wrap stack lg"><h2>Experiences</h2><div class="grid g3">
  {card("Photo", "Tasting flight", "45 min · $00 pp · Seated tasting of current releases.", "Request")}
  {card("Photo", "Orchard &amp; cellar tour", "90 min · $00 pp · Walk the farm, then taste.", "Request")}
  {card("Photo", "Private / group visit", "By request · Groups of 8+.", "Enquire")}
</div></div></section>
<section class="soft"><div class="wrap split">
  <div class="stack"><h2>Plan your visit</h2>
  <div class="row">{I["pin"]}<span>Address · Directions</span></div><div class="row">{I["cal"]}<span>Open Thu–Sun, 11–5</span></div><div class="row">{I["info"]}<span>Accessibility, dogs, kids, parking</span></div>
  {btn("Take the visual tour first", "outline", "03-farm-tour.html")}</div>
  <div class="img" style="min-height:320px">{I["pin_big"]}<span>Map</span></div></div></section>
<section><div class="wrap stack lg"><h2>Questions</h2>{acc(["How far ahead should I ask?", "Can I bring children or dogs?", "Is the farm accessible?", "Can I buy bottles on site?"])}</div></section>""", "Visit")

    # 11 Visit request (handled by email, no booking platform)
    def opt(name, meta, sel=False):
        return f'<div class="box stack{" selected" if sel else ""}">{check(name, sel, True)}<span class="small muted">{meta}</span></div>'

    def how(steps_):
        return "".join(f'<div class="row" style="flex-wrap:nowrap"><span class="badge dark">{i}</span><span>{t}</span></div>' for i, t in enumerate(steps_, 1))

    page("11-visit-request", "Request a Visit", S_BOOK, f"""
<section class="tight"><div class="wrap stack lg">{crumbs("Visit", "Request a visit")}<h1>Request a tour or tasting</h1>
<p class="muted">Tell us when you would like to come. We reply by email to confirm.</p>
<div class="split wide"><div class="stack lg">
<h3>1. Experience</h3><div class="grid g3">{opt("Tasting flight", "45 min · $00 pp")}{opt("Orchard &amp; cellar tour", "90 min · $00 pp", True)}{opt("Private / group", "8+ guests")}</div>
<h3>2. When</h3><div class="grid g2">{field("Preferred date", "Select date", I["cal"])}{field("Backup date (optional)", "Select date", I["cal"])}</div>
<div class="field"><label>Preferred time</label><div class="tags"><span class="tag">Morning</span><span class="tag on">Midday</span><span class="tag">Afternoon</span><span class="tag">Flexible</span></div></div>
<div class="grid g2">{field("Guests", "2", filled=True)}{select("Occasion (optional)", "Select")}</div>
<h3>3. Your details</h3><div class="grid g2">{field("Name", "")}{field("Email", "")}{field("Phone (optional)", "")}</div>
{field("Anything we should know?", "Dietary needs, accessibility, celebrations", area=True)}
{check("Everyone in my group is 21 or older", True)}{check("Sign me up for the newsletter")}</div>
<div class="box soft stack"><h3>How it works</h3>{how(["Send your request", "We email you to confirm the date, time and price", "Pay the Stripe invoice we send you"])}
<span class="small muted">Form emails the LM team. They reply with a Stripe invoice; your visit is confirmed once it is paid.</span>
<div class="divider"></div><span class="small">Prefer to write? <u>visits@ email address</u></span></div></div>
<div class="row between">{btn("Back", "ghost", "10-visit.html")}{btn("Send request", "", "12-visit-request-sent.html")}</div></div></section>""", "Visit")

    # 12 Request sent
    page("12-visit-request-sent", "Visit Request Sent", S_BOOK, f"""
<section><div class="wrap stack lg center" style="max-width:760px">
<div class="toast light">{I["check"]}<span>Request sent. A copy is on its way to you@example.com</span></div>
<h1>Thanks, we will be in touch</h1><p class="muted center">Orchard &amp; cellar tour · Sat 14 June (backup Sun 15) · Midday · 2 guests</p>
<p class="muted center">We usually reply within 2 working days with a Stripe invoice. Your visit is confirmed once it is paid.</p>
<div class="row">{btn("Take the farm tour", "outline", "03-farm-tour.html")}{btn("Back to home", "ghost", "01-home.html")}</div></div></section>
<section class="soft"><div class="wrap grid g3">
  {card("Photo: the cabin", "Make a night of it", "Stay in the cabin after your visit.", "Check dates")}
  {card("Photo: bottles", "Find our wines &amp; ciders", "Shops, restaurants and bars that stock us.", "See stockists")}
  {card("Photo: club", "Love what you taste?", "Ask about the club when you visit.", "About the club")}
</div></section>""", "Visit")

    # 13 Cabin
    page("13-cabin", "Stay in the Cabin", S_CABIN, f"""
<section class="tight"><div class="wrap stack lg"><div class="grid g2" style="grid-template-columns:2fr 1fr">{img("Hero: the cabin exterior", 520)}<div class="stack">{img("Interior", 252)}{img("View from the porch", 252)}</div></div>
<div class="split wide"><div class="stack lg"><h1>Stay in the cabin</h1><p class="muted">Description: sleeps 2–4, setting, what makes it special.</p>
<div class="grid g4 m2"><div class="row">{I["bed"]}<span>1 bedroom</span></div><div class="row">{I["user"]}<span>Sleeps 4</span></div><div class="row">{I["glass"]}<span>Welcome bottle</span></div><div class="row">{I["info"]}<span>Wood stove</span></div></div>
<h3>House rules &amp; info</h3>{acc(["Check-in / check-out", "What is included", "Cancellation policy", "Getting here"])}</div>
<div class="box stack selected"><div class="row between"><h3>$000 <span class="small muted">/ night</span></h3><span class="small">2-night min</span></div>
<div class="grid g2">{field("Check in", "Add date", I["cal"])}{field("Check out", "Add date", I["cal"])}</div>{select("Guests", "2 guests")}
<a class="small" href="14-cabin-book-1-dates-promo.html" style="text-decoration:underline">Have a promo code?</a>
{btn("Check availability", "block", "14-cabin-book-1-dates-promo.html")}<span class="small muted">Live availability from Hapio</span></div></div></div></section>""", "Stay")

    CAB = ["Dates", "Details &amp; payment", "Confirmed"]

    def cabin_summary(promo):
        extra = '<div class="line"><span>Promo FRIENDS25 (−25%)</span><span>−$00</span></div>' if promo else ""
        return f"""<div class="box soft stack"><h3>The Cabin</h3>{img("Cabin photo", 140)}
<div class="summary"><div class="line"><span>Fri 13 – Sun 15 June</span><span></span></div><div class="line"><span>2 nights × $000</span><span>$000</span></div>
<div class="line"><span>Cleaning fee</span><span>$00</span></div>{extra}<div class="line total"><span>Total</span><span>$000</span></div></div></div>"""

    # 14 dates + promo states
    page("14-cabin-book-1-dates-promo", "Cabin 1: Dates & Promo Code", S_CABIN, f"""
<section class="tight"><div class="wrap stack lg">{steps(CAB, 1)}<h2>Choose your dates</h2>
<div class="split wide"><div class="stack lg"><div class="grid g2">{cal(sel=(13, 15), rng=(14,), off=(1, 2, 7, 8, 20, 21, 22))}
<div class="stack">{select("Guests", "2 guests")}
<div class="box soft stack"><h4>Promo code</h4><span class="small muted">For special guests, partners and club members.</span>
<div class="row" style="flex-wrap:nowrap"><div class="input filled" style="flex:1"><span>FRIENDS25</span></div>{btn("Apply", "outline")}</div>
<div class="field success"><span class="hint">✓ FRIENDS25 applied: 25% off your stay</span></div><span class="small muted">Code rules (who, dates, discount) managed by LM. Validation via Hapio or custom: TBC.</span></div>
<div class="stack"><span class="eyebrow">Promo states</span>
{field("Promo code", "FRIEND", state="error", hint="That code is not valid or has expired.", filled=True)}
{field("Promo code", "VIPHOST", state="success", hint="✓ Special-guest rate applied. Minimum stay waived.", filled=True)}
{field("Promo code", "CLUB10", state="error", hint="This code needs you to sign in as a club member.", filled=True)}</div></div></div></div>
{cabin_summary(True)}</div>
<div class="row between">{btn("Back", "ghost", "13-cabin.html")}{btn("Continue", "", "15-cabin-book-2-details.html", I["chev_r"])}</div></div></section>""", "Stay")

    # 15 details
    page("15-cabin-book-2-details", "Cabin 2: Details & Payment", S_CABIN, f"""
<section class="tight"><div class="wrap stack lg">{steps(CAB, 2)}<h2>Guest details</h2>
<div class="split wide"><div class="stack lg"><div class="grid g2">{field("First name", "")}{field("Last name", "")}{field("Email", "")}{field("Phone", "")}</div>
{select("Estimated arrival", "4–6 pm")}{field("Anything we should know?", "Celebrations, allergies, accessibility", area=True)}
<h3>Payment</h3><div class="grid g2">{field("Card number", "", I["lock"])}{field("Expiry / CVC", "MM/YY · CVC")}</div>
<span class="small muted">Booking created in Hapio. Payment provider TBC (Hapio handles scheduling, not payments).</span>
{check("I agree to the house rules and cancellation policy", True)}{check("I would like a tasting during my stay (we will email you)")}</div>
{cabin_summary(True)}</div>
<div class="row between">{btn("Back", "ghost", "14-cabin-book-1-dates-promo.html")}{btn("Confirm &amp; pay", "", "16-cabin-confirmation.html")}</div></div></section>""", "Stay")

    # 16 confirmation
    page("16-cabin-confirmation", "Cabin 3: Confirmation", S_CABIN, f"""
<section><div class="wrap stack lg center" style="max-width:760px">{steps(CAB, 3)}
<div class="toast light">{I["check"]}<span>Stay confirmed. Details sent to you@example.com</span></div>
<h1>Your cabin is booked</h1><p class="muted center">Fri 13 – Sun 15 June · 2 guests · Promo FRIENDS25 applied</p>
<div class="row">{btn("Add to calendar", "outline", "#", I["cal"])}{btn("Get directions", "outline", "#", I["pin"])}</div>
<div class="box soft stack" style="width:100%;text-align:left"><h3>Before you arrive</h3><p class="muted">Check-in instructions arrive 48 hours before. Door code, parking, Wi-Fi.</p></div></div></section>""", "Stay")

    # 17 Club
    def tier(name, price, items, sel=False):
        lis = "".join(f'<div class="row" style="flex-wrap:nowrap">{I["check"]}<span>{i}</span></div>' for i in items)
        pop = '<span class="badge dark">Most popular</span>' if sel else ""
        return f'<div class="box stack lg{" selected" if sel else ""}">{pop}<h3>{name}</h3><h2>{price}<span class="small muted"> / shipment</span></h2><div class="stack">{lis}</div>{btn("Choose " + name, "block" if sel else "outline block", "18-club-join.html")}</div>'
    page("17-club", "Wine & Cider Club", S_CLUB, f"""
<section class="tight"><div class="wrap split"><div class="stack lg"><span class="eyebrow">Membership</span><h1>The Las Mujeres club</h1>
<p class="muted">Seasonal shipments of our newest wines and ciders, member pricing and farm events.</p>
<div class="row">{btn("Join the club", "lg", "18-club-join.html")}</div></div>{img("Photo: club shipment / members at a farm event", 440)}</div></section>
<section class="soft"><div class="wrap stack lg"><h2 class="center">Benefits</h2><div class="grid g4 m2">
  <div class="stack center">{I["glass"]}<h4>First access to releases</h4></div><div class="stack center">{I["info"]}<h4>Member pricing</h4></div>
  <div class="stack center">{I["cal"]}<h4>Member-only events</h4></div><div class="stack center">{I["bed"]}<h4>Cabin discounts</h4></div></div></div></section>
<section><div class="wrap stack lg"><h2>Choose your membership</h2><div class="grid g3">
  {tier("Cider", "$00", ["4 ciders, 3× a year", "10% off at the tasting room", "Free tastings for 2"])}
  {tier("Mixed", "$00", ["3 wines + 3 ciders, 3× a year", "15% off at the tasting room", "Free tastings for 4", "Cabin discount"], True)}
  {tier("Wine", "$00", ["6 wines, 3× a year", "15% off at the tasting room", "Free tastings for 4"])}
</div><span class="small muted">Apply online. The LM team confirms by email and arranges payment. Ship or pick up at the farm.</span></div></section>
<section class="soft"><div class="wrap stack lg"><h2>Questions</h2>{acc(["How do shipments work?", "Can I customise or skip a shipment?", "Where do you ship?", "How do I cancel?"])}</div></section>""", "Club")

    # 18 Club application (club run manually by LM with spreadsheets)
    def tier_opt(name, price, meta, sel=False):
        return f'<div class="box stack{" selected" if sel else ""}">{check(name, sel, True)}<h3>{price}</h3><span class="small muted">{meta}</span></div>'

    page("18-club-join", "Join the Club: Application", S_CLUB, f"""
<section class="tight"><div class="wrap stack lg">{crumbs("Club", "Join")}<h1>Join the club</h1>
<p class="muted">Fill this in and we will email you to confirm your membership and arrange payment.</p>
<div class="split wide"><div class="stack lg">
<h3>1. Membership</h3><div class="grid g3">{tier_opt("Cider", "$00", "4 ciders")}{tier_opt("Mixed", "$00", "3 wines + 3 ciders", True)}{tier_opt("Wine", "$00", "6 wines")}</div>
<h3>2. Delivery</h3><div class="grid g2"><div class="box selected">{check("Ship to me", True, True)}</div><div class="box">{check("Pick up at the farm", radio=True)}</div></div>
<h3>3. Your details</h3><div class="grid g2">{field("First name", "")}{field("Last name", "")}{field("Email", "")}{field("Phone", "")}{field("Date of birth", "MM / DD / YYYY", hint="You must be 21+ to join.")}</div>
<h3>Shipping address</h3><div class="grid g2">{field("Address", "")}{field("City", "")}{select("State", "Select state")}{field("Zip code", "")}</div>
{field("Anything else?", "Gift membership, questions", area=True)}
{check("I agree to the membership terms", True)}{check("Send me the newsletter too", True)}
<span class="small muted">No account or card details on this form. The LM team adds you to the club spreadsheet and arranges payment. Club payment method TBC.</span></div>
<div class="box soft stack"><h3>What happens next</h3>
<div class="row" style="flex-wrap:nowrap"><span class="badge dark">1</span><span>We review your application</span></div>
<div class="row" style="flex-wrap:nowrap"><span class="badge dark">2</span><span>We email you to confirm and arrange payment</span></div>
<div class="row" style="flex-wrap:nowrap"><span class="badge dark">3</span><span>Your first shipment goes out with the next release</span></div>
<div class="divider"></div><div class="summary"><div class="line"><span>Mixed membership</span><span>$00 / shipment</span></div><div class="line"><span>3 shipments a year</span><span></span></div></div></div></div>
<div class="row between">{btn("Back", "ghost", "17-club.html")}{btn("Send application", "", "19-club-thanks.html")}</div></div></section>""", "Club")

    # 19 Application sent
    page("19-club-thanks", "Join the Club: Application Sent", S_CLUB, f"""
<section><div class="wrap stack lg center" style="max-width:760px">
<div class="toast light">{I["check"]}<span>Application sent. A copy is on its way to you@example.com</span></div>
<h1>Thanks, Name</h1><p class="muted center">Mixed membership · ships to City, ST</p>
<p class="muted center">We will email you within a few days to confirm your membership and arrange payment.</p>
<div class="row">{btn("Request a visit", "outline", "11-visit-request.html")}{btn("Back to home", "ghost", "01-home.html")}</div></div></section>
<section class="soft"><div class="wrap grid g3">
  {card("Photo: event", "Farm events", "Release parties, harvest days.", "See what is on")}
  {card("Photo: cabin", "Stay in the cabin", "Members get a cabin discount code.", "Check dates")}
  {card("Photo: bottles", "Find our wines &amp; ciders", "Shops, restaurants and bars that stock us.", "See stockists")}
</div></section>""", "Club")

    # 20 Trade login
    page("20-trade-login", "Trade Login", S_B2B, f"""
<section><div class="wrap split"><div class="stack lg"><span class="eyebrow">For trade</span><h1>Trade portal</h1>
<p class="muted">Restaurants, shops and distributors: check live availability, download sheets and place orders.</p>
<div class="row">{I["download"]}<span>Price lists</span></div><div class="row">{I["list"]}<span>Current availability</span></div></div>
<div class="box stack lg selected"><h3>Log in</h3>{field("Email", "")}{field("Password", "", I["lock"])}
<div class="row between">{check("Remember me")}<a class="small" href="#" style="text-decoration:underline">Forgot password?</a></div>
{btn("Log in", "block", "21-trade-availability.html")}<div class="divider"></div>
<span class="small">New trade customer?</span>{btn("Request a trade account", "outline block", "22-trade-enquiry.html")}</div></div></section>""")

    # 21 Availability
    rows = [("Product name", "Cider", "2025", "120 cs", "In stock"), ("Product name", "Cider", "2024", "40 cs", "In stock"),
            ("Product name", "Wine", "2024", "18 cs", "Low stock"), ("Product name", "Wine", "2023", "0", "Sold out"),
            ("Product name", "Cider", "2026", "—", "Pre-order · ships Sept"), ("Product name", "Wine", "2025", "60 cs", "In stock")]
    trs = "".join(f'<tr><td>{a}</td><td class="hide-m">{b}</td><td>{c}</td><td>{e}</td><td><span class="badge{" dark" if f == "In stock" else ""}">{f}</span></td></tr>' for a, b, c, e, f in rows)
    page("21-trade-availability", "Trade Availability", S_B2B, f"""
<section class="tight"><div class="wrap stack lg">
<div class="row between stack-m"><div class="stack" style="gap:4px"><h1>Current availability</h1><span class="muted small">Updated today at 9:00</span></div>
<div class="row">{btn("Download PDF", "outline", "#", I["download"])}{btn("Download CSV", "outline", "#", I["download"])}</div></div>
<table><thead><tr><th>Product</th><th class="hide-m">Type</th><th>Vintage</th><th>Available</th><th>Status</th></tr></thead><tbody>{trs}</tbody></table>
<div class="box stack" style="max-width:560px"><h3>Questions?</h3><p class="small muted">Orders, pricing, samples or anything else. Send us a message and we will get back to you.</p>{btn("Contact us", "outline", "22-trade-enquiry.html")}</div></div></section>""")

    # 22 Trade enquiry (form emails the LM team)
    page("22-trade-enquiry", "Trade Enquiry", S_B2B, f"""
<section class="tight"><div class="wrap stack lg">{crumbs("Trade availability", "Contact us")}<h1>Trade enquiry</h1>
<p class="muted">Questions about orders, pricing, samples or availability. We reply by email.</p>
<div class="split wide"><div class="stack lg">
<div class="grid g2">{field("Name", "")}{field("Business name", "")}{field("Email", "")}{field("Phone (optional)", "")}</div>
{select("Topic", "Select a topic")}
{field("Message", "How can we help?", area=True)}</div>
<div class="box soft stack"><h3>What happens next</h3>{how(["Send your message", "The LM team replies by email"])}
<span class="small muted">Form emails the LM team.</span>
<div class="divider"></div><span class="small">Prefer to write? <u>trade@ email address</u></span></div></div>
<div class="row between">{btn("Back", "ghost", "21-trade-availability.html")}{btn("Send message", "", "#")}</div></div></section>""")

    # 23 Stockists
    def row(t):
        return f'<div class="list-row"><div class="stack" style="gap:2px"><h4>Stockist name</h4><span class="small muted">{t} · Address</span></div><a class="link" href="#">Website</a></div>'
    areas = [("Portland", ["Shop", "Restaurant", "Bar"]), ("Hood River", ["Shop", "Restaurant"]), ("Elsewhere in Oregon", ["Shop", "Bar"])]
    cols = "".join(f'<div class="stack"><h3>{a}</h3>{"".join(row(t) for t in ts)}</div>' for a, ts in areas)
    page("23-stockists", "Stockists", S_STOCK, f"""
<section class="tight"><div class="wrap stack lg"><h1>Where to find our wines &amp; ciders</h1>
<p class="muted">Shops, restaurants and bars that pour or sell Las Mujeres, listed by area. You can also buy at the tasting room or join the club.</p>
<div class="grid g3">{cols}</div></div></section>""", "Stockists")

    # 24 Newsletter states
    page("24-newsletter", "Newsletter Signup States", S_NEWS, f"""
<section class="tight"><div class="wrap stack"><h2>Newsletter signup: entry points and states</h2>
<p class="muted">Footer form on every page (see below), a popup after scroll / exit intent, and an inline block on the home page.</p></div></section>
<div class="modal-bg"><div class="modal"><div class="row between"><span class="eyebrow">Popup</span>{I["x"]}</div>{img("Photo: orchard", 180)}
<h3>Get farm news &amp; new releases</h3><p class="muted">Harvest updates, events and first access to releases.</p>
{field("Email", "you@example.com")}<div class="tags"><span class="tag on">Ciders</span><span class="tag on">Wines</span><span class="tag">Events</span><span class="tag">Cabin</span></div>
{btn("Subscribe", "block")}<span class="small muted center">No spam. Unsubscribe any time.</span></div></div>
<section><div class="wrap grid g3">
  <div class="stack"><span class="eyebrow">Error</span>{field("Email", "you@exa", state="error", hint="Enter a valid email address.", filled=True)}{btn("Subscribe")}</div>
  <div class="stack"><span class="eyebrow">Already subscribed</span>{field("Email", "you@example.com", state="success", hint="You're already on the list. Thanks!", filled=True)}</div>
  <div class="stack"><span class="eyebrow">Success</span><div class="toast">{I["check"]}<span>Thanks! Check your inbox to confirm.</span></div></div>
</div></section>""")

    write_index()


def write_index():
    groups = {}
    for slug, title, story, _ in PAGES:
        groups.setdefault(story, []).append((slug, title))
    items = ""
    for story, pages in groups.items():
        links = "".join(f'<li><a href="screens/{s}.html">{s.split("-")[0]} · {t}</a></li>' for s, t in pages)
        items += f'<div class="box stack"><p class="small">{story}</p><ul>{links}</ul></div>'
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Las Mujeres Wireframes</title><link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap" rel="stylesheet">
<style>{CSS} ul{{list-style:none;display:flex;flex-direction:column;gap:6px}} ul a{{text-decoration:underline}}</style></head>
<body><section><div class="wrap stack lg"><h1>Las Mujeres · Wireframes</h1>
<p class="muted">Low-fi screens per user story, Paper Wireframe Kit style. Each screen is responsive: import at 1440 and 375 with html.to.design.</p>
<div class="grid g3">{items}</div></div></section></body></html>"""
    (OUT / "index.html").write_text(html)


if __name__ == "__main__":
    build()
    print(f"Wrote {len(PAGES)} screens to {SCREENS}")
