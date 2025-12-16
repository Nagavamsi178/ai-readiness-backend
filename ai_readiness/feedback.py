from .scoring import get_category

BUCKET_TEXT = {
    "AI Aspirant": {
        "range": "40% to 55%",
        "title": "AI Aspirant: The Foundational Stage",
        "description": (
            "You are actively identifying AI's potential but are strategically focused on building the core "
            "prerequisites: data consistency, cloud foundation, and cross-functional alignment.\n\n"
            "We Understand:\n"
            "Organizations at this stage need assurance. They need a clear path that moves them from "
            "'Maybe' to 'Must-Have.'\n\n"
            "Forgebyte's Partnership Approach:\n"
            "We don’t push large projects. We start by de-risking your investment with a Focused Discovery "
            "& Readiness POC. We deliver a rapid, contained pilot (for example, automated data "
            "classification for 1–2 core processes) to prove value quickly and create a reliable 12-month "
            "AI Blueprint. We provide the confidence you need to take the next step.\n\n"
            "Ready to establish a confident, clear foundation?\n"
            "Contact our partnership team at Assist@forgebyte.com to start your discovery."
        ),
    },

    "AI Explorer": {
        "range": "56% to 65%",
        "title": "AI Explorer: The Proof-of-Value Phase",
        "description": (
            "You have successfully run initial AI experiments or POCs, validating the technology’s "
            "potential. Your challenge now is scaling these isolated successes, integrating them across "
            "departments, and measuring true enterprise-wide ROI.\n\n"
            "We Understand:\n"
            "The risk of 'Pilot Purgatory'—where promising ideas never make it into production. Your focus "
            "shifts from proving that AI works to making it reliable, scalable, and profitable.\n\n"
            "Forgebyte's Partnership Approach:\n"
            "Our experience spans dozens of domains, from Transport & Logistics (predictive maintenance "
            "POCs) to Insurance (automated claims processing). We specialize in engineering the transition "
            "from POC to Industrialized AI Solutions. We implement robust MLOps practices, fortify data "
            "governance, and upskill your internal teams—guaranteeing stability for a long-term operational "
            "relationship.\n\n"
            "Ready to turn successful pilots into sustainable, scalable business assets?\n"
            "Contact our scaling experts at Assist@forgebyte.com to discuss your transition."
        ),
    },

    "AI Adopter": {
        "range": "66% to 80%",
        "title": "AI Adopter: The Transformation Phase",
        "description": (
            "You possess mature technical infrastructure and AI is already integrated into core business "
            "units. You are now ready to leverage advanced capabilities like Generative AI to gain a "
            "significant competitive advantage.\n\n"
            "We Understand:\n"
            "At this level, you need a partner who can challenge existing systems and drive true "
            "competitive differentiation. You require expertise not just in deployment, but also in "
            "ethical governance, responsible AI practices, and continuous optimization.\n\n"
            "Forgebyte's Partnership Approach:\n"
            "We go beyond basic implementation. Leveraging our cross-industry expertise—ranging from "
            "Healthcare (drug discovery acceleration) to Retail (hyper-personalized customer experiences)—"
            "we introduce state-of-the-art models and architectures. We act as your long-term innovation "
            "lab, focusing on optimizing cost-to-serve and proactively maintaining your AI governance "
            "framework to ensure sustained, responsible growth.\n\n"
            "Ready to future-proof your leadership position with next-generation, transformative AI?\n"
            "Engage our innovation team at Assist@forgebyte.com for a strategy session."
        ),
    },
}


def generate_narrative(assessment, raw_pct: float, capped_pct: float) -> str:
    cat = get_category(capped_pct)
    b = BUCKET_TEXT.get(cat, {})

    narrative = (
        f"Raw AI readiness score: {raw_pct:.2f}%. "
        f"Client presentation (capped) score: {capped_pct:.2f}% ({cat}).\n\n"
        f"{b.get('title', '')}\n\n"
        f"{b.get('description', '')}"
    )

    return narrative

