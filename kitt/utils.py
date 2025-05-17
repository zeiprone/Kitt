def summarize_scores(scores):
    values = list(map(lambda x: x['score'], scores))
    high_scores = list(filter(lambda s: s > 7, values))
    print(f"Toplam drift: {len(values)}, 8+ puanlı drift sayısı: {len(high_scores)}")
    return high_scores