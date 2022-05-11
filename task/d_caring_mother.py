def solution(node, elem) -> int:
    count = 0
    while elem != count:
        if node == None:
            return -1
        if elem != node.value:
            node = node.next_item
            count += 1
        else:
            return count
