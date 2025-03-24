# class Pokemon():
# 	def  __init__(self, name, hp, damage):
# 		self.name = name
# 		self.hp = hp # hit points
# 		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
# 	def attack(self, opponent):
#             opponent.hp -= self.damage
#             if opponent.hp <= 0:
#                 print(f"{opponent.name} has fainted!")
#             else:
#                 print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
  
  

# pikachu = Pokemon("Pikachu", 35, 55)
# bulbasaur = Pokemon("Bulbasaur", 45, 30) 
# opponent = bulbasaur
# pikachu.attack(opponent)


# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
# lst = ["Jigglypuff", "Wigglytuff"]
# head = None
# for i in reversed(lst):
# 	head = Node(i, head)

# node_1 = head
# node_2 = head.next

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)



# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next


# def add_first(head, new_node):
# 	new_node.next = head
# 	return new_node


# # Using the Linked List from Problem 2
# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)

# print(node_1.value, "->", node_1.next.value)

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def get_tail(head):
#     if not head:
#         return None
    
#     current = head
#     while current.next:
#         current = current.next
#     return current

# num3 = Node("num3")
# num2 = Node("num2", num3)
# num1 = Node("num1", num2)
 
 
# # linked list: num1->num2->num3
# head = num1
# tail = get_tail(num1)
# print(tail.value)


# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
# def ll_replace(head, original, replacement):
# 	curr = head
# 	while curr :
# 		if curr.value == original:
# 			curr.value = replacement
# 		curr = curr.next
 
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> ")
#         current = current.next
#     print("None")


# num3 = Node(5)
# num2 = Node(6, num3)
# num1 = Node(5, num2)
# # initial linked list: 5 -> 6 -> 5

# head = num1
# ll_replace(head, 5, "banana")
# # updated linked list: "banana" -> 6 -> "banana"
# print_linked_list(num1)

# class Node:
# 		def __init__(self, value, next=None):
# 			self.value = value
# 			self.next = next
# 		node = Node('apple')
# 		node.next = Node('banana')
# 		node.next.next = Node('cherry')
# print(node.value)  # Output: apple
# print(node.next.value)  # Output: banana
# print(node.next.next.value)  # Output: cherry
    
# class Card:
# 	def __init__(self, suit, rank):
# 		self.suit = suit
# 		self.rank = rank

# 	#@staticmethod
# 	def is_four_of_a_kind(hand):
# 		rank_count = {}
# 		for card in hand:
# 			if card.rank in rank_count:
# 				rank_count[card.rank] += 1
# 			else:
# 				rank_count[card.rank] = 1

# 		for count in rank_count.values():
# 			if count == 4:
# 				return True
# 		return False

# Here’s how you could implement the node_exists function to check if a node with the given value exists in the linked list:

# python
# def node_exists(head, val):
#     current = head
#     while current:  # Traverse the linked list
#         if current.val == val:  # Check if the current node's value matches
#             return True  # Node exists
#         current = current.next  # Move to the next node
#     return False  # Node does not exist in the list

# def equal_length(head_a, head_b):
#     # Initialize counters for both linked lists
#     length_a = 0
#     length_b = 0
    
#     # Traverse the first list to calculate its length
#     current_a = head_a
#     while current_a:
#         length_a += 1
#         current_a = current_a.next
    
#     # Traverse the second list to calculate its length
#     current_b = head_b
#     while current_b:
#         length_b += 1
#         current_b = current_b.next
    
#     # Compare the lengths of both lists
#     return length_a == length_b