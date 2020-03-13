


finished = False
min_length = 2



while not finished:
    password = input("enter password: ")
    if len(password) >= min_length:
        for i in range(0, len(password), 1):
            print("*", end='')
            finished = True
    else:
        print("Password invalid")




