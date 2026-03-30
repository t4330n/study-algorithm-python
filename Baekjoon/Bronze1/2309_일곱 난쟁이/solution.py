lengths = sorted([int(input()) for _ in range(9)])
result = []


def solve():
    for a in range(9 - 6):
        for b in range(a + 1, 9 - 5):
            for c in range(b + 1, 9 - 4):
                for d in range(c + 1, 9 - 3):
                    for e in range(d + 1, 9 - 2):
                        for f in range(e + 1, 9 - 1):
                            for g in range(f + 1, 9 - 0):
                                total_length = lengths[a] + lengths[b] + lengths[c] + lengths[d] + lengths[e] + lengths[
                                    f] + \
                                               lengths[g]
                                if total_length == 100:
                                    result.append(lengths[a])
                                    result.append(lengths[b])
                                    result.append(lengths[c])
                                    result.append(lengths[d])
                                    result.append(lengths[e])
                                    result.append(lengths[f])
                                    result.append(lengths[g])
                                    return


solve()
for length in result:
    print(length)
