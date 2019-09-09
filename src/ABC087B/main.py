def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    print('----------------------')
    print("a: {}, b: {}, c: {}, x: {}".format(a, b, c, x))
    print('----------------------')

    total = 0
    count = 0
    for _ in range(3):
        for i in range(1, a + 1):
            r = i * 500
            if r > x:
                break

            total += r
            count += 1

        for i in range(1, b + 1):
            r = total + (i * 100)
            if r > x:
                break

            print('b; r: {}, i: {}'.format(r, i))
            total += r
            count += 1

        for i in range(1, c + 1):
            r = total + (i * 50)
            if r > x:
                break

            print('c; r: {}, i: {}'.format(r, i))
            total += r
            count += 1

    print('----------------------')
    print('total:{}, count:{}'.format(total, count))
    print('----------------------')


if __name__ == "__main__":
    main()
