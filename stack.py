# Create an empty stack
stack = []

# Push operation (add element)
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Pop operation (remove top element)
removed = stack.pop()
print("Popped element:", removed)

print("Stack after pop:", stack)

# Peek operation (top element)
top = stack[-1]
print("Top element:", top)

# Check if stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")
