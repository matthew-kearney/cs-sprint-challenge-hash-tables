#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # create cache
    cache = {}
    # create an arr that grows with length input
    storage = [None] * length
    #  loop thru our tickets input arr
    for i in tickets:
        if i.source == "NONE":
            storage[0] = i.destination
        cache[i.source] = i.destination
# loop thru range starting at 1 and end at our given length
    for x in range(1, length):
        # reconstruct our storage arr with the proper order
        storage[x] = cache[storage[x - 1]]

    return storage
