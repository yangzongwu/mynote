def insert_sorted_num(nums, num):
    if not nums:
        return [num]

    if nums[-1] < num:
        return nums + [num]

    if num<nums[0]:
        return [num]+nums

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return nums[:r+1] + [num] + nums[r+1:]


def insertion_sort(nums):
    rep = []
    for num in nums:
        rep = insert_sorted_num(rep, num)
    return rep
