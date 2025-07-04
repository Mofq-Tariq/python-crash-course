def make_album(artist,album_title,number_of_songs=0) :
    "making an album of the artist name and the title"
    temp= {
        "artirst":artist ,
        "title":album_title
    }
    if(number_of_songs) :
        temp["numer of songs"]=number_of_songs
    return temp
call_1=make_album("yeat","lean")
call_2=make_album("singer","piano")
call_3=make_album("jaffari","the unknown")
for i in call_1 :
    print(f"{i} is {call_1[i]}",end=" | ")
print()
for i in call_2 :
    print(f"{i} is {call_2[i]}",end=" | ")
print()
for i in call_3 :
    print(f"{i} is {call_3[i]}",end=" | ")
print()
call_4=make_album("me","hate",8)
for i in call_4 :
    if i=="numer of songs" :
        print(f"{i} are {call_4[i]}",end=" | ")
    else :
        print(f"{i} is {call_4[i]}",end=" | ")