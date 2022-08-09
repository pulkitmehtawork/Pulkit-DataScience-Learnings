## reference - https://aman.ai/code/data-structures

# stack - LIFO - last in first out 

# wrapper class to emulate stack as a list in python

class stack:
    # initialize stack with empty list
    def __init__(self , init_val = []):
        self.stack = init_val
    
    # append element at the end
    def push(self,element):
        self.stack.append(element)
        return self.stack

    # pop last element
    def pop(self):
        return self.stack.pop(-1)
    
    # print full stack
    def checkStack(self):
        print(self.stack)

    # get top of stack
    def checkTop(self):
        print(self.stack[-1])

if __name__ =="__main__":
    stack_example = stack()
    stack_example.push(1)
    stack_example.push(2)
    stack_example.push(3)
    print(stack_example.pop())
    stack_example.checkStack()
    stack_example.checkTop()

