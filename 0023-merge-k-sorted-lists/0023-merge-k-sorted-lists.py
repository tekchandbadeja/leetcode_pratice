# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def list_to_linked_list(arr):
    if len(arr)==0:
        return None

    head=None 
    tail=None 
    #while arr:
    for i in arr:
        new_node=ListNode(i)
        
        #new_node=ListNode(arr.pop())
        if head==None:
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
    return head 

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None 
        ans=[]
        for i in range (len(lists)):
            head=lists[i]
            while head!=None:
                ans.append(head.val)
                head=head.next

        ans.sort()
        output=list_to_linked_list(ans)
        return output
         