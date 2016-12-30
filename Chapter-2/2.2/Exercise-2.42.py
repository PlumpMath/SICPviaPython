import sys
sys.setrecursionlimit(5000)

# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
listLength = lambda items: 0 if items == None else 1 + listLength(cdr(items))
listRef = lambda items, n: car(items) if n == 0 else listRef(cdr(items), n - 1)
accumulate = lambda op, initial, sequence: initial if sequence == None else op(car(sequence), accumulate(op, initial, cdr(sequence)))
enumerateInterval = lambda low, high: None if low > high else cons(low, enumerateInterval(low + 1, high))
appendList = lambda list1, list2: accumulate(cons, list2, list1)
mapList = lambda p, sequence: accumulate(lambda x, y: cons(p(x), y), None, sequence)
flatMap = lambda proc, seq: accumulate(appendList, None, mapList(proc, seq))
filterList = lambda predicate, sequence: None if sequence == None \
             else cons(car(sequence), filterList(predicate, cdr(sequence))) if predicate(car(sequence)) \
             else filterList(predicate, cdr(sequence))

def printList(items):
    displayList = lambda items: '[' + displayItems(items) + ']' 
    displayItems = lambda items: displayItem(car(items)) if cdr(items) == None \
                   else displayItem(car(items)) + ', ' + displayItem(cdr(items)) if not callable(cdr(items)) \
                   else displayItem(car(items)) + ', ' + displayItems(cdr(items))
    displayItem = lambda item: '[]' if item == None \
                  else str(item) if not callable(item) \
                  else displayList(item)
    print(displayList(items))

# Eight-queens puzzle
emptyBoard = None

def adjoinPosition(row, positions):
    return appendList(positions, makeList(row))

def queens(boardSize):
    def queenCols(k):
        if k == 0:
            return makeList(emptyBoard)
        else:
            return filterList(lambda positions: safe(k, positions),
                              flatMap(lambda restOfQueens: mapList(lambda newRow: adjoinPosition(newRow, restOfQueens),
                                                                   enumerateInterval(1, boardSize)),
                                      queenCols(k - 1)))
    return queenCols(boardSize)

def safe(col, positions):
    def safeIter(q, board, i):
        if i == col:
            return True
        else:
            return q != car(board) and abs(q - car(board)) != abs(col - i) and safeIter(q, cdr(board), i + 1)
    return safeIter(listRef(positions, col - 1), positions, 1)

print(listLength(queens(8)))
# 92
printList(queens(8))
##[[1, 5, 8, 6, 3, 7, 2, 4], [1, 6, 8, 3, 7, 4, 2, 5], [1, 7, 4, 6, 8, 2, 5, 3],
## [1, 7, 5, 8, 2, 4, 6, 3], [2, 4, 6, 8, 3, 1, 7, 5], [2, 5, 7, 1, 3, 8, 6, 4],
## [2, 5, 7, 4, 1, 8, 6, 3], [2, 6, 1, 7, 4, 8, 3, 5], [2, 6, 8, 3, 1, 4, 7, 5],
## [2, 7, 3, 6, 8, 5, 1, 4], [2, 7, 5, 8, 1, 4, 6, 3], [2, 8, 6, 1, 3, 5, 7, 4],
## [3, 1, 7, 5, 8, 2, 4, 6], [3, 5, 2, 8, 1, 7, 4, 6], [3, 5, 2, 8, 6, 4, 7, 1],
## [3, 5, 7, 1, 4, 2, 8, 6], [3, 5, 8, 4, 1, 7, 2, 6], [3, 6, 2, 5, 8, 1, 7, 4],
## [3, 6, 2, 7, 1, 4, 8, 5], [3, 6, 2, 7, 5, 1, 8, 4], [3, 6, 4, 1, 8, 5, 7, 2],
## [3, 6, 4, 2, 8, 5, 7, 1], [3, 6, 8, 1, 4, 7, 5, 2], [3, 6, 8, 1, 5, 7, 2, 4],
## [3, 6, 8, 2, 4, 1, 7, 5], [3, 7, 2, 8, 5, 1, 4, 6], [3, 7, 2, 8, 6, 4, 1, 5],
## [3, 8, 4, 7, 1, 6, 2, 5], [4, 1, 5, 8, 2, 7, 3, 6], [4, 1, 5, 8, 6, 3, 7, 2],
## [4, 2, 5, 8, 6, 1, 3, 7], [4, 2, 7, 3, 6, 8, 1, 5], [4, 2, 7, 3, 6, 8, 5, 1],
## [4, 2, 7, 5, 1, 8, 6, 3], [4, 2, 8, 5, 7, 1, 3, 6], [4, 2, 8, 6, 1, 3, 5, 7],
## [4, 6, 1, 5, 2, 8, 3, 7], [4, 6, 8, 2, 7, 1, 3, 5], [4, 6, 8, 3, 1, 7, 5, 2],
## [4, 7, 1, 8, 5, 2, 6, 3], [4, 7, 3, 8, 2, 5, 1, 6], [4, 7, 5, 2, 6, 1, 3, 8],
## [4, 7, 5, 3, 1, 6, 8, 2], [4, 8, 1, 3, 6, 2, 7, 5], [4, 8, 1, 5, 7, 2, 6, 3],
## [4, 8, 5, 3, 1, 7, 2, 6], [5, 1, 4, 6, 8, 2, 7, 3], [5, 1, 8, 4, 2, 7, 3, 6],
## [5, 1, 8, 6, 3, 7, 2, 4], [5, 2, 4, 6, 8, 3, 1, 7], [5, 2, 4, 7, 3, 8, 6, 1],
## [5, 2, 6, 1, 7, 4, 8, 3], [5, 2, 8, 1, 4, 7, 3, 6], [5, 3, 1, 6, 8, 2, 4, 7],
## [5, 3, 1, 7, 2, 8, 6, 4], [5, 3, 8, 4, 7, 1, 6, 2], [5, 7, 1, 3, 8, 6, 4, 2],
## [5, 7, 1, 4, 2, 8, 6, 3], [5, 7, 2, 4, 8, 1, 3, 6], [5, 7, 2, 6, 3, 1, 4, 8],
## [5, 7, 2, 6, 3, 1, 8, 4], [5, 7, 4, 1, 3, 8, 6, 2], [5, 8, 4, 1, 3, 6, 2, 7],
## [5, 8, 4, 1, 7, 2, 6, 3], [6, 1, 5, 2, 8, 3, 7, 4], [6, 2, 7, 1, 3, 5, 8, 4],
## [6, 2, 7, 1, 4, 8, 5, 3], [6, 3, 1, 7, 5, 8, 2, 4], [6, 3, 1, 8, 4, 2, 7, 5],
## [6, 3, 1, 8, 5, 2, 4, 7], [6, 3, 5, 7, 1, 4, 2, 8], [6, 3, 5, 8, 1, 4, 2, 7],
## [6, 3, 7, 2, 4, 8, 1, 5], [6, 3, 7, 2, 8, 5, 1, 4], [6, 3, 7, 4, 1, 8, 2, 5],
## [6, 4, 1, 5, 8, 2, 7, 3], [6, 4, 2, 8, 5, 7, 1, 3], [6, 4, 7, 1, 3, 5, 2, 8],
## [6, 4, 7, 1, 8, 2, 5, 3], [6, 8, 2, 4, 1, 7, 5, 3], [7, 1, 3, 8, 6, 4, 2, 5],
## [7, 2, 4, 1, 8, 5, 3, 6], [7, 2, 6, 3, 1, 4, 8, 5], [7, 3, 1, 6, 8, 5, 2, 4],
## [7, 3, 8, 2, 5, 1, 6, 4], [7, 4, 2, 5, 8, 1, 3, 6], [7, 4, 2, 8, 6, 1, 3, 5],
## [7, 5, 3, 1, 6, 8, 2, 4], [8, 2, 4, 1, 7, 5, 3, 6], [8, 2, 5, 3, 1, 7, 4, 6],
## [8, 3, 1, 6, 2, 5, 7, 4], [8, 4, 1, 3, 6, 2, 7, 5]]
