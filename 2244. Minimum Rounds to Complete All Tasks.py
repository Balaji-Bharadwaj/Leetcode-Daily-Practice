"""
You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

 

Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
 

Constraints:

1 <= tasks.length <= 105
1 <= tasks[i] <= 109
"""
def minimumRounds(self, tasks):
    """
    :type tasks: List[int]
    :rtype: int
    """
    a={}
    for i in tasks:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    c=0
    for i in a.values():
        if i==1:
            return -1
        elif i%3==0:
            c+=i//3
        elif i%3==2:
            c+=((i-2)//3)+1
        elif i%3==1:
            c+=((i-2)//3)+2
    return c

#using python inbuilt counter
def minimumRounds(self, tasks):
    """
    :type tasks: List[int]
    :rtype: int
    """
    a=Counter(tasks)
    c=0
    for i in a.values():
        if i==1:
            return -1
        elif i%3==0:
            c+=i//3
        elif i%3==2:
            c+=((i-2)//3)+1
        elif i%3==1:
            c+=((i-2)//3)+2
    return c
