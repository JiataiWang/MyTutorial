from datastructure.TreeNode import TreeNode
from datastructure.TreeNode import List2Tree
import collections
#合并二叉树
#其实就是两个树的对应节点相加就可以


#方法一（深度优先搜索）
#整体思路：可以使用深度优先搜索合并两个二叉树。从根节点开始同时遍历两个二叉树，并将对应的节点进行合并。
#而且存在3种情况，对一个节点进行合并之后，还要对该节点的左右子树分别进行合并。这是一个递归的过程。
#速背：三行代码搞定，新的根节点合并无需调用递归函数，直接新建一个根节点，使合并的两个根节点的值相加。
#新的左子树调用递归函数合并两个数的左子树，新的右子树调用递归函数合并两个数的右子树
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



#方法二（广度优先搜索）
#整体思路：广度优先搜索离不开队列，所以广度优先搜索是队列
#速背：  广度优先搜索并不需要递归的方法，先定义一个根节点和三个队列，队列用collections对象，并且用deque和popletf
#方法控制入队或者出队，然后就考试进入循环，循环的持续条件是两个队列都不为空，每次循环所有队列都要出队一个元素，后两个队列出队的左右子树需要记录下来
#也就是有4棵树被记录，然后分别对两颗左子树和两颗右子树做判断，判断都是一样的，具体步骤为：
#如果两颗子树都存在，就通过求和新建节点，然后将新建节点赋值给原节点的子树，然后入队。
#如果只存在一颗树的话，直接赋值。
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        
        merged = TreeNode(t1.val + t2.val)  #先定义一个新的根节点
        queue = collections.deque([merged])  #定义三个队列，第一个队列存放新树的节点
        queue1 = collections.deque([t1])  #剩下两个节点存放输入两颗树的节点
        queue2 = collections.deque([t2])

        while queue1 and queue2:  #队中都有元素就一直循环
            node = queue.popleft()  #这里popleft()是从左出队的意思，从第一个队列种弹出的元素就是正是新树需要构造的节点
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            left1, right1 = node1.left, node1.right #拿到两棵树的左右子树
            left2, right2 = node2.left, node2.right
            if left1 or left2:   #先看左子树，左子树种只要有一个子树不为空就要进行判断
                if left1 and left2:   #如果左子树和右子树都不为空
                    left = TreeNode(left1.val + left2.val) #左子树的根节点就新建一个值
                    node.left = left  #并将这个新建的节点赋值给左子树的值
                    queue.append(left)  #然后三个队列各自入队，但是要注意新建的这个值需要放在第一个队列当中
                    queue1.append(left1)
                    queue2.append(left2)
                elif left1:   #如果只有一个节点不为空的话，就将剩下的子树赋给新树当中，右子树同理
                    node.left = left1
                elif left2:
                    node.left = left2
            if right1 or right2:  #右子树同理
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    node.right = right
                    queue.append(right)
                    queue1.append(right1)
                    queue2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2
        
        return merged




if __name__ == "__main__":
    t1 = List2Tree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])
    t2 = List2Tree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])

    test = Solution()
    print(test.mergeTrees(t1, t2))
    pass