def day05(lines, cond):
    offsets = [int(line) for line in lines]
    n = 0
    i = 0
    while i >= 0 and i < len(offsets):
        offset = offsets[i]
        if cond(offset):
            offsets[i] -= 1
        else:
            offsets[i] += 1
        i += offset
        n += 1
    return n

def main():
    with open("inputs/day05.txt") as file:
        lines = file.readlines()
        result = day05(lines, lambda offset: False)
        print(result)
        result = day05(lines, lambda offset: offset >= 3)
        print(result)

if __name__ == "__main__":
    main()
