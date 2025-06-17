from datastructure.TreeNode import TreeNode
from datastructure.TreeNode import List2Tree
import collections
#路径总和
#给一棵树和一个数字，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于这个数字


#方法一（深度优先搜索）
#整体思路： 
#速背：三行代码递归搞定
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:         #递归的终止条件，判断两棵树是否为空树
            return t2
        if not t2:
            return t1
        
        merged = TreeNode(t1.val + t2.val)  #新建一个节点，两个树的根节点相加
        merged.left = self.mergeTrees(t1.left, t2.left)  #左子树和左子树合并
        merged.right = self.mergeTrees(t1.right, t2.right)   #右子树和右子树合并
        return merged