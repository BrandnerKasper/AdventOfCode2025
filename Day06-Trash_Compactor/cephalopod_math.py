def parse_homework(sheet: str) -> list[list[str]]:
    numbers_list = []
    for l in sheet.splitlines():
        numbers = l.split()
        numbers_list.append(numbers)
    exercises = []
    for num in numbers_list[0]:
        exercise = [num]
        exercises.append(exercise)
    for i in range(1, len(numbers_list)):
        for j in range(0, len(numbers_list[i])):
            exercises[j].append(numbers_list[i][j])
    return exercises


def mul(nums: list[int]) -> int:
    res = 1
    for num in nums:
        res *= num
    return res


def calc_exercise(exercise: list[str]) -> int:
    nums, sign = exercise[:-1], exercise[-1:]
    nums = [int(num) for num in nums]
    sign = sign[0]
    res = 0
    match sign:
        case "+":
            res = sum(nums)
        case "*":
            res = mul(nums)
    return res


def do_homework(homework: str) -> int:
    exercises = parse_homework(homework)
    solutions = [calc_exercise(ex) for ex in exercises]
    return sum(solutions)


def main() -> None:
    file = "homework.txt"
    with open(file, "r") as f:
        homework =  f.read()
    sol = do_homework(homework)
    print(f"The sum of the solutions of the homework is: {sol}")


if __name__ == "__main__":
    main()
