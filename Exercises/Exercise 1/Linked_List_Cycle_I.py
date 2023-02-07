#141 Linked List Cycle I
# Runtime: 61ms 56.85% Memory: 17.7MB 28.13%

#Definiton for singly-linked list
# classs ListNode:
# def __init__(self, x):
#       self.val = x
#       self.next = None

#Using two pointer method we can detect whether or not there is a cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        # check if we are at the end of a linked list, only if there is no cycle
        while(fast != None and fast.next != None): 
            fast = fast.next.next
            slow = slow.next
            # if the fast pointer catches up to the slow pointer while traversing through cycle
            if(fast == slow): 
                return True
        return False # if we reach the end of the linked list and there is no cycle we fall out of the loop