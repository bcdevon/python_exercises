def decode(encoded, first):
    ans = [first]
    for i in encoded:
        first = first ^ i
        
        ans.append(first)
    print(ans)

decode([1,2,3], 1)

arr = 1,0,2,1
first = 2