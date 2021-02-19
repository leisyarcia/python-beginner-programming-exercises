def number_of_bottles():
    for num in range(99,2,-1):
        print(f'{num} bottles of milk on the wall, {num} bottles of milk.\nTake one down and pass it around, {num-1} bottles of milk on the wall.')
    print('2 bottles of milk on the wall, 2 bottles of milk.\nTake one down and pass it around, 1 bottle of milk on the wall.\n1 bottle of milk on the wall, 1 bottle of milk.\nTake one down and pass it around, no more bottles of milk on the wall.\nNo more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, 99 bottles of milk on the wall.')
number_of_bottles()