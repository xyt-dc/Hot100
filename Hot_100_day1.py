class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        target_search = {}
        for x in range(len(nums)):
            if nums[x] not in target_search:
                target_search[target - nums[x]] = x
            else:
                return [target_search[nums[x]], x]
        return []

if __name__ == '__main__':
    result = Solution().twoSum([2, 7, 11, 15], 9)
    print(result)

