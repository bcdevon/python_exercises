edges = [[1,2],[2,3],[4,2]]
def find_center(edges):
    seen = set ()
    for i in edges:
        for j in i:
            if j in seen:
                return j
            else:
                seen.add(j)
    
print(find_center(edges))


                

       

    