def make_album(artist,album_title,number_of_songs=0) :
    "making an album of the artist name and the title"
    temp= {
        "artirst":artist ,
        "title":album_title
    }
    if(number_of_songs) :
        temp["numer of songs"]=number_of_songs
    return temp
while True :
    print("enter the artist name and title and you may \nenter the number of songs  if you dont want type any vale <=0" \
    ", \nif you want to quit enter two numbers for each of them")
    artist=input("artist : ")
    title=input("title : ")
    "strip removes the arguments from start and end of string "
    artist=artist.strip(" ")
    title=title.strip(" ")
    if artist.isdigit() and title.isdigit() :
        break
    number_of_songs=int(input("number of songs : "))
    user_album=make_album(artist,title,max(0,number_of_songs))
    for i in user_album :
        if i=="numer of songs" :
            print(f"{i} are {user_album[i]}",end=" | ")
        else :
            print(f"{i} is {user_album[i]}",end=" | ")
    print()
    