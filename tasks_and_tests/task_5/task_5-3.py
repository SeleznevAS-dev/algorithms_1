from .task_5 import Queue

def test_size():
    queue = Queue()
    assert queue.size() == 0
    queue.enqueue(1)
    assert queue.size() == 1

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.size() == 1
    queue.enqueue(2)
    assert queue.size() == 2
    queue.enqueue(3)
    assert queue.size() == 3
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    
def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3