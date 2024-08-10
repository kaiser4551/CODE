class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def combi(start_idx, comb, target):
            if target == 0:
                res.append(comb[:])
                return
            if target < 0 or start_idx >= len(candidates):
                return
    
    # Include the current candidate and continue
            comb.append(candidates[start_idx])
            combi(start_idx, comb, target - candidates[start_idx])
    
    # Backtrack and exclude the current candidate, then move to the next
            comb.pop()
            combi(start_idx + 1, comb, target)
        combi(0,[],target)
        return res