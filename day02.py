import numpy as np

def day02p1(table):
    return np.sum(table.max(axis=1) - table.min(axis=1))

def day02p2(table):
    checksum = 0
    for row in table:
        for i, m in enumerate(row):
            for n in row[i + 1:]:
                a = max(m, n)
                b = min(m, n)
                if a % b == 0:
                    checksum += a // b
                    break
            else:
                continue
            break
    return checksum

def main():
    table = np.genfromtxt("inputs/day02.txt", delimiter='\t', dtype=np.int64)
    result = day02p1(table)
    print(result)
    result = day02p2(table)
    print(result)

if __name__ == "__main__":
    main()
