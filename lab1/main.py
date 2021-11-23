
def main():
    while(True):
        p = input("Wprowadz liczbe elementow p: ")
        try:
            if(int(p) < 20):
                break;
            else:
                print("p musi byc mniejsze od 20")
        except ValueError:
            print("p musi byc liczbą calkowitą")

    add_table(int(p))
    mul_table(int(p))
    opp_table(int(p))
    rec_table(int(p))
    multiplicative(int(p))

def add_table(p):
    print("\nTabliczka dodawania: ")
    for i in range(0,p):
        print("\n")
        for j in range(0,p):
            x= (i+j) % p
            print(str(x), end=" ")

def mul_table(p):
    print("\nTabliczka mnozenia: ")
    for i in range(0,p):
        print("\n")
        for j in range(0,p):
            x= (i*j) % p
            print(str(x), end=" ")

def opp_table(p):
    print("\nTabliczka liczb przeciwnych: ")
    for i in range(0,p):
        print(str(i) + " " + str(-i%p))

def rec_table(p):
    print("\nTabliczka liczb odwrotnych: ")
    for i in range(1, p):
        print(str(i) + " " + str((i * i)  % p))

def multiplicative(p):
    print("\nRząd multiplikatywny ")
    for i in range (1,p):
        for j in range (1,10000):
            x = pow(i,j)
            if(x%p == 1):
                break;
        print(str(i) + " " + str(j))

main()
