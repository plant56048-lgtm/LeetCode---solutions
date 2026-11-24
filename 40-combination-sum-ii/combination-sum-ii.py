class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        cur = []
        def backtrack(start, rem):
            if rem == 0:
                res.append(cur.copy())
                return
            if rem<0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>rem:
                    break
                cur.append(candidates[i])
                backtrack(i+1, rem-candidates[i])
                cur.pop()
        backtrack(0,target)
        return res
            