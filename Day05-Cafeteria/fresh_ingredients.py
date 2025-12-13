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


def get_fresh_ingredients_ids(id_ranges: list[tuple[int, int]]) -> list[int]:
    id_set = set()
    for id_range in id_ranges:
        start, end = id_range[0], id_range[1]
        for i in range(start, end+1):
            id_set.add(i)
            print(f"We add the ID {i} to our list.")
    fresh_ingredients_ids = sorted(id_set)
    return fresh_ingredients_ids


def count_fresh_ingredients_ids(ingredients_data: str) -> int:
    id_ranges, food_ids = ingredients_data.split("\n\n")
    id_ranges = parse_id_ranges(id_ranges)
    fresh_ids = get_fresh_ingredients_ids(id_ranges)
    return len(fresh_ids)


def fuse_id_ranges(id_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    fused_ranges = []
    start_list = []
    end_list = []
    for id_range in id_ranges:
        start, end = id_range[0], id_range[1]
        start_list.append(start)
        end_list.append(end)
    start_list = sorted(start_list)
    end_list = sorted(end_list)
    start, end = start_list[0], end_list[0]
    for i in range(1, len(start_list)):
        if start_list[i] > end:
            fused_ranges.append((start, end))
            start = start_list[i]
        end = end_list[i]
    fused_ranges.append((start, end))
    return fused_ranges


def get_fresh_ingredients_ids_efficient(id_ranges: str) -> list[int]:
    id_ranges = parse_id_ranges(id_ranges)
    fused_ranges = fuse_id_ranges(id_ranges)
    fresh_ingredients_ids = get_fresh_ingredients_ids(fused_ranges)
    return fresh_ingredients_ids


def count_fresh_ingredients_ids_efficient(ingredients_data: str) -> int:
    id_ranges, food_ids = ingredients_data.split("\n\n")
    id_ranges = parse_id_ranges(id_ranges)
    fused_ranges = fuse_id_ranges(id_ranges)
    count = 0
    for fused_range in fused_ranges:
        start, end = fused_range[0], fused_range[1]
        count += end - start + 1
    return count

def parse_ingredients_database(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def main() -> None:
    file = "ingredients_data.txt"
    file = parse_ingredients_database(file)
    count = count_fresh_ingredients(file)
    print(f"{count} amount of ingredients are fresh!")
    count_id = count_fresh_ingredients_ids_efficient(file)
    print(f"{count_id} amount of ingredient IDs are considered fresh.")


if __name__ == "__main__":
    main()

