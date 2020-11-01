for i in range(100000, 10000000):
    based = "false"
    if i%2==0:
        based = "true"
    print("\tif (n == " + str(i) + ") return " + based)
