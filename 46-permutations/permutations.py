class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        curr = []
        res = []
        used = [False]*len(nums)
        def backtrack():
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    curr.append(nums[i])
                    used[i]=True
                    backtrack()
                    curr.pop()
                    used[i]=False
        backtrack()
        return res
