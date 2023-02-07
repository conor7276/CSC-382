# 876. Middle of the Linked list https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# Runtime 61 ms Beats 24.11%
# Memory 13.9 MB Beats 55.33%
# Time Complexity: O(n * log(n)) solution 
# Space Complexity: O(1)


## Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if num of nodes is even return second middle
        if head == None:
            return head
        temp = head
        res = 0
        while temp != None: # get the number of nodes
            res += 1
            temp = temp.next
            print(res)
        if res % 2 == 0: # divide by 2 to get half of the nodes
            res = (res / 2)
        else:
            res = res / 2
        temp = head
        for node in range(int(res)): # get everything after half of the list
            if node == res:
                return temp
            else:
                temp = temp.next
        return temp


# O(N) time solution using slow and fast pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow