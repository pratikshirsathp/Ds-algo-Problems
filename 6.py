#finding union and intersection
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        #union
        se = set()
        for i in range(0,n):
            se.add(a[i])
        for i in range(0,m):
            se.add(b[i])
        return(len(se))        
        
        #intersection
    def doIntersection(self,a,n,b,m):  
        se2 = set()
        for i in range(0,n):
            se.add(a[i])
        se3 = ser()   
        for i in range (0,m)
            if i in se2:
                se3.add(b[i])
        return(len(s2))                
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
        
        print(ob.doIntersection(a,n,b,m))
# } Driver Code Ends
