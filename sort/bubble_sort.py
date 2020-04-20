def bubble_sort(nums):
    for i in range(len(nums)):
        length = len(nums) - i
        for j in range(length - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]

    return nums


print(bubble_sort([5,2,3,1]))
