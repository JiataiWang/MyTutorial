class TreeNode():
    def __init__(self, val=0, left=None, right=None ):
        self.val = val
        self.left = left
        self.right = right

def List2Tree(l:list)->TreeNode:
    q = []
    if not l:
        return
    root = TreeNode(val=l.pop(0))
    q.append(root)
    while q:
        #t就是我们要构造的树
        t = q.pop(0)
        if l:
            if l[0] != 'null':
                t.left = TreeNode(val = l.pop(0))
                q.append(t.left)
            else:
                l.pop(0)
        if l:
            if l[0] != 'null':
                t.right = TreeNode(val = l.pop(0))
                q.append(t.right)
            else:
                l.pop(0)
    return root
        

        
import collections      
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            
            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)

    




if __name__ == "__main__":
    t = List2Tree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])

    test = Solution()
    print(test.pathSum(t, 9))
    pass





    
