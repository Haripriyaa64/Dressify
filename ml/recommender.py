

MOOD_COLOR_MAP = {
    "happy": ["yellow", "orange", "pink", "red", "light blue"],
    "calm": ["blue", "light blue", "lavender", "green", "grey", "white"],
    "confident": ["black", "red", "dark red", "navy", "indigo"],
    "romantic": ["pink", "red", "blush", "purple", "lavender"],
    "energetic": ["orange", "yellow", "red", "green"],
    "elegant": ["black", "navy", "white", "grey", "dark green"],
    "sad": ["grey", "blue", "navy", "black"],
    "playful": ["pink", "yellow", "orange", "light blue", "green"],
}

OCCASION_TYPE_MAP = {
    "party": ["party", "casual", "ethnic"],
    "formal": ["formal", "business"],
    "casual": ["casual", "streetwear"],
    "wedding": ["ethnic", "formal", "party"],
    "date": ["party", "casual", "formal"],
    "work": ["formal", "business", "casual"],
    "festive": ["ethnic", "party"],
    "outdoor": ["casual", "streetwear", "sportswear"],
}


def recommend(dresses, mood=None, occasion=None, wear_type=None):
    results = []

    for d in dresses:
        score = 0
        reasons = []

        # Wear type match (strong signal)
        if wear_type and d['wear_type'].lower() == wear_type.lower():
            score += 10
            reasons.append(f"Matches wear type: {wear_type}")

        # Occasion/dress_type match
        if occasion:
            allowed_types = OCCASION_TYPE_MAP.get(occasion.lower(), [occasion.lower()])
            if d['dress_type'].lower() in allowed_types:
                score += 8
                reasons.append(f"Fits {occasion}")
            elif d['dress_type'].lower() == occasion.lower():
                score += 8

        # Mood-color match
        if mood:
            preferred_colors = MOOD_COLOR_MAP.get(mood.lower(), [])
            dress_colors = [c.strip().lower() for c in d['color'].split(',')]
            matched = [c for c in dress_colors if c in preferred_colors]
            if matched:
                score += 5 * len(matched)
                reasons.append(f"Color matches {mood} mood")

        results.append((d, score, reasons))

    # Sort by score descending, randomize ties slightly for variety
    results.sort(key=lambda x: x[1], reverse=True)
    return [(d, score) for d, score, _ in results]
