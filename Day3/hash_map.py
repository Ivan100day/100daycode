"""Defines a Hashmap."""

HASHMAP_ARRAY_SIZE = 10000


class HashMap:
    """This represents a HashMap."""
    
    def __init__(self):
        self.hashmap = [None] * HASHMAP_ARRAY_SIZE

    def _hashed_index(self, key):
        hashed_value = hash(key)
        hashmap_index = hashed_value % HASHMAP_ARRAY_SIZE
        return hashmap_index

    def set_item(self, tup):
        hashmap_index = self._hashed_index(tup[0])
        tup_list = self.hashmap[hashmap_index]
        if tup_list:
            for i in range(len(tup_list)):
                tup_element = tup_list[i]
                if tup_element[0] == tup[0]:
                    tup_list[i] = tup
                    return
            tup_list.append(tup)

        else:
            self.hashmap[hashmap_index] = [tup]

    def get_value(self, key):
        hashmap_index = self._hashed_index(key)
        tup_list = self.hashmap[hashmap_index]
        if tup_list is None:
            raise IndexError("This key does not exist")

        for i in range(len(tup_list)):
            tup_element = tup_list[i]
            if tup_element[0] == key:
                return tup_element[1]

        raise IndexError("This key does not exist")

    def remove_element(self, key):
        hashmap_index = self._hashed_index(key)
        tup_list = self.hashmap[hashmap_index]
        if tup_list is None:
            raise IndexError("This key does not exist")

        for i in range(len(tup_list)):
            tup_element = tup_list[i]
            if tup_element[0] == key:
                tup_list.pop(i)
                return

        raise IndexError("This key does not exist")

