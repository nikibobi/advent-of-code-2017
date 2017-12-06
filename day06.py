def day06(banks):
    history = list()
    iterations = 0
    n = len(banks)
    next = lambda i: (i + 1) % n

    while True:
        m = max(range(n), key=lambda i: banks[i])
        blocks = banks[m]
        banks[m] = 0
        i = next(m)
        for _ in range(blocks):
            banks[i] += 1
            i = next(i)
        iterations += 1

        entry = str(banks)
        if entry in history:
            index = iterations - history.index(entry) - 1
            break
        history.append(entry)

    return iterations, index

def main():
    with open("inputs/day06.txt") as file:
        banks = [int(i) for i in file.readline().split('\t')]
        result = day06(banks)
        print(result[0])
        print(result[1])

if __name__ == "__main__":
    main()
