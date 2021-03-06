# -*- coding: utf-8 -*-
"""
    @file: medium.permute.py
    @date: 2020-09-24 08:38 AM
    @desc: 全排列
    @url : https://leetcode-cn.com/problems/permutations/
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack(first=0)
        return res
