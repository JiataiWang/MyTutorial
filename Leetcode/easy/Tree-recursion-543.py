from datastructure.TreeNode import TreeNode
from datastructure.TreeNode import List2Tree
#计算二叉树的直径
#二叉树的直径是树中任意两个节点最短路径的最大值
#其实就是找出二叉树中最长的最短路径


#方法一（深度优先搜索）
#整体思路：我们以根节点为起点，定义一个求深度的函数，然后求深度，但是这个和单纯求深度的函数不太一样，递归完
#左子树和右子树的深度后会实时更新一个全局变量，这个全局变量用来记录直径。
#我们有一个节点，那么这个节点的深度为max(L, R) + 1
#而这个节点的直径为L+R+1
#速背：定义一个全局变量记录直径，定义一个递归函数求树的深度，函数中要求至今并实时跟新到全局变量里。
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1     #定义一个全局变量，初始值为1
        def depth(node):   #定义一个求树深度的函数，但是在求深度的过程中会实时更新全局变量
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1   #别忘了最后返回值要-1





        
if __name__ == "__main__":
    t = List2Tree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])

    test = Solution()
    print(test.maxDepth(t))
    passs