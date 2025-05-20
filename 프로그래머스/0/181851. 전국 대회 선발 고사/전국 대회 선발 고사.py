def solution(rank, attendance):
    answer = 0
    a = sorted(dict(zip(rank, attendance)).items())
    c=[]
    for i,j in a :
        if j :
            c.append(i)

    answer = 10000*rank.index(c[0]) + 100*rank.index(c[1]) + rank.index(c[2])
    return answer