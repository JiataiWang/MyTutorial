from datastructure.TreeNode import TreeNode
from datastructure.TreeNode import List2Tree
import collections
#子树
#就是给两棵树，判断其中一棵树包不包含另一颗树


#方法一（深度优先搜索）
#整体思路：其实就是在母树上每个节点都遍历，判断该子节点是否和t相等，总体来说就是三步走
#1.当前两棵树相等，2.或者是左子树，3.或者是又子树
#速背：这道题默认问的是第一棵树包不包含第二棵树，首先需要写一个判断两棵树是否相等的函数，这个用递归写，两个if判断树
#是否存在，返回两个and。有了这个函数之后，直接返回两个or，连接要么相等，要么左子树包含，要么右子树包含。
class Solution:
    def isSubtree(self, t1: TreeNode, t2: TreeNode):
        #想知道一棵树是不是另一棵树的子树，首先先判断这两棵树是否存在
        if not t1 and not t2:    #如果两棵树都不存在则返回True
            return True
        if not t1 or not t2:    #如果只存在一棵树，肯定是false
            return False
        #还需要额外写一个判断两棵树是否相等的函数
        #如果一棵树包含另一棵树，要么一棵树等于另一棵树，要么一棵树的左子树包含另一棵树，要么一棵树的右子树包含另一棵树
        return self.isSameTree(t1, t2) or self.isSubtree(t1.left, t2) or self.isSameTree(t1.right, t2)
    
    
    #这里需要定义额外的递归函数，作用是判断两棵树是否是同一棵树
    def isSameTree(self, t1: TreeNode, t2: TreeNode):
        #同样先判断树的合法性
        if not t1 and not t2:    #如果两棵树都不存在则返回True
            return True
        if not t1 or not t2:    #如果只存在一棵树，肯定是false
            return False
        #返回两个and，两棵树的值相等，两棵树的左子树相等，两棵树的右子树相等
        return t1.val == t2.val and self.isSameTree(t1.left, t2.left) and self(t1.right, t2.right)
        




        





        
        return 







if __name__ == "__main__":
    t1 = List2Tree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])
    t2 = List2Tree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])

    test = Solution()
    print(test.mergeTrees(t1, t2))
    pass