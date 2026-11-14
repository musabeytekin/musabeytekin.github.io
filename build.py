"""Writes index.html (English) and tr/index.html (Turkish) from the content below.

    python3 build.py

Standard library only. Edit the text in PAGES, run the script and commit the result.
"""

from pathlib import Path

SITE = "https://musabeytekin.github.io/"
EMAIL = "musabeytekin867@gmail.com"
GITHUB = "https://github.com/musabeytekin"
LINKEDIN = "https://www.linkedin.com/in/musabeytekin"
EXRADIUS = "https://github.com/musabeytekin/exradius"
SMART_HOME = "https://github.com/musabeytekin/smart-home-controller-ai"
FONTS = (
    "https://fonts.googleapis.com/css2"
    "?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800"
    "&family=Instrument+Sans:wght@400..700&display=swap"
)
MODELS = (
    "gemma3:4b, gemma2:9b, llama2:7b, llama3.1:8b, mistral:7b, qwen2.5:7b, "
    "granite3.3:8b, olmo2:7b, olmo-3:7b, gpt-oss:20b"
)

PAGES = {
    "en": {
        "path": "index.html",
        "root": "",
        "url": SITE,
        "other_href": "tr/",
        "other_lang": "tr",
        "other_name": "Türkçe",
        "title": "Musa Beytekin, AI engineer",
        "description": (
            "AI engineer building LLM agent systems, their evaluation and the backend they run on. "
            "Author of Exradius, an open-source platform that runs AI agents in isolated Kubernetes pods."
        ),
        "job_title": "AI Engineer",
        "skip": "Skip to content",
        "nav_label": "Sections",
        "nav": [
            ("exradius", "Exradius"),
            ("thesis", "Thesis"),
            ("experience", "Experience"),
            ("skills", "Skills"),
            ("contact", "Contact"),
        ],
        "role": "AI engineer building LLM agent systems, their evaluation, and the backend they run on.",
        "summary": (
            "I designed and built Exradius, an open-source platform that runs AI agents in isolated "
            "environments on Kubernetes. In my MSc thesis I compared 10 open-weight LLMs on speed, "
            "reliability, linguistic quality and emotion scoring. At Turkish Airlines I work on "
            "reservation systems that process about 1,000 records per second."
        ),
        "cv_href": "cv/Musa_Beytekin_CV_EN.pdf",
        "cv_label": "Download CV (PDF)",
        "email_label": "Email",
        "exradius_lead": (
            "An open-source, self-hosted platform that runs AI agents on a company's own code. "
            "Every task gets its own locked-down Kubernetes pod. The agent works there, asks a person "
            "when it needs to, and delivers a branch or a patch."
        ),
        "exradius_role": (
            "I designed and built all of it: the API and worker, the Kubernetes operator, "
            "the egress proxy, the admin panel and the install."
        ),
        "run_title": "One run, start to finish",
        "run": [
            ("", "A task arrives",
             "A message on a RabbitMQ queue names a project and an agent. Bridges for Jira and GitHub put it there."),
            ("", "The config is read",
             "The worker reads the project's <code>exradius.yaml</code> from its git repository and creates a Run."),
            ("", "A pod starts",
             "An operator written in Go builds one pod for the run: non-root, read-only filesystem, "
             "no capabilities, no cluster credentials."),
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
            "API and worker in Python (FastAPI, PostgreSQL, RabbitMQ). Every state change is stored "
            "with its event in one transaction, and the event is published after commit.",
            "A Kubernetes operator in Go (controller-runtime) with custom resources for runs and image builds.",
            "An egress proxy in Go that adds the model key and repository credentials to requests "
            "on the way out, so no pod ever holds them.",
            "The runner and its built-in MCP server: ask a person, submit the result, attach files.",
            "An admin panel in React and TypeScript.",
            "A Helm chart, and Terraform modules for AWS (EKS), GCP (GKE) and Azure (AKS).",
            "Secret stores kept encrypted in PostgreSQL or read from HashiCorp Vault.",
            "A Claude Code skill that sets a codebase up for Exradius, and an evaluation set of "
            "real upstream bug fixes for measuring agents (in progress).",
        ],
        "exradius_link": "Source on GitHub",
        "exradius_license": "Apache-2.0 license.",
        "thesis_h": "MSc thesis",
        "thesis_title": "Which local LLM fits which chat character?",
        "thesis_when": (
            "İnönü University, 2026. Official title: Communication Between Interactive Virtual "
            "Characters with an AI-Supported Language Learning Application."
        ),
        "thesis": [
            "Language learners chat with AI characters in the app the thesis proposes: a conversation "
            "partner, a language teacher, an emotional-support companion. I investigated which local "
            "model is a candidate for each role.",
            "I ran 10 open-weight LLMs (4B to 20B parameters) on the same hardware with Ollama and "
            "compared them on four groups of measures: response speed, reliability, linguistic "
            "quality and emotion scoring.",
            "I profiled how each model scores 27 emotions on the GoEmotions (Reddit comments), "
            "SST-2 (movie reviews) and TweetEval (tweets) datasets.",
            "Across the models, the lowest time to first token was 233 ms, the shortest total "
            "response time 2.0 s and the highest generation speed 94 tokens per second.",
        ],
        "models_label": "Models",
        "side_h": "Side project",
        "side_title": "Smart Home Controller AI",
        "side_when": "A multi-agent system in Python and LangChain.",
        "side": (
            "A coordinator agent reads a natural-language command such as “turn on the kitchen "
            "lights and set the temperature to 22 degrees” and routes each part to a specialist "
            "agent for lighting or climate. Only the agents a command needs are called, which "
            "keeps token cost low."
        ),
        "side_link": "Source on GitHub",
        "experience_h": "Experience",
        "jobs": [
            ("Software Engineer, Turkish Airlines", "May 2026 to present, remote", [
                "Develop Java and Spring Boot microservices for airline reservation systems that "
                "process about 1,000 reservation records per second.",
                "Added agent registration and permission features to the reservation and "
                "sales-agent management systems.",
                "Diagnose and resolve production issues across interconnected backend services.",
                "Work with Oracle and Couchbase in the data layer, and contribute to testing and code reviews.",
            ]),
            ("Software Engineer, ID3", "May 2024 to May 2026, remote", [
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
            ("MSc, Software Engineering", "İnönü University, 2024 to 2026. Thesis completed, "
                                          "defense pending; expected graduation December 2026."),
            ("BSc, Computer Engineering", "İnönü University, 2019 to 2023."),
            ("Spoken languages", "Turkish (native), English (B1)."),
        ],
        "contact_h": "Contact",
        "contact": "Email is the quickest way to reach me. I am based in Türkiye.",
        "footer": "Musa Beytekin, 2026.",
    },
    "tr": {
        "path": "tr/index.html",
        "root": "../",
        "url": SITE + "tr/",
        "other_href": "../",
        "other_lang": "en",
        "other_name": "English",
        "title": "Musa Beytekin, AI mühendisi",
        "description": (
            "LLM agent sistemleri kuran, değerlendiren ve altındaki backend'i yazan AI mühendisi. "
            "AI agent'larını izole Kubernetes pod'larında çalıştıran açık kaynak platform Exradius'un geliştiricisi."
        ),
        "job_title": "AI Mühendisi",
        "skip": "İçeriğe geç",
        "nav_label": "Bölümler",
        "nav": [
            ("exradius", "Exradius"),
            ("thesis", "Tez"),
            ("experience", "Deneyim"),
            ("skills", "Yetenekler"),
            ("contact", "İletişim"),
        ],
        "role": "LLM agent sistemleri kuran, değerlendiren ve altındaki backend'i yazan AI mühendisi.",
        "summary": (
            "AI agent'larını Kubernetes üzerinde izole ortamlarda çalıştıran açık kaynak platform "
            "Exradius'u tasarlayıp geliştirdim. Yüksek lisans tezimde 10 açık ağırlıklı LLM'i hız, "
            "güvenilirlik, dilsel kalite ve duygu puanlama açısından karşılaştırdım. Türk Hava "
            "Yolları'nda saniyede yaklaşık 1.000 kayıt işleyen rezervasyon sistemlerinde çalışıyorum."
        ),
        "cv_href": "../cv/Musa_Beytekin_CV_TR.pdf",
        "cv_label": "CV'yi indir (PDF)",
        "email_label": "E-posta",
        "exradius_lead": (
            "AI agent'larını bir şirketin kendi kodu üzerinde çalıştıran, açık kaynak ve self-hosted "
            "bir platform. Her görev kendi sıkılaştırılmış Kubernetes pod'unda çalışır. Agent işini "
            "orada yapar, gerektiğinde bir insana sorar ve sonunda bir branch ya da patch teslim eder."
        ),
        "exradius_role": (
            "Tamamını ben tasarlayıp geliştirdim: API ve worker, Kubernetes operator, egress proxy, "
            "yönetim paneli ve kurulum."
        ),
        "run_title": "Bir çalıştırma, baştan sona",
        "run": [
            ("", "Görev gelir",
             "RabbitMQ kuyruğuna düşen mesaj bir proje ve bir agent adı taşır. Mesajı Jira ve GitHub "
             "bridge'leri gönderir."),
            ("", "Config okunur",
             "Worker projenin git deposundaki <code>exradius.yaml</code> dosyasını okur ve bir Run oluşturur."),
            ("", "Pod açılır",
             "Go ile yazılmış operator çalıştırma için tek bir pod kurar: root'suz, salt okunur dosya "
             "sistemi, capability yok, cluster yetkisi yok."),
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
            "Python ile API ve worker (FastAPI, PostgreSQL, RabbitMQ). Her durum değişikliği olayıyla "
            "birlikte tek transaction'da saklanır, olay commit'ten sonra yayınlanır.",
            "Go ile Kubernetes operator (controller-runtime); çalıştırmalar ve imaj build'leri için "
            "custom resource'lar.",
            "Go ile egress proxy: model anahtarını ve depo kimlik bilgilerini isteğe çıkışta ekler, "
            "böylece hiçbir pod bunları tutmaz.",
            "Runner ve içindeki MCP sunucusu: insana soru sorma, sonuç teslimi, dosya ekleri.",
            "React ve TypeScript ile yönetim paneli.",
            "Helm chart ve AWS (EKS), GCP (GKE), Azure (AKS) için Terraform modülleri.",
            "PostgreSQL'de şifreli tutulan ya da HashiCorp Vault'tan okunan secret store'lar.",
            "Bir kod tabanını Exradius'a kuran Claude Code skill'i ve agent'ları ölçmek için gerçek "
            "upstream hata düzeltmelerinden oluşan değerlendirme seti (devam ediyor).",
        ],
        "exradius_link": "GitHub'da kaynak kod",
        "exradius_license": "Apache-2.0 lisansı.",
        "thesis_h": "Yüksek lisans tezi",
        "thesis_title": "Hangi yerel LLM hangi sohbet karakterine uygun?",
        "thesis_when": (
            "İnönü Üniversitesi, 2026. Resmî başlık: Yapay Zeka Destekli Dil Öğrenme Uygulaması ile "
            "Etkileşimli Sanal Karakterler Arası İletişim."
        ),
        "thesis": [
            "Tezin önerdiği uygulamada dil öğrenenler AI karakterlerle mesajlaşıyor: sohbet arkadaşı, "
            "dil öğretmeni, duygusal destek. Her role hangi yerel modelin aday olduğunu araştırdım.",
            "10 açık ağırlıklı LLM'i (4B ile 20B parametre arası) Ollama ile aynı donanımda çalıştırıp "
            "dört ölçüt grubunda karşılaştırdım: yanıt hızı, güvenilirlik, dilsel kalite ve duygu puanlama.",
            "GoEmotions (Reddit yorumları), SST-2 (film yorumları) ve TweetEval (tweet'ler) veri "
            "setlerinde her modelin 27 duyguyu nasıl puanladığını çıkardım.",
            "Modeller arasında en düşük ilk token'a ulaşma süresi 233 ms, en kısa toplam yanıt süresi "
            "2,0 s, en yüksek üretim hızı saniyede 94 token oldu.",
        ],
        "models_label": "Modeller",
        "side_h": "Yan proje",
        "side_title": "Smart Home Controller AI",
        "side_when": "Python ve LangChain ile çoklu agent sistemi.",
        "side": (
            "Koordinatör agent “mutfak ışıklarını aç ve sıcaklığı 22 dereceye ayarla” gibi doğal dil "
            "komutunu okur ve her parçayı aydınlatma ya da iklimlendirme için uzman agent'a yönlendirir. "
            "Yalnızca komutun gerektirdiği agent'lar çağrıldığı için token maliyeti düşük kalır."
        ),
        "side_link": "GitHub'da kaynak kod",
        "experience_h": "Deneyim",
        "jobs": [
            ("Yazılım Mühendisi, Türk Hava Yolları", "Mayıs 2026'dan bugüne, uzaktan", [
                "Saniyede yaklaşık 1.000 rezervasyon kaydı işleyen havayolu rezervasyon sistemlerinin "
                "Java ve Spring Boot mikroservislerini geliştiriyorum.",
                "Rezervasyon ve satış acentesi yönetim sistemlerine acente kaydı ve yetkilendirme "
                "özellikleri ekledim.",
                "Birbirine bağlı backend servislerinde üretim hatalarını teşhis edip gideriyorum.",
                "Veri katmanında Oracle ve Couchbase kullanıyor, test yazımı ve code review "
                "süreçlerine katkı veriyorum.",
            ]),
            ("Yazılım Mühendisi, ID3", "Mayıs 2024 – Mayıs 2026, uzaktan", [
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
        "contact": "Bana en hızlı e-postayla ulaşabilirsiniz. Türkiye'de yaşıyorum.",
        "footer": "Musa Beytekin, 2026.",
    },
}


def items(lines):
    return "\n".join(f"          <li>{line}</li>" for line in lines)


def page(lang, t):
    root = t["root"]
    nav = "\n".join(f'        <a href="#{anchor}">{label}</a>' for anchor, label in t["nav"])
    run = "\n".join(
        f'          <li{" class=" + chr(34) + kind + chr(34) if kind else ""} style="--i: {i}">'
        f"<strong>{title}</strong>{text}</li>"
        for i, (kind, title, text) in enumerate(t["run"])
    )
    thesis = "\n".join(f"        <p>{line}</p>" for line in t["thesis"])
    jobs = "\n".join(
        f"""        <article class="entry">
          <h3>{title}</h3>
          <p class="when">{when}</p>
          <ul class="points">
{items(points).replace("          <li>", "            <li>")}
          </ul>
        </article>"""
        for title, when, points in t["jobs"]
    )
    skills = "\n".join(f"          <dt>{name}</dt>\n          <dd>{value}</dd>" for name, value in t["skills"])
    education = "\n".join(
        f"          <dt>{name}</dt>\n          <dd>{value}</dd>" for name, value in t["education"]
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
  <meta name="theme-color" content="#f2f4f8" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0c1220" media="(prefers-color-scheme: dark)">
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

  <header class="top wrap">
    <nav aria-label="{t["nav_label"]}">
{nav}
    </nav>
    <a class="lang" href="{t["other_href"]}" lang="{t["other_lang"]}" hreflang="{t["other_lang"]}">{t["other_name"]}</a>
  </header>

  <main id="main">
    <section class="hero wrap">
      <h1>Musa Beytekin</h1>
      <div class="hero-text">
        <p class="role">{t["role"]}</p>
        <p class="summary">{t["summary"]}</p>
        <ul class="actions">
          <li><a class="button" href="{t["cv_href"]}">{t["cv_label"]}</a></li>
          <li><a href="{GITHUB}">GitHub</a></li>
          <li><a href="{LINKEDIN}">LinkedIn</a></li>
          <li><a href="mailto:{EMAIL}">{t["email_label"]}</a></li>
        </ul>
      </div>
    </section>

    <section class="block wrap" id="exradius">
      <h2>Exradius</h2>
      <div class="content">
        <p class="lead">{t["exradius_lead"]}</p>
        <p>{t["exradius_role"]}</p>
      </div>
      <div class="run wide">
        <h3>{t["run_title"]}</h3>
        <ol class="track">
{run}
        </ol>
      </div>
      <div class="content">
        <h3>{t["built_title"]}</h3>
        <ul class="points">
{items(t["built"])}
        </ul>
        <p><a href="{EXRADIUS}">{t["exradius_link"]}</a> <span class="note">{t["exradius_license"]}</span></p>
      </div>
    </section>

    <section class="block wrap" id="thesis">
      <h2>{t["thesis_h"]}</h2>
      <div class="content">
        <h3>{t["thesis_title"]}</h3>
        <p class="note">{t["thesis_when"]}</p>
{thesis}
        <p class="models">{t["models_label"]}: {MODELS}</p>
      </div>
    </section>

    <section class="block wrap" id="side-project">
      <h2>{t["side_h"]}</h2>
      <div class="content">
        <h3>{t["side_title"]}</h3>
        <p class="note">{t["side_when"]}</p>
        <p>{t["side"]}</p>
        <p><a href="{SMART_HOME}">{t["side_link"]}</a></p>
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
        <dl class="facts">
{skills}
        </dl>
      </div>
    </section>

    <section class="block wrap" id="education">
      <h2>{t["education_h"]}</h2>
      <div class="content">
        <dl class="facts">
{education}
        </dl>
      </div>
    </section>

    <section class="block wrap" id="contact">
      <h2>{t["contact_h"]}</h2>
      <div class="content">
        <p>{t["contact"]}</p>
        <p><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a></p>
        <ul class="links">
          <li><a href="{LINKEDIN}">linkedin.com/in/musabeytekin</a></li>
          <li><a href="{GITHUB}">github.com/musabeytekin</a></li>
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
