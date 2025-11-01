# app.py — Streamlit Portfolio (version simple & compilable)
import os
import streamlit as st

# ------------------ CONFIG ------------------

st.set_page_config(page_title="Portfolio – Martin Junior SOUOP", page_icon="📊", layout="wide")

# --- Titre & couleurs globales ---
st.markdown("""
<style>
  .hero {
    padding: 18px 22px; border-radius: 16px;
    background: linear-gradient(90deg,#7C3AED,#06B6D4,#10B981);
    color: white; font-weight: 800; font-size: 26px; letter-spacing:.3px;
    box-shadow: 0 10px 24px rgba(0,0,0,.12);
  }
  .subhero { color: rgba(255,255,255,.92); font-weight:500; font-size:14px; margin-top:4px;}
</style>
<div class="hero">PORTFOLIO DE MARTIN — Data • Finance • SAP BI</div>
""", unsafe_allow_html=True)
st.write("")  # petit espace

def L(fr, en, lang):
    return fr if lang == "FR" else en

def exists(p):
    try:
        return bool(p) and os.path.exists(p)
    except Exception:
        return False

def mime(fname):
    f = (fname or "").lower()
    if f.endswith(".pdf"): return "application/pdf"
    if f.endswith(".xlsx"): return "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    if f.endswith(".csv"): return "text/csv"
    return "application/octet-stream"

def image_or_note(path, label):
    if exists(path):
        st.image(path, use_container_width=True)
    else:
        st.info(f"📷 Image manquante — {label}")

# ------------------ DATA ------------------
DATA = {
  "profile": {
    "name": "Martin Junior SOUOP",
    "titleFR": "Consultant Data / Finance / SAP BI (Junior)",
    "titleEN": "Junior Data / Finance / SAP BI Consultant",
    "location": "Paris, France",
    "email": "martin.souop@groupe-esigelec.org",
    "phone": "+33 7 80 25 50 91",
    "links": {
      "linkedin": "https://www.linkedin.com/in/martin-j-souop-b154402b6/",
      "github": "https://github.com/",
      "cv": "files/Martin_Junior_SOUOP_CV.pdf",
      "cv_alt":""  #
    },
    "photo": "images/photo.jpg",
    "signature": "images/signature.png",
    "summaryFR": ("Projets phares : API C# investissement, IA prix véhicules, Blockchain facture, "
                  "SAP SAC (SHOES Avenue), Ingénieur – prêts structurés."),
    "summaryEN": ("Flagship projects: C# investment API, AI vehicle pricing, Blockchain invoice, "
                  "SAP SAC (SHOES Avenue), Engineering – structured loans.")
  },

  # 5 projets (gros paragraphes FR/EN)
  "projects": [
    {
      "id":"prj_api_csharp",
      "title":"API C# – Gestion des investissements d’un client",
      "img":"images/api_csharp_swagger.jpg",
      "tags":["C#",".NET","EF Core","REST","Swagger","SQL Server","Auth"],
      "files":["files/Program.cs"],
      "detailsFR":(
        "Service d’API REST pour gérer portefeuilles et transactions d’un client. EF Core gère les migrations, "
        "les relations (Client, Compte, Instrument, Transaction) et l’intégrité. Endpoints CRUD pour l’onboarding, "
        "l’ingest (achat/vente/dividende) et la lecture agrégée (positions, P&L, cash-flows). Une couche de calcul "
        "agrège en positions journalières (MV, PRU, P&L réalisé/non-réalisé), applique taxes/frais et expose des KPI "
        "BI-ready. Sécurité JWT + rôles (Conseiller/Auditeur), DTO validés, documentation Swagger. Résultat : socle "
        "back robuste, traçable, prêt pour Power BI ou portail client."
      ),
      "detailsEN":(
        "REST API to manage client portfolios/transactions. EF Core migrations & relations (Client, Account, "
        "Instrument, Transaction). CRUD endpoints for onboarding, ingest (buy/sell/dividend) and aggregated reads "
        "(positions, P&L, cash-flows). Computation layer builds daily positions (MV, avg cost, realized/unrealized P&L), "
        "applies taxes/fees, exposes BI-ready KPIs. JWT roles, DTO validation, Swagger docs. Solid, auditable backend."
      )
    },
    {
      "id":"prj_ai_vehicles",
      "title":"IA – Prévision du prix de vente des véhicules d’occasion",
      "img":"images/ai_vehicles.jpg",
      "tags":["Python","Pandas","Scikit-learn","Keras","Regression"],
      "files":["/mnt/data/Projet_prix de_vente_Euriel.pdf"],
      "detailsFR":(
        "Objectif : estimer un prix de vente ‘market-consistent’ depuis l’historique des annonces. Pipeline : "
        "nettoyage (NA/outliers), encodage (one-hot marque/modèle), standardisation, split train/test, CV. Benchmark : "
        "régressions linéaire/Lasso, arbres (RandomForest/XGBoost) et réseau dense Keras. R²/RMSE supérieurs sur les "
        "modèles non linéaires, le réseau captant les interactions (kilométrage×âge×motorisation). Livrables : "
        "notebook réplicable, rapport PDF, fonction ‘predict_price’ réutilisable."
      ),
      "detailsEN":(
        "Goal: market-consistent sale price estimation from listings. Pipeline: cleaning, one-hot encoding, scaling, "
        "train/test split, CV. Bench: linear/Lasso vs RF/XGB and a Keras dense net. Nonlinear models win on R²/RMSE. "
        "Deliverables: reproducible notebook, PDF report, reusable predict_price()."
      )
    },
    {
      "id":"prj_blockchain_invoice",
      "title":"Blockchain – Certification de la validité d’une facture",
      "img":"images/blockchain_invoice.jpg",
      "tags":["Blockchain","Hash","Timestamp","Audit"],
      "files":["/mnt/data/Projet Blockchain - facturation.pdf"],
      "detailsFR":(
        "Problème : prouver qu’une facture n’a pas été altérée. Solution : calcul d’un hash SHA-256 du PDF+métadonnées "
        "et ancrage horodaté (on-chain ou journal off-chain). La vérification recalcule le hash du document présenté et "
        "compare à la preuve (id bloc/transaction). Bénéfices : non-répudiation, détection d’altérations, auditabilité. "
        "POC : CLI hash, service de preuve, viewer de vérification."
      ),
      "detailsEN":(
        "Problem: prove an invoice wasn’t altered. Solution: SHA-256 hash of PDF+metadata anchored with a timestamp "
        "(on-chain or off-chain log). Verification recomputes the hash and compares with the anchor (block/tx id). "
        "Benefits: non-repudiation, tamper detection, auditability. PoC: hash CLI, proof service, verify viewer."
      )
    },
    {
      "id":"prj_sap_shoes",
      "title":"Consultant Junior SAP – SHOES Avenue (SAC Planning)",
      "img":"images/sap_shoes.png",
      "tags":["SAP SAC","Planning","Data Actions","Rôles","What-if","KPI"],
      "files":[],
      "detailsFR":(
        "Montage d’un cycle budgétaire dans SAP Analytics Cloud : versions (Budget/Forecast/Réel), formulaires d’entrée "
        "magasin, Data Actions (copy, FX, allocations). Modèle étoile (magasin, produit, temps), sécurité par rôles, "
        "ingestion Excel/HANA. Tableaux de bord CA/Marge/Stock et scénarios what-if (prix, promo, mix). "
        "Résultat : visibilité consolidée et décisions accélérées."
      ),
      "detailsEN":(
        "SAC Planning setup: versions, input forms, data actions (copy/FX/allocation). Star schema, role-based security, "
        "Excel/HANA ingest. Dashboards (Revenue/Margin/Inventory) + what-if scenarios. Faster consolidated decisions."
      )
    },
    {
      "id":"prj_structured_loans",
      "title":"Projet Ingénieur – Structuration des prêts aux entreprises",
      "img":"images/structured_loans.jpeg",
      "tags":["Finance","Credit","Cashflows","Python","Stress test"],
      "files":["/mnt/data/FP PING 15.pdf"],
      "detailsFR":(
        "Consolider plusieurs prêts en un instrument unique (taux/échéancier recalculés) et émettre des notes structurées "
        "pour investisseurs. Moteur Python : cashflows (amortissement/intérêts), indicateurs (duration, convexité, DSCR), "
        "stress (taux/retards). Sorties : term-sheet, maquette de dashboard crédit, support comité d’octroi."
      ),
      "detailsEN":(
        "Consolidate corporate loans into a single instrument and issue structured notes. Python engine for cashflows, "
        "duration/convexity/DSCR, rate & delay stress. Outputs: term-sheet and credit dashboard mockup."
      )
    },
  ],

  # 2 stages (texte long + UML/Parsing/SQL pour Gustave)
  "experience":[
    {
      "company":"LMR Assurances",
      "titleFR":"Stagiaire – Analyste Risques Quantitatifs",
      "titleEN":"Intern – Quant Risk Analyst",
      "period":"2024", "location":"Paris",
      "bulletsFR":[
        "Dashboards Power BI (sinistres, S/P)",
        "Automatisation Power Query & Excel",
        "Définition de KPI"
      ],
      "bulletsEN":[
        "Power BI dashboards (claims, loss ratio)",
        "Power Query & Excel automation",
        "KPI definition"
      ],
      "longFR":(
        "Mission sinistralité : tableaux de bord fréquence/coût moyen/S-P, fiabilisation du pipeline Power Query, "
        "KPI partagés avec actuariat et ops, harmonisation des dimensions (produit/zone/profil) et règles de gestion documentées. "
        "Impact : production plus rapide et pilotage S-P par segment."
      ),
      "longEN":"Claims analytics in Power BI, hardened Power Query pipeline, shared KPIs, harmonized dimensions."
    },
    {
      "company":"Université Gustave Eiffel – LAMES",
      "titleFR":"Stagiaire – Data Analyst",
      "titleEN":"Intern – Data Analyst",
      "period":"2023", "location":"Paris",
      "bulletsFR":["Analyses R & Power BI","Nettoyage, jointures, viz","Dataset pour étude"],
      "bulletsEN":["R & Power BI analysis","Cleaning, joins, viz","Dataset for study"],
      "longFR":(
        "Construction d’un dataset de recherche et de tableaux de bord exploratoires. UML (sources→staging→jeu d’études). "
        "Parsing/cleaning avec Pandas (typage dates, normalisation, jointures), contrôles qualité (NA/doublons/outliers) et export SQL. "
        "Requêtes exemples : CA client, densité produit, séries temporelles, vues BI."
      ),
      "detail":{
        "uml_img":"images/uml_gustave.png",
        "python_steps":[
          "Lecture CSV/Excel avec pandas (encoding/séparateur)",
          "Typage dates & numériques, gestion NA/outliers",
          "Normalisation labels, déduplication",
          "Jointures dimensionnelles, champs dérivés",
          "Export SQL + vues BI"
        ],
        "sql_snippets":[
          "CREATE TABLE ventes (id INT PRIMARY KEY, date DATE, client_id INT, produit_id INT, montant NUMERIC(12,2));",
          "SELECT client_id, SUM(montant) AS ca FROM ventes WHERE date BETWEEN '2023-01-01' AND '2023-12-31' GROUP BY client_id ORDER BY ca DESC;",
          "WITH base AS (SELECT produit_id, COUNT(*) n, AVG(montant) avg_m FROM ventes) SELECT * FROM base WHERE n>10;"
        ]
      }
    }
  ],

  "skills":{
    "categories":[
      {"titleFR":"Risques de marché","titleEN":"Market Risk",
       "items":["VaR / SVaR","Pricing d'instruments","Yield to Maturity","Sensibilités (DV01/Greeks)","P&L explain","Stress testing","Gap de liquidité","Notions de hedge"]},
      {"titleFR":"Mathématiques financières","titleEN":"Financial Mathematics",
       "items":["Options (vanilles)","Taux d'intérêt & de change","Equity / Delta one"]},
      {"titleFR":"Analyse quantitative","titleEN":"Quantitative Analysis",
       "items":["Actions & indices","Rentabilité / Sharpe","Portefeuille de Markowitz","MEDAF (CAPM)","Mesure de performance"]},
    ]
  },

  "education":[
    {"school":"ESIGELEC, Rouen","degreeFR":"Cycle Ingénieur – Data & Finance","degreeEN":"Engineering cycle – Data & Finance","years":"2022–2025"}
  ]
}

# ------------------ SIDEBAR ------------------
lang = st.sidebar.radio("Langue / Language", ["FR","EN"], horizontal=True, index=0)
section = st.sidebar.radio(L("Sections","Sections",lang),
                           ["Projects","Experience","Skills","Education","Downloads","Contact"],
                           index=0)

# ------------------ HEADER ------------------
col1, col2 = st.columns([3,1], vertical_alignment="top")
with col1:
    if exists(DATA["profile"].get("photo")):
        st.image(DATA["profile"]["photo"], width=180)
    st.markdown(f"### {DATA['profile']['name']}")
    st.caption(L(DATA["profile"]["titleFR"], DATA["profile"]["titleEN"], lang))
    st.write(L(DATA["profile"]["summaryFR"], DATA["profile"]["summaryEN"], lang))
with col2:
    st.markdown(f"**{L('Localisation','Location',lang)}:** {DATA['profile']['location']}  \n"
                f"**Email:** {DATA['profile']['email']}  \n"
                f"**Tel:** {DATA['profile']['phone']}")
    st.link_button("LinkedIn", DATA["profile"]["links"]["linkedin"])
    st.link_button("GitHub", DATA["profile"]["links"]["github"])
    cv_alt = DATA["profile"]["links"].get("cv_alt")
    cv_path = cv_alt if exists(cv_alt) else DATA["profile"]["links"]["cv"]
    if exists(cv_path):
        with open(cv_path, "rb") as f:
            st.download_button(L("Télécharger le CV","Download CV",lang), f,
                               file_name=os.path.basename(cv_path), mime="application/pdf", key="cv_downloads_btn",)
    else:
        st.info(L("CV introuvable (place-le dans files/).","CV not found (put it in files/).",lang))
sig = DATA["profile"].get("signature")
if exists(sig):
    st.image(sig, caption=L("Signature","Signature",lang), width=160)

st.divider()

# ------------------ PROJECTS ------------------
def render_projects():
    st.markdown(f"### {L('Projets','Projects',lang)}")
    cols = st.columns(2, vertical_alignment="top")
    for i,p in enumerate(DATA["projects"]):
        with cols[i % 2]:
            st.subheader(p["title"])
            image_or_note(p.get("img"), p["title"])
            if p.get("tags"):
                st.caption(" • ".join(p["tags"]))
            with st.expander(L("Voir l’explication détaillée","Read detailed explanation",lang), expanded=False):
                st.write(L(p["detailsFR"], p["detailsEN"], lang))
                for fpath in p.get("files", []):
                    if exists(fpath) and (fpath.startswith("files/") or fpath.startswith("/mnt/")):
                        with open(fpath, "rb") as fh:
                            st.download_button(L("Télécharger le document","Download document",lang),
                                               fh, file_name=os.path.basename(fpath), mime=mime(fpath))

# ------------------ EXPERIENCE ------------------
def render_experience():
    st.markdown(f"### {L('Expériences','Experience',lang)}")
    for exp in DATA["experience"]:
        st.markdown(f"**{exp['company']}**")
        st.caption(f"{L(exp['titleFR'], exp['titleEN'], lang)} · {exp['period']} · {exp['location']}")
        # texte long
        longtxt = exp.get("longFR") if lang=="FR" else exp.get("longEN", exp.get("longFR",""))
        if longtxt:
            with st.expander(L("Lire l’explication complète","Read full explanation",lang), expanded=False):
                st.write(longtxt)
                if "Gustave Eiffel" in exp["company"]:
                    st.markdown("**UML**")
                    image_or_note(exp.get("detail",{}).get("uml_img",""), "UML Gustave Eiffel")
                    st.markdown("**Étapes Python (parsing)**")
                    for s in exp.get("detail",{}).get("python_steps",[]):
                        st.markdown(f"- {s}")
                    st.markdown("**Exemples de requêtes SQL**")
                    for q in exp.get("detail",{}).get("sql_snippets",[]):
                        st.code(q, language="sql")
        # bullets
        for b in (exp["bulletsFR"] if lang=="FR" else exp.get("bulletsEN", exp["bulletsFR"])):
            st.markdown(f"- {b}")
        st.markdown("---")

# ------------------ SKILLS / EDUCATION / DOWNLOADS / CONTACT ------------------
def render_skills():
    st.markdown(f"### {L('Compétences','Skills',lang)}")
    cols = st.columns(3)
    for i,cat in enumerate(DATA["skills"]["categories"]):
        with cols[i % 3]:
            st.markdown(f"**{L(cat['titleFR'], cat['titleEN'], lang)}**")
            for it in cat["items"]:
                st.markdown(f"- {it}")

def render_education():
    st.markdown(f"### {L('Formation','Education',lang)}")
    for ed in DATA["education"]:
        st.markdown(f"**{ed['school']}**")
        st.caption(f"{L(ed['degreeFR'], ed['degreeEN'], lang)} · {ed['years']}")
        st.markdown("---")

def render_downloads():
    st.markdown(f"### {L('Téléchargements','Downloads',lang)}")
    # CV
    cv_alt = DATA["profile"]["links"].get("cv_alt")
    cv = cv_alt if exists(cv_alt) else DATA["profile"]["links"]["cv"]
    if exists(cv):
        with open(cv, "rb") as f:
            st.download_button(L("Télécharger le CV","Download CV",lang), f,
                               file_name=os.path.basename(cv), mime="application/pdf")
    else:
        st.info(L("CV introuvable (files/).","CV not found (files/).",lang))
    # Docs projets
    for p in DATA["projects"]:
        for fpath in p.get("files", []):
            if exists(fpath) and (fpath.startswith("files/") or fpath.startswith("/mnt/")):
                with open(fpath, "rb") as fh:
                    st.download_button(f"{L('Télécharger','Download',lang)} — {p['title']}",
                                       fh, file_name=os.path.basename(fpath), mime=mime(fpath),  key=f"dl_{p['id']}_{os.path.basename(fpath)}",)

def render_contact():
    st.markdown(f"### {L('Contact','Contact',lang)}")
    name = st.text_input(L("Votre nom","Your name",lang))
    email = st.text_input(L("Votre email","Your email",lang))
    msg = st.text_area(L("Votre message","Your message",lang), height=120)
    if st.button(L("Envoyer","Send",lang)):
        st.success(L("Merci, je vous répondrai rapidement (simulation).","Thanks, I'll get back to you soon (simulated).",lang))
        st.write("—", name, email)
        st.write(msg)
    st.caption(f"📧 {DATA['profile']['email']}")

# ------------------ ROUTING ------------------
if section == "Projects":
    render_projects()
elif section == "Experience":
    render_experience()
elif section == "Skills":
    render_skills()
elif section == "Education":
    render_education()
elif section == "Downloads":
    render_downloads()
elif section == "Contact":
    render_contact()

st.divider()
st.caption(f"© {DATA['profile']['name']} — " + L("Portfolio de projets & expériences","Projects & experience portfolio",lang))
