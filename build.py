"""Writes index.html (English) and tr/index.html (Turkish) from the content below.

    python3 build.py

Standard library only. Edit the text in PAGES, run the script and commit the result.
"""

from pathlib import Path

SITE = "https://musabeytekin.github.io/"
SITE_SOURCE = "https://github.com/musabeytekin/musabeytekin.github.io"
EMAIL = "musabeytekin867@gmail.com"
GITHUB = "https://github.com/musabeytekin"
LINKEDIN = "https://www.linkedin.com/in/musabeytekin"
EXRADIUS = "https://github.com/musabeytekin/exradius"
TREE = EXRADIUS + "/tree/main/"
DOCS = EXRADIUS + "/blob/main/docs/architecture.md"
SMART_HOME = "https://github.com/musabeytekin/smart-home-controller-ai"
FONTS = (
    "https://fonts.googleapis.com/css2"
    "?family=Newsreader:opsz,wght@6..72,400..500"
    "&family=Instrument+Sans:wght@400..600&display=swap"
)
MODELS = (
    "gemma3:4b, gemma2:9b, llama2:7b, llama3.1:8b, mistral:7b, qwen2.5:7b, "
    "granite3.3:8b, olmo2:7b, olmo-3:7b, gpt-oss:20b"
)


def link(href, text):
    return f'<a href="{href}">{text}</a>'


PAGES = {
    "en": {
        "path": "index.html",
        "root": "",
        "url": SITE,
        "languages": [("en", "English", ""), ("tr", "Türkçe", "tr/")],
        "languages_label": "Language",
        "title": "Musa Beytekin, AI engineer",
        "description": (
            "AI engineer building LLM agent systems, their evaluation and the backend they run on. "
            "Author of Exradius, an open-source platform that runs AI agents in isolated Kubernetes pods."
        ),
        "job_title": "AI Engineer",
        "skip": "Skip to content",
        "place": "AI engineer, Türkiye",
        "lead": "I build LLM agent systems, the evaluation around them, and the backend they run on.",
        "summary": (
            f"I designed and built {link('#exradius', 'Exradius')}, an open-source platform that runs "
            "AI agents in isolated environments on Kubernetes. For my "
            f"{link('#thesis', 'MSc thesis')} I compared 10 open-weight LLMs on speed, reliability, "
            "linguistic quality and emotion scoring. At Turkish Airlines I work on reservation "
            "systems that process about 1,000 records per second."
        ),
        "cv_href": "cv/Musa_Beytekin_CV_EN.pdf",
        "cv_label": "Download CV (PDF)",
        "email_label": "Email",
        "exradius_h": "Open source",
        "exradius_note": "A self-hosted platform for running AI agents. Apache-2.0.",
        "exradius": [
            "Exradius runs AI agents on a company's own code. Every task gets its own locked-down "
            "Kubernetes pod. The agent works there, asks a person when it needs to, and delivers "
            "a branch or a patch.",
            "I designed and built all of it. The "
            f"{link(EXRADIUS, 'source')} and the {link(DOCS, 'design notes')} are on GitHub.",
        ],
        "run_title": "One run, start to finish",
        "run": [
            ("", "A task arrives",
             "A message on a RabbitMQ queue names a project and an agent. Bridges for Jira and GitHub put it there."),
            ("", "The config is read",
             "The worker reads the project's <code>exradius.yaml</code> from its git repository and creates a Run."),
            ("", "A pod starts",
             "An operator builds one pod for the run: non-root, read-only filesystem, no capabilities, "
             "no cluster credentials."),
            ("", "The agent works",
             "The runner drives it through the Claude Agent SDK. Its traffic passes an egress proxy "
             "that allows only listed hosts."),
            ("person", "A person answers",
             "The agent can ask a question through an MCP tool. Once someone answers, the session "
             "resumes in the same pod."),
            ("", "The result goes out",
             "The agent pushes a branch or attaches a patch. Status and the result are published as events."),
        ],
        "built_title": "What I built",
        "built": [
            ("API and worker", "backend",
             "Python, FastAPI, PostgreSQL and RabbitMQ. Every state change is stored with its event "
             "in one transaction and published after commit."),
            ("Operator", "operator",
             "Go and controller-runtime, with custom resources for runs and image builds."),
            ("Egress proxy", "egress",
             "Go, standard library only. It adds the model key and repository credentials on the way "
             "out, so no pod ever holds them."),
            ("Runner", "backend/exradius/runner",
             "Drives the agent through the Claude Agent SDK and hosts an MCP server: ask a person, "
             "submit the result, attach files."),
            ("Admin panel", "frontend", "React and TypeScript."),
            ("Install", "charts/exradius",
             f"A Helm chart, and {link(TREE + 'deploy/terraform', 'Terraform modules')} for AWS (EKS), "
             "GCP (GKE) and Azure (AKS)."),
            ("Secret stores", "backend/exradius/secret_backends",
             "Kept encrypted in PostgreSQL or read from HashiCorp Vault."),
            ("Setup skill", "skill",
             "A Claude Code skill that reads a codebase and sets it up for Exradius."),
            ("Evaluation set", "evals",
             "Real upstream bug fixes for measuring agents. In progress."),
        ],
        "thesis_h": "Research",
        "thesis_title": "Which local LLM fits which chat character?",
        "thesis_note": (
            "MSc thesis, İnönü University, 2026. Official title: Communication Between Interactive "
            "Virtual Characters with an AI-Supported Language Learning Application."
        ),
        "thesis": [
            "Language learners chat with AI characters in the app the thesis proposes: a conversation "
            "partner, a language teacher, an emotional-support companion. I investigated which local "
            "model is a candidate for each role.",
            "I ran 10 open-weight LLMs (4B to 20B parameters) on the same hardware with Ollama and "
            "compared them on four groups of measures: response speed, reliability, linguistic "
            "quality and emotion scoring. I also profiled how each model scores 27 emotions on the "
            "GoEmotions, SST-2 and TweetEval datasets.",
        ],
        "results_title": "Best result in each speed measure",
        "results": [
            ("Time to first token", "233 ms, llama2:7b"),
            ("Total response time", "2.0 s, olmo2:7b"),
            ("Generation speed", "94 tokens per second, gemma3:4b"),
        ],
        "models_label": "Models",
        "side_h": "Side project",
        "side_title": "Smart Home Controller AI",
        "side_note": "A multi-agent system in Python and LangChain.",
        "side": (
            "A coordinator agent reads a natural-language command such as “turn on the kitchen "
            "lights and set the temperature to 22 degrees” and routes each part to a specialist "
            "agent for lighting or climate. Only the agents a command needs are called, which "
            "keeps token cost low. The "
            f"{link(SMART_HOME, 'source')} is on GitHub."
        ),
        "experience_h": "Experience",
        "jobs": [
            ("Turkish Airlines", "Software Engineer, remote", "May 2026 – present", [
                "Develop Java and Spring Boot microservices for airline reservation systems that "
                "process about 1,000 reservation records per second.",
                "Added agent registration and permission features to the reservation and "
                "sales-agent management systems.",
                "Diagnose and resolve production issues across interconnected backend services.",
                "Work with Oracle and Couchbase in the data layer, and contribute to testing and code reviews.",
            ]),
            ("ID3", "Software Engineer, remote", "May 2024 – May 2026", [
                "Co-developed a multi-node reservation system (Java, Spring Boot, Oracle, event-driven architecture).",
                "Co-developed a planner that assigns airport tasks automatically.",
                "Wrote unit and integration tests with JUnit. Applications were deployed on "
                "Red Hat OpenShift with Jenkins.",
                "Started as an intern, moved to a full-time role after three months and was "
                "promoted to Software Engineer twelve months later.",
            ]),
        ],
        "skills_h": "Skills",
        "skills": [
            ("AI and LLM", "AI agents, multi-agent workflows, LLM evaluation, Claude Agent SDK, MCP, "
                           "LangChain, Ollama, OpenAI API, Claude Code"),
            ("Languages", "Python, Java, Go, TypeScript"),
            ("Backend", "FastAPI, Spring Boot, microservices, event-driven architecture, RabbitMQ, JUnit"),
            ("Infrastructure", "Kubernetes, Docker, Helm, Terraform, OpenShift, Jenkins"),
            ("Databases", "PostgreSQL, Oracle, Couchbase"),
        ],
        "education_h": "Education",
        "education": [
            ("MSc, Software Engineering", "İnönü University, 2024 – 2026. Thesis completed, "
                                          "defense pending; expected graduation December 2026."),
            ("BSc, Computer Engineering", "İnönü University, 2019 – 2023."),
            ("Spoken languages", "Turkish (native), English (B1)."),
        ],
        "contact_h": "Contact",
        "contact": "Email is the quickest way to reach me.",
        "footer": f"Musa Beytekin, 2026. The {link(SITE_SOURCE, 'source of this site')} is on GitHub.",
    },
    "tr": {
        "path": "tr/index.html",
        "root": "../",
        "url": SITE + "tr/",
        "languages": [("en", "English", "../"), ("tr", "Türkçe", "")],
        "languages_label": "Dil",
        "title": "Musa Beytekin, AI mühendisi",
        "description": (
            "LLM agent sistemleri kuran, değerlendiren ve altındaki backend'i yazan AI mühendisi. "
            "AI agent'larını izole Kubernetes pod'larında çalıştıran açık kaynak platform Exradius'un geliştiricisi."
        ),
        "job_title": "AI Mühendisi",
        "skip": "İçeriğe geç",
        "place": "AI mühendisi, Türkiye",
        "lead": "LLM agent sistemleri kuruyor, onları değerlendiriyor ve altındaki backend'i yazıyorum.",
        "summary": (
            "AI agent'larını Kubernetes üzerinde izole ortamlarda çalıştıran açık kaynak platform "
            f"{link('#exradius', 'Exradius')}'u tasarlayıp geliştirdim. "
            f"{link('#thesis', 'Yüksek lisans tezimde')} 10 açık ağırlıklı LLM'i hız, güvenilirlik, "
            "dilsel kalite ve duygu puanlama açısından karşılaştırdım. Türk Hava Yolları'nda saniyede "
            "yaklaşık 1.000 kayıt işleyen rezervasyon sistemlerinde çalışıyorum."
        ),
        "cv_href": "../cv/Musa_Beytekin_CV_TR.pdf",
        "cv_label": "CV'yi indir (PDF)",
        "email_label": "E-posta",
        "exradius_h": "Açık kaynak",
        "exradius_note": "AI agent'larını çalıştıran self-hosted platform. Apache-2.0.",
        "exradius": [
            "Exradius, AI agent'larını bir şirketin kendi kodu üzerinde çalıştırır. Her görev kendi "
            "sıkılaştırılmış Kubernetes pod'unda çalışır. Agent işini orada yapar, gerektiğinde bir "
            "insana sorar ve sonunda bir branch ya da patch teslim eder.",
            "Tamamını ben tasarlayıp geliştirdim. "
            f"{link(EXRADIUS, 'Kaynak kod')} ve {link(DOCS, 'tasarım notları')} GitHub'da.",
        ],
        "run_title": "Bir çalıştırma, baştan sona",
        "run": [
            ("", "Görev gelir",
             "RabbitMQ kuyruğuna düşen mesaj bir proje ve bir agent adı taşır. Mesajı Jira ve GitHub "
             "bridge'leri gönderir."),
            ("", "Config okunur",
             "Worker projenin git deposundaki <code>exradius.yaml</code> dosyasını okur ve bir Run oluşturur."),
            ("", "Pod açılır",
             "Operator çalıştırma için tek bir pod kurar: root'suz, salt okunur dosya sistemi, "
             "capability yok, cluster yetkisi yok."),
            ("", "Agent çalışır",
             "Runner agent'ı Claude Agent SDK üzerinden yürütür. Trafiği, yalnızca izinli adreslere "
             "açılan bir egress proxy'den geçer."),
            ("person", "İnsan yanıtlar",
             "Agent bir MCP aracıyla soru sorabilir. Yanıt gelince oturum aynı pod'da kaldığı yerden sürer."),
            ("", "Sonuç çıkar",
             "Agent bir branch push eder ya da patch ekler. Durum ve sonuç, olay olarak yayınlanır."),
        ],
        "built_title": "Neler geliştirdim",
        "built": [
            ("API ve worker", "backend",
             "Python, FastAPI, PostgreSQL ve RabbitMQ. Her durum değişikliği olayıyla birlikte tek "
             "transaction'da saklanır ve commit'ten sonra yayınlanır."),
            ("Operator", "operator",
             "Go ve controller-runtime; çalıştırmalar ve imaj build'leri için custom resource'lar."),
            ("Egress proxy", "egress",
             "Go, yalnızca standart kütüphane. Model anahtarını ve depo kimlik bilgilerini isteğe "
             "çıkışta ekler, böylece hiçbir pod bunları tutmaz."),
            ("Runner", "backend/exradius/runner",
             "Agent'ı Claude Agent SDK üzerinden yürütür ve bir MCP sunucusu barındırır: insana soru "
             "sorma, sonuç teslimi, dosya ekleri."),
            ("Yönetim paneli", "frontend", "React ve TypeScript."),
            ("Kurulum", "charts/exradius",
             f"Helm chart ve AWS (EKS), GCP (GKE), Azure (AKS) için "
             f"{link(TREE + 'deploy/terraform', 'Terraform modülleri')}."),
            ("Secret store'lar", "backend/exradius/secret_backends",
             "PostgreSQL'de şifreli tutulur ya da HashiCorp Vault'tan okunur."),
            ("Kurulum skill'i", "skill",
             "Bir kod tabanını okuyup Exradius'a kuran Claude Code skill'i."),
            ("Değerlendirme seti", "evals",
             "Agent'ları ölçmek için gerçek upstream hata düzeltmeleri. Devam ediyor."),
        ],
        "thesis_h": "Araştırma",
        "thesis_title": "Hangi yerel LLM hangi sohbet karakterine uygun?",
        "thesis_note": (
            "Yüksek lisans tezi, İnönü Üniversitesi, 2026. Resmî başlık: Yapay Zeka Destekli Dil "
            "Öğrenme Uygulaması ile Etkileşimli Sanal Karakterler Arası İletişim."
        ),
        "thesis": [
            "Tezin önerdiği uygulamada dil öğrenenler AI karakterlerle mesajlaşıyor: sohbet arkadaşı, "
            "dil öğretmeni, duygusal destek. Her role hangi yerel modelin aday olduğunu araştırdım.",
            "10 açık ağırlıklı LLM'i (4B ile 20B parametre arası) Ollama ile aynı donanımda çalıştırıp "
            "dört ölçüt grubunda karşılaştırdım: yanıt hızı, güvenilirlik, dilsel kalite ve duygu "
            "puanlama. Ayrıca GoEmotions, SST-2 ve TweetEval veri setlerinde her modelin 27 duyguyu "
            "nasıl puanladığını çıkardım.",
        ],
        "results_title": "Hız ölçütlerinde en iyi sonuçlar",
        "results": [
            ("İlk token'a ulaşma", "233 ms, llama2:7b"),
            ("Toplam yanıt süresi", "2,0 s, olmo2:7b"),
            ("Üretim hızı", "saniyede 94 token, gemma3:4b"),
        ],
        "models_label": "Modeller",
        "side_h": "Yan proje",
        "side_title": "Smart Home Controller AI",
        "side_note": "Python ve LangChain ile çoklu agent sistemi.",
        "side": (
            "Koordinatör agent “mutfak ışıklarını aç ve sıcaklığı 22 dereceye ayarla” gibi doğal dil "
            "komutunu okur ve her parçayı aydınlatma ya da iklimlendirme için uzman agent'a yönlendirir. "
            "Yalnızca komutun gerektirdiği agent'lar çağrıldığı için token maliyeti düşük kalır. "
            f"{link(SMART_HOME, 'Kaynak kod')} GitHub'da."
        ),
        "experience_h": "Deneyim",
        "jobs": [
            ("Türk Hava Yolları", "Yazılım Mühendisi, uzaktan", "Mayıs 2026 – bugün", [
                "Saniyede yaklaşık 1.000 rezervasyon kaydı işleyen havayolu rezervasyon sistemlerinin "
                "Java ve Spring Boot mikroservislerini geliştiriyorum.",
                "Rezervasyon ve satış acentesi yönetim sistemlerine acente kaydı ve yetkilendirme "
                "özellikleri ekledim.",
                "Birbirine bağlı backend servislerinde üretim hatalarını teşhis edip gideriyorum.",
                "Veri katmanında Oracle ve Couchbase kullanıyor, test yazımı ve code review "
                "süreçlerine katkı veriyorum.",
            ]),
            ("ID3", "Yazılım Mühendisi, uzaktan", "Mayıs 2024 – Mayıs 2026", [
                "Çok node'lu bir rezervasyon sistemini ekiple birlikte geliştirdim (Java, Spring Boot, "
                "Oracle, olay güdümlü mimari).",
                "Havalimanı görevlerini otomatik atayan planlayıcıyı ekiple birlikte geliştirdim.",
                "JUnit ile birim ve entegrasyon testleri yazdım. Uygulamalar Red Hat OpenShift "
                "üzerinde Jenkins ile dağıtılıyordu.",
                "Stajyer olarak başladım, üç ay sonra tam zamanlı kadroya geçtim, on iki ay sonra "
                "Yazılım Mühendisi unvanına terfi ettim.",
            ]),
        ],
        "skills_h": "Yetenekler",
        "skills": [
            ("AI ve LLM", "AI agent'lar, çoklu agent iş akışları, LLM değerlendirme, Claude Agent SDK, "
                          "MCP, LangChain, Ollama, OpenAI API, Claude Code"),
            ("Programlama dilleri", "Python, Java, Go, TypeScript"),
            ("Backend", "FastAPI, Spring Boot, mikroservisler, olay güdümlü mimari, RabbitMQ, JUnit"),
            ("Altyapı", "Kubernetes, Docker, Helm, Terraform, OpenShift, Jenkins"),
            ("Veritabanı", "PostgreSQL, Oracle, Couchbase"),
        ],
        "education_h": "Eğitim",
        "education": [
            ("Yüksek Lisans, Yazılım Mühendisliği", "İnönü Üniversitesi, 2024 – 2026. Tez tamamlandı, "
                                                    "savunma aşamasında; beklenen mezuniyet Aralık 2026."),
            ("Lisans, Bilgisayar Mühendisliği", "İnönü Üniversitesi, 2019 – 2023."),
            ("Diller", "Türkçe (ana dil), İngilizce (B1)."),
        ],
        "contact_h": "İletişim",
        "contact": "Bana en hızlı e-postayla ulaşabilirsiniz.",
        "footer": f"Musa Beytekin, 2026. {link(SITE_SOURCE, 'Bu sitenin kaynak kodu')} GitHub'da.",
    },
}


def rows(pairs, indent):
    pad = " " * indent
    return "\n".join(f"{pad}<dt>{name}</dt>\n{pad}<dd>{value}</dd>" for name, value in pairs)


def page(lang, t):
    root = t["root"]
    languages = "\n".join(
        f'      <span aria-current="true" lang="{code}">{name}</span>'
        if code == lang
        else f'      <a href="{href}" lang="{code}" hreflang="{code}">{name}</a>'
        for code, name, href in t["languages"]
    )
    exradius = "\n".join(f"        <p>{line}</p>" for line in t["exradius"])
    run = "\n".join(
        "          <li"
        + (f' class="{kind}"' if kind else "")
        + f' style="--i: {i}"><strong>{title}</strong><span>{text}</span></li>'
        for i, (kind, title, text) in enumerate(t["run"])
    )
    built = rows([(link(TREE + path, name), text) for name, path, text in t["built"]], 10)
    thesis = "\n".join(f"        <p>{line}</p>" for line in t["thesis"])
    jobs = "\n".join(
        f"""        <article class="entry">
          <div class="entry-head">
            <h3>{company}</h3>
            <p class="when">{when}</p>
          </div>
          <p class="note">{role}</p>
          <ul class="points">
"""
        + "\n".join(f"            <li>{point}</li>" for point in points)
        + """
          </ul>
        </article>"""
        for company, role, when, points in t["jobs"]
    )
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t["title"]}</title>
  <meta name="description" content="{t["description"]}">
  <meta name="author" content="Musa Beytekin">
  <link rel="canonical" href="{t["url"]}">
  <link rel="alternate" hreflang="en" href="{SITE}">
  <link rel="alternate" hreflang="tr" href="{SITE}tr/">
  <link rel="alternate" hreflang="x-default" href="{SITE}">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{t["title"]}">
  <meta property="og:description" content="{t["description"]}">
  <meta property="og:url" content="{t["url"]}">
  <meta property="og:image" content="{SITE}assets/og.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#fdfdfc" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#131312" media="(prefers-color-scheme: dark)">
  <link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="{FONTS}">
  <link rel="stylesheet" href="{root}assets/site.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Musa Beytekin",
    "jobTitle": "{t["job_title"]}",
    "url": "{t["url"]}",
    "email": "mailto:{EMAIL}",
    "sameAs": ["{GITHUB}", "{LINKEDIN}"],
    "alumniOf": {{"@type": "CollegeOrUniversity", "name": "İnönü University"}},
    "address": {{"@type": "PostalAddress", "addressCountry": "TR"}}
  }}
  </script>
</head>
<body>
  <a class="skip" href="#main">{t["skip"]}</a>

  <header class="wrap">
    <nav class="top" aria-label="{t["languages_label"]}">
{languages}
    </nav>
  </header>

  <main id="main">
    <section class="hero wrap">
      <h1>Musa Beytekin</h1>
      <p class="place">{t["place"]}</p>
      <p class="lead">{t["lead"]}</p>
      <p class="summary">{t["summary"]}</p>
      <ul class="actions">
        <li><a class="button" href="{t["cv_href"]}">{t["cv_label"]}</a></li>
        <li><a href="{GITHUB}">GitHub</a></li>
        <li><a href="{LINKEDIN}">LinkedIn</a></li>
        <li><a href="mailto:{EMAIL}">{t["email_label"]}</a></li>
      </ul>
    </section>

    <section class="block wrap" id="exradius">
      <h2>{t["exradius_h"]}</h2>
      <div class="content">
        <h3>Exradius</h3>
        <p class="note">{t["exradius_note"]}</p>
{exradius}
        <h4>{t["run_title"]}</h4>
        <ol class="track">
{run}
        </ol>
        <h4>{t["built_title"]}</h4>
        <dl class="rows">
{built}
        </dl>
      </div>
    </section>

    <section class="block wrap" id="thesis">
      <h2>{t["thesis_h"]}</h2>
      <div class="content">
        <h3>{t["thesis_title"]}</h3>
        <p class="note">{t["thesis_note"]}</p>
{thesis}
        <h4>{t["results_title"]}</h4>
        <dl class="rows">
{rows(t["results"], 10)}
        </dl>
        <p class="models">{t["models_label"]}: {MODELS}</p>
      </div>
    </section>

    <section class="block wrap" id="side-project">
      <h2>{t["side_h"]}</h2>
      <div class="content">
        <h3>{t["side_title"]}</h3>
        <p class="note">{t["side_note"]}</p>
        <p>{t["side"]}</p>
      </div>
    </section>

    <section class="block wrap" id="experience">
      <h2>{t["experience_h"]}</h2>
      <div class="content">
{jobs}
      </div>
    </section>

    <section class="block wrap" id="skills">
      <h2>{t["skills_h"]}</h2>
      <div class="content">
        <dl class="rows">
{rows(t["skills"], 10)}
        </dl>
      </div>
    </section>

    <section class="block wrap" id="education">
      <h2>{t["education_h"]}</h2>
      <div class="content">
        <dl class="rows">
{rows(t["education"], 10)}
        </dl>
      </div>
    </section>

    <section class="block wrap" id="contact">
      <h2>{t["contact_h"]}</h2>
      <div class="content">
        <p>{t["contact"]}</p>
        <p><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a></p>
        <ul class="links">
          <li><a href="{LINKEDIN}">LinkedIn</a></li>
          <li><a href="{GITHUB}">GitHub</a></li>
          <li><a href="{t["cv_href"]}">{t["cv_label"]}</a></li>
        </ul>
      </div>
    </section>
  </main>

  <footer class="wrap">
    <p>{t["footer"]}</p>
  </footer>

  <script src="{root}assets/site.js" defer></script>
</body>
</html>
"""


def main():
    here = Path(__file__).parent
    for lang, t in PAGES.items():
        target = here / t["path"]
        target.parent.mkdir(exist_ok=True)
        target.write_text(page(lang, t), encoding="utf-8")
        print("wrote", t["path"])


if __name__ == "__main__":
    main()
