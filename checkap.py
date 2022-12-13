class Solution:
    
    def checkIsAP(self, arr, n):
        # code here
        arr.sort()
        min1=arr[0]
        min2=arr[1]
        d=min2-min1
        j=1
        c=0
        for i in range(0,n):
            if arr[i]==min1+((j-1)*d):
                j+=1
            else:
                c+=1
        
        if c!=0:
            return False
        else:
            return True