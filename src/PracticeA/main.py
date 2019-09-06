def main() -> None:
  a = int(input())
  b = sum([int(x) for x in str(input()).strip().split(" ")])
  c = str(input())

  result = "{0} {1}".format(int(a + b), c)
  print(result)

if __name__ == "__main__":
  main()