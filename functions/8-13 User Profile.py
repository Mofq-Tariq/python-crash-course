def build_profile(first,last,**user_info) :
    user_info["first"]=first
    user_info["last"]=last
    return user_info
profile=build_profile("mowafaq","malahem",father="Tariq",location="Amman",age=19)
for info in profile.keys() :
    print(info,profile[info])