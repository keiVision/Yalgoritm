import sys

class Solve:
    def __init__(self):
        self.n_row = None
        self.n_col = None
        self.matrix = []
    
    def listen_input(self):
        self.n_row, self.n_col = map(int, sys.stdin.readline().split())
        if self.test_matrix_demension():
            for row_idx in range(0, self.n_row):
                row = list(map(int, sys.stdin.readline().split()))
                self.matrix.append(row)
        if self.test_weights_limit(self.matrix):
           pass

    def test_matrix_demension(self) -> bool:
        if not (self.n_row >= 1 and self.n_row <= 20) or not ((self.n_col >= 1 and self.n_col <= 20)):
            raise ValueError('N < 1 or N > 20. Write number between 1 and 20, include this range.')
        return True
    
    def test_weights_limit(self, matrix) -> bool:
        for row in matrix:
            for w in row:
                if (w > 100 or w < 0):
                    raise ValueError('W < 0 or W > 100. Write weight number between 1 and 100, include this range.')
        return True
    
    def solve(self) -> int:
        null_matrix = [[0] * self.n_col for _ in range(self.n_row)]
        null_matrix[0][0] = self.matrix[0][0]
        for j in range(1, self.n_col):
            null_matrix[0][j] = null_matrix[0][j - 1] + self.matrix[0][j]
        for i in range(1, self.n_row):
            null_matrix[i][0] = null_matrix[i - 1][0] + self.matrix[i][0]
        for i in range(1, self.n_row):
            for j in range(1, self.n_col):
                null_matrix[i][j] = min(null_matrix[i - 1][j], null_matrix[i][j - 1]) + self.matrix[i][j]
        return null_matrix[-1][-1]

def main():
    solver = Solve()
    solver.listen_input()
    answer = solver.solve()
    print(answer)
    return answer

if __name__ == "__main__":
    main()