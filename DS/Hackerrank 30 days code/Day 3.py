if __name__ == '__main__':
    N = int(input().strip())
    if not N&1:
        if 2<=N<=5:
            print("Not Weird")
        elif 6<=N<=20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
