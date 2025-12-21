def main(n) :
    a, b, c = n[0], n[1], n[2]
    
    print(int(a)+int(b)-int(c))
    d = a+b
    print(int(d)-int(c))

main(open(0).read().split())