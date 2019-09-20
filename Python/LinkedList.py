class LinkNode:
	def __init__(self, val):
		self.val = val
		self.next = None  # the pointer initially points to nothing

node1 = LinkNode(12)
node2 = LinkNode(15)
node3 = LinkNode(98)

node1.next = node2 # 12->15
node2.next = node3 # 15->98


curr = dummy = LinkNode(0)

curr.next = node1  # 0->12


curr = curr.next
print(curr.val)

curr = curr.next.next.next

#0->12->15->98
if curr==None or dummy==None:
	print("none")
else:
	print("not none")

s = "strings"

dic = enumerate(s)

for item in dic:
	print(item)