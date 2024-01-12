class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif max(nums) < target:
                return len(nums)
            elif target <= nums[i]:
                return i