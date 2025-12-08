def parse_joltage_banks(file: str) -> list[str]:
    banks = []
    with open(file, "r") as f:
        for l in f:
            banks.append(l.rstrip())
    return banks


# def calculate_highest_joltage_part_1(bank: str) -> int:
#     nums = [int(num) for num in bank]
#     first = 0
#     first_idx = 0
#     for i in range(0, len(nums)-1):
#         if nums[i] > first:
#             first = nums[i]
#             first_idx = i
#     second = 0
#     for i in range(first_idx+1, len(nums)):
#         n = nums[i]
#         if n > second:
#             second = n
#     return first * 10 + second


def calculate_highest_joltage(bank: str, max_digits: int) -> int:
    nums = [int(num) for num in bank]
    digits = []
    idx = -1
    for i in reversed(range(0, max_digits)):
        digit = 0
        for j in range(idx+1, len(nums)-i):
            if nums[j] > digit:
                digit = nums[j]
                idx = j
        digits.append(digit)
    return digits_to_num(digits)


def digits_to_num(digits: list[int]) -> int:
    res = 0
    c = 0
    for d in digits:
        c += 1
        res += pow(10, len(digits)-c) * d
    return res


def sum_joltage_banks(banks: list[str], max_digits: int) -> int:
    s = 0
    for b in banks:
        s += calculate_highest_joltage(b, max_digits)
    return s



def main() -> None:
    f = "joltage_banks.txt"
    banks = parse_joltage_banks(f)
    max_digits = 12
    print(f"The sum of the best possible {max_digits} number combination per bank is: {sum_joltage_banks(banks, max_digits)}")


if __name__ == "__main__":
    main()
