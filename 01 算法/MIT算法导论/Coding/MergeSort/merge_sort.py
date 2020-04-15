def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    k = len(nums) // 2
    return merge_two_sorted_list(merge_sort(nums[:k]), merge_sort(nums[k:]))


def merge_two_sorted_list(nums1, nums2):
    nums = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    if i != len(nums1):
        nums += nums1[i:]
    if j != len(nums2):
        nums += nums2[j:]
    return nums
