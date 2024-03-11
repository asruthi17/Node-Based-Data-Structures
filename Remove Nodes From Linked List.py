'''You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        dummy=newHead=ListNode(None,head)
        curr=head
        while curr:
            while stack and stack[-1].val<curr.val:
                stack.pop()
            stack.append(curr)
            curr=curr.next
        for node in stack:
            newHead.next=node
            newHead=newHead.next
        return dummy.next
