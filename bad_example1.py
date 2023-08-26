def f(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max, end = 0, 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max:
                    max = dp[i][j]
                    end = i
    start = end - max
    x = a[start:end]
    return x


a = "abcdefg"
b = "xyzdef"
result = f(a, b)
print(f(a, b))
