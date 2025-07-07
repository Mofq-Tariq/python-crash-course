def sandwithc_items(*items) :
    """ gives the items that the use want to order"""
    return items
def print_items(items) :
    for item in items :
        print(item,end=" ")
    print()
order_1=sandwithc_items("garlic","katchap","meat")
print_items(order_1)
order_2=sandwithc_items("onion","chicken")
print_items(order_2)
order_3=sandwithc_items("chicken","meat","wings","salt","peper","tomato")
print_items(order_3)
