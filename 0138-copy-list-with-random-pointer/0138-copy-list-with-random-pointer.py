class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        mp = {}

        current = head

        while current:
            mp[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            mp[current].next = mp.get(current.next)
            mp[current].random = mp.get(current.random)
            current = current.next

        return mp[head]