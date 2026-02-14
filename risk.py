def score_url(url):
    score = 0

    if "?" in url:
        score += 2

    risky_keywords = ["login", "admin", "cart", "user", "search"]
    for k in risky_keywords:
        if k in url.lower():
            score += 1

    if url.startswith("http://"):
        score += 2

    if score >= 4:
        return "High Risk"
    elif score >= 2:
        return "Medium Risk"
    else:
        return "Low Risk"