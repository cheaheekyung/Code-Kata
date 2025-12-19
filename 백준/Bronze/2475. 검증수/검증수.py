def main(s) :
    a = list(map(int,s.split()))
    b = 0
    for i in a :
        b += i**2
    print(b % 10)
    
main(open(0).read())