class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        curr = []
        def backtrack(index, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return
            if remaining<0 or index==len(candidates):
                return
            curr.append(candidates[index])
            backtrack(index, remaining-candidates[index])
            curr.pop()
            backtrack(index+1, remaining)
        backtrack(0, target)
        return res
