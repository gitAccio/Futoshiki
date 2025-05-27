class FutoshikiPuzzle:
    def __init__(self, size, grid, constraints):
        self.size = size
        self.grid = grid
        self.constraints = constraints

    def is_valid(self, row, col, num):
        for i in range(self.size):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        for (r1, c1, op, r2, c2) in self.constraints:
            val1 = self.grid[r1][c1]
            val2 = self.grid[r2][c2]

            if (r1, c1) == (row, col):
                val1 = num
            if (r2, c2) == (row, col):
                val2 = num

            if val1 is not None and val2 is not None:
                if op == '<' and not val1 < val2:
                    return False
                if op == '>' and not val1 > val2:
                    return False

        return True

    def solve(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] is None:
                    for num in range(1, self.size + 1):
                        if self.is_valid(r, c, num):
                            self.grid[r][c] = num
                            if self.solve():
                                return True
                            self.grid[r][c] = None
                    return False
        return True


def stampa_esempio():
    esempio = [
        ". . . . 2",
        "    ^    ",
        ". . .<. .",
        "  v      ",
        ". . . . .",
        "^        ",
        ".<. .>.>.",
        "v   v    ",
        "3 . . . ."
    ]
    print("Esempio formato input per n = 5 (9 righe da 9 caratteri ciascuna):")
    for i, riga in enumerate(esempio):
        print(f"riga {i}: {riga}")


def leggi_input():
    size = int(input("Dimensione griglia n (es 5): "))
    righe = []
    print(f"\nInserisci {2*size - 1} righe da {2*size - 1} caratteri ciascuna (numeri, '.', vincoli '< > ^ v' o spazi):")
    for i in range(2*size - 1):
        r = input(f"riga {i}: ")
        if len(r) != 2*size - 1:
            print(f"Errore: la riga deve contenere esattamente {2*size -1} caratteri.")
            return leggi_input()
        righe.append(r)
    return size, righe


def interpreta_griglia(size, righe):
    grid = [[None]*size for _ in range(size)]
    constraints = []

    for r in range(2*size - 1):
        for c in range(2*size - 1):
            ch = righe[r][c]

            if r % 2 == 0 and c % 2 == 0:
                if ch == '.':
                    grid[r//2][c//2] = None
                elif ch.isdigit():
                    grid[r//2][c//2] = int(ch)
                else:
                    raise ValueError(f"Carattere non valido in cella: '{ch}' in riga {r} colonna {c}")

            elif r % 2 == 0 and c % 2 == 1:
                if ch in ('<', '>'):
                    row = r // 2
                    c1 = c // 2
                    c2 = c1 + 1
                    constraints.append((row, c1, ch, row, c2))

            elif r % 2 == 1 and c % 2 == 0:
                if ch in ('^', 'v'):
                    r1 = (r - 1)//2
                    r2 = r1 + 1
                    col = c // 2
                    if ch == '^':
                        constraints.append((r1, col, '>', r2, col))
                    else:
                        constraints.append((r1, col, '<', r2, col))

    return grid, constraints


def stampa_soluzione(grid):
    size = len(grid)
    for r in range(size):
        print(" ".join(str(cell) if cell is not None else "." for cell in grid[r]))


if __name__ == "__main__":
    print("=== Futoshiki Solver ===\n")
    stampa_esempio()
    print()
    size, righe = leggi_input()
    try:
        grid, constraints = interpreta_griglia(size, righe)
    except ValueError as e:
        print("Errore input:", e)
        exit(1)

    puzzle = FutoshikiPuzzle(size, grid, constraints)
    if puzzle.solve():
        print("\nSoluzione trovata:")
        stampa_soluzione(puzzle.grid)
    else:
        print("\nNessuna soluzione trovata.")
