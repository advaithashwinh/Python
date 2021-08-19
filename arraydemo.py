def common(a, b):
    sa = set(a)
    sb = set(b)

    if (sa & sb):
        print(sa & sb)
    else:
        print("No common elements")

a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
common(a,b)


ls=[1,4,9,16,25,36,49,64,81,100]
print([e for e in ls if e%2==0])