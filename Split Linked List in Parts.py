'''Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        width,r=divmod(length,k) 
        result,current=[],head
        for i in range(k):
            dummy=write=ListNode(0)
            for j in range(width+(i<r)):
                if current:
                    write.next=write=ListNode(current.val)                  
                    current=current.next
            result.append(dummy.next)
        return result       
