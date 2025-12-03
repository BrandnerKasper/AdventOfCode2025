def str_to_int(rotation: str) -> int:
    sign, num = rotation[0], rotation[1:]
    if sign == 'R':
        sign = 1
    if sign == 'L':
        sign = -1
    num = sign * (int(num) % 100)
    return num


def dial(rotations: list[str]) -> int:
    c = 0
    d = 50
    print(f"The dial starts by pointing at {d}.")
    for r in rotations:
        num = str_to_int(r)
        d = (d + num) % 100
        if d == 0:
            c += 1
        print(f"The dial is rotated {r} to point at {d}.")
    return c


def read_dials_from_txt(file: str) -> list[str]:
    rotations = []
    with open(file, "r") as f:
        for l in f:
            rotations.append(l.strip())
    return rotations


def main() -> None:
    # read rotations
    file = "dials.txt"
    rotations = read_dials_from_txt(file)
    count = dial(rotations)
    print(f"We hit exactly 0 {count} many times.")

if __name__ == '__main__':
    main()
