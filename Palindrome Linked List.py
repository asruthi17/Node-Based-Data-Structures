'''Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.
 Input: head = [1,2,2,1]
Output: true'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        curr=slow
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        first=head
        second=prev
        while second:
            if(second.val!=first.val):
                return False
            first=first.next
            second=second.next
        return True
