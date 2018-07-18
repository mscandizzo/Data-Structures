"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node

  def remove_head(self):
    if not self.head:
      return None
    elif not self.head.get_next():
      head = self.head
      self.head = None
      self.tail = None
      return head.value
    else:
      value = self.head.value
      self.head = self.head.get_next()
      return value

  def contains(self, value):
    if not self.head:
      return None
    current = self.head
    while current:
      if current.value == value:
        return True
      current = current.get_next()
    return False

  def get_max(self):
    if not self.head:
      return None
    max_value = self.head.value
    current = self.head.get_next()
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.get_next()
    return max_value

