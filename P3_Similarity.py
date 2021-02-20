sequence_one=input("Enter the first sequence: ")
sequence_two=input("Enter the second sequence: ")
how_many=int(input("How many elements for similarity condition?"))
similarities=[]
for i in range(0,how_many):
    a=input("Enter an element: ")
    c=int(input("How many elements is it similar to? "))
    similarities.append([])
    similarities[i].append(a)

    for j in range(0,c):
        b=input("What is it similar to? ")
        similarities[i].append(b)

def compare(o,t,s):
    print(o)
    print(t)
    print(s)
    #checking if similar
    score=0
    for i in range(len(o)):
        for j in range(len(s)):
            if o[i] in s[j] and t[i] in s[j] and o[i] != t[i]:
                score+=1
    #calculating similarity
    similarity= (score*100)/len(o)
    return similarity
print(compare(list(sequence_one),list(sequence_two),similarities),"%") 




        
//OUTPUT:
Enter the first sequence: ACTGACTG
Enter the second sequence: CGTACGTA
How many elements for similarity condition?1
Enter an element: A
How many elements is it similar to? 1
What is it similar to? C
['A', 'C', 'T', 'G', 'A', 'C', 'T', 'G']
['C', 'G', 'T', 'A', 'C', 'G', 'T', 'A']
[['A', 'C']]
25.0 %
> 
