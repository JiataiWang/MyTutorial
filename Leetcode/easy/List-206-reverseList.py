from typing import List
from datastructure.ListNode import ListNode
#链表反转

#方法一（双指针或者三指针）
#速背：pre指针指向None，后继指针cur指向第一个节点，后继指针不为空就一直循环，循环中定义临时变量指向
#cur的后继节点，再把cur的指针指向改变为指向pre，最后pre和cur都向后移动。
#时间复杂度：On
#空间复杂度：O1
class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
     

#方法二（递归）
#速背：官方的递归代码比较难理解，因为循环和递归是互通的，所以根据双指针可以对应着把递归代码写出来
#两个函数三个return，首先先定义一个递归函数，再写原函数的返回值是双指针的方法的初始条件，原来双
#指针的返回值现在写在递归函数里，最后递归函数的返回值要返回调用递归函数。
#时间复杂度：On
#空间复杂度：O1
# class Solution:
#     def reverseList(self, head:ListNode) -> ListNode:
#         if(head==None or head.next==None): return head
#         cur = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return cur
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def reverse(pre,cur):
            if not cur:
                return pre               
            tmp = cur.next
            cur.next = pre
            return reverse(cur,tmp)
        return reverse(None,head)




if __name__ == "__main__":
    l1 =  [1,2,3,4,5]
    if isinstance(l1,list):
            l1 = ListNode(l1)

    test = Solution()
    print(test.reverseList(l1).val)
