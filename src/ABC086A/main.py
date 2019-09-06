def main():
    a = [int(x) for x in str(input()).strip().split(" ")]
    r = a[0] * a[1]
    if r % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()
