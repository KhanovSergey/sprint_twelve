def solution(node):
    p = node
    q = p.next
    p.next = None
    p.prev = q
    while q is not None:
        q.prev = q.next
        q.next = p
        p = q
        q = q.prev
    node = p
    return node
