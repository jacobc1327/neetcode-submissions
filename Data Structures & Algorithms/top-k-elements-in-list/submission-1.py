class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_dict = Counter(nums)
        standard_dict = dict(counts_dict)
        top = Counter(standard_dict).most_common(k)
        just_names = [item[0] for item in top]
        return just_names