class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        previous = dummy

        while True:

            kth = previous

            for i in range(k):

                kth = kth.next

                if kth is None:
                    return dummy.next

            next_group = kth.next

            current = previous.next
            prev = next_group

            for i in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            temp = previous.next
            previous.next = kth

            previous = temp
        