from typing import Dict, List

RATED_QIDS = [f"Q{i}" for i in range(1, 16)]
MAX_SCORE_PER_Q = 5.0
TOTAL_MAX = MAX_SCORE_PER_Q * len(RATED_QIDS)  # 75.0


def compute_raw_percentage_from_numeric_scores(scores: Dict[str, int]) -> float:
    """
    scores: dict { "Q1": 4, "Q2": 3, ... }
    returns raw percentage 0..100
    """
    total = 0.0
    count = 0
    for q in RATED_QIDS:
        v = scores.get(q)
        if v is None:
            continue
        try:
            v = float(v)
        except Exception:
            continue
        total += v
        count += 1

    # compute relative to TOTAL_MAX (75) to keep consistent scale
    raw_pct = (total / TOTAL_MAX) * 100.0
    return round(raw_pct, 2)


# Capping rule: floor 40%, ceiling 80%
def apply_capping(raw_pct: float) -> float:
    if raw_pct < 40.0:
        return 40.0
    if raw_pct > 80.0:
        return 80.0
    return round(raw_pct, 2)


# Category mapping based on capped score
def get_category(capped_pct: float) -> str:
    if 40.0 <= capped_pct <= 55.0:
        return "AI Aspirant"
    if 56.0 <= capped_pct <= 65.0:
        return "AI Explorer"
    # 66-80
    return "AI Adopter"
