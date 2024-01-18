# -----------------Q8-------------------
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize the table with None values

    def _hash_function(self, key):
        return hash(key) % self.size  # Basic hash function using Python's built-in hash function

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            # If the index is empty, create a new node
            self.table[index] = Node(key, value)
        else:
            # If the index is not empty, traverse the chain and insert at the end
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value  # Update value if key already exists
                    return
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value  # Return value if key is found
            current = current.next
        return None  # Key not found

    def delete(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        previous = None

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next  # Remove node from table
                else:
                    self.table[index] = current.next  # Update the head of the table
                return
            previous = current
            current = current.next
# -----------------Q9-------------------
def even_or_odd(num):
    # Check if the least significant bit is set (1)
    if num & 1 == 0:
        return "Even"
    else:
        return "Odd"

def count_set_bits(number):
    count = 0
    while number:
        # Increment count if the least significant bit is set (1)
        if number & 1 == 1:
            count += 1
        # Right shift the number to move to the next bit
        number >>= 1

    return count


if __name__ == '__main__':
    # -------Q8--------
    hash_table = HashTable(size=9)
    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")
    print("==========Q8==========")
    print("Search Result (key2):", hash_table.search("key2"))
    hash_table.delete("key2")
    print("Search Result (key2):", hash_table.search("key2"))
    # -------Q9-------
    # Q9-1
    print("==========Q9==========")
    num = 10
    result = even_or_odd(num)
    print(f"The number {num} is {result}.")
    # Q9-2
    integer_to_count_bits = 9
    result = count_set_bits(integer_to_count_bits)
    print(f"The number of set bits in {integer_to_count_bits} is {result}.")
