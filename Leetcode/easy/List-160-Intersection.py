from typing import List
from datastructure.ListNode import ListNode
#找出两个链表的交点
#所有代码跑不出来是因为输入本身就是一个分叉链表，而不是两个链表，一个和两个还是有区别的。在leetcode系统中，默认的是链表的重合部分地址一样


#方法一（循环暴力法）
#速背：双循环，双等号==判断
#时间复杂度n2，因为嵌套了循环
#空间复杂度1，
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        moveA = headA
        while moveA:
            moveB = headB
            while moveB:
                if moveB == moveA:
                    return moveB
                moveB = moveB.next
            moveA = moveA.next
        return None
    

#方法二（哈希法）
#速背：建一个哈希表，两个单循环并列，第一个循环把第一个链表所有可能加入，第二个循环用in判断紧接着就能return
#时间复杂度n，其实就是a+b两个链表长度
#空间复杂度n，哈希表所在内存
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        setA = set()
        moveA = headA
        while moveA:
            setA.add(moveA)
            moveA = moveA.next
        moveB = headB
        while moveB:
            if moveB in setA:
                return moveB
            moveB = moveB.next
        return None


#方法三（双指针）
#速背：一个循环中两个链表掉，循环终止条件两个链表相等。
#时间复杂度n，其实就是a+b两个链表长度
#空间复杂度1，两个指针所占内存是常数级
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A



if __name__ == "__main__":
    l1 =  [4,1,8,4,5]
    l2 =  [5,6,1,8,4,5]
    if isinstance(l1,list):
            l1 = ListNode(l1)
    if isinstance(l2,list):
            l2 = ListNode(l2)

    test = Solution()
    print(test.getIntersectionNode(l1, l2))
    