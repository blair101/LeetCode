# -*- coding: utf-8 -*-
"""
    @file: easy.twoSum.py
    @date: 2020-09-30 08:38 AM
    @desc: 25. K 个一组翻转链表
    @url : https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
"""


# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#  
#
# 示例：
#
# 给你这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def medium(self, head: ListNode, k: int) -> ListNode:
        pass
