class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        root = int(pow(c,1/2))
        arr = []
        for i in range(0,root+1):
            arr.append(i)
        i = 0
        j = len(arr)-1
        while i<=j:
            if pow(arr[i],2)+pow(arr[j],2) == c:
                return True
            elif pow(arr[i],2)+pow(arr[j],2) < c:
                i+=1
            else:
                j-=1
        return False