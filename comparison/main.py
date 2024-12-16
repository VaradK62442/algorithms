from stringDistance import StringDistance

from pprint import pprint as pp


def main():
    s = "abadcdb"
    t = "acbacacb"

    sd = StringDistance(s, t)
    print(sd)
    print(f"Distance: {sd.get_distance()}")
    print(f"Steps: {sd.steps}")

    print()
    print()

    s = "agcgatc"
    t = "ctacgaccg"

    def lcs(s, t, i, j, table) -> tuple[int, tuple[int, int]]:
        if i == 0: return 0, None
        if j == 0: return 0, None

        if s[i] == t[j]:
            return 1 + table[i-1][j-1], (i-1, j-1)
        
        return max(
            table[i-1][j],
            table[i][j-1]
        ), max(
            (i-1, j),
            (i, j-1),
            key=lambda x: table[x[0]][x[1]]
        )
    
    sd = StringDistance(s, t, func=lcs)
    print(sd)
    print(f"Longest Common Subsequence length: {sd.table[-1][-1]}")


if __name__ == '__main__':
    main()