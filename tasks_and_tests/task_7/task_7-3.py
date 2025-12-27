from .task_7 import OrderedList, OrderedStringList


def test_ordered_list_add_asc():
    ol = OrderedList(True)
    ol.add(3)
    ol.add(1)
    ol.add(2)
    ol.add(4)

    values = [node.value for node in ol.get_all()]
    assert values == [1, 2, 3, 4]


def test_ordered_list_add_desc():
    ol = OrderedList(False)
    ol.add(3)
    ol.add(1)
    ol.add(2)
    ol.add(4)

    values = [node.value for node in ol.get_all()]
    assert values == [4, 3, 2, 1]


def test_ordered_list_find_asc():
    ol = OrderedList(True)
    ol.add(3)
    ol.add(1)
    ol.add(2)
    ol.add(4)

    node = ol.find(2)
    assert node is not None
    assert node.value == 2
    assert node.next.value == 3
    assert node.prev.value == 1

    node = ol.find(5)
    assert node is None


def test_ordered_list_find_desc():
    ol = OrderedList(False)
    ol.add(3)
    ol.add(1)
    ol.add(2)
    ol.add(4)

    node = ol.find(2)
    assert node is not None
    assert node.value == 2
    assert node.next.value == 1
    assert node.prev.value == 3

    node = ol.find(5)
    assert node is None


def test_ordered_list_delete_asc():
    ol = OrderedList(True)
    ol.add(3)
    ol.add(1)
    ol.add(2)
    ol.add(4)

    ol.delete(2)
    values = [node.value for node in ol.get_all()]
    assert values == [1, 3, 4]

    ol.delete(1)
    values = [node.value for node in ol.get_all()]
    assert values == [3, 4]
    ol.delete(5)
    values = [node.value for node in ol.get_all()]
    assert values == [3, 4]


def test_ordered_list_delete_desc():
    ol = OrderedList(False)
    ol.add(3)
    ol.add(1)
    ol.add(2)
    ol.add(4)

    ol.delete(2)
    values = [node.value for node in ol.get_all()]
    assert values == [4, 3, 1]

    ol.delete(3)
    values = [node.value for node in ol.get_all()]
    assert values == [4, 1]
    ol.delete(5)
    values = [node.value for node in ol.get_all()]
    assert values == [4, 1]


def test_ordered_list_delete_single():
    ol = OrderedList(True)
    ol.add(1)
    ol.delete(1)
    assert ol.head is None
    assert ol.tail is None
    assert ol.len() == 0


def test_ordered_string_list_compare():
    osl = OrderedStringList(True)
    assert osl.compare("  a  ", "b") == -1
    assert osl.compare("b", "  a  ") == 1
    assert osl.compare("  a  ", "a") == 0
