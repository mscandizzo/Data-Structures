class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    pass

  def insert_before(self, value):
    pass

  def delete(self):
    pass

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_head(self, value):
    new_node  = ListNode(value, None,None)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def remove_from_head(self):
    pass

  def add_to_tail(self, value):
    new_node  = ListNode(value, None,None)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
