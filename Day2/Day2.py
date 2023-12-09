def D2input():
    with open("input.txt") as file:
        return file.readlines()

fileobj = open("input.txt")
lines=[]
for line in fileobj:
    lines.append(line.strip())
print(lines)

def strat_score():
    cum_score = 0
    dataset = lines
    print(dataset)
    for line in dataset:
        if line == "A Z" or line == "B X" or line == "C Y":
            cum_score = cum_score
        elif line == "A Y" or line == "B Z" or line == "C X":
            cum_score += 6
        else:
            cum_score += 3
    return cum_score

if __name__ == "__main__":
    print(strat_score())

def choice_score():
    c_score = 0
    dataset = lines
    for line in dataset:
        if line == "A X" or line == "B X" or line == "C X":
            c_score += 1
        elif line == "A Y" or line == "C Y" or line == "B Y":
            c_score += 2
        else:
            c_score += 3
    return c_score


if __name__ == "__main__":
    print(choice_score())

print(4155 + 4778)
