class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            _mid = int((l + r) / 2)
            if target == nums[_mid]:
                return _mid

            if target < nums[_mid]:
                r = _mid - 1
            else:
                l = _mid + 1
        return -1
