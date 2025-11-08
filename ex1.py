def find(s, n):
    l=len(s)
    for i in range(l):
        for j in range(i+1,l):
            if s[i]+s[j]==n:
                print(s[i],s[j])
                return (i,j)


    return None

if __name__ == "__main__":
    s=[10,15,3,7]
    n=17
    result=find(s,n)
