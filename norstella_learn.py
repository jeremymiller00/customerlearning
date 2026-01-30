#!/usr/bin/env python3
"""
Norstella Customer Learning App
Daily 15-30 min learning sessions for a DS Product Manager
"""

import json
import os
import random
import time
import textwrap
from datetime import datetime, date
from pathlib import Path

DATA_DIR = Path(__file__).parent / "learning_data"
PROGRESS_FILE = DATA_DIR / "progress.json"

# ─────────────────────────────────────────────────────────────────────
# KNOWLEDGE BASE
# ─────────────────────────────────────────────────────────────────────

MODULES = [
    {
        "id": "norstella_overview",
        "title": "Norstella: The Big Picture",
        "order": 1,
        "lessons": [
            {
                "id": "what_is_norstella",
                "title": "What is Norstella?",
                "content": textwrap.dedent("""\
                    Norstella is a $5B global pharmaceutical technology and intelligence
                    company formed in 2022. It unites five brands under one mission:
                    "smooth the path to lifesaving therapies for patients and providers."

                    THE FIVE BRANDS:
                      1. Citeline  — Clinical trial intelligence & drug pipeline tracking
                      2. Evaluate  — Commercial intelligence & pharma asset valuation
                      3. MMIT      — Market access, payer policy & formulary data
                      4. Panalgo   — Real-world evidence analytics (IHD platform)
                      5. The Dedham Group — Oncology & specialty market access consulting

                    KEY FACTS:
                    - ~1,600 employees, HQ in Yardley, PA
                    - Backed by Warburg Pincus, Hg, Ardian ($1.13B raised)
                    - Named to Fast Company's Most Innovative Companies 2025
                    - CEO: Kris Joshi (appointed July 2025)
                    - Flagship data asset: NorstellaLinQ (74B+ data points)

                    VALUE PROPOSITION:
                    Norstella covers the ENTIRE drug lifecycle — from pipeline intelligence
                    (Citeline, Evaluate) through clinical development (Panalgo RWD) to
                    commercialization and market access (MMIT, Dedham Group).

                    No other company offers this end-to-end view. Competitors typically
                    play in one segment: IQVIA (data/CRO), Veeva (CRM/clinical ops),
                    Clarivate (pipeline data). Norstella's moat is integration.
                """),
            },
            {
                "id": "customer_segments",
                "title": "Who Are Norstella's Customers?",
                "content": textwrap.dedent("""\
                    Norstella serves the LIFE SCIENCES industry. Key customer segments:

                    1. LARGE PHARMA (e.g., Pfizer, Novartis, Roche, Lilly)
                       - Use Evaluate for pipeline valuation & competitive intelligence
                       - Use MMIT to understand payer coverage for launched products
                       - Use Citeline for clinical trial planning & site selection
                       - Use Panalgo IHD for HEOR and real-world evidence studies

                    2. BIOTECH / EMERGING BIOPHARMA
                       - Smaller teams, need efficient tools
                       - Citeline Pharmaprojects for competitive landscape
                       - MMIT for pre-launch market access planning
                       - Evaluate for fundraising/valuation benchmarks

                    3. MEDTECH & DIAGNOSTICS
                       - Evidence generation with Panalgo
                       - Market access strategy with MMIT

                    4. CROs (Contract Research Organizations)
                       - Citeline Sitetrove for investigator/site identification
                       - Trialtrove for trial benchmarking

                    5. PAYERS & HEALTH SYSTEMS
                       - MMIT analytics for formulary management
                       - Dedham Group for clinical pathway design

                    6. CONSULTING & FINANCIAL SERVICES
                       - Evaluate data for M&A due diligence
                       - Pipeline analytics for investment decisions

                    CUSTOMER JOURNEY THROUGH NORSTELLA BRANDS:
                    Discovery → Citeline (Pharmaprojects)
                    Clinical Dev → Citeline (Trialtrove, Sitetrove) + Panalgo (RWD)
                    Regulatory → Citeline + Evaluate
                    Launch Prep → MMIT (payer landscape) + Dedham Group (pathways)
                    Commercial → MMIT (formulary tracking) + Evaluate (forecasts)
                    Post-Market → Panalgo (real-world evidence) + MMIT
                """),
            },
        ],
    },
    {
        "id": "citeline",
        "title": "Deep Dive: Citeline",
        "order": 2,
        "lessons": [
            {
                "id": "citeline_products",
                "title": "Citeline Products & Capabilities",
                "content": textwrap.dedent("""\
                    Citeline is Norstella's CLINICAL INTELLIGENCE brand. It powers
                    smarter, faster decisions across drug development.

                    CORE PRODUCTS:

                    PHARMAPROJECTS (Drug Pipeline Intelligence)
                    - Industry standard for tracking the global drug R&D landscape
                    - Covers drugs from discovery through post-launch
                    - Used by BD&L, strategy, and competitive intelligence teams
                    - Key question it answers: "What's in the pipeline for Disease X?"

                    TRIALTROVE (Clinical Trial Intelligence)
                    - Curated data on trial design, enrollment, and execution
                    - 60,000+ trusted data sources
                    - Covers: trial design, enrollment timelines, patient populations,
                      endpoints, outcomes, geographic trends
                    - Key question: "How are competitors designing their Phase 3 trials?"

                    SITETROVE (Investigator & Site Intelligence)
                    - Industry-leading investigator and site selection tool
                    - Helps find and evaluate clinical trial sites globally
                    - Key question: "Which sites enrolled fastest for this indication?"

                    AI / SMARTSOLUTIONS (launched 2024):
                    - Protocol SmartDesign: AI-driven protocol optimization
                    - Uses ML + LLMs on top of Trialtrove & Sitetrove data
                    - Predictive analytics for trial feasibility

                    "PLUS" UPGRADES (Feb 2025):
                    - Trialtrove+, Sitetrove+, Pharmaprojects+
                    - Proprietary performance metrics
                    - "Ella" AI assistant integrated into the UI
                    - Enhanced data visualization

                    WHO BUYS CITELINE?
                    - Clinical operations teams (trial planning)
                    - R&D strategy & portfolio teams
                    - Business development & licensing
                    - Medical affairs
                    - CROs (site selection)
                """),
            },
        ],
    },
    {
        "id": "evaluate",
        "title": "Deep Dive: Evaluate",
        "order": 3,
        "lessons": [
            {
                "id": "evaluate_products",
                "title": "Evaluate Products & Capabilities",
                "content": textwrap.dedent("""\
                    Evaluate is Norstella's COMMERCIAL INTELLIGENCE brand, providing
                    predictive analytics and valuation for pharma assets since 1996.

                    CORE PRODUCTS:

                    EVALUATE PHARMA
                    - Consensus revenue forecasts for drugs and companies
                    - Net Present Value (NPV) for pipeline assets
                    - Used for portfolio planning, BD&L, and M&A
                    - Example: Novo's Cagrisema valued at $80B NPV (highest in industry)
                    - Key question: "What's the commercial potential of this drug?"

                    EVALUATE OMNIUM
                    - Self-service analytics platform
                    - Custom dashboards and scenario modeling
                    - Compare company portfolios and therapeutic areas

                    EP VANTAGE
                    - Editorial and analysis arm
                    - Data-driven commentary on industry trends
                    - M&A analysis, pipeline reviews, market forecasts
                    - Widely read by C-suite and investors

                    KEY INDUSTRY INSIGHTS (from Evaluate):
                    - Pharma R&D CAGR slowing: 3% (2023-2030) vs 9% (2016-2023)
                    - R&D as % of sales: dropping from 27% (2024) to 21% (2030)
                    - Medicare drug price negotiations expanding (15 more drugs in 2026)

                    WHO BUYS EVALUATE?
                    - CFOs and corporate strategy teams
                    - Business development & licensing
                    - Investor relations
                    - Buy-side analysts and investment banks
                    - Consulting firms (McKinsey, BCG, etc.)
                """),
            },
        ],
    },
    {
        "id": "mmit",
        "title": "Deep Dive: MMIT",
        "order": 4,
        "lessons": [
            {
                "id": "mmit_products",
                "title": "MMIT Products & Market Access",
                "content": textwrap.dedent("""\
                    MMIT (Managed Markets Insight & Technology) is Norstella's
                    MARKET ACCESS brand. It answers: "Can patients actually GET this drug?"

                    THE MARKET ACCESS PROBLEM:
                    Even after FDA approval, a drug faces coverage decisions by:
                    - Commercial payers (UnitedHealthcare, Cigna, Aetna, etc.)
                    - Medicare Part D plans
                    - Medicaid programs
                    - PBMs (CVS Caremark, Express Scripts, Optum Rx)
                    - IDNs / Health Systems
                    Each can impose: formulary tiers, prior auth, step therapy,
                    quantity limits, specialty pharmacy requirements.

                    CORE PRODUCTS:

                    ANALYTICS PLATFORM
                    - Formulary and medical benefit coverage data
                    - Covered lives analysis
                    - Policy and restriction tracking across payers
                    - Key question: "How is my drug covered across all US payers?"

                    FORMTRAK
                    - Connects coverage data to field team assets
                    - Promotional templates with real-time payer insights

                    CONTRACT VALIDATION
                    - Automates crosschecking rebate offers vs. actual formulary placement
                    - Only platform of its kind in the industry

                    PATIENT ACCESS ANALYTICS
                    - Combines coverage + claims data
                    - Shows payer AND prescriber behavior
                    - Key question: "Why aren't patients filling prescriptions?"

                    IDN FORMULARY INSIGHTS
                    - Health system formulary visibility
                    - Clinical pathway tracking within IDNs

                    PAYER LANDSCAPE & DIRECTORY
                    - Segment payers by market share, LOB, geography
                    - Identify decision-makers

                    WHO BUYS MMIT?
                    - Market access / trade teams
                    - Account managers (payer-facing)
                    - Commercial analytics teams
                    - Brand marketing teams
                    - HEOR teams (health economics & outcomes research)
                """),
            },
        ],
    },
    {
        "id": "panalgo",
        "title": "Deep Dive: Panalgo",
        "order": 5,
        "lessons": [
            {
                "id": "panalgo_products",
                "title": "Panalgo & Real-World Evidence",
                "content": textwrap.dedent("""\
                    Panalgo is Norstella's REAL-WORLD EVIDENCE (RWE) analytics brand.
                    Its mission: make healthcare data analysis accessible to non-coders.

                    WHY RWE MATTERS:
                    Clinical trials show efficacy in controlled settings. RWE shows
                    how drugs perform in the REAL WORLD — diverse patients, varied
                    adherence, co-morbidities, real clinical practice.
                    FDA increasingly accepts RWE for label expansions & safety signals.

                    CORE PRODUCTS:

                    IHD (INSTANT HEALTH DATA)
                    - Flagship no-code analytics platform
                    - Point-and-click cohort creation, study design
                    - Eliminates need for SAS/R/SQL programming
                    - 85% faster than traditional analytics methods
                    - Key users: HEOR scientists, medical affairs, epidemiologists

                    IHD CLOUD (launched 2024)
                    - AWS-powered scalable analytics
                    - Centralize data and technology for evidence teams
                    - Enterprise-grade security and governance

                    ELLA AI
                    - AI assistant integrated into IHD
                    - Natural language cohort creation
                    - No SQL or technical expertise required
                    - "Show me diabetic patients over 65 on metformin" → instant cohort

                    LINQNOTES (launched May 2025)
                    - Unlocks UNSTRUCTURED clinical data (80% of patient insight)
                    - Physician narratives, imaging reports, discharge summaries
                    - NLP/AI extraction of clinical context
                    - Answers the "WHY" behind treatment decisions

                    NORSTELLALINQ DATA ASSET:
                    - 74 billion data points
                    - Integrates: EMR, labs, open/closed claims, SDoH, mortality
                    - Largest linked patient-level dataset in the industry
                    - Feeds into IHD for analysis

                    WHO BUYS PANALGO?
                    - HEOR teams
                    - Medical affairs
                    - Epidemiology groups
                    - Market access (evidence generation)
                    - Regulatory affairs (post-market commitments)
                """),
            },
        ],
    },
    {
        "id": "dedham_group",
        "title": "Deep Dive: The Dedham Group",
        "order": 6,
        "lessons": [
            {
                "id": "dedham_products",
                "title": "The Dedham Group & Clinical Pathways",
                "content": textwrap.dedent("""\
                    The Dedham Group is Norstella's STRATEGIC CONSULTING brand,
                    focused on ONCOLOGY and SPECIALTY market access.

                    WHAT ARE CLINICAL PATHWAYS?
                    Standardized, evidence-based treatment protocols that guide
                    oncologists on which drugs to use for specific cancer types/stages.
                    Think of them as "treatment playbooks" for oncology.

                    WHY THEY MATTER:
                    - 62% of US oncologists are exposed to a clinical pathway
                    - 80% adherence rate among those using pathways
                    - Being OFF-pathway = limited brand perception and utilization
                    - FDA issued 60+ oncology approvals in 2024 alone
                    - Pathways help generalist oncologists navigate complexity

                    KEY TRENDS:
                    - Practice aggregators (e.g., OneOncology) are standardizing
                      pathways across community oncology networks
                    - Payers increasingly tying reimbursement to pathway adherence
                    - Value-based care models relying on pathways for cost control

                    DEDHAM GROUP SERVICES:
                    - Clinical pathway strategy (get ON pathway / improve position)
                    - Oncology market access consulting
                    - Payer engagement strategy
                    - Value-based care advisory
                    - IDN and health system contracting strategy
                    - Competitive intelligence in oncology

                    HOW DEDHAM CONNECTS TO OTHER BRANDS:
                    - Uses MMIT data for payer landscape understanding
                    - Leverages Panalgo RWE for evidence to support pathway inclusion
                    - Citeline data for competitive trial landscape
                    - Evaluate for commercial forecasting

                    WHO BUYS DEDHAM GROUP SERVICES?
                    - Oncology brand teams
                    - Market access leaders (specialty/oncology)
                    - Commercial strategy teams
                    - Medical affairs (pathway evidence generation)
                """),
            },
        ],
    },
    {
        "id": "drug_lifecycle",
        "title": "The Drug Development Lifecycle",
        "order": 7,
        "lessons": [
            {
                "id": "lifecycle_stages",
                "title": "From Discovery to Post-Market",
                "content": textwrap.dedent("""\
                    Understanding the drug lifecycle is essential because Norstella's
                    products map to EVERY STAGE.

                    STAGE 1: DISCOVERY (2-5 years)
                    - 5,000-10,000 compounds screened per candidate
                    - Target identification, lead optimization
                    - Norstella touchpoint: Citeline Pharmaprojects

                    STAGE 2: PRECLINICAL (1-2 years)
                    - Lab & animal studies (toxicology, pharmacokinetics)
                    - IND (Investigational New Drug) application filed
                    - Norstella touchpoint: Citeline, Evaluate (asset valuation)

                    STAGE 3: CLINICAL TRIALS (6-10 years)
                    - Phase I: 20-100 healthy volunteers, safety/dosing (70% advance)
                    - Phase II: 100-500 patients, efficacy signal (33% advance)
                    - Phase III: 1,000-5,000 patients, confirm efficacy (25-30% advance)
                    - Norstella touchpoints: Citeline (Trialtrove, Sitetrove, SmartDesign),
                      Panalgo (RWE for trial design), Evaluate (pipeline valuation)

                    STAGE 4: REGULATORY REVIEW (1-2 years)
                    - NDA (drugs) or BLA (biologics) submission
                    - FDA pathways: Standard, Priority, Fast Track, Breakthrough,
                      Accelerated Approval
                    - Norstella touchpoint: Citeline (regulatory tracking)

                    STAGE 5: LAUNCH & COMMERCIALIZATION
                    - Payer negotiations, formulary placement
                    - Field team deployment, KOL engagement
                    - Norstella touchpoints: MMIT (market access), Dedham Group
                      (pathway strategy), Evaluate (commercial forecasts)

                    STAGE 6: POST-MARKET / LIFECYCLE MANAGEMENT
                    - Phase IV studies, label expansions
                    - Real-world evidence generation
                    - Norstella touchpoints: Panalgo (IHD, LinQNotes),
                      MMIT (ongoing coverage tracking)

                    KEY STATS:
                    - Average cost: $2.6 billion per approved drug
                    - Average time: 10-15 years from discovery to approval
                    - Overall success rate: ~10-20% of clinical candidates
                    - Only 1 in 20,000-30,000 screened compounds gets approved
                """),
            },
        ],
    },
    {
        "id": "industry_landscape",
        "title": "The Competitive & Industry Landscape",
        "order": 8,
        "lessons": [
            {
                "id": "competitors",
                "title": "Norstella vs. Competitors",
                "content": textwrap.dedent("""\
                    Understanding WHO ELSE plays in Norstella's space helps you
                    articulate differentiation to customers.

                    PIPELINE & CLINICAL INTELLIGENCE:
                    - Citeline vs. Clarivate (Cortellis) vs. GlobalData
                    - Citeline advantage: depth of trial-level data, SmartSolutions AI
                    - Clarivate strength: broad IP + scientific data

                    COMMERCIAL ANALYTICS:
                    - Evaluate vs. GlobalData vs. BMI (Fitch Solutions)
                    - Evaluate advantage: consensus forecasts, NPV methodology
                    - Evaluate is gold standard for pharma M&A due diligence

                    MARKET ACCESS:
                    - MMIT vs. Fingertip Formulary vs. IQVIA (access data)
                    - MMIT advantage: depth of payer policy data, Contract Validation
                    - IQVIA strength: massive claims data, broader analytics

                    REAL-WORLD EVIDENCE:
                    - Panalgo vs. Aetion vs. TriNetX vs. Flatiron (Roche)
                    - Panalgo advantage: no-code IHD platform, NorstellaLinQ scale
                    - Aetion strength: regulatory-grade evidence platform
                    - Flatiron strength: oncology depth (EHR-derived)

                    CONSULTING:
                    - Dedham Group vs. Precision AQ vs. IntrinsiQ (IQVIA)
                    - Dedham advantage: integrated with MMIT data + Panalgo RWE

                    NORSTELLA'S OVERALL DIFFERENTIATOR:
                    No competitor offers the full pipeline-to-patient journey.
                    - IQVIA is closest but is a conglomerate, not purpose-built
                    - Veeva is strong in CRM/clinical ops but not intelligence
                    - Clarivate has pipeline data but no market access
                    - The INTEGRATION of 5 brands + NorstellaLinQ is unique
                """),
            },
            {
                "id": "industry_trends",
                "title": "Industry Trends Shaping Customers",
                "content": textwrap.dedent("""\
                    These trends affect WHAT customers need from Norstella:

                    1. AI/ML IN DRUG DEVELOPMENT
                    - AI-designed molecules, predictive trial design
                    - Customers want: AI-powered insights, not just raw data
                    - Norstella response: SmartSolutions, Ella AI, LinQNotes

                    2. REAL-WORLD EVIDENCE (RWE) EXPANSION
                    - FDA 21st Century Cures Act: RWE for regulatory decisions
                    - Payers demanding RWE for coverage
                    - Customers want: faster, cheaper evidence generation
                    - Norstella response: Panalgo IHD + NorstellaLinQ

                    3. DRUG PRICING PRESSURE
                    - IRA Medicare price negotiations (expanding to 15 more drugs 2026)
                    - Payer prior auth and step therapy increasing
                    - Customers want: granular payer intelligence
                    - Norstella response: MMIT policy tracking, Dedham Group strategy

                    4. PRECISION MEDICINE / BIOMARKER-DRIVEN TRIALS
                    - Smaller patient populations, more complex trial design
                    - Customers want: better site selection, patient identification
                    - Norstella response: Citeline Sitetrove+, NorstellaLinQ

                    5. PHARMA M&A WAVE
                    - Big pharma buying biotech to fill pipeline gaps
                    - Customers want: deal intelligence, target valuation
                    - Norstella response: Evaluate NPV, EP Vantage analysis

                    6. DECENTRALIZED CLINICAL TRIALS (DCTs)
                    - COVID accelerated remote/hybrid trials
                    - Customers want: data on DCT performance, site selection
                    - Norstella response: Citeline trial design intelligence

                    7. R&D PRODUCTIVITY DECLINE
                    - R&D spend growing slower (3% CAGR vs 9% historically)
                    - Customers want: do more with less, data-driven decisions
                    - Norstella response: integrated analytics, efficiency tools
                """),
            },
        ],
    },
    {
        "id": "ds_pm_role",
        "title": "DS Product Management at Norstella",
        "order": 9,
        "lessons": [
            {
                "id": "ds_pm_context",
                "title": "Your Role in Context",
                "content": textwrap.dedent("""\
                    As a DATA SCIENCE PRODUCT MANAGER at Norstella, you sit at the
                    intersection of data, AI/ML, and customer value.

                    YOUR STAKEHOLDERS:
                    - Data science / ML engineering teams (your team)
                    - Product managers for each brand (Citeline, MMIT, etc.)
                    - Commercial / sales teams (customer-facing)
                    - Customer success teams
                    - Executive leadership

                    KEY QUESTIONS CUSTOMERS ASK THAT YOU SHOULD UNDERSTAND:
                    - "Can NorstellaLinQ help us find the right sites for our trial?"
                    - "How does Ella AI compare to our internal data science team?"
                    - "Can we use Panalgo IHD for our FDA post-market commitment?"
                    - "How fresh is your claims data?"
                    - "Can I link your data to our internal data assets?"
                    - "What's the patient coverage for our drug across Medicare Part D?"

                    DATA SCIENCE OPPORTUNITIES:
                    1. NorstellaLinQ as a platform play
                       - 74B data points = massive feature engineering potential
                       - Linking clinical, claims, RWD, and commercial data
                    2. AI/ML model development
                       - Trial success prediction
                       - Patient identification & recruitment
                       - Payer decision prediction
                       - Drug revenue forecasting
                    3. NLP / unstructured data
                       - LinQNotes: extracting insight from clinical notes
                       - Ella AI: natural language query interface
                    4. Productionizing models
                       - Moving from ad-hoc analysis to scalable products
                       - Model monitoring, drift detection, retraining

                    YOUR PM PRINCIPLES APPLIED:
                    - "Understand, Identify, Execute" (Naomi Gleit framework)
                    - Understand: customer jobs-to-be-done at each lifecycle stage
                    - Identify: where DS/ML creates the highest-ROI value
                    - Execute: ship models as features within existing products
                """),
            },
        ],
    },
]

# ─────────────────────────────────────────────────────────────────────
# QUIZ BANK
# ─────────────────────────────────────────────────────────────────────

QUIZZES = {
    "norstella_overview": [
        {
            "type": "multiple_choice",
            "q": "Which of the following is NOT one of Norstella's five brands?",
            "options": ["Citeline", "Evaluate", "Veeva", "MMIT", "Panalgo"],
            "answer": "Veeva",
            "explanation": "Veeva is a separate company (CRM/clinical ops). Norstella's five brands are Citeline, Evaluate, MMIT, Panalgo, and The Dedham Group.",
        },
        {
            "type": "multiple_choice",
            "q": "What is NorstellaLinQ?",
            "options": [
                "A CRM platform for pharma sales teams",
                "The industry's first fully integrated data asset (74B+ data points)",
                "A clinical trial management system",
                "An FDA regulatory submission portal",
            ],
            "answer": "The industry's first fully integrated data asset (74B+ data points)",
            "explanation": "NorstellaLinQ integrates EMR, labs, claims, SDoH, and mortality data — 74 billion data points — into a single linked patient-level dataset.",
        },
        {
            "type": "fill_blank",
            "q": "Norstella's mission is to '_______ the path to lifesaving therapies for patients and providers.'",
            "answer": "smooth",
            "explanation": "The mission is to 'smooth the path to lifesaving therapies for patients and providers.'",
        },
        {
            "type": "multiple_choice",
            "q": "Which Norstella brand would a biotech CEO use to value their pipeline asset for a fundraise?",
            "options": ["MMIT", "Citeline", "Evaluate", "Panalgo"],
            "answer": "Evaluate",
            "explanation": "Evaluate provides consensus revenue forecasts and NPV valuations for drug assets — exactly what's needed for fundraising and M&A.",
        },
        {
            "type": "matching",
            "q": "Match each Norstella brand to its PRIMARY focus area:",
            "pairs": {
                "Citeline": "Clinical trial intelligence & drug pipeline",
                "Evaluate": "Commercial intelligence & asset valuation",
                "MMIT": "Market access & payer policy data",
                "Panalgo": "Real-world evidence analytics",
                "Dedham Group": "Oncology market access consulting",
            },
        },
        {
            "type": "scenario",
            "q": textwrap.dedent("""\
                SCENARIO: A large pharma company is planning a Phase 3 trial for a new
                cancer drug. They need to: (1) find the best sites, (2) understand the
                competitive trial landscape, and (3) plan their market access strategy.

                Which Norstella brands would you recommend for EACH need?"""),
            "answer": textwrap.dedent("""\
                1. Find best sites → CITELINE (Sitetrove / Sitetrove+)
                2. Competitive trial landscape → CITELINE (Trialtrove) + EVALUATE (pipeline valuation)
                3. Market access strategy → MMIT (payer landscape) + DEDHAM GROUP (pathway strategy for oncology)"""),
        },
    ],
    "citeline": [
        {
            "type": "multiple_choice",
            "q": "What is Trialtrove primarily used for?",
            "options": [
                "Drug pricing analytics",
                "Curated clinical trial intelligence (design, enrollment, outcomes)",
                "Payer formulary tracking",
                "Real-world evidence generation",
            ],
            "answer": "Curated clinical trial intelligence (design, enrollment, outcomes)",
            "explanation": "Trialtrove provides curated data on trial design, enrollment, and execution from 60,000+ sources.",
        },
        {
            "type": "multiple_choice",
            "q": "Citeline's SmartSolutions use what technology to optimize trial planning?",
            "options": [
                "Blockchain and distributed ledgers",
                "AI, ML, and large language models",
                "Manual expert curation only",
                "Simple statistical models",
            ],
            "answer": "AI, ML, and large language models",
            "explanation": "SmartSolutions (Protocol SmartDesign) use AI, ML, and LLMs on top of Trialtrove & Sitetrove data.",
        },
        {
            "type": "fill_blank",
            "q": "_______ is the industry standard for tracking the global drug R&D landscape.",
            "answer": "pharmaprojects",
            "explanation": "Pharmaprojects tracks drugs from discovery through post-launch and is the industry standard for pipeline intelligence.",
        },
        {
            "type": "scenario",
            "q": textwrap.dedent("""\
                SCENARIO: A CRO needs to find experienced investigators in Southeast Asia
                for a hepatitis B trial. They want sites that have enrolled quickly in
                similar trials before.

                Which Citeline product(s) would best serve this need?"""),
            "answer": textwrap.dedent("""\
                SITETROVE+ — provides investigator and site intelligence globally, including
                performance metrics on enrollment speed. The "plus" version adds proprietary
                performance data. Combined with TRIALTROVE+ for benchmarking against similar
                hepatitis B trials in the region."""),
        },
    ],
    "evaluate": [
        {
            "type": "multiple_choice",
            "q": "What does NPV stand for in the context of Evaluate's pipeline analytics?",
            "options": [
                "New Product Validation",
                "Net Present Value",
                "National Pharma Valuation",
                "Normalized Pipeline Volume",
            ],
            "answer": "Net Present Value",
            "explanation": "Evaluate uses Net Present Value (NPV) to estimate the current value of future cash flows from pipeline drugs.",
        },
        {
            "type": "multiple_choice",
            "q": "According to Evaluate data, pharma R&D spend as % of sales is projected to:",
            "options": [
                "Increase from 21% to 27% by 2030",
                "Remain flat at 27% through 2030",
                "Decrease from 27% (2024) to 21% (2030)",
                "Double by 2030",
            ],
            "answer": "Decrease from 27% (2024) to 21% (2030)",
            "explanation": "R&D spending as a percentage of sales is expected to decline, reflecting productivity pressure and portfolio optimization.",
        },
        {
            "type": "fill_blank",
            "q": "EP _______ is Evaluate's editorial and analysis arm providing data-driven commentary on pharma trends.",
            "answer": "vantage",
            "explanation": "EP Vantage (Evaluate Pharma Vantage) provides editorial analysis on pipeline developments, M&A, and market forecasts.",
        },
    ],
    "mmit": [
        {
            "type": "multiple_choice",
            "q": "Which MMIT product automates crosschecking rebate offers vs. actual formulary placement?",
            "options": [
                "FormTrak",
                "Contract Validation",
                "Patient Access Analytics",
                "Payer Landscape",
            ],
            "answer": "Contract Validation",
            "explanation": "Contract Validation is the only workflow automation platform that crosschecks rebate offer requirements against actual payer formulary data.",
        },
        {
            "type": "multiple_choice",
            "q": "What is 'step therapy' in the context of payer restrictions?",
            "options": [
                "A phased clinical trial design",
                "A requirement to try cheaper drugs before a payer covers a more expensive one",
                "A drug manufacturing process",
                "A patient education program",
            ],
            "answer": "A requirement to try cheaper drugs before a payer covers a more expensive one",
            "explanation": "Step therapy (or 'fail first') requires patients to try and fail on cheaper alternatives before the payer will cover a preferred drug.",
        },
        {
            "type": "scenario",
            "q": textwrap.dedent("""\
                SCENARIO: A brand manager notices prescriptions are being written but
                patients aren't filling them. They suspect payer restrictions.

                What MMIT product(s) would help diagnose this problem?"""),
            "answer": textwrap.dedent("""\
                PATIENT ACCESS ANALYTICS — combines coverage and claims data to show both
                payer and prescriber behavior, revealing whether prior auth requirements,
                step therapy, or formulary tier placement are causing abandonment.
                ANALYTICS PLATFORM — to see specific restrictions by payer."""),
        },
    ],
    "panalgo": [
        {
            "type": "multiple_choice",
            "q": "What percentage faster is IHD compared to traditional analytics methods?",
            "options": ["25%", "50%", "85%", "95%"],
            "answer": "85%",
            "explanation": "IHD Cloud accelerates healthcare analytics by 85% compared to traditional SAS/R programming methods.",
        },
        {
            "type": "multiple_choice",
            "q": "What percentage of patient insight lives in unstructured data (per Panalgo)?",
            "options": ["20%", "40%", "60%", "80%"],
            "answer": "80%",
            "explanation": "Up to 80% of patient insight lives in unstructured notes — physician narratives, imaging reports, discharge summaries — which LinQNotes unlocks.",
        },
        {
            "type": "fill_blank",
            "q": "_______ is Panalgo's AI assistant that enables natural language cohort creation without SQL.",
            "answer": "ella",
            "explanation": "Ella AI lets users create cohorts using natural language queries, removing the need for programming skills.",
        },
        {
            "type": "scenario",
            "q": textwrap.dedent("""\
                SCENARIO: An HEOR team needs to generate real-world evidence for an FDA
                post-market commitment. They need to analyze treatment patterns in
                diabetic patients but their team doesn't know SAS or R.

                Which Panalgo products would you recommend?"""),
            "answer": textwrap.dedent("""\
                IHD (Instant Health Data) — no-code analytics platform, point-and-click
                study design. Combined with NORSTELLALINQ data (74B data points including
                claims and EMR). ELLA AI for natural language cohort creation. If they need
                to understand WHY treatment patterns exist, LINQNOTES for unstructured data."""),
        },
    ],
    "dedham_group": [
        {
            "type": "multiple_choice",
            "q": "What percentage of US oncologists are currently exposed to a clinical pathway?",
            "options": ["25%", "42%", "62%", "85%"],
            "answer": "62%",
            "explanation": "According to MMIT Pulse Analytics data, roughly 62% of US oncologists are exposed to a clinical pathway.",
        },
        {
            "type": "multiple_choice",
            "q": "Among oncologists using pathways, what is the adherence rate?",
            "options": ["40%", "60%", "80%", "95%"],
            "answer": "80%",
            "explanation": "80% of oncologists using pathways adhere to recommended treatment guidelines, making pathway inclusion critical for drug utilization.",
        },
        {
            "type": "fill_blank",
            "q": "Practice aggregators like _______ are standardizing pathways across community oncology networks.",
            "answer": "oneoncology",
            "explanation": "OneOncology has been rapidly acquiring community oncology clinics and standardizing clinical pathway decision support tools.",
        },
    ],
    "drug_lifecycle": [
        {
            "type": "multiple_choice",
            "q": "How many compounds are typically screened in drug discovery for each approved drug?",
            "options": ["100-500", "1,000-5,000", "5,000-10,000", "20,000-30,000"],
            "answer": "5,000-10,000",
            "explanation": "5,000-10,000 compounds are screened per candidate (though only 1 in 20,000-30,000 screened overall gets approved).",
        },
        {
            "type": "multiple_choice",
            "q": "What is the average cost to develop one approved drug?",
            "options": ["$500 million", "$1.2 billion", "$2.6 billion", "$5 billion"],
            "answer": "$2.6 billion",
            "explanation": "On average, it costs $2.6 billion to develop one new medicine, including the cost of many failures.",
        },
        {
            "type": "multiple_choice",
            "q": "What percentage of Phase I trials advance to Phase II?",
            "options": ["30%", "50%", "70%", "90%"],
            "answer": "70%",
            "explanation": "Roughly 70% of Phase I trials yield satisfactory results and move to Phase II.",
        },
        {
            "type": "fill_blank",
            "q": "A _______ is filed for biologic drugs (as opposed to an NDA for small molecules).",
            "answer": "bla",
            "explanation": "A Biologics License Application (BLA) is filed for biologics, while a New Drug Application (NDA) is for small molecule drugs.",
        },
        {
            "type": "matching",
            "q": "Match each FDA pathway to its description:",
            "pairs": {
                "Standard Review": "Default pathway, ~10-12 months",
                "Priority Review": "Significant improvement over existing treatments, ~6 months",
                "Fast Track": "Serious conditions with unmet need, rolling submission",
                "Breakthrough": "Preliminary evidence of substantial improvement",
                "Accelerated Approval": "Based on surrogate endpoint, confirmatory trial required",
            },
        },
    ],
    "industry_landscape": [
        {
            "type": "multiple_choice",
            "q": "Which competitor is closest to Norstella in offering end-to-end pipeline-to-patient intelligence?",
            "options": ["Veeva", "IQVIA", "Clarivate", "Flatiron"],
            "answer": "IQVIA",
            "explanation": "IQVIA is closest as a conglomerate covering data, analytics, CRO, and technology. But it's not purpose-built for integration like Norstella.",
        },
        {
            "type": "multiple_choice",
            "q": "The IRA (Inflation Reduction Act) allows Medicare to negotiate prices for how many additional drugs in 2026?",
            "options": ["5", "10", "15", "25"],
            "answer": "15",
            "explanation": "Medicare will select up to 15 more drugs for price negotiations effective in 2026, adding to the initial 10.",
        },
        {
            "type": "scenario",
            "q": textwrap.dedent("""\
                SCENARIO: A customer says "We already use IQVIA for everything. Why should
                we add Norstella?"

                How would you respond?"""),
            "answer": textwrap.dedent("""\
                Key differentiation points:
                1. DEPTH vs BREADTH: MMIT has deeper payer policy data than IQVIA's access solutions
                2. NO-CODE RWE: Panalgo IHD democratizes analytics (IQVIA requires heavy consulting)
                3. CLINICAL PATHWAYS: Dedham Group specializes in oncology pathways (IQVIA's IntrinsiQ is less focused)
                4. NORSTELLALINQ: Purpose-built integrated dataset vs. IQVIA's fragmented data assets
                5. ASSET VALUATION: Evaluate is the gold standard (IQVIA doesn't do NPV)
                6. AI-NATIVE: SmartSolutions and Ella AI are product features, not consulting add-ons"""),
        },
    ],
    "ds_pm_role": [
        {
            "type": "scenario",
            "q": textwrap.dedent("""\
                SCENARIO: Your VP asks you to prioritize the next data science initiative.
                You have three options:
                A) Build a trial success prediction model using Citeline data
                B) Create an AI-powered payer decision predictor using MMIT data
                C) Improve LinQNotes NLP accuracy for clinical note extraction

                Walk through how you'd evaluate these using the "Understand, Identify,
                Execute" framework."""),
            "answer": textwrap.dedent("""\
                UNDERSTAND: What are the customer jobs-to-be-done for each?
                - A) Clinical teams need to de-risk Phase 3 decisions ($2.6B per drug)
                - B) Market access teams need to anticipate formulary changes pre-launch
                - C) HEOR teams need to extract treatment rationale from unstructured data

                IDENTIFY: Evaluate each on Value x Feasibility:
                - A) High value (massive $ at stake), medium feasibility (need labeled outcomes data)
                - B) High value (direct revenue impact), high feasibility (MMIT has rich structured data)
                - C) Medium value (improves existing product), high feasibility (existing NLP pipeline)

                EXECUTE: Recommendation framework:
                - B has best ROI: high value + high feasibility + clear data advantage
                - C is a quick win that improves existing product (ship fast, learn fast)
                - A is high-value but longer horizon — start with a proof of concept"""),
        },
        {
            "type": "multiple_choice",
            "q": "Which NorstellaLinQ data types are MOST relevant for a DS PM building patient journey models?",
            "options": [
                "Only claims data",
                "EMR + claims + labs + SDoH + mortality (all integrated)",
                "Only clinical trial data from Citeline",
                "Only payer policy data from MMIT",
            ],
            "answer": "EMR + claims + labs + SDoH + mortality (all integrated)",
            "explanation": "The power of NorstellaLinQ is the INTEGRATION of all these data types into a single linked dataset, enabling complete patient journey analysis.",
        },
    ],
}

# ─────────────────────────────────────────────────────────────────────
# PROGRESS MANAGEMENT
# ─────────────────────────────────────────────────────────────────────

def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {
        "sessions": [],
        "lessons_completed": [],
        "quiz_scores": {},
        "streak_days": [],
        "total_time_min": 0,
        "mastery": {},  # module_id -> score 0-100
    }

def save_progress(progress):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2, default=str))

# ─────────────────────────────────────────────────────────────────────
# UI HELPERS
# ─────────────────────────────────────────────────────────────────────

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"
MAGENTA = "\033[95m"

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def header(text):
    w = 68
    print(f"\n{CYAN}{'━' * w}")
    print(f"  {BOLD}{text}{RESET}{CYAN}")
    print(f"{'━' * w}{RESET}\n")

def subheader(text):
    print(f"\n{YELLOW}{BOLD}▸ {text}{RESET}")

def success(text):
    print(f"{GREEN}✓ {text}{RESET}")

def error(text):
    print(f"{RED}✗ {text}{RESET}")

def info(text):
    print(f"{DIM}{text}{RESET}")

def prompt(text=""):
    try:
        return input(f"\n{MAGENTA}❯ {text}{RESET}").strip()
    except (EOFError, KeyboardInterrupt):
        return "q"

def progress_bar(current, total, width=30):
    filled = int(width * current / total) if total > 0 else 0
    bar = "█" * filled + "░" * (width - filled)
    pct = int(100 * current / total) if total > 0 else 0
    return f"{bar} {pct}%"

def paginate(text, lines_per_page=25):
    lines = text.strip().split("\n")
    for i in range(0, len(lines), lines_per_page):
        chunk = lines[i : i + lines_per_page]
        print("\n".join(chunk))
        if i + lines_per_page < len(lines):
            info("\n[Press Enter for more, or 'q' to skip]")
            r = prompt()
            if r.lower() == "q":
                break

# ─────────────────────────────────────────────────────────────────────
# QUIZ ENGINE
# ─────────────────────────────────────────────────────────────────────

def run_quiz_question(q):
    """Run a single quiz question. Returns (correct: bool, user_answer: str)."""
    qtype = q["type"]

    if qtype == "multiple_choice":
        print(f"\n{BOLD}{q['q']}{RESET}\n")
        opts = q["options"]
        for i, opt in enumerate(opts, 1):
            print(f"  {i}) {opt}")
        ans = prompt("Your answer (number): ")
        try:
            chosen = opts[int(ans) - 1]
        except (ValueError, IndexError):
            chosen = ans
        correct = chosen == q["answer"]
        if correct:
            success("Correct!")
        else:
            error(f"Incorrect. Answer: {q['answer']}")
        if "explanation" in q:
            info(f"  💡 {q['explanation']}")
        return correct, chosen

    elif qtype == "fill_blank":
        print(f"\n{BOLD}{q['q']}{RESET}")
        ans = prompt("Your answer: ").lower().strip()
        correct = ans == q["answer"].lower()
        if correct:
            success("Correct!")
        else:
            error(f"Incorrect. Answer: {q['answer']}")
        if "explanation" in q:
            info(f"  💡 {q['explanation']}")
        return correct, ans

    elif qtype == "matching":
        print(f"\n{BOLD}{q['q']}{RESET}\n")
        items = list(q["pairs"].keys())
        values = list(q["pairs"].values())
        random.shuffle(values)
        for i, v in enumerate(values, 1):
            print(f"  {i}) {v}")
        print()
        score = 0
        total = len(items)
        for item in items:
            ans = prompt(f"  {item} → (number): ")
            try:
                chosen_val = values[int(ans) - 1]
            except (ValueError, IndexError):
                chosen_val = ""
            if chosen_val == q["pairs"][item]:
                success(f"  {item} → {chosen_val}")
                score += 1
            else:
                error(f"  {item} → should be: {q['pairs'][item]}")
        correct = score == total
        print(f"\n  Matched {score}/{total}")
        return correct, f"{score}/{total}"

    elif qtype == "scenario":
        print(f"\n{BOLD}{q['q']}{RESET}")
        print(f"\n{DIM}(Type your answer, then press Enter. This is self-assessed.){RESET}")
        ans = prompt("Your answer:\n")
        print(f"\n{YELLOW}{BOLD}SUGGESTED ANSWER:{RESET}")
        print(q["answer"])
        rating = prompt("Rate yourself: (1) Missed it  (2) Partial  (3) Nailed it: ")
        correct = rating == "3"
        return correct, ans

    return False, ""

def run_quiz(module_id, progress):
    """Run a full quiz for a module."""
    questions = QUIZZES.get(module_id, [])
    if not questions:
        info("No quiz available for this module yet.")
        return

    header(f"QUIZ: {module_id.replace('_', ' ').title()}")
    random.shuffle(questions)

    correct_count = 0
    total = len(questions)

    for i, q in enumerate(questions, 1):
        print(f"\n{DIM}Question {i}/{total}{RESET}")
        is_correct, _ = run_quiz_question(q)
        if is_correct:
            correct_count += 1

    # Score
    pct = int(100 * correct_count / total) if total > 0 else 0
    print(f"\n{'━' * 40}")
    print(f"{BOLD}Score: {correct_count}/{total} ({pct}%){RESET}")
    if pct >= 80:
        success("Excellent — module mastered!")
    elif pct >= 60:
        print(f"{YELLOW}Good progress — review weak areas.{RESET}")
    else:
        print(f"{RED}Needs work — re-read the lesson material.{RESET}")

    # Save
    progress["quiz_scores"].setdefault(module_id, []).append({
        "date": str(date.today()),
        "score": pct,
        "correct": correct_count,
        "total": total,
    })
    progress["mastery"][module_id] = max(
        progress["mastery"].get(module_id, 0), pct
    )
    save_progress(progress)

# ─────────────────────────────────────────────────────────────────────
# FLASHCARD MODE
# ─────────────────────────────────────────────────────────────────────

FLASHCARDS = [
    ("What does MMIT stand for?", "Managed Markets Insight & Technology"),
    ("What does IHD stand for?", "Instant Health Data (Panalgo's platform)"),
    ("What is a BLA?", "Biologics License Application — regulatory submission for biologic drugs"),
    ("What is step therapy?", "Payer restriction requiring patients to try/fail cheaper drugs first"),
    ("What is NorstellaLinQ?", "Integrated data asset: 74B+ data points (EMR, claims, labs, SDoH, mortality)"),
    ("What does NPV mean in pharma?", "Net Present Value — Evaluate's method for pipeline asset valuation"),
    ("What is EP Vantage?", "Evaluate's editorial arm providing data-driven pharma industry analysis"),
    ("What are clinical pathways?", "Standardized evidence-based treatment protocols guiding drug selection"),
    ("What is prior authorization?", "Payer requirement for pre-approval before covering a drug"),
    ("What does HEOR stand for?", "Health Economics and Outcomes Research"),
    ("What is a formulary?", "A list of drugs covered by a health plan, organized by tiers"),
    ("What is the IRA's impact on pharma?", "Inflation Reduction Act enables Medicare drug price negotiations"),
    ("What percentage of screened compounds get approved?", "~1 in 20,000-30,000"),
    ("What is a PBM?", "Pharmacy Benefit Manager — intermediary managing drug benefits (e.g., CVS Caremark)"),
    ("What does RWE stand for?", "Real-World Evidence — data on drug performance outside clinical trials"),
    ("What is Sitetrove?", "Citeline's investigator and clinical trial site intelligence platform"),
    ("What is Trialtrove?", "Citeline's curated clinical trial intelligence database (60,000+ sources)"),
    ("What is Pharmaprojects?", "Citeline's industry-standard drug pipeline tracking platform"),
    ("What is Contract Validation?", "MMIT's tool to crosscheck rebate offers vs. actual formulary placement"),
    ("What is LinQNotes?", "Panalgo's NLP tool for extracting insights from unstructured clinical notes"),
    ("What is Ella AI?", "Panalgo's AI assistant for natural language cohort creation, no coding needed"),
    ("Average cost to develop one approved drug?", "$2.6 billion (including failures)"),
    ("Average time from discovery to approval?", "10-15 years"),
    ("What % of Phase I trials advance?", "~70%"),
    ("What % of US oncologists use clinical pathways?", "~62%"),
    ("What is OneOncology?", "A practice aggregator standardizing pathways across community oncology"),
    ("Who is Norstella's CEO (as of 2025)?", "Kris Joshi"),
    ("What is IHD Cloud?", "AWS-powered version of Panalgo's IHD, 85% faster than traditional methods"),
    ("What is an IDN?", "Integrated Delivery Network — a health system with hospitals, clinics, and payers"),
    ("What is an NDA?", "New Drug Application — regulatory submission for small molecule drugs"),
]

def run_flashcards():
    header("FLASHCARD DRILL")
    cards = list(FLASHCARDS)
    random.shuffle(cards)

    correct = 0
    total = min(10, len(cards))  # 10 cards per session
    cards = cards[:total]

    for i, (front, back) in enumerate(cards, 1):
        print(f"\n{DIM}Card {i}/{total}{RESET}")
        print(f"\n{BOLD}{front}{RESET}")
        prompt("[Think, then press Enter to reveal]")
        print(f"\n{GREEN}{back}{RESET}")
        r = prompt("Did you know it? (y/n): ")
        if r.lower() in ("y", "yes"):
            correct += 1
            success("Got it!")
        else:
            error("Review this one again.")

    pct = int(100 * correct / total)
    print(f"\n{'━' * 40}")
    print(f"{BOLD}Flashcards: {correct}/{total} ({pct}%){RESET}")

# ─────────────────────────────────────────────────────────────────────
# SPEED ROUND
# ─────────────────────────────────────────────────────────────────────

def run_speed_round():
    header("SPEED ROUND ⚡")
    info("Answer as fast as you can! Match the brand to the description.\n")

    pairs = [
        ("Clinical trial intelligence & drug pipeline", "Citeline"),
        ("Commercial intelligence & asset valuation", "Evaluate"),
        ("Market access & payer policy data", "MMIT"),
        ("Real-world evidence analytics", "Panalgo"),
        ("Oncology market access consulting", "Dedham Group"),
        ("No-code analytics platform", "Panalgo (IHD)"),
        ("Consensus drug revenue forecasts", "Evaluate"),
        ("Formulary tracking & contract validation", "MMIT"),
        ("Clinical pathway strategy", "Dedham Group"),
        ("AI-powered trial site selection", "Citeline (Sitetrove)"),
    ]
    random.shuffle(pairs)
    pairs = pairs[:7]

    correct = 0
    start = time.time()

    for desc, answer in pairs:
        ans = prompt(f"  {desc}  →  ")
        # Flexible matching
        if answer.lower().split()[0] in ans.lower() or ans.lower() in answer.lower():
            correct += 1
            success("✓")
        else:
            error(f"→ {answer}")

    elapsed = time.time() - start
    print(f"\n{BOLD}Result: {correct}/{len(pairs)} in {elapsed:.1f}s{RESET}")

# ─────────────────────────────────────────────────────────────────────
# DAILY SESSION LOGIC
# ─────────────────────────────────────────────────────────────────────

def get_next_lesson(progress):
    """Get the next unread lesson."""
    completed = set(progress["lessons_completed"])
    for module in sorted(MODULES, key=lambda m: m["order"]):
        for lesson in module["lessons"]:
            lid = f"{module['id']}/{lesson['id']}"
            if lid not in completed:
                return module, lesson
    return None, None

def show_dashboard(progress):
    clear()
    header("NORSTELLA CUSTOMER LEARNING")

    # Streak
    today = str(date.today())
    streak = progress.get("streak_days", [])
    streak_count = 0
    if streak:
        # Count consecutive days ending today or yesterday
        from datetime import timedelta
        d = date.today()
        for s in reversed(streak):
            if s == str(d) or s == str(d - timedelta(days=1)):
                streak_count += 1
                d = date.fromisoformat(s) - timedelta(days=1)
            else:
                break
    print(f"  🔥 Streak: {streak_count} day(s)    📚 Sessions: {len(progress['sessions'])}")
    total_lessons = sum(len(m["lessons"]) for m in MODULES)
    done_lessons = len(progress["lessons_completed"])
    print(f"  📖 Lessons: {done_lessons}/{total_lessons}  {progress_bar(done_lessons, total_lessons, 20)}")
    print()

    # Module mastery
    subheader("Module Mastery")
    for module in sorted(MODULES, key=lambda m: m["order"]):
        score = progress["mastery"].get(module["id"], 0)
        status = "✓" if score >= 80 else "○"
        bar = progress_bar(score, 100, 15)
        print(f"  {status} {module['title']:<42} {bar}")

    print()

def main_menu():
    print(f"\n{BOLD}What would you like to do?{RESET}\n")
    print("  1) 📖  Continue learning (next lesson)")
    print("  2) 📝  Take a quiz")
    print("  3) 🃏  Flashcard drill")
    print("  4) ⚡  Speed round")
    print("  5) 📚  Browse all modules")
    print("  6) 📊  View progress")
    print("  q) 👋  Quit")
    return prompt("Choice: ")

# ─────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────

def main():
    progress = load_progress()
    session_start = time.time()
    today = str(date.today())

    # Track streak
    if today not in progress.get("streak_days", []):
        progress.setdefault("streak_days", []).append(today)
        save_progress(progress)

    show_dashboard(progress)

    while True:
        choice = main_menu()

        if choice == "1":
            # Next lesson
            module, lesson = get_next_lesson(progress)
            if module is None:
                success("You've completed all lessons! Try quizzes to reinforce.")
                continue
            header(f"{module['title']} → {lesson['title']}")
            paginate(lesson["content"])
            lid = f"{module['id']}/{lesson['id']}"
            if lid not in progress["lessons_completed"]:
                progress["lessons_completed"].append(lid)
                save_progress(progress)
            success(f"Lesson complete: {lesson['title']}")

            # Offer quiz
            if module["id"] in QUIZZES:
                r = prompt("Take the quiz for this module? (y/n): ")
                if r.lower() in ("y", "yes"):
                    run_quiz(module["id"], progress)

        elif choice == "2":
            # Quiz selection
            subheader("Available Quizzes")
            quiz_modules = [m for m in MODULES if m["id"] in QUIZZES]
            for i, m in enumerate(quiz_modules, 1):
                score = progress["mastery"].get(m["id"], 0)
                print(f"  {i}) {m['title']} (best: {score}%)")
            sel = prompt("Which quiz? (number): ")
            try:
                mod = quiz_modules[int(sel) - 1]
                run_quiz(mod["id"], progress)
            except (ValueError, IndexError):
                error("Invalid selection.")

        elif choice == "3":
            run_flashcards()

        elif choice == "4":
            run_speed_round()

        elif choice == "5":
            # Browse modules
            subheader("All Modules")
            for i, m in enumerate(sorted(MODULES, key=lambda x: x["order"]), 1):
                done = sum(
                    1 for l in m["lessons"]
                    if f"{m['id']}/{l['id']}" in progress["lessons_completed"]
                )
                total = len(m["lessons"])
                print(f"  {i}) {m['title']} ({done}/{total} lessons)")
            sel = prompt("Read which module? (number, or Enter to go back): ")
            if sel:
                try:
                    mod = sorted(MODULES, key=lambda x: x["order"])[int(sel) - 1]
                    for lesson in mod["lessons"]:
                        header(f"{mod['title']} → {lesson['title']}")
                        paginate(lesson["content"])
                        lid = f"{mod['id']}/{lesson['id']}"
                        if lid not in progress["lessons_completed"]:
                            progress["lessons_completed"].append(lid)
                            save_progress(progress)
                except (ValueError, IndexError):
                    error("Invalid selection.")

        elif choice == "6":
            show_dashboard(progress)

        elif choice in ("q", "Q", "quit", "exit"):
            elapsed = (time.time() - session_start) / 60
            progress["sessions"].append({
                "date": today,
                "duration_min": round(elapsed, 1),
            })
            progress["total_time_min"] = round(
                progress.get("total_time_min", 0) + elapsed, 1
            )
            save_progress(progress)
            print(f"\n{GREEN}Session: {elapsed:.1f} min | Total: {progress['total_time_min']:.0f} min{RESET}")
            print(f"{CYAN}See you tomorrow! 🚀{RESET}\n")
            break

        else:
            error("Invalid choice.")


if __name__ == "__main__":
    main()
