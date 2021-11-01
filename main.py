def get_largest_prime_below(n):
    '''
    Găsește ultimul număr prim mai mic decât un număr dat.
    :param n: un numar natural
    :return: ultimul numar prim mai mic decat numarul dat
    '''
    if n<=2:
        return ("Nu exista un astfel de numar")
    else:
        for i in range(n - 1, 1, -1):
            verify = 1
            j = 2
            while j * j <= i and verify == 1:
                if i % j == 0:
                    verify = 0
                else:
                    j = j + 1
            if verify == 1:
                return i

def test_get_largest_prime_below():
    assert get_largest_prime_below(2)=="Nu exista un astfel de numar"
    assert get_largest_prime_below(5)==3
    assert get_largest_prime_below(999)==997
    assert get_largest_prime_below(21)==20

def is_superprime(n):
    '''
    Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu, 233 este superprim,
deoarece 2, 23 și 233 sunt toate prime, dar 237 nu este superprim, deoarece 237 nu este prim
    :param n: un numar natural
    :return: True|False
    '''
    if n<2 :
        return False
    while n :
        if n < 2 :
            return False
        i=2
        while i*i <= n:
            if n%i==0:
                return False
            i=i+1
        n=n//10
    return True

def test_is_superprime():
    assert is_superprime(2)==1
    assert is_superprime(23)==1
    assert is_superprime(233)==1
    assert is_superprime(237)==0

def is_palindrome(n) :
    '''
    Verifica daca un numar este palindrom
    :param n: numar narural
    :return: True|False
    '''
    nr=0
    n2=n
    while n :
        nr=nr*10 + n%10
        n=n//10
    if nr==n2 :
        return 1
    else: return 0

def test_is_palindrome():
    assert is_palindrome(77)==1
    assert is_palindrome(21)==0


def main ():
    while True:
        print("Alege o optune de mai jos: ")
        print("1. Găsește ultimul număr prim mai mic decât un număr dat. ")
        print("2. Determină dacă un număr este superprim. ")
        print("3. Verifica daca un numar este palindrom")
        print("4. Iesire")

        optiune=int(input("Dati optiunea "))

        if optiune==1:
            opt1=1
            test_get_largest_prime_below()
            print("Algoritmul alegerii a trecut testele de baza ")
            while opt1==1 :
                numar = int(input("Dati numarul pt care vreti sa verificati "))
                afisare = get_largest_prime_below(numar)
                print("Rezultatul este " + str(afisare))
                print("Alegeti o optiune: ")
                print("1. Pentru a verifica alt numar ")
                print("2. Pentru a te intoarce la meniu ")
                opt1=int(input())
                while opt1>2:
                    print("Optiune gresita")
                    print("Alegeti o optiune: ")
                    print("1. Pentru a verifica alt numar ")
                    print("2. Pentru a te intoarce la meniu ")
                    opt1 = int(input())
        elif optiune==2:
            opt2=1
            test_is_superprime()
            print("Algoritmul alegerii a trecut testele de baza ")
            while opt2==1 :
                numar = int(input("Dati numarul pt care vreti sa verificati "))
                afisare = is_superprime(numar)
                if afisare :
                    print("Numarul este superprim ")
                else:
                    print("Numarul nu este superprim ")
                print("Alegeti o optiune: ")
                print("1. Pentru a verifica alt numar ")
                print("2. Pentru a te intoarce la meniu ")
                opt2=int(input())
                while opt2>2:
                    print("Optiune gresita")
                    print("Alegeti o optiune: ")
                    print("1. Pentru a verifica alt numar ")
                    print("2. Pentru a te intoarce la meniu ")
                    opt2 = int(input())
        elif optiune ==3:
            opt3 = 1
            test_is_palindrome()
            print("Algoritmul alegerii a trecut testele de baza ")
            while opt3 == 1:
                numar = int(input("Dati numarul pt care vreti sa verificati "))
                afisare = is_palindrome(numar)
                if afisare:
                    print("Numarul este palindrom")
                else:
                    print("Numarul nu este palindrom ")
                print("Alegeti o optiune: ")
                print("1. Pentru a verifica alt numar ")
                print("2. Pentru a te intoarce la meniu ")
                opt3 = int(input())
                while opt3 > 2:
                    print("Optiune gresita")
                    print("Alegeti o optiune: ")
                    print("1. Pentru a verifica alt numar ")
                    print("2. Pentru a te intoarce la meniu ")
                    opt3 = int(input())


        elif optiune==4 :
            break
        else :
            print("Optiune gresita. ")

if __name__ == '__main__':
    main()