from typing import List
def maxArea(height: List[int]) -> int:
        n=len(height)
        maxArea = float("-inf")
        i=0
        j=n-1
        while(i<j):
            minHeight = min(height[i],height[j])
            width = j-i
            maxArea = max(maxArea, (minHeight*width))
            print(f"{i}:{j}:{minHeight}:{width}:{maxArea}")
            if minHeight == height[i]:
                i+=1
            else:
                j-=1
        return maxArea

heights = [int(ele) for ele in input().split()]
area = maxArea(heights)
print(area)
