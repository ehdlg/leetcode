"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""

pairs = {
    "{": "}",
    "(": ")",
    "[": "]"
}

valid_chars = set('[](){}')

def isValid(s:str):
    if len(s) % 2 != 0:
        return False

    pairs = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    valid_chars = set('[](){}')
    stack = []
    
    for i in s:
        if i not in valid_chars:
            return False

        is_closing = pairs.get(i) is None

        if is_closing:
            if len(stack) == 0: 
                return False
            
            pair = stack[len(stack) - 1]

            if pairs.get(pair) != i:
                return False
            else:
                stack.pop()
        else:
            stack.append(i)
    
    return len(stack) == 0






print(isValid('()()'))