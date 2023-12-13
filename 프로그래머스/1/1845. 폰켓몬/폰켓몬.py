def solution(nums):
    num = set(nums)
    len_num = len(num)
    len_nums = len(nums)//2
    return min(len_num, len_nums)