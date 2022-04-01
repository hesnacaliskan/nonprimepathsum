def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def sum_path(n, m):
    if (n >= len(triangle)):
        return 0
    if (is_prime(triangle[n][m])):
        return 0
    else:
        return triangle[n][m] + max(sum_path(n + 1, m), sum_path(n + 1, m + 1))

triangle = [
    [1],
    [8,4],
    [2,6,9],
    [8,5,9,3]
]

print(sum_path(0, 0))