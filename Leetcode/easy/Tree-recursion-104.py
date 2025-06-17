from datastructure.TreeNode import TreeNode
from datastructure.TreeNode import List2Tree
#求树的高度
#方法很多，是很多算法题的基础
#这道题主要考察深度优先和广度优先


#方法一（深度优先搜索）
#整体思路：计算当前二叉树的最大深度时，可以先递归计算出其左子树和右子树的最大深度，然后在 O(1)
#时间内计算出当前二叉树的最大深度。递归在访问到空节点时退出。
#速背：非常简单，只需一个if else就行，在else里面调用自己即可，最后返回max+1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:    #递归的终止条件是当树中没有节点
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 


#方法二（广度优先搜索，也叫层次遍历）
#整体思路：DFS是不确定是否是最大深度的，但是BFS是确定的。广度优先搜索这里没有提供递归算法
#速背：树为空返回0。定义一个队列，队列的本质是包含一个元组的列表，元组有两个元素，第一个元素是
#初始深度1，第二个元素是树。然后通过一个循环中两个if并列，就可以完成遍历。循环的终止条件是队列
#为空，然后一个元素出队，然后分别判断，左子树存在就入队它的左子树并且深度+1，右子树存在就入队它
# 的右子树并且深度+1，最后返回深度即可，这个深度是循环中定义的局部变量。
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:   #如果为空树的话则直接返回0
            return 0
        queue = [(1, root)]   #定义一个队列，此时队列中有一个元素，就是一个元组，第一个值为1，第二个值为root
        while queue:          #队中第一个元素为1，是因为队中初始深度为1
            depth, node = queue.pop(0)   #出队，此时队中没有元素
            if node.left:
                queue.append((depth+1,node.left))  #如果存在左子树，那么深度加1，左子树入队
            if node.right:
                queue.append((depth+1,node.right))   #如果存在右子树，那么深度加1，右子树入队
        return depth




if __name__ == "__main__":
    t = List2Tree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])

    test = Solution()
    print(test.maxDepth(t))
    pass