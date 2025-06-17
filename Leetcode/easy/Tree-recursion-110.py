from datastructure.TreeNode import TreeNode
from datastructure.TreeNode import List2Tree
#给定一个二叉树，判断它是否是平衡二叉树。
#平衡二叉树的所有子树都是平衡二叉树
#这道题只能用递归的方法来做，但是有两种，分别是从下往上遍历和从上往下遍历


#方法一（自顶向下递归）
#整体思路：首先这道题需要用到上一道题递归获取深度，判断其左右子树的高度差是否不超过1
#速背：先定义获取树高度的递归函数，空树直接返回是，最后返回双and判断3条件
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #这里先把上一道题递归计算树高度的函数定义出来
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        if not root:
            return True #如果树是空树的话就返回是平衡二叉树
        #最后返回两个and判断，需要同时满足三个条件：这棵树左右子树深度差小于等于1，左子树是平衡树，右子树是平衡树
        #调用计算树深度的递归函数，左右子树的深度差的绝对值小于等于1，并且左子树和右子树传入最大的一层递归函数判断是否是平衡二叉树
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


#方法二（自底向上递归）
#整体思路：自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，
# 再判断以当前节点为根的子树是否平衡。如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），
# 否则返回 −1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。
#速背：
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:  #如果树是空树返回0
                return 0
            leftHeight = height(root.left)  #左子树调用递归函数
            rightHeight = height(root.right)   #右子树调用递归函数
            #如果左子树不是平衡树，右子树也不是平衡树，根节点树也不是平衡树，这里不用and，用or
            #翻译过来就是左子树高度-1，右子树高度-1，根节点左右子树差大于1
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1  #只要有一个不满足就返回-1
            else:
                return max(leftHeight, rightHeight) + 1  #否则就返回左子树和右子树的最大值+1

        return height(root) >= 0 #最终树的高度只要不是-1就说明是平衡树

        
if __name__ == "__main__":
    t = List2Tree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])

    test = Solution()
    print(test.maxDepth(t))
    pass