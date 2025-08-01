def sample1(a,b):
    vol1=a**3
    vol2=b**3
    
    return vol1//vol2

if __name__=='__main__':
    a=int(input())
    b=int(input())
    
    print(sample1(a,b))