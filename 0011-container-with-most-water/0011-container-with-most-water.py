class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height)-1
        max_water = 0
        while lp < rp:
            ht = min(height[lp],height[rp])
            wd = abs(rp-lp)
            max_water = max(max_water,ht*wd)
            if height[lp] < height[rp]:
                lp+=1
            else:
                rp-=1
        return max_water