# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def printer(start,postend):
    p = start
    while(p is not postend):
        print(p.val)
        p=p.next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(k==1 or head==None):
            return head
        prehead = ListNode(0,head)
        pre = prehead
        while(...):
            start = pre.next
            p=start
            for i in range(k-1):
                if(p == None):
                    break
                else:
                    p=p.next
            if(p == None):
                break
            end = p
            postend = end.next
            newstart,newend = rev(start,end)
            pre.next = newstart
            newend.next = postend
            pre = newend
        return prehead.next

def rev(start,end):
    # both start and end are NOT None
    pre=None
    cur=start
    postEnd = end.next
    while(cur is not postEnd):
        next = cur.next
        
        cur.next = pre

        pre=cur
        cur = next
    return end,start