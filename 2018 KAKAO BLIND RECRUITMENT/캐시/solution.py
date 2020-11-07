def get_least_recently_used_item(cache):
    item = sorted(cache.items(), key=lambda x: x[1])[0][0]
    return item


def solution(cacheSize, cities):
    cache = dict()
    time = 0
    for idx, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            time += 1
            cache[city] = idx
        else:
            time += 5
            if not cacheSize:
                continue

            if len(cache) < cacheSize:
                cache[city] = idx
            else:
                item_lru = get_least_recently_used_item(cache)
                cache.pop(item_lru)
                cache[city] = idx

    return time


if __name__ == "__main__":
    cacheSize = 3
    ciites = [
        'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA',
        'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'
    ]
