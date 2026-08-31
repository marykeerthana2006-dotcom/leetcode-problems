import heapq

class Solution:
    def mergeKLists(self, lists):

        dummy = ListNode(0)
        tail = dummy

        heap = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:

            value, i, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next