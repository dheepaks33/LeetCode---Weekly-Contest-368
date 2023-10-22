class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float('inf')
        i = nums[0]
        right = [0]*n

        right[-1] = nums[-1]
        for a in range(n-2,-1,-1):
            right[a] = min(right[a+1], nums[a])
            

        for j in range(1,n-1):
            if i<nums[j] and right[j]<nums[j]:
                mini = min(mini , i+right[j] + nums[j])
            i = min(i,nums[j])
        return mini if mini!=float('inf') else -1 