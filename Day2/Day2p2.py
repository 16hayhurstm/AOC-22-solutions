fileobj = open("input.txt")
lines=[]
for line in fileobj:
    lines.append(line.strip())

def out_score():
    outcome_score = 0
    dataset = lines
    for line in dataset:
        if line == "A X" or line == "B X" or line == "C X":
            outcome_score = outcome_score
        elif line == "A Y" or line == "B Y" or line == "C Y":
            outcome_score +=3
        else:
            outcome_score +=6
    return outcome_score

if __name__ == "__main__":
    print(out_score())

def opt_score():
    option_score = 0
    dataset = lines
    for line in dataset:
        if line == "A Y" or line == "B X" or line == "C Z":
            option_score += 1
        elif line == "A Z" or line == "B Y" or line == "C X":
            option_score += 2
        else:
            option_score += 3
    return option_score

if __name__ == "__main__":
    print(opt_score())

print(6834 + 5164)

