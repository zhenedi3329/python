list = []
def sigma(list):
    p = 0
    for i in list:
        p = p + i[1]
        return p
    for i in range(int(input())):
        name = input("name tovar")
        price = float(input("prc"))
        amount = int(input("skok"))
