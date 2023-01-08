"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
def maxPoints(self, points: List[List[int]]) -> int:
    if len(points)<3:
        return len(points)
    def line(p,q):
        if q[0]-p[0] == 0:
            return p[0]
        slope=(q[1]-p[1])/(q[0]-p[0])
        c=q[1]-slope*q[0]
        return slope,round(c,5)

    q=[]
    for i in range(len(points)):
        b={}
        for j in range(i+1,len(points)):
            P=points[i]
            Q=points[j]
            a=line(P,Q)
            if a not in b:
                b[a]=1
            else:
                b[a]+=1
        if b:
            c=max(b.values())
            q.append(c)
    return max(q)+1
  
  """
  O(n^2): Time complexity, possibly can be improved?
  """
