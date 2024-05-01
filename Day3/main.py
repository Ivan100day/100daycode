"""Tests the HashMap class and its functions"""

from hash_map import HashMap


def solution(keys, values):
    tup_list = list(zip(keys, values))
    hashmap = HashMap()
    for i in range(len(tup_list)):
        hashmap.set_item(tup_list[i])
        tup = tup_list[i]
        print(hashmap.get_value(tup[0]))
        
    hashmap.remove_element("key2")
    print(hashmap.get_value("key1"))
    # print(hashmap.get_value("key2"))


def main():
    keys = ["key1", "key2"]
    values = [1, 2]
    solution(keys, values)

main()