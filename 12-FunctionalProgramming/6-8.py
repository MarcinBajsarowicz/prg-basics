
scores = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]


def min_pts(limit):
    return lambda pts: pts >= limit


limits = [70, 40, 30]

for limit in limits:
    result = list(filter(min_pts(limit), scores))
    print(f"Min {limit} pts: {result}")
