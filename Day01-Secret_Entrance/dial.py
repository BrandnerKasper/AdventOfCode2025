def read_dials_from_txt(file: str) -> list[str]:
    rotations = []
    with open(file, "r") as f:
        for l in f:
            rotations.append(l.strip())
    return rotations


def str_to_int(rotation: str) -> int:
    sign, num = rotation[0], rotation[1:]
    if sign == 'R':
        sign = 1
    if sign == 'L':
        sign = -1
    num = sign * int(num)
    return num


def dial(rotations: list[str], exact: bool) -> int:
    if exact:
        return dial_count_exact_zero(rotations)
    else:
        return dial_count_zero(rotations)


def dial_count_exact_zero(rotations: list[str]) -> int:
    c = 0
    d = 50
    print(f"The dial starts by pointing at {d}.")
    for r in rotations:
        n = str_to_int(r)
        n = n % 100
        d = (d + n) % 100
        if d == 0:
            c += 1
        print(f"The dial is rotated {r} to point at {d}.")
    return c


def dial_count_zero(rotations: list[str]) -> int:
    c = 0
    d = 50
    print(f"The dial starts by pointing at {d}.")
    for r in rotations:
        n = str_to_int(r)
        c_r = int(abs(n) / 100)
        n = n - int(n / 100) * 100
        if d + n > 100:
            c_r += 1
        elif d + n < 0 and d != 0:
            c_r += 1
        c += c_r
        d = (d + n) % 100
        if d == 0:
            c += 1
        print(f"The dial is rotated {r} to point at {d}.")
        if c_r > 0:
            print(f"During this rotation it points at 0 {c_r} times.")
    return c


def main() -> None:
    # read rotations
    file = "dials.txt"
    rotations = read_dials_from_txt(file)
    count = dial(rotations, False)
    print(f"We hit exactly 0 {count} many times.")


if __name__ == '__main__':
    main()
