def nod(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def main() -> None:
    a = int(input("Введите a: ").strip())
    b = int(input("Введите b: ").strip())
    print("НОД =", nod(a, b))


if __name__ == "__main__":
    main()
