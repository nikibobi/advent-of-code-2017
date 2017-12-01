def day01(digits, step=1):
    n = len(digits)
    s = 0
    for i in range(n):
        j = (i + step) % n
        if digits[i] == digits[j]:
            s += int(digits[i])
    return s

def main():
    with open("day01.txt") as file:
        digits = file.readline()
        result = day01(digits, 1)
        print(result)
        result = day01(digits, len(digits) // 2)
        print(result)

if __name__ == "__main__":
    main()
