from typing import List
from datastructure.ListNode import ListNode
#输入一个链表，判断这个链表是不是回文链表，而且不能借助任何的空间结构
#首先什么是回文链表，其实就是镜像链表，最直观的解法就是切成两半，把后半段反转，然后比较两半是否相等。

#方法一（借助列表法）
#速背：定义一个空列表和指向链表的指针，通过循环将链表所有值放在列表中，然后用数组切片的方式来判断。
class Solution:
    def isPalindrome(self, l: ListNode) -> bool:
        vals = []  #定义一个空列表用于存放这个链表当中的所有元素
        cur = l  #定义一个指针
        while cur is not None:  #通过遍历将链表中的值添加的列表中
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]   #最后通过对列表的切片就能轻松判断
    

#方法二（快慢指针）
#速背：找到前半部分链表的尾节点也即整个链表终点，再配合链表长度的奇偶找到后半段链表，将后半段链表反转
#然后判断是否回文
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l, move = 0, head #重新定义链表是要判断链表长度
        #通过遍历获取链表长度
        while move:
            move = move.next
            l += 1
        #定义快慢指针，并且均指向头节点
        fast, slow = head, head
        #快慢两个指针同时移动，快指针移动到最后的时候，慢指针停在中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #但如果链表长度是个奇数的话，慢指针还得再往后移动一位
        if l%2:
            slow = slow.next
        #此时我们要将链表的后半段反转
        dummy = ListNode()
        while slow:
            dummy.next = slow  
            slow.next = dummy.next  #看到.next出现在前面就知道要改变指针方向了
            slow = slow.next
        tail = dummy.next  #得到了后半部分链表反过来了
        move = head  #这里重新赋值
        #最后在循环中将俩个链表的值一一比较
        while tail:
            if move.val != tail.val:
                return False
            move = move.next
            tail = tail.next
        return True




        