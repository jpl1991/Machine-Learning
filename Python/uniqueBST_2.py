class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def generateTree(self, n):
		'''
		:type n: int
		:rtype List[TreeNode]
		'''
		if n == 0:
			return []
		return self.helper(1,n)

	def helper(self, start, end):
		ls = [];

		if(start > end):
			ls.append(None)
			return ls


		for i in range(start, end+1):

			leftSubtree = self.helper(start, i-1)

			rightSubtree = self.helper(i+1, end)

			for j in range(len(leftSubtree)):
				left = leftSubtree[j]

				for k in range(len(rightSubtree)):

					right = rightSubtree[k]
					node = TreeNode(i)
					node.left = left
					node.right = right
					ls.append(node)

		return ls

def preorder(root):

	if(root != None):
		print(root.val, end=" ")
		preorder(root.left)
		preorder(root.right)
	else:
		print("Null")



tree = Solution();
result = tree.generateTree(3)

for i in range(len(result)-2):
	preorder(result[i])
	print()

