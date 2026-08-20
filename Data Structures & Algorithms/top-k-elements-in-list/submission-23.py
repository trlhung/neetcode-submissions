class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Tao hash map luu gia tri va tan suat:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Tao 1 min-heap gom k phan tu de luu tru linh hoat cac phan tu
        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))
            # Neu heap chua nhieu hon k phan tu thi se pop ra phan tu nho nhat
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Tao mang result chu k gia tri lap lai
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res