def num_cascate2(n):
    for x in range(1, n+1):
        print(x , end ='\n')
        if x == n: 5

        else:
            for y in range(1,n+1):
                if x >= y:
                    print(y, end='')

num_cascate2(3)
