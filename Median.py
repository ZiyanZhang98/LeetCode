import unittest


def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    length = len(nums)
    nums.sort()
    mid_point = length/2
    if length % 2 == 0:
        mid_point = int(mid_point)
        print(float((nums[mid_point] + nums[mid_point - 1]) / 2))
    else:
        mid_point -= 0.5
        mid_point = int(mid_point)
        print(float(nums[mid_point]))


findMedianSortedArrays([],[4])