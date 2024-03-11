'''Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1=oddlist=ListNode()
        head2=evenlist=ListNode()
        temp=head
        i=0
        while(temp):
            if(i%2==0):
                evenlist.next=temp
                evenlist=evenlist.next
            else:
                oddlist.next=temp
                oddlist=oddlist.next
            temp=temp.next
            i=i+1
        oddlist.next=None
        evenlist.next=head1.next
        return head2.next
                
        
            
        
