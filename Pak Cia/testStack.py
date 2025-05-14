from stack import Stack
import random
sizeStack = 6
st = Stack(sizeStack)
while(sizeStack):
    data = random.randrange(1,100)
    print("Pushing ", data)
    st.push(data)
    sizeStack-=1
print("Stack Size ",st.size())
print("Top Stack ",st.peek())
print("Popping ",st.pop())
print("Top Stack ",st.peek())
