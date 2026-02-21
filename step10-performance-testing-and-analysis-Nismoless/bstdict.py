from dictabs import DictAbstract

#Declaring a private node class
class _BSTNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    #Definiting our print format. Now we can call
    #print(Node)
    def __str__(self):
        return str(self.key) + ": " + str(self.value)

#Implementing a dictionary using a binary search tree
class BSTDict(DictAbstract):

    def __init__(self):
        #Constructing an empty Dict
        self._root = None
        self._size = 0

    def __len__(self):
        #Return the number of items stored in the dictionary
        return self._size

    #Implementing the python magic method __contains__
    #This will help to use in true or false sentences
    #e.g., if key is in dict
    def __contains__(self, key):
        #Return true if key is in the dictionary, False otherwise
        return not self._find(self._root, key) is None

    #Implementing the python magic method __getitem__
    #This function will help in using this sytax dict[key]
    def __getitem__(self, key):
        #Given a key, return the coresponding value. Raises a KeyError
        #if key is not in the map.
        #dict[4]
        node = self._find(self._root, key)
        if node == None:
            raise KeyError("Item does not exist")
        return node.value

    def values(self):
        values_list = []
        if self._root is not None:
            return self._values(self._root, values_list)
        return None
    
    def _values(self, node, values_list):
        if node is not None:
            values_list = self._values(node.left, values_list)
            values_list.append(node.value)
            values_list = self._values(node.right, values_list)

        return values_list

    #Internal function that looks for the node with
    #the given specified value
    def _find(self, node, key):
        #This is a recursive function that recursively Search
        #through the binary tree to find the key-value pair
        #with the specified given key
        #IF the key is found, return the node with the given key
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._find(node.left, key)
        elif key > node.key:
            return self._find(node.right, key)


    def __setitem__(self, key, value):
        #Implements self[key] = value.  If key is already stored in
        #the dictionary then its value is modified.  If key is not in the map,
        #it is added.
        if self._root == None:
            self._root = _BSTNode(key, value)
            self._size += 1
        else:
            self._insert(self._root, key, value)


    #Internal function to insert a key-value pair into the dictionary
    def _insert(self, node, key, value):
        # If a matching key found, then update the value
        if node.key == key:
            node.value = value

        # If the matching key is smaller, then look in
        # the left subtree
        elif key < node.key:
            if node.left is not None:
                self._insert(node.left, key, value)
            else:
                node.left = _BSTNode(key, value)
                self._size += 1
        # If the matching key is larger, then look in the
        # right subtree
        else:
            if node.right is not None:
                self._insert(node.right, key, value)
            else:
                node.right = _BSTNode(key, value)
                self._size += 1

    #Remove a node from the tree with the indicated key
    #Return the value after removing the node
    #Raise a KeyError if the key is not in the map."
    def pop(self, key):

        #Calling the __getitem__ function to get the value
        #If the entry with the given key
        value = self[key]
        self._root = self._remove(self._root, key)
        self._size -= 1
        return value

    #Internal helper function that recursively search for the node
    #with the given key. If the key does not exist, then raise an
    #exception
    def _remove(self, node, key):

        # Key is not found, raise an exception
        assert node is not None, "Cannot remove non-existent key."

        # If key is smaller, then go to the left tree
        if key < node.key:
            node.left = self._remove(node.left, key)

        # IF data is larger, go to the right tree
        elif key > node.key:
            node.right = self._remove(node.right, key)

        # key is found
        else:
            # Empty left side
            if node.left is None:
                temp = node.right
                node = None
                return temp
            # Empty right child
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            # Has two children
            # Find the inorder successor and replace it
            # with the node
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            #Delete the inorder successor after swapping
            node.right = self._remove(node.right, node.key)

        return node

    # Internal helper function that looks for the smallest successor key
    def _min_value_node(self, node):
        current = node
        while (current.left is not None):
            current = current.left
        return current

    # Inorder traversal to print the tree
    # There is a better way of implementing a print function
    # through using iterators. This part is more advanced
    # Will use a simple print function that loops through the tree
    def __str__(self):
        if self._root is not None:
            self._print_tree(self._root)

    # Internal helper function that recursively print
    # everything in the tree
    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            #print("{key} : {value}".format(key = node.key, value = node.value))
            print(node)
            self._print_tree(node.right)