from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        sum =0
        for j in range(i, len(nums)):
            sum += num[j]
            if sum == target:
                return [i+1, j+1]
    return [-1]