def main(data) :
    n, m = int(data[0]), int(data[1])
    nl = data[2:2+n]
    ml = data[2+n:2+n+m]
    answer = list(set(nl) & set(ml))
    answer.sort()
    print(len(answer))
    print(*answer, sep='\n')
    
   
main(open(0).read().split())




