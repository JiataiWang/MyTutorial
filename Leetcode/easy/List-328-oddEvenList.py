from typing import List
from datastructure.ListNode import ListNode
#分离节点后合并
#给一个链表，将所有索引为奇数的节点放在前面，索引为偶数的节点放在后面.
#虽然第一个节点的索引是偶数0，但是这道题默认第一个节点的索引是奇数

#方法一（双指针，分离成两个链表后再拼接）
#速背：先用双指针的方法对链表进行分离，定义一个奇数链表指针指向头节点，定义一个
#偶数链表指针指向第二个节点，通过循环分离。更新奇数节点时，奇数节点的后一个节点需要指向偶数节点的后一个节点
#更新偶数节点时，偶数节点的后一个节点需要指向奇数节点的后一个节点

class Solution:
    def oddEvenList(self, l: ListNode) -> ListNode:
        if not l:
            return l
        
        evenHead = l.next  #这里别忘了单独定义出偶链表
        odd, even = l, evenHead #定义奇指针和偶指针
        while even and even.next: #偶指针不为空就一直循环
            odd.next = even.next  #奇指针指向偶指针的后一个节点，此时偶指针断开
            odd = odd.next  #然后奇指针后移
            even.next = odd.next #偶指针指向奇指针的后一个节点，交替进行
            even = even.next  #偶指针后移
        odd.next = evenHead  #最后把偶链表拼在奇链表后面
        return l

        