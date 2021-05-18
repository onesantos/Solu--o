def has_cycle(head):
    if head is None:
        return 0
    cont = 0
    n = head
    while n is not None:
        n = n.next
        cont += 1
        if cont > 100:
            return 1
    return 0
