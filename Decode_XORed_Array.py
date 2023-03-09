def decode(encoded, first):
    ans = [first]
    for i in encoded:
        first = first ^ i
        
        ans.append(first)
    print(ans)

decode([1,2,3], 1)

