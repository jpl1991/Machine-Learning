def superStack(operations):
	stack = []
	for operation in operations:		
		oper = str(operation).split(" ")
		
		if(oper[0] == "push"):
			
			stack.append(int(oper[1]))
			print(oper[1])
			
		elif(oper[0] == "pop"):
			stack.pop()
			if stack == []:
				print("EMPTY")
			else:
				print(stack[len(stack)-1])
		elif(oper[0] == "inc"):
			l = int(oper[1])
			for i in range(l):
				stack[i] += int(oper[2])
			print(stack[len(stack)-1])
	return stack

ls = ["12", "push 4", "pop", "push 3", "push 5","push 2", "inc 3 1", "pop","push 1", "inc 2 2", "push 4","pop", "pop"]

stack = superStack(ls)
