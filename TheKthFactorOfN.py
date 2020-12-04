# https://leetcode.com/problems/the-kth-factor-of-n/
import heapq

class Solution :
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        j = n
        mylist = list()
        myset = set()
        while i <= j:
            j = int(n / i)
            if n % i == 0:
                myset.add(i)
                if i != j:
                    myset.add(j)
            i += 1
        for ele in myset:
            mylist.append(ele)
        mylist.sort()
        print(mylist)
        if k-1 < len(mylist):
            return mylist[k-1]
        else:
            return -1

    def kthFactorNew(self, n: int, k: int) -> int:
        curr_fact = 0
        # go till half range of given value
        for i in range(1,1 + (n+1)//2):
            if n % i == 0:
                curr_fact += 1

            if curr_fact == k:
                return i

        # half way is covered above , after that we need to just check last number itself
        if curr_fact + 1 == k:
            return n
        else:
            return -1


sol = Solution()
print(sol.kthFactorNew(12,3))
print(sol.kthFactorNew(7,2))
print(sol.kthFactorNew(4,4))
print(sol.kthFactorNew(1,1))
print(sol.kthFactorNew(1000,3))
