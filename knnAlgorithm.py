import math
# https://realpython.com/knn-python/

def norm(a, b):
    sideValues = 0
    for n in range(0, max(len(a),len(b))):
        sideValues += ((a[n]-b[n])**2) # Add a check for if there is no value in that position
    norm = math.sqrt(sideValues)
    return norm

def main():
    a = [19, 0, 6]
    b = [14, 8, 7]
    c = [16, 15, 14]
    d = [19, 5, 3]
    e = [15, 18, 1]
    f = [11, 6, 15]
    g = [12, 16, 6]
    h = [8, 0, 1]
    i = [10, 9, 4]
    j = [15, 8, 1]
    k = [12, 15, 15]
    l = [17, 3, 1]
    m = [18, 13, 8]
    n = [19, 0, 11]
    o = [17, 17, 2]
    p = [3, 16, 9]
    q = [9, 9, 5]
    r = [16, 7, 0]
    s = [3, 6, 6]
    t = [13, 1, 16]
    u = [8, 1, 12]
    v = [5, 9, 11]
    w = [16, 4, 11]
    x = [16, 14, 18]
    y = [13, 17, 7]
    z = [5, 2, 8]
    alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    output_set = set()
    new_point = [5,3,8]
    for i in range(0,len(alphabet)):
        output_set.add(round((norm(alphabet[i], new_point)),2))
    print((output_set))

if __name__ == '__main__':
    main()