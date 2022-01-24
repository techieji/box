def box(table):
    cell_width = max(len(x) for y in table for x in y)
    return '\n'.join([f"┌─{'─┬─'.join(['─'  *  cell_width]  *  len(table[0]))}─┐",
                      f"│ {' │ '.join(x.center(cell_width) for x in table[0])} │",
                      f"├─{'─┼─'.join(['─'  *  cell_width]  *  len(table[0]))}─┤",
                    *[f"│ {' │ '.join( x.ljust(cell_width)  for  x  in  row )} │" for row in table],
                      f"└─{'─┴─'.join(['─'  *  cell_width]  *  len(table[0]))}─┘"])

print(box([['asdf', 'fdsa'], ['a', 'b'], ['faehwfihwaifaw', 'fwiohfoia']]))
