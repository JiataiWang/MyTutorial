from typing import List
from datastructure.ListNode import ListNode
#有序链表删除重复元素


#方法一（循环法）
#速背：重复的元素在链表中出现的位置是连续的，因此我们只需要一个指针从头到尾遍历，来对比cur和cur.next是否相同即可
#时间复杂度
#空间复杂度
class Solution:
    def deleteDuplicates(self, l: ListNode) -> ListNode:
        if not l:
            return l #需要先判断特殊情况空链表
        cur = l
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return l  #这里要注意，这里返回的是l链表而不是自己定义的指针，一定要理解好链表与指针的本质，这里的指针最后都没有了




