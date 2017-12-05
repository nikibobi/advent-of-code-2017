def valid1(words):
    return len({*words}) == len(words)

def valid2(words):
    return len({''.join(sorted(word)) for word in words}) == len(words)

def day04(lines, valid):
    return len([line for line in lines if valid(line.rstrip().split(' '))])

def main():
    with open("inputs/day04.txt") as file:
        lines = file.readlines()
        result = day04(lines, valid1)
        print(result)
        result = day04(lines, valid2)
        print(result)

if __name__ == "__main__":
    main()
