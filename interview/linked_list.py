from hashlib import new


class Node:
    """

    An oblject for sorting a single node of a linked list models two attributes - data
    and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
       self.data = data


    def __repr__(self):
        return "<Node data: %s>" % self.data

class linked_list:

      """
    singly linked list
    """
      def add(sel, data):
          new_node = Node(data)

        



  