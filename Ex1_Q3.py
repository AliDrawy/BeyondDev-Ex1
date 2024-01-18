from queue import Queue
# ==================== 1 =======================
class Stack_using_2queues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, data):
        # put the element into the first queue
        self.queue1.put(data)

    def pop(self):
        if self.queue1.empty() and self.queue2.empty():
            return None

        # Move elements from queue1 to queue2 until only one element is left
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        # return the last element from queue1
        popped_element = self.queue1.get()

        # Swap the names of queue1 and queue2 to keep the order consistent
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_element

# ==================== 2 =======================
class Queue_using_2stacks:
    def __init__(self):
        self.stack1 = []  # For enqueue operations
        self.stack2 = []  # For dequeue operations

    def push(self, data):
        # Push the element onto the first stack
        self.stack1.append(data)

    def pop(self):
        if not self.stack2:
            # Transfer elements from stack1 to stack2 if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            # If stack2 is still empty, the queue is empty
            return None

        # Return the front element from stack2 (FIFO)
        return self.stack2.pop()

# ==================== 3 =======================
def is_balanced_parentheses(s):
    stack = []
    opening_brackets = "({["  # Opening parentheses
    closing_brackets = ")}]"  # Closing parentheses

    for i in s:
        if i in opening_brackets:
            # If an opening parenthesis, push onto the stack
            stack.append(i)
        elif i in closing_brackets:
            # If a closing parenthesis, check if the stack is empty
            if not stack:
                return False

            # Pop the top element from the stack
            top_element = stack.pop()

            # Check if the popped element matches the corresponding opening parenthesis
            if opening_brackets.index(top_element) != closing_brackets.index(i):
                return False

    # After processing all characters, the stack should be empty for a balanced expression
    return not stack



if __name__ == '__main__':
    # -------------Q3---------------
    # Q3-1
    print("\nQ3-1\n")
    stack = Stack_using_2queues()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Output: 3
    print(stack.pop())  # Output: 2
    print(stack.pop())  # Output: 1
    # Q3-2
    print("\nQ3-2\n")
    queue = Queue_using_2stacks()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.pop())  # Output: 1
    print(queue.pop())  # Output: 2
    print(queue.pop())  # Output: 3
    # Q3-3
    print("\nQ3-3\n")
    s = "{[()]}"
    result = is_balanced_parentheses(s)
    print(s)
    if result:
        print("there's a balanced parentheses.")
    else:
        print("there's not a balanced parentheses.")