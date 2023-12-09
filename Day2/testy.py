test_list = ['B X', 'C Y', 'A X', 'B X']

def strat_score():
    cum_score = 0
    dataset = test_list
    for line in dataset:
        if line == 'A X':
            print("you got it")
    return cum_score

print(strat_score())