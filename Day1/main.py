from collections import Counter
import sys


def solution(s, l):
    s_count = Counter(s)
    s_keys = list(s_count.keys())
    s_values = list(s_count.values())
    max_val = 0

    for i in range(len(l)):
        l_count = Counter(l[i])
        l_keys = list(l_count.keys())
        l_values = list(l_count.values())
        min_val = sys.maxsize

        if l_keys:
            for j in range(len(l_keys)):
                if l_keys[j] in s_keys:
                    element = s_keys.index(l_keys[j])
                    min_val = min(s_values[element]//l_values[j], min_val)
            if min_val != sys.maxsize:
                max_val = max(max_val, min_val)

    return max_val


def main():
    S = "BILLOBILLOLLOBBIIBBBBOLLL"
    L = ["BILLL", "BOB", "A"]

    print(solution(S, L))


main()
