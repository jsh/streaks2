from streaks2.streaks import KvStreaks


def print_kv_streaks(n):
    for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
        print(kv_streaks)


if __name__ == "__main__":
    n = 3
    print_kv_streaks(n)


# def all_streaks(n):
#     for perm in permutations(range(1, n + 1)):
#         streaks = sts.Streaks(perm)
#         yield streaks.streaks


# # count len(streaks) across all permutations of range(1, n+1)
# def streak_count(n):
#     streak_counts = Counter()
#     for streaks in all_streaks(n):
#         streak_counts[len(streaks)] += 1
#     return dict(sorted(streak_counts.items()))


# def kv_streak_count(n):
#     kv_streak_counts = Counter()
#     for kv_streaks in all_kv_streaks(n):
#         kv_streak_counts[len(kv_streaks)] += 1
#     return dict(sorted(kv_streak_counts.items()))

# for i in range(9, 12):
#     start_time = time.perf_counter()
#     print(f"{streak_count(i)=}")
#     end_time = time.perf_counter()
#     elapsed_time = end_time - start_time
#     print(f"Elapsed time: {elapsed_time:.6f} seconds")
#     start_time = time.perf_counter()
#     print(f"{kv_streak_count(i)=}")
#     end_time = time.perf_counter()
#     elapsed_time = end_time - start_time
#     print(f"Elapsed time: {elapsed_time:.6f} seconds")


# start_time = time.perf_counter()
# kv_streaks = sts.KvStreaks(range(1, 1000001))
# print(f"{len(keys(kv_streaks))=}")
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time:.6f} seconds")
