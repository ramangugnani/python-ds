# https://leetcode.com/problems/can-place-flowers/
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_avail = 0
        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 0:
                if (i-1 < 0 or flowerbed[i-1] == 0) and (i + 1 >= len(flowerbed) or flowerbed[i+1] == 0):
                    flowerbed_avail += 1
                    flowerbed[i] = 1

            if flowerbed_avail >= n:
                #print(flowerbed)
                return True

        #print(flowerbed)
        return False

sol = Solution()

flowerbed = [1,0,0,0,1,0,0,0]
n = 2
print(sol.canPlaceFlowers(flowerbed,n))

flowerbed = [1,0,0,0,1]
n = 1
print(sol.canPlaceFlowers(flowerbed,n))

flowerbed = [1,0,0,0,1]
n = 2
print(sol.canPlaceFlowers(flowerbed,n))

flowerbed = [0,0,1,0,0]
n = 2
print(sol.canPlaceFlowers(flowerbed,n))