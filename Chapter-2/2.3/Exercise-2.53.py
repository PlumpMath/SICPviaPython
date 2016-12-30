# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
cadr = lambda x: car(cdr(x))
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
memQ = lambda item, x: False if x == None else x if item == car(x) else memQ(item, cdr(x))

def printList(items):
    displayList = lambda items: '[' + displayItems(items) + ']' 
    displayItems = lambda items: displayItem(car(items)) if cdr(items) == None \
                   else displayItem(car(items)) + ', ' + displayItem(cdr(items)) if not callable(cdr(items)) \
                   else displayItem(car(items)) + ', ' + displayItems(cdr(items))
    displayItem = lambda item: '[]' if item == None \
                  else str(item) if not callable(item) \
                  else displayList(item)
    print(displayList(items))

# Print lists
printList(makeList("a", "b", "c"))
# [a, b, c]
printList(makeList(makeList("george")))
# [[george]]
printList(cdr(makeList(makeList("x1", "x2"), makeList("y1", "y2"))))
# [[y1, y2]]
printList(cadr(makeList(makeList("x1", "x2"), makeList("y1", "y2"))))
# [y1, y2]
print(callable(car(makeList("a", "short", "list"))))
# False
print(memQ("red", makeList(makeList("red", "shoes"), makeList("blue", "socks"))))
# False
printList(memQ("red", makeList("red", "shoes", "blue", "socks")))
# [red, shoes, blue, socks]
