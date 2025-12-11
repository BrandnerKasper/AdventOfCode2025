def parse_id_ranges(id_ranges: str) -> list[tuple[int, int]]:
    l = []
    for id_range in id_ranges.splitlines():
        start, end = id_range.split("-")
        l.append((int(start), int(end)))
    return l


def fresh(id_ranges: str, food_id: str) -> bool:
    f = False
    # parse id ranges
    id_ranges = parse_id_ranges(id_ranges)
    fresh_ranges = []
    # loop through each range
    for id_range in id_ranges:
        # determine if fresh
        start, end = id_range[0], id_range[1]
        if start <= int(food_id) <= end:
            f = True
            # save ranges
            fresh_ranges.append(f"{start}-{end}")
    # print
    f_s = "fresh" if f else "spoiled"
    print(f"Ingredient ID {food_id} is {f_s}. The range is: {fresh_ranges}")
    return f


def parse_food_ids(food_ids: str) -> list[str]:
    l = []
    for food_id in food_ids.splitlines():
        l.append(food_id)
    return l


def count_fresh_ingredients(ingredients_data: str) -> int:
    id_ranges, food_ids = ingredients_data.split("\n\n")
    food_ids = parse_food_ids(food_ids)
    count = 0
    for food_id in food_ids:
        count += fresh(id_ranges, food_id)
    return count


def parse_ingredients_database(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def main() -> None:
    file = "ingredients_data.txt"
    file = parse_ingredients_database(file)
    count = count_fresh_ingredients(file)
    print(f"{count} amount of ingredients are fresh!")


if __name__ == "__main__":
    main()

