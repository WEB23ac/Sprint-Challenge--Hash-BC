#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    

# * adds each weight entry to HT
    for i in range(length):
        hash_table_insert(ht, weights[i], i)


    for j in range(length):
        check_val = limit - weights[j]
        matched_idx = hash_table_retrieve(ht, check_val)

        if matched_idx is not None:
            if matched_idx > j:
                return (matched_idx, j)
            else:
                return  (j, matched_idx)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
