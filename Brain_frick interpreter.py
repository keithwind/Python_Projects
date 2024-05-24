class Cell:
    def __init__(self,data,left=None,right=None):
        self.value = data
        self.left = left
        self.right = right
    
    def input(self,input):
        self.value = input
    def output(self):
        return chr(self.value)
    def inc(self):
        self.value += 1
    def dec(self):
        self.value -= 1

class MemoryTape:
    def __init__(self):
        self.curr = Cell(0)
        self.output = ''
    def m_left(self):
        if(self.curr.left == None):
            self.curr.left = Cell(0)
            self.curr.left.right = self.curr
        self.curr = self.curr.left

    def m_right(self):
        if(self.curr.right == None):
            self.curr.right = Cell(0)
            self.curr.right.left = self.curr 
        self.curr = self.curr.right
    
    def execute(self,code):
        i = 0
        mem = self
        while(i < len(code)):
            if(code[i] == '>'):
                mem.m_right()
            elif(code[i]== '<'):
                mem.m_left()
            elif(code[i]=='+'):
                mem.curr.inc()
            elif(code[i]=='-'):
                mem.curr.dec()
            elif(code[i]=='.'):
                self.output += mem.curr.output()
            elif(code[i]==','):
                n = ord(str(input()).strip())
                #n = int(input())
                mem.curr.input(n)
            elif(code[i]=='['):
                if(mem.curr.value == 0):
                    count = 1
                    while(count != 0):
                        i+=1
                        if(code[i]=='['): count+=1
                        elif(code[i]==']'):count -= 1
            elif(code[i]==']'):
                if(mem.curr.value != 0):
                    count = 1
                    while(count != 0):
                        i-=1
                        if(code[i]==']'):count+=1
                        elif(code[i]=='['):count-=1
            elif(code[i] == '\n' or code[i] == ' '):
                i+=1
                continue
            else:
                print(f"Unexpected token '{code[i]}' at position {i}")
                raise Exception
            i+=1



if __name__ == '__main__':
    import sys
    fname = sys.argv[1]
    with open(fname) as f:
        code = f.read().strip()
        mem = MemoryTape()
        mem.execute(code)
        print(mem.output)
    