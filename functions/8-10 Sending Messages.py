def show_messages(text) :
    "prints the passed list"
    for i in text :
        print(i)
def send_messages(text) :
    sent_messages=[]
    show_messages(text)
    for i in text :
        sent_messages.append(i)
        text.remove(i)
    return sent_messages
Text=["my","record","c++","now","human"]
new_text=send_messages(Text)
for i in new_text : # all copied Text valuess
    print(i)
for i in Text : # no output
    print(i)