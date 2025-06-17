from datastructure.TreeNode import TreeNode
from datastructure.TreeNode import List2Tree
#翻转树
#输入一个树
#输出一个树，输出的树是输入的树左右子树都相反

#方法一（递归）
#整体思路：这是一道很经典的二叉树问题。显然，我们从根节点开始，递归地对树进行遍历，并从叶子节点先开始
# 翻转。如果当前遍历到的节点 root的左右两棵子树都已经翻转，那么我们只需要交换两棵子树的位置，即可完成以
#  root为根节点的整棵子树的翻转。
#速背：非常简单的递归函数，三行代码解决：左子树入递归，右子树入递归，交换左右子树。
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root   #如果树是空树直接返回这颗树
        
        left = self.invertTree(root.left)   #左子树调用递归函数
        right = self.invertTree(root.right)   #右子树调用递归函数
        root.left, root.right = right, left   #交换两颗子树的位置
        return root
