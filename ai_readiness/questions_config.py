QUESTIONS = [
    # -----------------------------
    # 1. Prioritization, Budget & Timeline
    # -----------------------------
    {
        "id": "Q1",
        "section": "Prioritization, Budget & Timeline",
        "label": "How important is AI adoption for your business in the next 12 months?",
        "type": "single_choice",
        "options": [
            "No clear interest",
            "Exploring but unsure",
            "Some interest with initial discussions",
            "Actively planning AI initiatives",
            "AI adoption is a top strategic priority"
        ],
    },
    {
        "id": "Q2",
        "section": "Prioritization, Budget & Timeline",
        "label": "What is your organization’s available budget for AI initiatives?",
        "type": "single_choice",
        "options": [
            "No dedicated budget",
            "Small experimental budget",
            "Moderate budget with approvals",
            "Budget allocated for multiple pilots",
            "Strong budget commitment for scaling AI"
        ],
    },
    {
        "id": "Q3",
        "section": "Prioritization, Budget & Timeline",
        "label": "Timeline for starting your first AI project?",
        "type": "single_choice",
        "options": [
            "No timeline / not planned",
            "6–12 months",
            "3–6 months",
            "Within 1–3 months",
            "Immediate (ready to begin)"
        ],
    },

    # -----------------------------
    # 2. Technical, Data & Cloud Readiness
    # -----------------------------
    {
        "id": "Q4",
        "section": "Technical, Data & Cloud Readiness",
        "label": "How mature is your current data infrastructure?",
        "type": "single_choice",
        "options": [
            "Scattered spreadsheets / unstructured data",
            "Basic databases but low standardization",
            "Some central repositories (CRM/ERP)",
            "Well-structured, accessible datasets",
            "Mature data warehouse / lake with governance"
        ],
    },
    {
        "id": "Q5",
        "section": "Technical, Data & Cloud Readiness",
        "label": "How clean and usable is your data for AI models?",
        "type": "single_choice",
        "options": [
            "Highly inconsistent / incomplete",
            "Needs major cleaning",
            "Moderate consistency",
            "Mostly clean and reliable",
            "High-quality, validated, AI-ready data"
        ],
    },
    {
        "id": "Q6",
        "section": "Technical, Data & Cloud Readiness",
        "label": "How ready is your cloud infrastructure for AI workloads?",
        "type": "single_choice",
        "options": [
            "Completely on-prem with no cloud",
            "Limited cloud adoption",
            "Hybrid cloud with basic readiness",
            "Strong cloud integration",
            "Fully cloud-native & optimized for AI"
        ],
    },

    # -----------------------------
    # 3. Service Mapping & Pain Points
    # -----------------------------
    {
        "id": "Q7",
        "section": "Service Mapping & Pain Points",
        "label": "How well have you identified key business problems where AI can help?",
        "type": "single_choice",
        "options": [
            "No clarity",
            "Only broad ideas",
            "Some mapped pain points",
            "Clear problems identified",
            "Fully defined AI use cases"
        ],
    },
    {
        "id": "Q8",
        "section": "Service Mapping & Pain Points",
        "label": "How urgent are the business challenges that AI can solve?",
        "type": "single_choice",
        "options": [
            "No urgency",
            "Low urgency",
            "Moderate impact challenges",
            "High-impact challenges",
            "Critical challenges needing immediate AI intervention"
        ],
    },
    {
        "id": "Q9",
        "section": "Service Mapping & Pain Points",
        "label": "How aligned are your internal teams on AI adoption?",
        "type": "single_choice",
        "options": [
            "No alignment",
            "Minimal alignment",
            "Partial alignment",
            "Good alignment across teams",
            "Full organizational alignment"
        ],
    },

    # -----------------------------
    # 4. Automation & Process Maturity
    # -----------------------------
    {
        "id": "Q10",
        "section": "Automation & Process Maturity",
        "label": "What is your current automation level in business processes?",
        "type": "single_choice",
        "options": [
            "Mostly manual",
            "Few automated processes",
            "Some automation but inconsistent",
            "Well-automated key processes",
            "Highly automated with workflows & tools"
        ],
    },
    {
        "id": "Q11",
        "section": "Automation & Process Maturity",
        "label": "How standardized are your internal processes?",
        "type": "single_choice",
        "options": [
            "No standardization",
            "Minimal standard SOPs",
            "Partially standardized",
            "Mostly standardized",
            "Fully standardized & measurable"
        ],
    },
    {
        "id": "Q12",
        "section": "Automation & Process Maturity",
        "label": "How comfortable is your workforce with automation tools?",
        "type": "single_choice",
        "options": [
            "No experience",
            "Very limited experience",
            "Some experience with guidance",
            "Good comfort level",
            "Highly skilled & automation-friendly"
        ],
    },

    # -----------------------------
    # 5. Client Business Overview
    # -----------------------------
    {
        "id": "Q13",
        "section": "Client Business Overview",
        "label": "How stable and scalable is your business model for AI?",
        "type": "single_choice",
        "options": [
            "Unstable / early stage",
            "Evolving without clarity",
            "Moderately stable",
            "Strong foundation",
            "Highly scalable and AI-ready"
        ],
    },
    {
        "id": "Q14",
        "section": "Client Business Overview",
        "label": "What is leadership commitment towards AI?",
        "type": "single_choice",
        "options": [
            "No leadership backing",
            "Very limited backing",
            "Moderate interest",
            "Good support",
            "Strong leadership commitment"
        ],
    },
    {
        "id": "Q15",
        "section": "Client Business Overview",
        "label": "How prepared are you to adopt changes brought by AI?",
        "type": "single_choice",
        "options": [
            "Very resistant",
            "Some resistance",
            "Neutral / open",
            "Open with strong interest",
            "Fully adaptable & ready for change"
        ],
    },

    # -----------------------------
    # Additional Details
    # -----------------------------
    {
        "id": "AUTOMATION_AREAS",
        "section": "Additional Details",
        "label": "Which areas are you looking to automate?",
        "type": "multi_choice",
        "options": [
            "Finance",
            "HR",
            "Operations",
            "Customer Support",
            "IT Processes",
            "Sales & Marketing",
            "Procurement / Supply Chain",
            "Legal / Compliance",
            "Other"
        ],
    },
    {
        "id": "INDUSTRY",
        "section": "Additional Details",
        "label": "Which Industry Defines you better?",
        "type": "single_choice",
        "options": [
            "Banking & Financial Services",
            "Insurance",
            "Healthcare & HealthTech",
            "Pharma / Med Devices",
            "Technology / IT Services",
            "Media / Entertainment / Telecom",
            "Retail & E-commerce",
            "Manufacturing",
            "Transport & Logistics",
            "Energy & Utilities",
            "Construction",
            "Real Estate",
            "Hospitality",
            "Food & Beverages",
            "Education / EdTech",
            "On-Demand Platforms",
            "Professional Services",
            "Government / Public Sector",
        ],
    },
    {
        "id": "USE_CASE",
        "section": "Additional Details",
        "label": "Which AI use case would you like to prioritize?",
        "type": "text",
    },
]
