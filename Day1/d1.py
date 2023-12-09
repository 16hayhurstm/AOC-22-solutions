def get_input():
    with open("Data.d1.txt") as file:
        return file.readlines()
print(get_input())




def part_1():
    max_calories1 = 0
    max_calories2 = 0
    max_calories3 = 0
    current_calories = 0
    data = get_input()
    for line in data:
        if line != "\n":
            current_calories += int(line)
        else:
            if current_calories > max_calories1:
                max_calories2 = max_calories1
                max_calories1 = current_calories
            elif current_calories > max_calories2:
                max_calories3 = max_calories2
                max_calories2 = current_calories
            elif current_calories > max_calories3:
                max_calories3 = current_calories
            current_calories = 0

    return max_calories1 + max_calories2 + max_calories3

if __name__ == "__main__":
    print(part_1())

