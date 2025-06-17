from typing import List
from datastructure.ListNode import ListNode
#删除链表的倒数第 N 个结点


#方法一（循环法）
#速背：先遍历整个链表获取链表的长度，然后定点删除第(l-n+1)这个元素,但是自己却有很多细节没考虑
#首先需要增加一个头节点，然后让指针移动到对应位置是，直接删除就行。
#时间复杂度
#空间复杂度
class Solution:
    def removeNthFromEnd(self, l: ListNode, n:int) -> ListNode:
        def getlen(l: ListNode):         
            length = 0
            while l:
                l = l.next
                length = length + 1
            return length 
        length = getlen(l)
        #得到这个长度后，我们通过第二次遍历删除这个节点,接下来就是删除节点的算法，知道一个节点坐标如何删除这个节点
        dummy = ListNode(0)  #新建一个伪头部
        dummy.next = l  #定义一个新链表，在原始基础上增加了头节点
        cur = dummy #定义一个指针
        for i in range(0,length-n):
            cur = cur.next
        cur.next = cur.next.next      #这一句代码连着两个全变了
        return dummy.next #在原始基础上还得去掉头节点



#方法二（栈）
#速背：定义一个新增头节点的列表，定义一个栈栈的本质是列表，定义一个指针指向头节点，然后对链表进行遍历，
#把所有的节点都放进栈中，或者说把指向每个元素的指针放入栈中，然后出栈n个元素，此时的栈顶元素就是我们想要
#的指针，把它后面的元素删除就行。
class Solution:
    def removeNthFromEnd(self, l: ListNode, n:int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = l #新定义一个列表，新增头节点
        stack = list() #定义一个栈
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n): #然后把倒数的前几个节点都出栈
            stack.pop()  
        prev = stack[-1]  #取出栈顶元素的指针，此时栈顶元素就是倒数第n个元素的前一个元素的指针
        prev.next = prev.next.next  #通过栈顶元素指针删除这个节点后面的节点
        return dummy.next
    
              

#方法二（快慢指针，双指针）
#速背：初始时 first 和 second 均指向头节点，然后用first遍历n个节点，此时first和second之间隔了n-1个节点
#此时我们同时对两个指针进行遍历，当first为null时，second恰好指向倒数第n个节点。但是知道这个节点删除这个节点
#不是很方便，最好是知道要删除节点的前一个节点这样比较方便，所以这里要设置哑节点,哑节点是头节点前面需要新加
#一个节点，多往前移动一位，其实也就是dummy
class Solution:
    def removeNthFromEnd(self, l: ListNode, n:int) -> ListNode:
         dummy = ListNode(0)
         dummy.next = l
         f = l
         s = dummy
         for i in range(n):
              f = f.next  #第一个指针先走n步
         while f:
              f = f.next
              s = s.next
         s.next = s.next.next
         return dummy.next
         
         



        
if __name__ == "__main__":
    l1 =  [1,2,3,5]
    l2 =  [5,6,1,8,4,5]
    if isinstance(l1,list):
            l1 = ListNode(l1)

    test = Solution()
    print(test.removeNthFromEnd(l1, 2))
    pass