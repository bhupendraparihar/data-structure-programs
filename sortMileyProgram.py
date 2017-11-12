
'''
Milly and her classmates
Milly and her classmates are standing in a queue to attend the morning assembly of her school. According to the rule any student should stand in his/her proper place in order to make the queue completely visible till the end. Milly being the class monitor is required to make this queue such that students should be standing in an increasing order of their heights. Student with smaller height should stand at front and the student with higher height should stand at the end. She can reverse one particular group of the students. But she can perform this action only once. Here group of students means one particular continuous segment. Height of the students are distinct. Your task is to help her in solving this problem. You have to output starting and ending position of that group. In case, if queue is already in required condition or it is not possible to solve then consider starting and ending positions as -1.

Input

First line of the input will contain T (No. of test cases).
For each test case, first line will contain a integer N (No. of students). Second line will contain N space separated integers (denoting distinct height of students in initial queue)
Output

For every test case, print the two space separated integers denoting the starting and ending positions of group in a new line.
Constraints

1 ≤ T ≤ 10
1 ≤ N ≤ 104
1 ≤ Height ≤ 109
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def getIndexOfReverseGroup(n):
    s = -1
    e = -1
    for i in range(0,len(n)):
        if i < (len(n)-1) and n[i+1] < n[i] and s == -1:
            s = i
        elif i < (len(n)-1) and n[i+1] < n[i] and s != -1 and e != -1:
            return str(-1) + " " + str(-1)
            
        if i < (len(n)-1) and n[i+1] > n[i] and s != -1 and e == -1:
            e = i

    if s== -1 and e == -1:
        return str(-1) + " " + str(-1)
        
    if  s == -1:
        s = 0
    
    if e == -1:
        e = len(n) - 1

    if isArraySortedAfterReverse(s,e,n) == True:
            return str(s+1) + " " + str(e+1)
    return str(-1) + " " + str(-1)

def isArraySortedAfterReverse(s,e,n):

    if (s > 0 and n[e] < n[s-1]) or (e < len(n)-1 and n[s] > n[e+1]):
        return False
    return True

t = input()
heights = []
for i in range(0,int(t)):
    N = input()
    height = input()
    height = [int(i) for i in height.split()]
    heights.append(height)

for i in heights:
    print(getIndexOfReverseGroup(i))

