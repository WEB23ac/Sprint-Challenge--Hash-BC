#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] *( length - 1)

    """
    YOUR CODE HERE
    """

    for i in range (length):
        curr_ticket = tickets[i]
        print(f'curr_ticket', curr_ticket.source, curr_ticket.destination)
        hash_table_insert(hashtable, curr_ticket.source, curr_ticket.destination)

    curr_loc = hash_table_retrieve(hashtable,'NONE')
    route_idx = 0
    while curr_loc is not 'NONE' and curr_loc is not None:
        route[route_idx] = curr_loc
        route_idx += 1
        curr_loc = hash_table_retrieve(hashtable,curr_loc)


    # for i in route:
    #     i = curr_loc
    #     curr_loc = hash_table_retrieve(curr_loc)

    return route
