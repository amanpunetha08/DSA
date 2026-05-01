class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height) -1
        leftmax,rightmax = height[l],height[r]
        res = 0
        while l<r:
            if leftmax < rightmax:
                l+=1
                leftmax = max(leftmax,height[l])
                res += leftmax - height[l]
                print(leftmax,height[l],res)
            else:
                r-=1
                rightmax = max(rightmax,height[r])
                res += rightmax - height[r]
                print(rightmax,height[r],res)
        return res
        