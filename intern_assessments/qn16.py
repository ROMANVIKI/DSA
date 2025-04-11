def mergeOverlappingIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    sol_arr = []
    for i in range(len(intervals)):
        try:
            if intervals[i][end] in range(
                intervals[i + 1][start], intervals[i + 1][end]
            ):
                sol_arr.append([intervals[i][start], intervals[i + 1][end]])
        except IndexError:
            continue

    return sol_arr


print(mergeOverlappingIntervals(intervals=[[1, 3], [2, 4], [5, 7], [6, 8]]))


def mergeOverlappingIntervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


# Example usage
print(mergeOverlappingIntervals([[1, 3], [2, 4], [5, 7], [6, 8]]))
