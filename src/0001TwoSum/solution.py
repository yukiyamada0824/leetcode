from typing import List

# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 一度取り出した数をkey,そのindexをvalueとして格納しておく辞書
        indices = {}

        for i, num in enumerate(nums):
            n = target - num
            if n not in indices:
                # targetとnumの差nが`indices`に格納されていない場合、 numを辞書に格納
                indices[num] = i
            else:
                # nが`indices`に格納されている場合は num + n = targetとなるので、indexを返して終了
                return [indices[n], i]