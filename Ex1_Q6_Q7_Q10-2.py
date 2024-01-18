# ---------------------Q6-------------------------
def linear_search(arr, num):
    for i, element in enumerate(arr):
        if element == num:
            return i  # Return the index if the num is found
    return -1  # Return -1 if the num is not found

def binary_search(arr, num):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == num:
            return mid  # Return the index if the num is found
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the num is not found

# ---------------------Q7-------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def generate_permutations(s):
    # Base case: if the input string is empty, return a list containing an empty string
    if len(s) == 0:
        return ['']

    # Extract the first character and the rest of the string
    current_char = s[0]
    rest_of_string = s[1:]
    # Recursively generate permutations for the remaining string
    permutations_without_current = generate_permutations(rest_of_string)
    # Initialize the list to store all permutations
    all_permutations = []
    # Call the helper function to generate permutations with the current character
    generate_per_helper(all_permutations, permutations_without_current, current_char, 0, 0)
    # Return the final list of all permutations
    return all_permutations

def generate_per_helper(all_permutations, permutations_without_current, current_char, j, i):
    # Ensure that j is within the bounds of permutations_without_current
    if j < len(permutations_without_current):
        # Ensure that i is within or at the end of the current permutation
        if i <= len(permutations_without_current[j]):
            # Insert the current character at position i in the current permutation
            new_permutation = permutations_without_current[j][:i] + current_char + permutations_without_current[j][i:]
            # Append the new permutation to the list
            all_permutations.append(new_permutation)
            # Recursively call the helper function for the next position i
            generate_per_helper(all_permutations, permutations_without_current, current_char, j, i + 1)
        # If i reaches the end of the current permutation, move to the next permutation
        if i == len(permutations_without_current[j]):
            generate_per_helper(all_permutations, permutations_without_current, current_char, j + 1, 0)

if __name__ == '__main__':
    # -----------------------Q6------------------------------
    # Q6-1
    arr = [64, 34, 25, 12, 22, 11, 90]
    num = 22
    result_linear = linear_search(arr, num)
    if result_linear != -1:
        print(f"Linear Search: Element {num} found at index {result_linear}.")
    else:
        print(f"Linear Search: Element {num} not found.")
    # Q6-2
    b_arr = [11, 12, 22, 25, 34, 64, 90]
    b_num = 22
    result_binary = binary_search(b_arr, b_num)

    if result_binary != -1:
        print(f"Binary Search: Element {b_num} found at index {result_binary}.")
    else:
        print(f"Binary Search: Element {b_num} not found.")
    # -----------------------Q7------------------------------
    # Q7-1
    number = 5
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")
    # Q7-2

    input_string = "abc"
    result = generate_permutations(input_string)
    print(f"All permutations of {input_string}: {result}")
    # Q10-2

    # factorial:
    #In the worst case, the maximum depth of the call stack is n (when n is the input value).
    # Therefore, the space complexity is O(n).

    # generate_permutations:
    #the depth of the call stack is proportional to the number of permutations,
    # which is n! (factorial of the input length n).Therefore, the space complexity is O(n!).