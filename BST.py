'''
Molina Nhoung
CS302
3/18/24
Program 4/5
The BST data structure to deal with storing items in an inventory. Each node can be
a different item type when the item is inserted into the list. Each node has a
linear linked list to hold duplicate items. To use an item, the list must be checked
first to use duplicates before deleting the node entirely.
'''
class TNode:
    #default constructor
    def __init__(self):
        self._data = []
        #self._head = None
        self._left = None
        self._right = None
        
    #destructor
    def __del__(self):
        self._head = None
        self._left = None
        self._right = None
    #set the left child
    def set_left(self, toset):
        self._left = toset
        
    #set the right child
    def set_right(self, toset):
        self._right = toset
        
    #get the left pointer
    def get_left(self):
        return self._left
    
    #get the right pointer
    def get_right(self):
        return self._right
    
class tree:
    #default constructor
    def __init__(self):
        self._root = None
        
    #wrapper function to insert into the tree
    def insert(self, to_add):
        self._root = self._insert(self._root, to_add)
        
    #recursive function to insert into the tree
    def _insert(self, root, to_add):
        if root == None:
            root = TNode()
            #root._data = to_add
            #root._head = LNode()
            root._data.append(to_add)
            return root
        #if to_add is less than current data, go left
        if to_add < root._data[0]:
            root.set_left(self._insert(root.get_left(), to_add))
        elif to_add > root._data[0]:
            root.set_right(self._insert(root.get_right(), to_add))
        #when we encounter duplicate data
        else:
            #add at the head of the list
            root._data.append(to_add)
        return root
    
    #display the tree, wrapper
    def display(self):
        if self._root == None:
            return False
        self._display(self._root)
    
    #recursive display
    def _display(self, root):
        if root == None:
            return False
        self._display(root.get_left())
        root._data[0].display_item()
        print(f'\tUse: {len(root._data)}')
        self._display(root.get_right())
        return True
    
    #count the nodes in the tree to not go past max inventory, should only hold 10 items
    def count_tree(self):
        if self._root == None:
            return 0
        return self._count_tree(self._root)
    
    #recursive call to count the tree:
    def _count_tree(self, root):
        if root == None:
            return 0
        #count the list
        count_dup = len(root._data)
        #recursively go through the tree and hold the count
        left_count = self._count_tree(root.get_left())
        right_count = self._count_tree(root.get_right())
        #returns the count
        return count_dup + left_count + right_count
    
    #retrieve an item by name, wrapper function
    def retrieve(self, to_retrieve):
        if not isinstance(to_retrieve, str):
            raise ValueError('not a string')
        if len(to_retrieve) < 1:
            raise ValueError('empty string')
        if self._root == None:
            return False
        return self._retrieve(self._root, to_retrieve)
        
    #recursive function
    def _retrieve(self, root, to_retrieve):
        if root == None:
            return False
        #check if same data, then return the data
        if root._data[0] == to_retrieve:
            return root._data[0]
        if to_retrieve < root._data[0]:
            return self._retrieve(root.get_left(), to_retrieve)
        else:
            return self._retrieve(root.get_right(), to_retrieve)
        
    #remove one item in the list, wrapper function
    def remove(self, to_remove):
        if not isinstance(to_remove, str):
            raise ValueError('not a string')
        if len(to_remove) < 1:
            raise ValueError('empty string')
        if self._root == None:
            return False
        #call the recursive then come back to reconnect
        self._root = self._remove(self._root, to_remove)
        return True
    
    #recursive function to remove one item
    def _remove(self, root, to_remove):
        if root == None:
            return None
        #traverse left and right until we find the node
        if to_remove < root._data[0]:
            root.set_left(self._remove(root.get_left(), to_remove))
            return root
        elif to_remove > root._data[0]:
            root.set_right(self._remove(root.get_right(), to_remove))
            return root
        #found the node, now check cases
        if len(root._data) > 1:
            root._data.pop(0)
            return root
        #leaf
        if root.get_left() == None and root.get_right() == None:
            return None
        #only left child, right child is none
        elif root.get_left() and root.get_right() == None:
            #root = root.get_left()
            return root.get_left()
        #only right child, left child is none
        elif root.get_left() == None and root.get_right():
            #root = root.get_right()
            return root.get_right()
        #have both children
        else:
            #check if ios is immediate right, then hold and replace
            if root.get_right().get_left() == None:
                left = root.get_left()
                right = root.get_right()
                root = right
                root.set_left(left)
                return root
                
            #find the ios to replace root, hold and replace
            ios = self.find_ios(root.get_right())
            #hold onto root's children
            left = root.get_left()
            right = root.get_right()
            root = ios
            root.set_left(left)
            root.set_right(right)
            return root
    
    #find the ios to replace a node        
    def find_ios(self, root):
        if root.get_left() == None:
            hold = root
            root = root.get_right()
            return hold
        return self.find_ios(root.get_left())