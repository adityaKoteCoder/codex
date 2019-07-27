class Stack:

    def __init__(self):
        self.st =[]

    def push(self,ele):
        self.st.append(ele)
        print("push success")

    def pop(self):
        if self.is.empty():
            print("stack" is empty")
        else:
            ele = self.st.pop()
            print(f"pop successful")

    def display(self):
        if self.is_empty():
            print("underflow")
        else:
            print("elements in the stack are:")
            for i in range(len(self.st)-1,-1,-1):
                print(self.st[i])

    def search(self):
        if self.is.empty:
            print("element is empty")
        else:
            num = int(input("Enter the ele to search:"))
            if num in self.st:
                print(f"element found at pos (self.st.index(num)+1)")
            else:
                print("elements not found")

    def is.empty(self):
        if len(self.st) == 0:
            return True
        else:
            print("elements not found")
    
    else:
        print("element not found")

if __name__ == "__main__":
    st.stack()]
    opt-dict = (1.st.push,2.st.pop,3.st.search.4.st.show,5.exit)
    while True:
        print("1.Push 2.Pop 3.search 4.show 5.exit")
        try:
            ch = int(input("enter the choice"))
            if ch == 1:
                ele = input("enter the element to be pushed")
                st.push(ele)
            
            elif ch ==2:
                st.pop()
            
            elif ch==3:
                ele = input("enter the element to be pushed")
                rest = st.search(ele)
            elif ch ==4:
