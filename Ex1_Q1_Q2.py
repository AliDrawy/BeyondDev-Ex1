
# --------------------Q1-----------------------
def rev_string(S):
    # convert the string to list
    rev_list= list(S)
    # count the length
    n = len(rev_list)
    # reverse the list in n/2
    for i in range(len(rev_list) // 2):
        rev_list[i], rev_list[n - 1 - i] = rev_list[n - 1 - i], rev_list[i]
    # convert list to string
    rev_string = ''.join(rev_list)
    return rev_string


def find_max_min_in_array(a):
    # Check if the array is empty
    if not a:
        return None

    # Initialize max and min with the first element of the array
    max = a[0]
    min = a[0]

    # Iterate through the array to find max and min
    for num in a:
        if num > max:
            max = num
        elif num < min:
            min = num

    return max, min


def remove_duplicates(a):
    # Check if the array is empty
    if not a:
        return []

    new_a = [a[0]]
    for i in range(1, len(a)):
        if a[i] != new_a[-1]:  # Compare with the last element in new_a if it's not the same as add the element
            new_a.append(a[i])
    return new_a

# --------------------Q2-----------------------
# create Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# create linked list
class LinkedList:
    def __init__(self):
        self.head = None
    # add node to linked list
    def append(self, data):
        new_node = Node(data)
        # if the linked list empty the head of linked list = the new node
        if not self.head:
            self.head = new_node
            return
        # add the node in the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    # reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        # change the next pointer of the node to the previous node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def middle_element(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer.data

    def detect_cycle(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                # Detected a cycle
                return True

        # No cycle detected
        return False
    # print the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == '__main__':
    # ---------Q1----------
    # Q1-1
    print(rev_string("hellow, world"))
    # Q1-2
    print(find_max_min_in_array([3, 1, 4, 1, 5, 9]))
    # Q1-3
    print(remove_duplicates([1, 1, 2, 2, 2, 3, 4, 4, 5]))
    # ---------Q2----------
    my_linked_list = LinkedList()
    for i in range(1, 10):
        my_linked_list.append(i)
    print("Original Linked List:")
    my_linked_list.display()
    # Q2-1
    print("\nReversed Linked List:")
    my_linked_list.reverse()
    my_linked_list.display()
    # Q2-2
    print("\nMiddle Element of Linked List:", my_linked_list.middle_element())
    # Q2-3
    my_linked_list.reverse()
    has_cycle = my_linked_list.detect_cycle()
    if has_cycle:
        print("Linked List has a cycle.")
    else:
        print("Linked List does not have a cycle.")

    # ---------Q3----------
