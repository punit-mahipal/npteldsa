'''
Define a Python function ascending(l) that returns True if each element in its input list is at least as big as the one before it.

Here are some examples to show how your function should work.
>>> ascending([])
True

>>> ascending([3,3,4])
True

>>> ascending([7,18,17,19])
False

Q2
Define a Python function alternating(l) that returns True if the values in the input list alternately go up and down (in a strict manner).

For instance:
>>> alternating([])
True

>>> alternating([1,3,2,3,1,5])
True

>>> alternating([3,2,3,1,5])
True

>>> alternating([3,2,2,1,5])
False

>>> alternating([3,2,1,3,5])
False

Q3
A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix
1  2  3
4  5  6
would be represented as [[1,2,3],[4,5,6]].

Write a Python function matmult(m1,m2) that takes as input two matrices using this row-wise representation and returns the matrix product m1*m2 using the same representation.

You may assume that the input matrices are well-formed and have compatible dimensions.

For instance:
>>> matmult([[1,2],[3,4]],[[1,0],[0,1]])
[[1,2],[3,4]]

>>> matmult([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]])
[[14, 32], [32, 77]]

'''
#Q1
def ascending(l):
    for i in range(len(l)-1):
        sume = 0
        if l[i]<=l[i+1]:
            sume = sume + i
        else:
            return False
    return True

#Q2
def alternating(l):
    for i in range(1,len(l)-1,2):
        if len(l)%2!=0:
            if ((l[i]<l[i-1] and l[i]<l[i+1]) or (l[i]>l[i-1] and l[i]>l[i+1])):
                sume=0
            else:
                return False
        else:
            if ((l[i]<l[i-1] and l[i]<l[i+1] and l[len(l)-1]<l[len(l)-2]) or (l[i]>l[i-1] and l[i]>l[i+1] and l[len(l)-1]>l[len(l)-2])):
                sume=0
            else:
                return False
    return True

#Q3
def matmult(l,n):
    col = []
    for i in range(len(l)):
        row = []
        for k in range(len(n[0])):
            sume =0
            for j in range(len(l[i]):
                sume = sume +l[i][j]*n[j][k]
            row.append(sume)
        col.append(row)
    return col
