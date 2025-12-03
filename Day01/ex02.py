def str_to_int(rotation: str) -> int:
    sign, num = rotation[0], rotation[1:]
    if sign == 'R':
        sign = 1
    if sign == 'L':
        sign = -1
    num = sign * int(num)
    return num


def dial(rotations: list[str]) -> int:
    c = 0
    d = 50
    print(f"The dial starts by pointing at {d}.")
    for r in rotations:
        num = str_to_int(r)
        c_r = int(abs(num)/100)
        num = num - int(num/100) * 100
        if d + num > 100:
            c_r += 1
        elif d + num < 0 and d is not 0:
            c_r += 1
        c += c_r
        d = (d + num) % 100
        if d == 0:
            c += 1
        print(f"The dial is rotated {r} to point at {d}.")
        if c_r > 0:
            print(f"During this rotation it points at 0 {c_r} times.")
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
