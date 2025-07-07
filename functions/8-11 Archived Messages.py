def show_messages(text) :
    "prints the passed list"
    for i in text :
        print(i,end=" ")
    print()
def send_messages(text) :
    sent_messages=[]
    show_messages(text)
    for i in range(len(text)-1,0-1,-1) :
        sent_messages.append(text[i])
        text.pop()
    return sent_messages
Text=["my","record","c++","now","human"]
new_text=send_messages(Text[:])
show_messages(Text)
show_messages(new_text)