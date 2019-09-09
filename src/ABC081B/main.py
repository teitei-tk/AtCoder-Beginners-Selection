def main():
    _ = input()
    c = 0
    n = []
    while True:
        try:
            list = input()
            if list == '':
                break

            is_odd = False
            cast_list = [int(x) for x in str(list).strip().split(' ')]
            for x in cast_list:
                if not x % 2 == 0:
                    is_odd = True

            if is_odd:
                break
            n.append(cast_list)
            c += 1
        except EOFError:
            break

    print(c)
#   t = int(input())
#   l = [input().split() for i in range(t)]

#   c = 0
#   for x in l:
#       if not x % 2 == 0:
#           break
#       c += 1
#   print(l)
#   print(c)

#   while True:
#       try:
#           odd = False
#           for x in [int(x) for x in str(input()).strip().split(' ')]:
#               if not x % 2 == 0:
#                   odd = True

#           if odd:
#               break

#           if not odd:
#               continue

#           c += 1
#       except EOFError:
#           break

#       print(c)


if __name__ == '__main__':
    main()
