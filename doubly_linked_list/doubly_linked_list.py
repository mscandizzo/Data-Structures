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
    self.count = 0

  def iter(self):
    current = self.head
    while current:
      node_val = current
      current = current.next
      yield node_val

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

  def move_to_front(self, value):
    for node_val in self.iter():
      if node_val.value != value:
          next 
      else:
        node_val.prev.next = node_val.next
        node_val.next.prev = node_val.prev
        self.head = node_val

  def move_to_end(self, value):
    for node_val in self.iter():
      if node_val.value != value:
          next
      else:
        node_val.prev.next = node_val.next
        node_val.next.prev = node_val.prev
        self.tail = node_val

  def delete(self, value):
    current = self.head
    node_deleted = False
    if current is None:
      node_deleted = False
    elif current.value == value:
      self.head = current.next
      self.head.prev = None
      node_deleted = True
    elif self.tail.value == value:
      self.tail = self.tail.prev
      self.tail.next = None
      node_deleted = True
    else:
      while current:
        if current.value == value:
          current.prev.next = current.next
          current.next.prev = current.prev
          node_deleted = True
        current = current.next
    if node_deleted:
      self.count -=1
