from datastructure.TreeNode import TreeNode
from datastructure.TreeNode import List2Tree
import collections
#路径总和3
#给一颗二叉树和一个数字，求这个二叉树中节点值之和等于这个节点的 路径 的数目。
#其实这道题考察的是一个前缀和


#方法一（深度优先搜索）
#整体思路： 其实就是穷举法，在深度优先搜索的过程中，递归地遍历每一个节点所有可能的路径
#速背：双层递归，最内层函数调用自己，传入左子树右子树和数字减去节点值
#最外层函数，初始化计数器调用最内层函数，最外层调用最外层用左子树和右子树和初始值
# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> int:
#         #这里先定义一个函数，这个函数需要传入根节点和一个数值
#         #这个函数会返回这个根节点向下遍历所有路径之和满足这个数值的情况条目
#         #所以我们将会使一棵树中所有节点都过一遍这个函数，把每个节点得到的值都加起来就可以了
#         def rootSum(root, targetSum):   
#             if root is None:    #如果传入一个空节点就为0
#                 return 0
#             ret = 0   #函数中初始化一个计数器
#             if root.val == targetSum:     #如果这个节点本身的值等于传入的值
#                 ret += 1     #计数器+1
#             ret += rootSum(root.left, targetSum - root.val)  #然后传入节点左子树调用这个节点，并用总和减去这个根节点的值
#             ret += rootSum(root.right, targetSum - root.val) #然后传入节点右子树调用这个节点，并用总和减去这个根节点的值
#             return ret #计数器
#         if root is None:  #先判断树是否为空树
#             return 0         
#         ret = rootSum(root, targetSum)   #将根节点和数字传入这个函数中
#         ret += self.pathSum(root.left, targetSum)   #左子树，右子树分别传入最外层函数
#         ret += self.pathSum(root.right, targetSum)
#         return ret
    

#方法二（前缀和）
#整体思路： 
#速背：
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)  #这个东西叫哈希map，
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            
            ret = 0    #存储一共有多少条路径
            curr += root.val     #当前节点的前缀和
            ret += prefix[curr - targetSum]  #更新hashmap节点，如果已经有了这个节点就不用再更新了，而且ret+vale，value是key出现了几次
            prefix[curr] += 1   #将当前节点的前缀和
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)#最左边走到头了，如果该节点的右孩子不存在的话，才会执行下面的代码
            prefix[curr] -= 1  #路径-1，hashmap回退一格，只是冒号后面的值-1而已

            return ret

        return dfs(root, 0)
    
if __name__ == "__main__":
    t = List2Tree([10,5,-3,3,2,'null',11,3,-2,'null',1])

    test = Solution()
    print(test.pathSum(t, 8))
    pass