def parse_id_ranges(file: str) -> list[str]:
    with open(file, "r") as f:
        for l in f:
            id_ranges = l.split(",")
    return id_ranges


def get_invalid_ids(id_range: str) -> list[int]:
    start, end = id_range.split("-")
    start, end = int(start), int(end)
    invalid_ids = []
    for ID in range(start, end+1):
        id_str = str(ID)
        c = 1
        while c != len(id_str):
            sub, rest = id_str[:c], id_str[c:]
            if sub == rest:
                invalid_ids.append(ID)
            c += 1
    return invalid_ids


def sum_invalid_ids(id_ranges: list[str]) -> int:
    s = 0
    for id_range in id_ranges:
        invalid_ids = get_invalid_ids(id_range)
        print(f"Range {id_range} has {len(invalid_ids)} IDs: [{"".join(f"{str(ID),}" for ID in invalid_ids)}]")
        for invalid_id in invalid_ids:
            s += invalid_id
    return s


def main() -> None:
    f = "id_ranges.txt"
    # parse all the id ranges
    id_ranges = parse_id_ranges(f)
    print(f"The sum of all these invalid IDs is: {sum_invalid_ids(id_ranges)}")


if __name__ == "__main__":
    main()
