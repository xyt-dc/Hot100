
from typing import Optional,List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            #对于空链表和单一节点链表不需要排序
            return head
        cur = head
        pre_cur = head
        while cur:
            prev = ListNode(-2**31 ,head)
            while prev is not pre_cur:
                #找到应该插入的位置
                if prev.val > cur.val:
                    break
                else:
                     prev = prev.next
            #插入节点
            if prev == pre_cur:
                #有序不必插入直接更新
                pre_cur = pre_cur.next #更新pre_cur
                cur = cur.next
            else:
                #需要插入节点
                pre_cur.next = cur.next #把cur安全拿走
                cur.next = prev.next #cur的下一个指向prev的下一个
                prev.next = cur #prev指向cur
                cur = pre_cur.next #cur 复位
        return head

if __name__ == '__main__':

    head = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
    Solution().insertionSortList(head)
    while head:
        print(head.val)
        head = head.next


