#  15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            # Skip duplicate i values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            j = i + 1
            k = n - 1

            while j < k:
                curr_sum = nums[j] + nums[k]

                if curr_sum == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif curr_sum < target:
                    j += 1
                else:
                    k -= 1

        return ans