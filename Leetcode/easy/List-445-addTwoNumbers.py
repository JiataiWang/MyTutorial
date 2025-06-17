from typing import List
from datastructure.ListNode import ListNode
#两个链表相加，一个链表代表一个数字，第一个节点代表最高位，返回一个链表，而且不能对原链表做修改
#所以一定要想到用栈来存储列表元素

#方法一（用栈，循环进位法）
#速背：首先做加法是从低位往高位加，所以最容易想到的就是定义两个栈存储链表节点，都压入栈中再依次取出相加
#在取元素相加的时候，我们要用头插法
class Solution:
    def addTwoNumbers(self, headA: ListNode, headB: ListNode) -> ListNode:
        s1, s2 = [], []  #先定义两个栈，然后将两个链表各自元素压入栈中
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None  #定义一个空的新链表
        carry = 0 #定义一个变量记录进位
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop() #栈中没有元素就为0，否则就弹栈
            b = 0 if not s2 else s2.pop() #栈中没有元素就为0，否则就弹栈
            cur = a + b + carry     #得到两个弹栈元素后，我们对弹栈元素做相加，还要加上之前的进位
            carry = cur // 10  #计算这个数字往前进了几位，每次循环中这个值会不断变化
            cur %= 10  #通过取余计算这个节点应该填写哪个值
            curnode = ListNode(cur)  #定义一个节点，并且把该值放入这个节点中
            curnode.next = ans  #
            ans = curnode
        return ans

