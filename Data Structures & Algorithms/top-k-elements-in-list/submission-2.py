class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_dict = Counter(nums)
        top = counts_dict.most_common(k)
        return [item[0] for item in top]
        