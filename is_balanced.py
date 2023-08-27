from linked_stack import LinkedStack
from linked_queue import LinkedQueue

def is_balanced(string):
    """Checks if the input string has balanced brackets
    
    :Input:
        string (str): The input string to check
    
    :Returns:
        bool: True if the input string has balanced brackets
    
    :Complexity: O(N) where N is the length of the string
    """
    stack = LinkedStack()
    queue = LinkedQueue()
    for char in string:
        pass
        # add code here

    return stack.is_empty() and queue.is_empty()


print(is_balanced("[{([)}]"))
