a = open(0).read().split()[:-1]

def main(s) :
    if s == s[::-1] :
        print('yes')
    else :
        print('no')

for i in a :
    main(i)