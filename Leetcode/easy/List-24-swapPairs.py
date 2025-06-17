from typing import List
from datastructure.ListNode import ListNode
#给一个链表，对这个链表所有节点两两间交换
#这里指不能单纯改变节点内部的值，而是要实际的进行节点交换


#方法一（循环法）
#速背：和之前套路一样，先新建一个带头节点的链表，并且新建一个指针指向头节点，随着这个指针每次移动两个
#格子遍历，我们定义一个专门的函数做交换就行，要注意这个函数的传入参数是3个值，if判断循环终止条件的这些
#直接用try except就行。
class Solution:
    def swapPairs(self, l: ListNode) -> ListNode:
        dumb = ListNode(0)  #首先先定义一个dumb作为假的指针头
        dumb.next = l       #然后构造了一个新的链表
        cur = dumb     #定义一个指针
        def swap(pre, x1, x2):  #这里定义一个函数，传入三个指针，分别是需要交换的两个节点的指针还有这两个节点之前的指针
            temp = x2.next  #这里定义一个临时变量来记录这两个节点之后的节点
            pre.next = x2  
            x2.next = x1
            x1.next = temp
        while True:   #我们只需要移动cur指针就能实现链表节点的两两交换
            try:
                swap(cur, cur.next, cur.next.next)
                cur = cur.next.next
            except:
                break
        return dumb.next

#方法一（递归法）
#速背：比较难理解，暂时不需要背
class Solution:
    def swapPairs(self, l: ListNode) -> ListNode:
        if not l or not l.next: #递归的终止条件是传入这个递归函数的链表只有1个或者没有节点了
            return l
        cur = l.next
        l.next = self.swapPairs(l.next)
        cur.next = l
        return cur
