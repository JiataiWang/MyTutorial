from typing import List
from datastructure.ListNode import ListNode
#拆分链表，传入一个链表和一个实数k，传出一个列表中有k个链表，也就是把一个链表平均分成k份

#方法一（循环进位法）
class Solution:
    def splitListToParts(self, l: ListNode, k:int) -> ListNode:
        n = 0  
        node = l
        while node:
            n += 1
            node = node.next  #这里通过遍历先算出链表的总长度
        quotient, remainder = n // k, n % k  #算出分别对k的商和余
        #算出来商和余之后，余数表示前余数个段长度是商加1，其余部分的长度都是商
        parts = [None for _ in range(k)]    #这里通过列表推导式构造一个列表，列表中有k段
        i, curr = 0, l   
        while i < k and curr:   
            parts[i] = curr  #将链表头节点传入列表中的第i个元素
            part_size = quotient + (1 if i < remainder else 0)  #计算出这一点的长度，用商加上循环次数与余数的比较
            for _ in range(part_size - 1):  #通过for循环然指针向后移动这一段的长度步
                curr = curr.next 
            temp = curr.next  #记录当前指针的后一个节点
            curr.next = None #断开此处的节点
            curr = temp  #重新让指针指向之前记录好的节点
            i += 1
        return parts

if __name__ == "__main__":
    l1 =  [4,1,8,4,5]
    l2 =  [5,6,1,8,4,5]
    if isinstance(l1,list):
            l1 = ListNode(l1)
    if isinstance(l2,list):
            l2 = ListNode(l2)

    test = Solution()
    print(test.splitListToParts(l1, 2))
    
