def main():
    _ = input()

    count = 0
    result = [int(x) for x in str(input()).strip().split(' ')]
    while True:
        loop = [x % 2 == 0 for x in result].count(False)
        if loop > 0:
            break

        result = [x // 2 for x in result]
        count = count + 1
    print(count)


if __name__ == '__main__':
    main()
