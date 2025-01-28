# Define a Node class to represent each element in the linked list
class Node:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.next = None    # Pointer to the next node, initially None

    def __str__(self):
        return f'Node value is: {self.value}.'

# Define a LinkedList class to manage the linked list operations
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # Create a new node with the given value
        self.head = new_node    # Set the head to the new node
        self.tail = new_node    # Set the tail to the new node
        self.length = 1         # Initialize the length of the list to 1

    # Method to append a new node to the end of the list
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:   # If the list is empty
            self.head = new_node  # Set the head to the new node
            self.tail = new_node  # Set the tail to the new node
        else:
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node       # Update the tail to the new node
        self.length += 1  # Increment the length of the list
        return True

    # Method to remove the last node from the list
    def pop(self):
        if self.length == 0:  # If the list is empty
            return None

        temporary = self.head  # Temporary pointer to traverse the list
        previous = self.head   # Pointer to keep track of the node before the last node

        while temporary.next:  # Traverse to the end of the list
            previous = temporary
            temporary = temporary.next

        self.tail = previous  # Update the tail to the second last node
        self.tail.next = None  # Remove the link to the last node
        self.length -= 1  # Decrement the length of the list

        if self.length == 0:  # If the list is now empty
            self.head = None
            self.tail = None
        return temporary.value  # Return the value of the removed node

    # Method to prepend a new node to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.length == 0:  # If the list is empty
            self.head = new_node  # Set the head to the new node
            self.tail = new_node  # Set the tail to the new node
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head = new_node       # Update the head to the new node
        self.length += 1  # Increment the length of the list
        return True

    # Method to remove the first node from the list
    def pop_first(self):
        if self.length == 0:  # If the list is empty
            return None
        temporary = self.head  # Temporary pointer to the current head
        self.head = self.head.next  # Update the head to the next node
        temporary.next = None  # Remove the link to the new head
        self.length -= 1  # Decrement the length of the list
        if self.length == 0:  # If the list is now empty
            self.tail = None
        return temporary.value  # Return the value of the removed node

    # Method to get the node at a specific index
    def get(self, index):
        if index < 0 or index >= self.length:  # If the index is out of bounds
            return None
        temporary = self.head  # Temporary pointer to traverse the list

        for _ in range(index):  # Traverse to the specified index
            temporary = temporary.next
        return temporary  # Return the node at the specified index

    # Method to print all the values in the list
    def print_list(self):
        temp = self.head  # Temporary pointer to traverse the list
        while temp is not None:  # Traverse until the end of the list
            print(temp.value)  # Print the value of the current node
            temp = temp.next   # Move to the next node

    # Method to set the value of a node at a specific index
    def set_value(self, index, value):
        temporary = self.get(index)  # Get the node at the specified index
        if temporary:  # If the node exists
            temporary.value = value  # Set the new value
            return True
        return False  # Return False if the node does not exist

    # Method to insert a new node at a specific index
    def insert(self, index, value):
        if index < 0 or index > self.length:  # If the index is out of bounds
            return False
        if index == 0:  # If inserting at the beginning
            return self.prepend(value)
        if index == self.length:  # If inserting at the end
            return self.append(value)
        new_node = Node(value)  # Create a new node with the given value
        temporary = self.get(index-1)  # Get the node before the specified index
        new_node.next = temporary.next  # Link the new node to the next node
        temporary.next = new_node  # Link the previous node to the new node
        self.length += 1  # Increment the length of the list
        return True

    # Method to remove a node at a specific index
    def remove(self, index):
        if index < 0 or index >= self.length:  # If the index is out of bounds
            return None
        if index == 0:  # If removing the first node
            return self.pop_first()
        if index == self.length - 1:  # If removing the last node
            return self.pop()
        previous = self.get(index-1)  # Get the node before the specified index
        temporary = previous.next  # Get the node to be removed
        previous.next = temporary.next  # Link the previous node to the next node
        temporary.next = None  # Remove the link to the list
        self.length -= 1  # Decrement the length of the list
        return temporary

    # Method to reverse the linked list
    def reverse(self):
        temporary = self.head  # Temporary pointer to the current head
        self.head = self.tail  # Set the head to the current tail
        self.tail = temporary  # Set the tail to the current head
        after_node = temporary.next  # Pointer to the next node
        before_node = None  # Pointer to the previous node
        for _ in range(self.length):  # Traverse the list
            after_node = temporary.next  # Move to the next node
            temporary.next = before_node  # Reverse the link
            before_node = temporary  # Move the previous pointer forward
            temporary = after_node  # Move the temporary pointer forward



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()








