from typing import List
def helper(self, candidates: List[int], target: int, index: int, subsequence: List[int], ans: List[int]):
        if index >= len(candidates):
            if target == 0:
                ans.append(subsequence[:])
            return 

        if candidates[index] <= target:
            subsequence.append(candidates[index])
            self.helper(candidates, target-candidates[index], index, subsequence, ans)
            subsequence.pop()
        self.helper(candidates, target, index+1, subsequence, ans)

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.helper(candidates, target, 0, [], ans)
        return ans
