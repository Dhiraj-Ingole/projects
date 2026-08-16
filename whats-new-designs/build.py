#!/usr/bin/env python3
"""Generate three HTML redesigns of the Learn Look Locate What's New page."""

IMG = "https://learnlooklocate.com/wp-content/uploads"

HERO_BG = f"{IMG}/2025/04/Whats-New-at-Learn-Look-Locate-%E2%80%94-Fresh-Voices-Breakthroughs-and-Global-Connections-At-Learn-Look-Locate-were-always-evolving-to-bring-you-the-latest-in-trusted-breast-cancer-education-and-hea.jpg"
HERO_BG2 = f"{IMG}/2025/04/Whats-New-at-Learn-Look-Locate-%E2%80%94-Fresh-Voices-Breakthroughs-and-Global-Connections-At-Learn-Look-Locate-were-always-evolving-to-bring-you-the-latest-in-trusted-breast-cancer-education-and-hea-4.jpg"
SPOTLIGHT_IMG = f"{IMG}/2025/09/spotlight-innovations-in-breast-cancer-care-progress-breakthroughs-learn-look-locate.jpg.png"
DIAGNOSIS = f"{IMG}/2024/09/diagnosis-img-1.webp"
YARA = f"{IMG}/2024/08/Dr.-Yara-Robertson-.jpg"

PARTNERS = [
    {
        "title": "Tumor Localization for Early-Stage Breast Cancer: Surgical Marker Navigation",
        "img": f"{IMG}/2024/07/img-2.webp",
        "logo": f"{IMG}/2025/09/5.png",
        "href": "https://learnlooklocate.com/breast-cancer-tumor-localization",
    },
    {
        "title": "Walgreens oncology-specialized pharmacy care team can support you beyond medication",
        "img": f"{IMG}/2023/02/walgreensLLL-img.png",
        "logo": f"{IMG}/2025/09/4.png",
        "href": "https://learnlooklocate.com/walgreens",
    },
    {
        "title": "The Role Of Genomic Testing: Unpacking A Treasure Chest Of Knowledge In Breast Cancer",
        "img": f"{IMG}/2024/04/banner-new.webp",
        "logo": f"{IMG}/2025/09/2.png",
        "href": "https://learnlooklocate.com/your-tumor",
    },
    {
        "title": "Understanding Treatment Options For Stage 4 Breast Cancer With Dr. Rahul Singh",
        "img": f"{IMG}/2025/02/Header-image-Stage-4-Breast-Cancer.webp",
        "logo": f"{IMG}/2025/09/1.png",
        "href": "https://learnlooklocate.com/understanding-treatment-options-for-stage-4-breast-cancer",
    },
    {
        "title": "Lumpectomy: Understanding Your Options and Lighting the Path Forward",
        "img": f"{IMG}/2025/11/Lumpectomy-18.png",
        "logo": f"{IMG}/2026/01/LumicellLogo.png",
        "href": "https://learnlooklocate.com/lumpectomy",
    },
    {
        "title": "Do I need Radiation if I have DCIS?",
        "img": f"{IMG}/2026/06/image.avif",
        "logo": f"{IMG}/2026/06/prelude.png",
        "href": "https://learnlooklocate.com/do-i-need-radiation-if-i-have-dcis",
    },
    {
        "title": "Understanding Breast Cancer Recurrence: ctDNA Insights with Dr. Barry Rosen",
        "img": f"{IMG}/2023/12/img-2.webp",
        "logo": f"{IMG}/2025/09/3.png",
        "href": "https://learnlooklocate.com/breast-cancer-recurrence-ctdna-dr-rosen",
    },
]

EDU = [
    {"date": "29 Jul, 2026", "title": "Medical Menopause—SERIOUSLY???", "img": DIAGNOSIS, "href": "https://learnlooklocate.com/educate/"},
    {"date": "14 Jun, 2026", "title": "Do I Need Radiation If I Have DCIS", "img": f"{IMG}/2026/06/image.avif", "href": "https://learnlooklocate.com/do-i-need-radiation-if-i-have-dcis"},
    {"date": "28 May, 2026", "title": "Metastatic Breast Cancer: First-Line & Maintenance Therapy", "img": f"{IMG}/2025/02/Header-image-Stage-4-Breast-Cancer.webp", "href": "https://learnlooklocate.com/understanding-treatment-options-for-stage-4-breast-cancer"},
    {"date": "23 Apr, 2026", "title": "Goldilocks Mastectomy", "img": f"{IMG}/2025/11/Lumpectomy-18.png", "href": "https://learnlooklocate.com/educate/"},
    {"date": "30 Mar, 2026", "title": "Late-Night Breast Cancer Questions, Answered", "img": SPOTLIGHT_IMG, "href": "https://learnlooklocate.com/educate/"},
]

DOCS = [
    {"date": "03 Nov, 2025", "title": "Breast Cancer in the Military", "img": f"{IMG}/2024/07/img-2.webp", "href": "https://learnlooklocate.com/educate/patient-education/"},
    {"date": "03 Apr, 2025", "title": "Understanding Inflammatory Breast Cancer: Symptoms, Risks And Treatments", "img": DIAGNOSIS, "href": "https://learnlooklocate.com/educate/patient-education/"},
    {"date": "22 Feb, 2025", "title": "Discover Expert Insights on Stage 4 Breast Cancer from Dr. Ramji Rajendran", "img": f"{IMG}/2025/02/Header-image-Stage-4-Breast-Cancer.webp", "href": "https://learnlooklocate.com/educate/patient-education/"},
    {"date": "14 Feb, 2025", "title": "Breast Cancer Screening & Treatment: What You Need to Know", "img": f"{IMG}/2024/04/banner-new.webp", "href": "https://learnlooklocate.com/educate/patient-education/"},
    {"date": "15 Jan, 2025", "title": "Comprehensive Insights: Dr. William Audeh and Breast Cancer Survivor Kelly on Aromatase Inhibitors", "img": YARA, "href": "https://learnlooklocate.com/educate/patient-education/"},
]

SURV = [
    {"date": "17 Jun, 2026", "title": "Knowledge Brings Confidence with DCISionRT", "img": f"{IMG}/2026/06/image.avif", "href": "https://learnlooklocate.com/survivor-stories/"},
    {"date": "17 Jun, 2026", "title": "How DCISionRT Helped a Cancer Survivor Avoid Over-Treatment", "img": f"{IMG}/2026/06/prelude.png", "href": "https://learnlooklocate.com/survivor-stories/"},
    {"date": "25 Feb, 2026", "title": "Stronger Than I Ever Knew: A Breast Cancer Survivor’s Journey", "img": DIAGNOSIS, "href": "https://learnlooklocate.com/survivor-stories/"},
    {"date": "12 Dec, 2025", "title": "DCIS Survivor Story: From Routine MRI to Resilience", "img": SPOTLIGHT_IMG, "href": "https://learnlooklocate.com/survivor-stories/"},
    {"date": "06 Nov, 2025", "title": "Dr. Leona Hamrick, Physician Associate & Breast Cancer Survivor", "img": YARA, "href": "https://learnlooklocate.com/survivor-stories/"},
]

BLOGS = [
    {"date": "13 Aug, 2026", "title": "Your Pathology Report: The Key to Understanding Your Breast Cancer Diagnosis", "img": DIAGNOSIS, "href": "https://learnlooklocate.com/blog/"},
    {"date": "12 Aug, 2026", "title": "Red Devil Alternatives & Doxil", "img": f"{IMG}/2025/02/Header-image-Stage-4-Breast-Cancer.webp", "href": "https://learnlooklocate.com/blog/"},
    {"date": "07 Aug, 2026", "title": "Breast Reconstruction After Breast Cancer: Your Options, Your Sensation, Your Choice", "img": f"{IMG}/2025/11/Lumpectomy-18.png", "href": "https://learnlooklocate.com/blog/"},
    {"date": "03 Aug, 2026", "title": "The Red Devil and What Comes Next: Immunotherapy and the Road Ahead", "img": f"{IMG}/2024/04/banner-new.webp", "href": "https://learnlooklocate.com/blog/"},
    {"date": "31 Jul, 2026", "title": "Why Emotional Support Is a Vital Part of Metastatic Breast Cancer Care", "img": SPOTLIGHT_IMG, "href": "https://learnlooklocate.com/blog/"},
]

COPY = {
    "kicker": "Education • Discussions • Survivors • Doctors • Blogs • Breast Cancer Innovations",
    "hero_p": "Stay informed with the newest educational pages, global interviews, and inspiring survivor stories from Learn Look Locate — where compassion meets science. Our What’s New section showcases the latest medically vetted resources created with our trusted medical advisors, leading experts in oncology, surgery, radiology, pharmacy, and women’s health.",
    "mission": "Each new addition reflects our mission to empower people worldwide through trusted, inclusive breast cancer education. From early detection, dense breast screening, and genetic testing to treatment advances, emotional recovery, and survivorship — these updates are designed to bring clarity, confidence, and connection to every stage of the breast cancer journey.",
    "explore": "Explore newly launched pages, interviews, and blogs featuring breakthrough innovations, patient experiences, and global collaborations with leading organizations and physicians. Every story, discussion, and partnership brings us closer to transforming how the world learns about breast health and breast cancer — one trusted page at a time.",
    "fresh_h": "What’s New at Learn Look Locate — Fresh Voices, Breakthroughs, and Global Connections",
    "fresh_p1": "At Learn Look Locate, we’re always evolving to bring you the latest in trusted breast cancer education and heartfelt survivor connection. Our goal is to bridge medical expertise and emotional support, so you always feel seen, heard, and empowered.",
    "fresh_p2": "Whether you’re newly diagnosed, navigating treatment, or seeking the latest in breast cancer advances, Learn Look Locate sparks awareness, turns action into hope, and transforms hope into a global movement of support and strength.",
    "fresh_p3": "From newly launched web pages and inspiring survivor stories to the latest blogs and vital resources, this is where you’ll find everything new guided by top oncology experts and advocates around the world.",
    "fresh_p4": "Stay connected to the newest advances, personal stories, and life-changing resources that continue to drive our mission forward.",
    "spot_h": "Spotlight: Where Progress Meets Patients and Breakthroughs Move Forward",
    "spot_q": "“Shining a light on the innovations that are redefining breast cancer care and guiding patients on their journey.”",
    "spot_card_title": "Do All Women with DCIS Need Radiation?",
    "spot_card_ex": "What’s New If you’ve just been diagnosed with DCIS (ductal carcinoma in situ), you may be wondering whether radiation is always the next step. This spotlight walks through the latest, medically vetted guidance so you can ask clearer questions.",
    "united_h": "United to Empower and Educate",
    "united_p1": "Learn Look Locate and leading voices in breast health, driving our global mission to bring you clear, empowering guidance.",
    "united_p2": "Together, we’re sharing trusted knowledge and meaningful support to help you navigate your breast health journey with clarity and confidence",
    "edu_h": "New Medically Vetted Breast Cancer Education: Where Compassion Meets Science",
    "edu_p1": "We’re bringing new, medically vetted breast cancer education pages to the forefront every day — created in collaboration with trusted oncologists, surgeons, radiologists, pharmacists, and survivors who share our mission to educate and empower people worldwide. Each new page reflects the evolving landscape of breast cancer care, uniting medical expertise with the heartfelt voices of real survivors. From early detection and genetic testing to dense breast screening, diagnosis, and treatment innovations — every page is designed to meet you wherever you are on your journey.",
    "edu_p2": "You’ll find expert insights on chemotherapy and hair changes, breast imaging, pathology, surgery and reconstruction, hormone therapy, and survivorship — all written in patient-friendly language and reviewed by our medical advisors for accuracy and trust.",
    "edu_p3": "These pages represent more than information; they are living connections between patients and experts — building a compassionate, global community of understanding, one new page at a time.",
    "know_h": "Stay in the Know. Stay Empowered.",
    "quote": "“The best patient is an empowered patient.”",
    "quote_by": "— Dr. Yara Robertson, Breast Surgical Oncologist & Learn Look Locate Medical Advisor",
    "nl_h": "Get the Latest from Learn Look Locate",
    "nl_p": "Sign up to receive the latest medically guided education, expert insights, and meaningful updates from Learn Look Locate — delivered with clarity and care.",
    "docs_h": "Discussions with Doctors",
    "docs_q": "“Real Conversations. Trusted Experts. Deeper Answers.”",
    "docs_overview": "At Learn Look Locate, Discussions with Doctors is more than an interview series — it’s a global platform for education, compassion, and connection. As a breast cancer survivor and founder, I know how valuable it is to hear directly from trusted medical experts. That’s why every discussion is personally conducted by me with leading oncologists, surgeons, radiologists, pharmacists, and researchers. Together, we explore the latest in breast cancer detection, diagnosis, treatment, and survivorship in a way that’s clear, caring, and easy to understand.",
    "docs_why": "What makes this series different is its authenticity and accessibility. Each episode is medically vetted and globally accessible, so patients everywhere can feel informed and supported. We talk openly about dense breast screening, imaging, treatment side effects, new technologies, and life after cancer — giving you answers that truly matter. These conversations go beyond surface-level information. They are heartfelt exchanges designed to empower patients, build trust, and offer hope.",
    "docs_global": "Discussions with Doctors connects people worldwide with reliable, patient-friendly breast cancer education. Each episode strengthens the bridge between medical expertise and emotional understanding, helping viewers feel confident in their journey.",
    "surv_h": "Survivor Conversations",
    "surv_p1": "Explore the newest breast cancer education resources from Learn Look Locate — all medically vetted and created with our trusted oncologists, surgeons, radiologists, pharmacists, and survivors. Together, we’re bringing accurate, compassionate, and globally accessible information to everyone navigating breast health.",
    "surv_p2": "Each page blends trusted medical expertise with real survivor voices, offering guidance across every stage of the journey — from early detection, genetic testing, and dense breast screening to diagnosis, treatment innovations, and survivorship.",
    "surv_p3": "Find expert insights on chemotherapy and hair changes, breast imaging, pathology, surgery and reconstruction, hormone therapy, and recovery — all written in patient-friendly language and reviewed by medical professionals for accuracy and trust.",
    "surv_p4": "Powered by breast cancer survivor and founder Cynthia Jordan and a network of 22 Learn Look Locate medical advisors, these continually expanding resources reflect the evolving landscape of breast cancer care and our mission to deliver trusted, medically reviewed education to people worldwide.",
    "blog_h": "Latest Breast Cancer Blogs",
    "blog_sub": "Breakthroughs in Breast Care",
    "blog_p": "These are the newest blogs on Learn Look Locate — created to support you with the latest breast cancer research, expert insights, and survivor stories. Each post is medically vetted and written with compassion to help you navigate every stage of your breast cancer journey — from early detection and diagnosis to treatment, recovery, and life after cancer. Our goal is to keep you informed, empowered, and connected to the latest breakthroughs in breast cancer care and support.",
}

SWITCHER = """
<div class="design-switcher">
  <span>Review mockups:</span>
  <a href="index.html">Overview</a>
  <a href="version-a-editorial.html"{a}>A · Editorial</a>
  <a href="version-b-clinical.html"{b}>B · Clinical</a>
  <a href="version-c-warm.html"{c}>C · Warm</a>
</div>
"""


def switcher(active):
    return SWITCHER.format(
        a=' class="is-active"' if active == "a" else "",
        b=' class="is-active"' if active == "b" else "",
        c=' class="is-active"' if active == "c" else "",
    )


def cards(items, extra=""):
    html = []
    for i, it in enumerate(items):
        feat = " is-feature" if extra == "edu" and i == 0 else ""
        html.append(
            f'''
        <a class="card{feat}" href="{it["href"]}">
          <div class="card-media"><img src="{it["img"]}" alt=""></div>
          <div class="card-body">
            <time>{it["date"]}</time>
            <h3>{it["title"]}</h3>
            <span class="more">Read more</span>
          </div>
        </a>'''
        )
    return "\n".join(html)


def partners(layout="grid"):
    html = []
    for p in PARTNERS:
        html.append(
            f'''
        <a class="partner" href="{p["href"]}">
          <div class="partner-photo"><img src="{p["img"]}" alt=""></div>
          <div class="partner-meta">
            <img class="partner-logo" src="{p["logo"]}" alt="">
            <h3>{p["title"]}</h3>
          </div>
        </a>'''
        )
    return "\n".join(html)


COMMON_HEAD = """
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet">
<style>
{css}
</style>
"""

CSS_SHARED = """
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;color:var(--ink);background:var(--bg);font-family:var(--sans);line-height:1.65}
img{max-width:100%;display:block}
a{color:inherit}
.wrap{width:min(1180px,calc(100% - 40px));margin-inline:auto}
.design-switcher{position:sticky;top:0;z-index:50;display:flex;gap:10px;align-items:center;flex-wrap:wrap;
  padding:10px 18px;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);border-bottom:1px solid rgba(0,0,0,.08);font-size:13px}
.design-switcher a{padding:6px 10px;border-radius:999px;text-decoration:none;border:1px solid transparent}
.design-switcher a.is-active{background:var(--accent);color:#fff}
.skip{position:absolute;left:-999px}
.site-nav{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:18px 0}
.site-nav nav{display:flex;gap:18px;flex-wrap:wrap;font-size:13px;letter-spacing:.04em;text-transform:uppercase}
.site-nav nav a{text-decoration:none;opacity:.8}
.logo{font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:13px;text-decoration:none}
.btn{display:inline-flex;align-items:center;gap:8px;text-decoration:none;border-radius:999px;padding:14px 22px;font-weight:600}
.btn-primary{background:var(--accent);color:#fff}
.btn-ghost{border:1px solid currentColor}
.section{padding:72px 0}
.kicker{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);font-weight:700}
h1,h2,h3{line-height:1.2;margin:0 0 .5em}
.lead{font-size:1.08rem;max-width:62ch}
.card{text-decoration:none;display:flex;flex-direction:column;overflow:hidden;background:var(--card);color:var(--ink)}
.card-media{aspect-ratio:16/10;overflow:hidden}
.card-media img{width:100%;height:100%;object-fit:cover}
.card-body{padding:16px 18px 20px}
.card time{font-size:12px;letter-spacing:.08em;text-transform:uppercase;opacity:.65}
.card h3{font-size:1.05rem;margin:.35em 0 .6em}
.more{font-size:13px;font-weight:700;color:var(--accent)}
.grid-5{display:grid;grid-template-columns:repeat(5,1fr);gap:18px}
.grid-partners{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.partner{text-decoration:none;display:flex;flex-direction:column;background:var(--card);overflow:hidden}
.partner-photo{aspect-ratio:16/9;overflow:hidden}
.partner-photo img{width:100%;height:100%;object-fit:cover}
.partner-meta{padding:16px 18px 20px;display:flex;flex-direction:column;gap:10px}
.partner-logo{height:36px;width:auto;object-fit:contain;align-self:flex-start}
.partner h3{font-size:.95rem}
.form{display:flex;gap:8px;flex-wrap:wrap}
.form input{flex:1;min-width:220px;padding:14px 16px;border:1px solid #d8cfd3;border-radius:10px;font:inherit}
.form button{border:0;background:var(--accent);color:#fff;padding:14px 20px;border-radius:10px;font-weight:700;cursor:pointer}
.footer{padding:40px 0;font-size:13px;opacity:.7}
@media (max-width:980px){
  .grid-5{grid-template-columns:repeat(2,1fr)}
  .grid-partners{grid-template-columns:1fr 1fr}
}
@media (max-width:640px){
  .grid-5,.grid-partners{grid-template-columns:1fr}
  .site-nav nav{display:none}
}
"""

CSS_A = CSS_SHARED + """
:root{
  --bg:#f7f1ea; --ink:#2c1f24; --accent:#b44a66; --card:#fffdf9;
  --sans:"Source Sans 3",system-ui,sans-serif; --serif:"Libre Baskerville",Georgia,serif;
}
body{background:
  radial-gradient(1200px 500px at 10% -10%, #f3dfe4 0%, transparent 50%),
  var(--bg)}
h1,h2,.serif{font-family:var(--serif);font-weight:400}
.hero{padding:48px 0 80px}
.hero-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:48px;align-items:center}
.hero h1{font-size:clamp(2.4rem,5vw,4.4rem);letter-spacing:-.02em}
.hero h1 em{font-style:italic;color:var(--accent)}
.hero-photo{border-radius:28px 4px 28px 4px;overflow:hidden;min-height:420px}
.hero-photo img{width:100%;height:100%;object-fit:cover;min-height:420px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 22px}
.chips span{border:1px solid #e3d3d7;border-radius:999px;padding:6px 12px;font-size:12px;letter-spacing:.04em}
.rule{height:1px;background:#e5d6d0;margin:10px 0 28px}
.mission{columns:2;gap:36px}
.mission p{margin:0 0 1em;break-inside:avoid}
.spotlight{display:grid;grid-template-columns:.9fr 1.1fr;gap:40px;align-items:center}
.spotlight img{border-radius:4px 40px 4px 40px}
.quote-lg{font-family:var(--serif);font-size:1.45rem;font-style:italic;max-width:28ch}
.newsletter{display:grid;grid-template-columns:280px 1fr;gap:36px;align-items:center;background:#fff;padding:32px;border-radius:24px}
.newsletter img{width:220px;height:220px;object-fit:cover;border-radius:50%}
.split-copy{display:grid;grid-template-columns:1fr 1fr;gap:40px}
.docs-intro{border-left:3px solid var(--accent);padding-left:22px}
.card{border-radius:4px;box-shadow:0 10px 30px rgba(80,30,40,.06)}
.partner{border-radius:4px}
@media (max-width:900px){
  .hero-grid,.spotlight,.newsletter,.split-copy,.mission{grid-template-columns:1fr;columns:1}
}
"""

CSS_B = CSS_SHARED + """
:root{
  --bg:#f4f6fa; --ink:#162033; --accent:#c43b63; --card:#fff; --navy:#13203a;
  --sans:"DM Sans",system-ui,sans-serif; --serif:"Fraunces",Georgia,serif;
}
h1,h2{font-family:var(--serif)}
.hero{background:var(--navy);color:#f7f3f0;padding:0 0 72px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(19,32,58,.92) 32%, rgba(19,32,58,.45));}
.hero .wrap{position:relative;z-index:1}
.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero h1{font-size:clamp(2.6rem,6vw,5rem);max-width:14ch}
.hero .kicker{color:#f3b3c4}
.subnav{display:flex;gap:8px;flex-wrap:wrap;margin:28px 0 0}
.subnav a{color:#fff;text-decoration:none;border:1px solid rgba(255,255,255,.25);padding:8px 12px;border-radius:8px;font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.panel{background:#fff;border-radius:18px;padding:28px;margin-top:-48px;position:relative;z-index:2;box-shadow:0 20px 50px rgba(19,32,58,.12)}
.panel p{margin-top:0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.spotlight-b{display:grid;grid-template-columns:1.2fr .8fr;gap:0;background:var(--navy);color:#fff;border-radius:20px;overflow:hidden}
.spotlight-b .copy{padding:36px}
.spotlight-b img{height:100%;object-fit:cover;min-height:320px}
.card{border-radius:16px;border:1px solid #e6ebf2}
.card.is-feature{grid-column:span 2}
.partner{border-radius:16px;border:1px solid #e6ebf2}
.quote-bar{display:grid;grid-template-columns:auto 1fr;gap:24px;align-items:center;background:linear-gradient(135deg,#13203a,#3a1d33);color:#fff;padding:32px;border-radius:20px}
.quote-bar img{width:96px;height:96px;border-radius:50%;object-fit:cover;border:3px solid #c43b63}
.quote-bar blockquote{font-family:var(--serif);font-size:1.6rem;margin:0}
@media (max-width:900px){
  .two,.spotlight-b,.quote-bar{grid-template-columns:1fr}
  .card.is-feature{grid-column:span 1}
}
"""

CSS_C = CSS_SHARED + """
:root{
  --bg:#fff8f3; --ink:#3b2430; --accent:#d46a4c; --card:#fff; --plum:#5b2744;
  --sans:"Nunito",system-ui,sans-serif; --serif:"Playfair Display",Georgia,serif;
}
h1,h2,.serif{font-family:var(--serif)}
.hero{min-height:88vh;display:grid;place-items:end start;padding:40px 0 64px;position:relative;color:#fff}
.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(91,39,68,.15),rgba(91,39,68,.78))}
.hero .wrap{position:relative;z-index:1}
.hero h1{font-size:clamp(3rem,8vw,6.2rem);line-height:.95;max-width:12ch}
.ribbon{display:inline-block;background:var(--accent);color:#fff;padding:6px 14px;border-radius:999px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:800}
.band{background:#f3e4d8;border-radius:32px;padding:36px}
.overlap{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:-48px}
.overlap .card:first-child{transform:rotate(-1.2deg)}
.overlap .card:last-child{transform:rotate(1deg);margin-top:48px}
.spotlight-c{position:relative;border-radius:32px;overflow:hidden;min-height:460px;color:#fff}
.spotlight-c img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.spotlight-c .copy{position:relative;z-index:1;padding:48px;background:linear-gradient(90deg,rgba(59,36,48,.82),transparent);max-width:34rem}
.partners-c .partner{border-radius:24px;box-shadow:0 12px 30px rgba(91,39,68,.08)}
.yara{display:flex;gap:28px;align-items:center;background:var(--plum);color:#fff;padding:28px;border-radius:999px}
.yara img{width:120px;height:120px;border-radius:50%;object-fit:cover}
.yara blockquote{font-family:var(--serif);font-size:1.5rem;margin:0}
.card{border-radius:22px}
@media (max-width:800px){
  .overlap,.yara{grid-template-columns:1fr;display:grid;border-radius:28px}
  .overlap .card{transform:none;margin:0}
}
"""


def page_a():
    c = COPY
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD.format(title="What's New — Design A Editorial | Learn Look Locate", fonts="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600;700&display=swap", css=CSS_A)}
</head>
<body>
{switcher("a")}
<header class="wrap site-nav">
  <a class="logo" href="https://learnlooklocate.com/">Learn Look Locate</a>
  <nav>
    <a href="#spotlight">Spotlight</a>
    <a href="#partners">Partners</a>
    <a href="#education">Education</a>
    <a href="#doctors">Doctors</a>
    <a href="#survivors">Survivors</a>
    <a href="#blogs">Blogs</a>
  </nav>
</header>
<section class="hero wrap">
  <div class="hero-grid">
    <div>
      <p class="kicker">What's New in Breast Cancer</p>
      <h1>What's New <em>in breast cancer</em></h1>
      <div class="chips">{''.join(f'<span>{x.strip()}</span>' for x in c['kicker'].split('•'))}</div>
      <p class="lead">{c['hero_p']}</p>
      <p><a class="btn btn-primary" href="#education">Explore What’s New</a></p>
    </div>
    <div class="hero-photo"><img src="{HERO_BG}" alt="Learn Look Locate What's New"></div>
  </div>
</section>
<section class="wrap section" style="padding-top:0">
  <div class="rule"></div>
  <div class="mission">
    <p>{c['mission']}</p>
    <p>{c['explore']}</p>
  </div>
</section>
<section class="wrap section" style="padding-top:0">
  <h2 class="serif">{c['fresh_h']}</h2>
  <div class="split-copy">
    <div>
      <p>{c['fresh_p1']}</p>
      <p>{c['fresh_p2']}</p>
    </div>
    <div>
      <p>{c['fresh_p3']}</p>
      <p>{c['fresh_p4']}</p>
    </div>
  </div>
</section>
<section id="spotlight" class="wrap section">
  <div class="spotlight">
    <div>
      <p class="kicker">Spotlight</p>
      <h2>{c['spot_h']}</h2>
      <p class="quote-lg">{c['spot_q']}</p>
      <a class="card" href="https://learnlooklocate.com/do-i-need-radiation-if-i-have-dcis">
        <div class="card-body">
          <time>Featured</time>
          <h3>{c['spot_card_title']}</h3>
          <p>{c['spot_card_ex']}</p>
          <span class="more">Read more</span>
        </div>
      </a>
    </div>
    <img src="{SPOTLIGHT_IMG}" alt="">
  </div>
</section>
<section id="partners" class="wrap section">
  <p class="kicker">Collaborations</p>
  <h2>{c['united_h']}</h2>
  <p class="lead">{c['united_p1']} {c['united_p2']}</p>
  <div class="grid-partners" style="margin-top:28px">{partners()}</div>
</section>
<section id="education" class="wrap section">
  <p class="kicker">Education</p>
  <h2>{c['edu_h']}</h2>
  <p class="lead">{c['edu_p1']}</p>
  <p>{c['edu_p2']}</p>
  <p>{c['edu_p3']}</p>
  <p><a class="btn btn-ghost" href="https://learnlooklocate.com/educate/">Explore What’s New</a></p>
  <div class="grid-5" style="margin-top:28px">{cards(EDU)}</div>
</section>
<section class="wrap section">
  <div class="newsletter">
    <img src="{YARA}" alt="Dr. Yara Robertson">
    <div>
      <h2>{c['know_h']}</h2>
      <blockquote class="quote-lg">{c['quote']}</blockquote>
      <p>{c['quote_by']}</p>
      <h3>{c['nl_h']}</h3>
      <p>{c['nl_p']}</p>
      <form class="form" action="#" onsubmit="return false">
        <input type="email" placeholder="Email address" aria-label="Email">
        <button type="submit">Subscribe</button>
      </form>
    </div>
  </div>
</section>
<section id="doctors" class="wrap section">
  <p class="kicker">{c['docs_h']}</p>
  <h2>{c['docs_q']}</h2>
  <div class="docs-intro">
    <p><strong>Overview.</strong> {c['docs_overview']}</p>
    <p><strong>Why it matters.</strong> {c['docs_why']}</p>
    <p><strong>Global impact.</strong> {c['docs_global']}</p>
  </div>
  <p><a class="btn btn-primary" href="https://learnlooklocate.com/educate/patient-education/">Watch now</a></p>
  <div class="grid-5" style="margin-top:28px">{cards(DOCS)}</div>
</section>
<section id="survivors" class="wrap section">
  <p class="kicker">Survivors</p>
  <h2>{c['surv_h']}</h2>
  <p class="lead">{c['surv_p1']}</p>
  <p>{c['surv_p2']}</p>
  <p>{c['surv_p3']}</p>
  <p>{c['surv_p4']}</p>
  <p><a class="btn btn-ghost" href="https://learnlooklocate.com/survivor-stories/">Learn more</a></p>
  <div class="grid-5" style="margin-top:28px">{cards(SURV)}</div>
</section>
<section id="blogs" class="wrap section">
  <p class="kicker">{c['blog_h']}</p>
  <h2>{c['blog_sub']}</h2>
  <p class="lead">{c['blog_p']}</p>
  <p><a class="btn btn-ghost" href="https://learnlooklocate.com/blog/">Learn more</a></p>
  <div class="grid-5" style="margin-top:28px">{cards(BLOGS)}</div>
</section>
<footer class="wrap footer">Learn Look Locate · Design mockup A (Editorial Quiet). Content and images from the live What’s New page. Not yet implemented in Elementor.</footer>
</body></html>
"""


def page_b():
    c = COPY
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD.format(title="What's New — Design B Clinical | Learn Look Locate", fonts="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,700;1,9..144,500&display=swap", css=CSS_B)}
</head>
<body>
{switcher("b")}
<section class="hero">
  <img class="hero-bg" src="{HERO_BG2}" alt="">
  <div class="wrap" style="padding-top:28px">
    <div class="site-nav" style="color:#fff">
      <a class="logo" href="https://learnlooklocate.com/">Learn Look Locate</a>
      <nav>
        <a href="#spotlight">Spotlight</a>
        <a href="#partners">Partners</a>
        <a href="#education">Education</a>
        <a href="#doctors">Doctors</a>
        <a href="#survivors">Survivors</a>
        <a href="#blogs">Blogs</a>
      </nav>
    </div>
    <p class="kicker">What's New in Breast Cancer</p>
    <h1>What's New in Breast Cancer</h1>
    <p style="max-width:58ch;opacity:.92">{c['hero_p']}</p>
    <p><a class="btn btn-primary" href="#education">Explore What’s New</a></p>
    <div class="subnav">
      {''.join(f'<a href="#{id}">{label}</a>' for id,label in [('spotlight','Spotlight'),('partners','Partners'),('education','Education'),('doctors','Doctors'),('survivors','Survivors'),('blogs','Blogs')])}
    </div>
  </div>
</section>
<div class="wrap"><div class="panel"><p>{c['kicker']}</p><p>{c['mission']}</p><p>{c['explore']}</p></div></div>
<section class="wrap section">
  <div class="two">
    <div>
      <h2>{c['fresh_h']}</h2>
      <p>{c['fresh_p1']}</p>
      <p>{c['fresh_p2']}</p>
    </div>
    <div>
      <p>{c['fresh_p3']}</p>
      <p>{c['fresh_p4']}</p>
    </div>
  </div>
</section>
<section id="spotlight" class="wrap section" style="padding-top:0">
  <div class="spotlight-b">
    <div class="copy">
      <p class="kicker">Spotlight</p>
      <h2>{c['spot_h']}</h2>
      <p>{c['spot_q']}</p>
      <h3>{c['spot_card_title']}</h3>
      <p>{c['spot_card_ex']}</p>
      <a class="btn btn-primary" href="https://learnlooklocate.com/do-i-need-radiation-if-i-have-dcis">Read the spotlight</a>
    </div>
    <img src="{SPOTLIGHT_IMG}" alt="">
  </div>
</section>
<section id="partners" class="wrap section">
  <h2>{c['united_h']}</h2>
  <p class="lead">{c['united_p1']} {c['united_p2']}</p>
  <div class="grid-partners" style="margin-top:24px">{partners()}</div>
</section>
<section id="education" class="wrap section">
  <h2>{c['edu_h']}</h2>
  <p>{c['edu_p1']}</p>
  <p>{c['edu_p2']}</p>
  <p>{c['edu_p3']}</p>
  <p><a class="btn btn-primary" href="https://learnlooklocate.com/educate/">Explore What’s New</a></p>
  <div class="grid-5" style="margin-top:24px">{cards(EDU,'edu')}</div>
</section>
<section class="wrap section">
  <div class="quote-bar">
    <img src="{YARA}" alt="Dr. Yara Robertson">
    <div>
      <h2 style="color:#fff">{c['know_h']}</h2>
      <blockquote>{c['quote']}</blockquote>
      <p>{c['quote_by']}</p>
      <p>{c['nl_p']}</p>
      <form class="form" onsubmit="return false">
        <input type="email" placeholder="Email address" aria-label="Email">
        <button type="submit">Get the latest</button>
      </form>
    </div>
  </div>
</section>
<section id="doctors" class="wrap section">
  <p class="kicker">{c['docs_h']}</p>
  <h2>{c['docs_q']}</h2>
  <div class="two">
    <p><strong>Overview.</strong> {c['docs_overview']}</p>
    <div>
      <p><strong>Why it matters.</strong> {c['docs_why']}</p>
      <p><strong>Global impact.</strong> {c['docs_global']}</p>
      <p><a class="btn btn-primary" href="https://learnlooklocate.com/educate/patient-education/">Watch now</a></p>
    </div>
  </div>
  <div class="grid-5" style="margin-top:24px">{cards(DOCS)}</div>
</section>
<section id="survivors" class="wrap section">
  <h2>{c['surv_h']}</h2>
  <p>{c['surv_p1']}</p>
  <p>{c['surv_p2']}</p>
  <p>{c['surv_p3']}</p>
  <p>{c['surv_p4']}</p>
  <p><a class="btn btn-ghost" href="https://learnlooklocate.com/survivor-stories/">Learn more</a></p>
  <div class="grid-5" style="margin-top:24px">{cards(SURV)}</div>
</section>
<section id="blogs" class="wrap section">
  <h2>{c['blog_h']}</h2>
  <p class="kicker">{c['blog_sub']}</p>
  <p>{c['blog_p']}</p>
  <p><a class="btn btn-ghost" href="https://learnlooklocate.com/blog/">Learn more</a></p>
  <div class="grid-5" style="margin-top:24px">{cards(BLOGS)}</div>
</section>
<footer class="wrap footer">Learn Look Locate · Design mockup B (Clinical Clarity). Same content and images as the live page.</footer>
</body></html>
"""


def page_c():
    c = COPY
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{COMMON_HEAD.format(title="What's New — Design C Warm | Learn Look Locate", fonts="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap", css=CSS_C)}
</head>
<body>
{switcher("c")}
<section class="hero">
  <img class="hero-bg" src="{HERO_BG}" alt="">
  <div class="wrap">
    <p class="ribbon">What's New</p>
    <h1>What's New in Breast Cancer</h1>
    <p style="max-width:48ch">{c['kicker']}</p>
    <p style="max-width:56ch">{c['hero_p']}</p>
    <p><a class="btn btn-primary" href="#education">Explore What’s New</a></p>
  </div>
</section>
<section class="wrap section">
  <div class="band">
    <p>{c['mission']}</p>
    <p>{c['explore']}</p>
  </div>
  <div class="overlap">
    <article class="card" style="padding:28px">
      <h2>{c['fresh_h']}</h2>
      <p>{c['fresh_p1']}</p>
      <p>{c['fresh_p2']}</p>
    </article>
    <article class="card" style="padding:28px">
      <p>{c['fresh_p3']}</p>
      <p>{c['fresh_p4']}</p>
    </article>
  </div>
</section>
<section id="spotlight" class="wrap section">
  <div class="spotlight-c">
    <img src="{SPOTLIGHT_IMG}" alt="">
    <div class="copy">
      <p class="ribbon">Spotlight</p>
      <h2>{c['spot_h']}</h2>
      <p>{c['spot_q']}</p>
      <h3>{c['spot_card_title']}</h3>
      <p>{c['spot_card_ex']}</p>
      <a class="btn btn-primary" href="https://learnlooklocate.com/do-i-need-radiation-if-i-have-dcis">Read more</a>
    </div>
  </div>
</section>
<section id="partners" class="wrap section partners-c">
  <h2>{c['united_h']}</h2>
  <p class="lead">{c['united_p1']}<br>{c['united_p2']}</p>
  <div class="grid-partners" style="margin-top:24px">{partners()}</div>
</section>
<section id="education" class="wrap section">
  <p class="ribbon">Education</p>
  <h2>{c['edu_h']}</h2>
  <p>{c['edu_p1']}</p>
  <p>{c['edu_p2']}</p>
  <p>{c['edu_p3']}</p>
  <p><a class="btn btn-primary" href="https://learnlooklocate.com/educate/">Explore What’s New</a></p>
  <div class="grid-5" style="margin-top:24px">{cards(EDU)}</div>
</section>
<section class="wrap section">
  <div class="yara">
    <img src="{YARA}" alt="Dr. Yara Robertson">
    <div>
      <h2 style="color:#fff">{c['know_h']}</h2>
      <blockquote>{c['quote']}</blockquote>
      <p>{c['quote_by']}</p>
    </div>
  </div>
  <div class="band" style="margin-top:22px">
    <h3>{c['nl_h']}</h3>
    <p>{c['nl_p']}</p>
    <form class="form" onsubmit="return false">
      <input type="email" placeholder="Email address" aria-label="Email">
      <button type="submit">Subscribe</button>
    </form>
  </div>
</section>
<section id="doctors" class="wrap section">
  <p class="ribbon">{c['docs_h']}</p>
  <h2>{c['docs_q']}</h2>
  <p>{c['docs_overview']}</p>
  <p>{c['docs_why']}</p>
  <p>{c['docs_global']}</p>
  <p><a class="btn btn-primary" href="https://learnlooklocate.com/educate/patient-education/">Watch now</a></p>
  <div class="grid-5" style="margin-top:24px">{cards(DOCS)}</div>
</section>
<section id="survivors" class="wrap section">
  <p class="ribbon">Survivors</p>
  <h2>{c['surv_h']}</h2>
  <p>{c['surv_p1']}</p>
  <p>{c['surv_p2']}</p>
  <p>{c['surv_p3']}</p>
  <p>{c['surv_p4']}</p>
  <p><a class="btn btn-ghost" href="https://learnlooklocate.com/survivor-stories/">Learn more</a></p>
  <div class="grid-5" style="margin-top:24px">{cards(SURV)}</div>
</section>
<section id="blogs" class="wrap section">
  <p class="ribbon">{c['blog_h']}</p>
  <h2>{c['blog_sub']}</h2>
  <p>{c['blog_p']}</p>
  <p><a class="btn btn-ghost" href="https://learnlooklocate.com/blog/">Learn more</a></p>
  <div class="grid-5" style="margin-top:24px">{cards(BLOGS)}</div>
</section>
<footer class="wrap footer">Learn Look Locate · Design mockup C (Warm Connection). Same content and images as the live page.</footer>
</body></html>
"""


INDEX = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>What's New page — design versions</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Fraunces:opsz,wght@9..144,600&display=swap" rel="stylesheet">
<style>
body{{margin:0;font-family:"DM Sans",system-ui,sans-serif;background:#f6f3ef;color:#241c20;line-height:1.6}}
.wrap{{width:min(1080px,calc(100% - 40px));margin:48px auto 80px}}
h1{{font-family:Fraunces,Georgia,serif;font-size:clamp(2rem,4vw,3.2rem);line-height:1.15}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:32px}}
a.opt{{display:block;background:#fff;border-radius:18px;overflow:hidden;text-decoration:none;color:inherit;box-shadow:0 12px 30px rgba(0,0,0,.06)}}
.swatch{{height:160px}}
.a{{background:linear-gradient(135deg,#f7f1ea,#b44a66)}}
.b{{background:linear-gradient(135deg,#13203a,#c43b63)}}
.c{{background:linear-gradient(135deg,#5b2744,#d46a4c)}}
.opt div{{padding:18px 20px 22px}}
.opt h2{{margin:0 0 8px;font-size:1.2rem}}
.note{{background:#fff;border-radius:16px;padding:20px 24px;margin-top:28px}}
@media(max-width:800px){{.grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<div class="wrap">
  <p style="letter-spacing:.16em;text-transform:uppercase;font-size:12px;font-weight:700;color:#b44a66">Learn Look Locate · client review</p>
  <h1>Three section redesigns for What’s New in Breast Cancer Education</h1>
  <p>These mockups keep the live page copy, partner stories, newsletter quote, and images. Only layout, type, color, and section rhythm change. Open a version, scroll the full page, then reply with A, B, C, or a mix (for example: “B hero + C partners”). After you confirm, we can rebuild it in Elementor.</p>
  <div class="grid">
    <a class="opt" href="version-a-editorial.html"><div class="swatch a"></div><div><h2>A · Editorial Quiet</h2><p>Magazine layout: serif headlines, cream paper, two-column essays, rounded photo crop. Calm and literary.</p></div></a>
    <a class="opt" href="version-b-clinical.html"><div class="swatch b"></div><div><h2>B · Clinical Clarity</h2><p>Navy hero, sticky section chips, high-contrast cards, featured education tile. Feels like a trusted medical resource.</p></div></a>
    <a class="opt" href="version-c-warm.html"><div class="swatch c"></div><div><h2>C · Warm Connection</h2><p>Full-bleed photo hero, overlapping story cards, pill ribbons, circular portrait quote. Community-forward.</p></div></a>
  </div>
  <div class="note">
    <strong>Unchanged on purpose:</strong> hero copy, mission paragraphs, Spotlight DCIS story, seven partner/education tiles (Tumor Localization, Walgreens, Genomic Testing, Stage 4, Lumpectomy, DCIS radiation, ctDNA recurrence), Dr. Yara Robertson quote, ConvertKit signup, Discussions / Survivors / Blogs sections and their post titles.
    <br><br>
    <strong>Live reference:</strong> <a href="https://learnlooklocate.com/whats-new-breast-cancer-education/">learnlooklocate.com/whats-new-breast-cancer-education</a>
  </div>
</div>
</body>
</html>
"""


def main():
    from pathlib import Path
    root = Path(__file__).parent
    (root / "index.html").write_text(INDEX, encoding="utf-8")
    (root / "version-a-editorial.html").write_text(page_a(), encoding="utf-8")
    (root / "version-b-clinical.html").write_text(page_b(), encoding="utf-8")
    (root / "version-c-warm.html").write_text(page_c(), encoding="utf-8")
    print("wrote", root)


if __name__ == "__main__":
    main()
