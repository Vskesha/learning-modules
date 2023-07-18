from collections import OrderedDict


# Solution using OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        self.od[key] = value
        self.od.move_to_end(key)
        if len(self.od) > self.capacity:
            self.od.popitem(last=False)



# Solution using dictionary and double-linked list
class ListNode:
    def __init__(self, key = 0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache2:

    def __init__(self, capacity: int):
        self.start = ListNode()
        self.end = ListNode()
        self.start.next = self.end
        self.end.prev = self.start
        self.d = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.remove_from_linked_list(node)
        self.insert_after_start(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.remove_from_linked_list(node)
        else:
            node = ListNode(key, value)
        self.insert_after_start(node)
        self.d[key] = node
        if len(self.d) > self.capacity:
            last = self.end.prev
            self.remove_from_linked_list(last)
            key = last.key
            del self.d[key]

    def remove_from_linked_list(self, node: ListNode) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert_after_start(self, node: ListNode) -> None:
        after_start = self.start.next
        after_start.prev = node
        node.next = after_start
        self.start.next = node
        node.prev = self.start


def main():
    null = None
    funcs = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    data = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expected = [null, null, null, 1, null, -1, null, -1, 3, 4]

    cache = LRUCache(data[0][0])
    result = [None]
    for func_string, params in zip(funcs[1:], data[1:]):
        if func_string == 'put':
            result.append(cache.put(*params))
        elif func_string == 'get':
            result.append(cache.get(*params))
        else:
            print('Unknown_function')
    print(expected)
    print(result)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    main()
