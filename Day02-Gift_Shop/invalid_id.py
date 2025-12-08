import re


def parse_id_ranges(file: str) -> list[str]:
    with open(file, "r") as f:
        for l in f:
            id_ranges = l.split(",")
    return id_ranges


def get_invalid_ids(id_range: str, part_1: bool) -> list[int]:
    start, end = id_range.split("-")
    start, end = int(start), int(end)
    invalid_ids = set()
    if part_1:
        check = lambda s, r: s == r
    else:
        check = lambda s, r: re.sub(s, '', r) == ""
    for ID in range(start, end + 1):
        id_str = str(ID)
        c = 1
        while c != len(id_str):
            sub, rest = id_str[:c], id_str[c:]
            if check(sub, rest):
                invalid_ids.add(ID)
            c += 1
    invalid_ids = list(invalid_ids)
    invalid_ids.sort()
    return invalid_ids


def sum_invalid_ids(id_ranges: list[str], part_1: bool) -> int:
    s = 0
    for id_range in id_ranges:
        invalid_ids = get_invalid_ids(id_range, part_1)
        print(f"Range {id_range} has {len(invalid_ids)} IDs: [{"".join(f"{str(ID),}" for ID in invalid_ids)}]")
        for invalid_id in invalid_ids:
            s += invalid_id
    return s


def main() -> None:
    f = "id_ranges.txt"
    id_ranges = parse_id_ranges(f)
    print(f"The sum of all these invalid IDs is: {sum_invalid_ids(id_ranges, False)}")


if __name__ == "__main__":
    main()
