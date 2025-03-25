import sys

def main():
    n_row, n_col = map(int, sys.stdin.readline().split())
    if not (0 <= n_row <= 100) or not (0 <= n_col <= 100):
        raise ValueError('N < 1 or N > 100. Write numbers between 1 and 100, inclusive.')
    
    matrix = []
    for _ in range(n_row):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)
    
    dp = [[0] * n_col for _ in range(n_row)]
    dp[0][0] = matrix[0][0]
    
    for i in range(1, n_col):
        dp[0][i] = dp[0][i - 1] + matrix[0][i]
    for i in range(1, n_row):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
    
    for i in range(1, n_row):
        for j in range(1, n_col):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
    
    path = []
    i, j = n_row - 1, n_col - 1
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if dp[i - 1][j] > dp[i][j - 1]:
                path.append('D')
                i -= 1
            else:
                path.append('R')
                j -= 1
        elif i > 0:
            path.append('D')
            i -= 1
        else:
            path.append('R')
            j -= 1
    
    path.reverse()
    print(dp[-1][-1])
    print(' '.join(path))

if __name__ == "__main__":
    main()
