class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqlist = Counter(nums)
        minheap = []

        for number, freq in freqlist.items():
            heapq.heappush(minheap, (freq, number))
            if len(minheap)>k:
                heapq.heappop(minheap)
        
        return [number for freq,number in minheap]