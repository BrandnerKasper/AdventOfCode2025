def parse_joltage_banks(file: str) -> list[str]:
    banks = []
    with open(file, "r") as f:
        for l in f:
            banks.append(l.rstrip())
    return banks


def calculate_highest_joltage(bank: str) -> int:
    nums = [int(num) for num in bank]
    first = 0
    first_idx = 0
    for i in range(0, len(nums)-1):
        if nums[i] > first:
            first = nums[i]
            first_idx = i
    second = 0
    for i in range(first_idx+1, len(nums)):
        n = nums[i]
        if n > second:
            second = n
    return first * 10 + second


def sum_joltage_banks(banks: list[str]) -> int:
    s = 0
    for b in banks:
        s += calculate_highest_joltage(b)
    return s


def main() -> None:
    f = "joltage_banks.txt"
    banks = parse_joltage_banks(f)
    print(f"The sum of the best possible two number combination per bank is: {sum_joltage_banks(banks)}")


if __name__ == "__main__":
    main()
