# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode("head")
        current_node = head
        carry = 0
        while l1 or l2:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            carry, total = divmod(carry + x + y, 10)

            # current_nodeに新しくListNodeを連結
            current_node.next = ListNode(total)
            # current_nodeを新しく連結したListNodeに移動
            current_node = current_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            current_node.next = ListNode(carry)

        return head.next

