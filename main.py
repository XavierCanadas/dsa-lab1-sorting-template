# TODO: implement the assignment


def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    for num in arr:
        print(num)


if __name__ == "__main__":
    main()