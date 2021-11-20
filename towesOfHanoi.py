def towersOfHanoi(n, src, to, temp):
    if n == 1:
        print(f"Move disk {n} from {src} to {to}")
        return
    towersOfHanoi(n-1, src, temp, to)
    print(f"Move disk {n} from {src} to {to}")
    towersOfHanoi(n-1, temp, to, src)

n = int(input("Enter the number of disks : "))
towersOfHanoi(n,'A','B', 'C')
