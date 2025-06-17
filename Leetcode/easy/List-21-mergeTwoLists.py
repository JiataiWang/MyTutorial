from typing import List
from datastructure.ListNode import ListNode
#合并两个有序链表


#方法一（循环归并排序）
#速背：首先得先新建一个链表，然后循环套一个判断，如果两个链表都不为空就一直循环，然后比较两个升序链表的第一个值,
#哪个更小就把自己新建链表的下一个指针指向这个节点，并将这个链表往后移动一位，判断结束后都要移动新建的链表，循环结束
#说明某一个链表已经空了，就把另一个链表拼接到新建列表的后面。
#时间复杂度
#空间复杂度
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(-1)  #新建一个伪头部
        while l1 and l2:
            if l1.val <= l2.val:  #如果l1的值小于等于l2
                cur.next = l1   #那么我们就优先选择l1
                l1 = l1.next   #并且使l1向后移动
            else:
                cur.next = l2  #否则就选择l2
                l2 = l2.next  #并让l2向后移动
            cur = cur.next   #每一步之后都要移动cur，使得它在新链表的结尾，这一步十分关键
        cur.next = l1 if l1 else l2  #循环外，如果l1或者l2为空了，我们就需要把还有节点的链表连接到最后
        return dummy.next
    

#方法二（递归）
#速背：先定义递归函数，然后判断终止条件，然后回溯算法
#时间复杂度
#空间复杂度
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def mergeT(l1, l2):
            if not l1: return l2 #递归的终止条件，如果1是空的就返回2，如果2是空的就返回1
            if not l2: return l1
            if l1.val< l2.val: #如果都不为空就可以进行比较头节点的大小了
                  l1.next = mergeT(l1.next, l2) #如果1更小，就合并1的后面和2，把合好的结果再让1指向
                  return l1
            else:
                  l2.next = mergeT(l1, l2.next)
                  return l2
        return mergeT(l1,l2)



if __name__ == "__main__":
    l1 =  [1,2,4]
    l2 =  [1,3,4]
    if isinstance(l1,list):
            l1 = ListNode(l1)
    if isinstance(l2,list):
            l2 = ListNode(l2)

    test = Solution()
    res = test.mergeTwoLists(l1, l2)
    print(res)
    pass