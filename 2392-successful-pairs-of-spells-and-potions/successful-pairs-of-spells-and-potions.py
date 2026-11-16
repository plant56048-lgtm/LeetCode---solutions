class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []
        
        for spell in spells:
            threshold = (success + spell - 1) // spell  
            
            idx = bisect.bisect_left(potions, threshold)

            result.append(m - idx)
        
        return result

        