from math import ceil, sqrt

def spiral(n):
    """
    Shamelessly stolen from https://math.stackexchange.com/a/163101
    """
    k = ceil((sqrt(n) - 1) / 2)
    t = 2 * k + 1
    m = t ** 2
    t = t - 1
    if n >= m - t:
        return k - (m - n), -k
    m -= t
    if n >= m - t:
        return -k, -k + (m - n)
    m -= t
    if n >= m - t:
        return -k + (m - n), k
    return k, k - (m - n - t)

def day03p1(n):
    x, y = spiral(n)
    return abs(x) + abs(y)

def day03p2(n):
    values = {(0, 0): 1}
    i = 2
    while True:
        x, y = spiral(i)
        value = sum([values.get((x + m, y + n), 0) for m in range(-1, 2) for n in range(-1, 2)])
        if value >= n:
            return value
        values[(x, y)] = value
        i += 1

def main():
    with open("inputs/day03.txt") as file:
        number = int(file.readline())
        result = day03p1(number)
        print(result)
        result = day03p2(number)
        print(result)

if __name__ == "__main__":
    main()
