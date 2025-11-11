from tasks_and_tests.task_1.task_1 import LinkedList, Node

# Course task number: 1
# Lesson task number: 1.8
# Short name: sum_two_linked_lists
# Complexity: time: O(n), space: O(n)
def sum_two_linked_lists(list1: LinkedList, list2: LinkedList):
    len1 = list1.len()
    len2 = list2.len()
    if len1 == len2:
        result = LinkedList()

        node1 = list1.head
        node2 = list2.head
        for _ in range(len1):
            sm = node1.value + node2.value
            new_result_node = Node(sm)
            result.add_in_tail(new_result_node)

            node1 = node1.next
            node2 = node2.next

        return result

def test_sum_two_linked_lists():
    list1 = LinkedList()
    list2 = LinkedList()
    
    n1 = Node(2)
    n2 = Node(4)
    list1.add_in_tail(n1)
    list1.add_in_tail(n2)
    
    n3 = Node(2)
    n4 = Node(4)
    list2.add_in_tail(n3)
    list2.add_in_tail(n4)
    
    list3 = sum_two_linked_lists(list1,list2)
    assert list3.head.value == 4
    assert list3.tail.value == 8
    