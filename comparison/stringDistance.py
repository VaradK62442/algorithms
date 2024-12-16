class StringDistance:
    def __init__(self, s, t, func=None):
        self.s = ' ' + s
        self.t = ' ' + t

        if func is None: self.func = self._levenshtein_distance
        else: self.func = func

        self._construct_table()
        self._populate_table()

    def __str__(self):
        res = ' |' + ' ' + '  '.join(list(self.t)) + '\n'
        res += '_' * (len(self.s)*3+4) + '\n'
        for i in range(len(self.s)):
            line = self.s[i] + '|'
            for j in range(len(self.t)):
                line += ' ' + str(self.table[i][j]) + ' '
            res += line + '\n'

        return res

    def _construct_table(self):
        self.table = [[0 for j in range(len(self.t))] for i in range(len(self.s))]
        self.traceback_table = [[None for j in range(len(self.t))] for i in range(len(self.s))]

    def _levenshtein_distance(self, s, t, i, j, table) -> tuple[int, tuple[int, int]]:
        if i == 0: return j, None
        if j == 0: return i, None

        if s[i] == t[j]:
            return table[i-1][j-1], (i-1, j-1)
        
        return 1 + min(
            table[i-1][j],
            table[i][j-1],
            table[i-1][j-1]
        ), min(
            (i-1, j),
            (i, j-1),
            (i-1, j-1),
            key=lambda x: table[x[0]][x[1]]
        )

    def _populate_table(self):
        for i in range(len(self.s)):
            for j in range(len(self.t)):
                self.table[i][j], self.traceback_table[i][j] = self.func(self.s, self.t, i, j, self.table)

    def get_distance(self):
        # traceback
        i, j = len(self.s)-1, len(self.t)-1
        entry = self.traceback_table[i][j]
        distance = 0
        steps = []

        while entry is not None:
            if entry == (i-1, j):
                steps.append(f"Delete {self.s[i]}")
            elif entry == (i, j-1):
                steps.append(f"Insert {self.t[j]}")
            elif entry == (i-1, j-1):
                if self.s[i] != self.t[j]:
                    steps.append(f"Replace {self.s[i]} with {self.t[j]}")
                else:
                    distance -= 1
                    steps.append(f"Keep {self.s[i]}")

            i, j = entry
            entry = self.traceback_table[i][j]
            distance += 1

        self.steps = steps[::-1]
        return distance