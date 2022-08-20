class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


def fun1(head):
	if(head == None):
		return
	fun1(head.next)
	print(head.data, end = ' ')


def fun2(start):
	if(start == None):
		return
	