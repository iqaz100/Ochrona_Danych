import math

import numpy as np

init_array = []
vectors_array = []
brange = 10

ZechTable = {
    4: (2, 1),
    8: (3, 6, 1, 5, 4, 2),
    16: (4, 8, 14, 1, 10, 13, 9, 2, 7, 5, 12, 11, 6, 3)
}

def user_input():
    while (True):
        p = input("Wprowadz liczbe elementow p: ")
        try:
            if (int(p) < 20):
                break;
            else:
                print("p musi byc mniejsze od 20")
        except ValueError:
            print("p musi byc liczbą calkowitą")

def inverse(x,p,q):
    if(x!=0 and p>2):
        return int((x+(q-1)/2)%(q-1))
    elif (x!=0 and p==2):
        return x
    elif (x==0):
        return 0

def generate_seq():
    init_array.clear()
    init_array.append(1)
    init_array.append(0)
    init_array.append(0)

    for i in range(0,brange):
        init_array.append((init_array[i]+init_array[i+1])%2)

def generate_vectors(size):
    vectors_array.clear()
    generate_seq()
    temparray = [0,0,0]
    vectors_array.append(temparray.copy())
    for i in range(0,size):
        temparray.clear()
        temparray.append(init_array[i])
        temparray.append(init_array[i+1])
        temparray.append(init_array[i+2])
        vectors_array.append(temparray.copy())
        #print("Wektor" + str(vectors_array[i]))

   # print(vectors_array)



def compare_vectors(vector):
    for i in range(0, brange-2):
        comparision = np.array(vector) == np.array(vectors_array[i])
        if(comparision.all()):
            if(i==0):
                x = 0
            elif(i==1):
                x = 1
            else:
                x = "a"+ str(i-1)
    return x

def mul_arr(size):
    print("\nTabliczka mnozenia: ")
    for i in range(0, size):
        print("\n")
        for j in range (0,size):
            if(i ==0 or j==0):
                x = 0
            elif ((i - 1 + j - 1) % (brange - 3) == 0):
                x = 1
            else:
                x = 'a' + str((i - 1 + j - 1) % (brange - 3))
            print(str(x),end=" ")

    print("\n")

def sum_arr():
    print("\nTabliczka dodawania: ")
    for i in range(0, brange-2):
        print("\n")
        for j in range (0,brange-2):
            first_array = np.array(vectors_array[i])
            second_array = np.array(vectors_array[j])
            final_array = (first_array +second_array)%2
            print(str(compare_vectors(final_array)),end=" ")
           # print(str(x), end=" ")

def sum(x:int,y:int,p:int,m:int):
    q = int(math.pow(p,m))
    if(y>x):
        x,y = y,x
    if(x !=0 and y!=0 and x>y):
        zech = ZechTable.get(q)[x-y-1]
        return ((y+zech-1) % (q-1) +1)
    elif (y==0 or x==0):
        return x+y
    elif (x!=0 and y== inverse(x,p,q)):
        return 0;

def mul(x:int,y:int,p:int,m:int):
    q = int(math.pow(p,m))
    if(x>0 and y>0):
        return 1 + (x+y-2) % (q-1)
    else:
        return 0

def mul_zech_arr(p,m):
    print("\n\n\nTabliczka mnozenia")
    q = int(math.pow(p,m))
    for i in range(0,q):
        print("\n")
        for j in range(0,q):
            x = mul(i,j,p,m)
            print(str(x), end=" ")

def sum_zech_arr(p,m):
    print("\n\n\nTabliczka dodawania")
    q = int(math.pow(p,m))
    for i in range(0,q):
        print("\n")
        for j in range(0,q):
            x = sum(i,j,p,m)
            print(str(x), end=" ")


def test():
    #generate_seq()
    print("---------------------------ZAD 1-----------------------------\n")
    generate_vectors(8)
    mul_arr(8)
    generate_vectors(6)
    mul_arr(6)
    print("\n---------------------------ZAD 2-----------------------------\n")
    x = input('Wprowadz pierwsza liczbe: ')
    y = input("Wprowadz druga liczbe: ")
    p = input("Wprowadz p: ")
    m = input("Wprowadz m: ")
    print("Wynik dodawnia: " + str(sum(int(x),int(y),int(p),int(m))))
    print("Wynik mnożenia: " + str(mul(int(x),int(y),int(p),int(m))))
    print("\n---------------------------ZAD 3-----------------------------\n")
    mul_zech_arr(2,2)
    sum_zech_arr(2,2)
    mul_zech_arr(2,3)
    sum_zech_arr(2,3)
    mul_zech_arr(2,4)
    sum_zech_arr(2,4)

test()
