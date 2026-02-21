from dictabs import DictAbstract

class _LLNode: # Rob Eusanio
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None     

class LLDict(DictAbstract):

    def __init__(self): # Rob Eusanio
        self._head  = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def __contains__(self, key): # Rob Eusanio
        return not self._find(self._head, key) is None
    
    def _find(self, node, key): # Rob Eusanio
        while node is not None:
            if node.key == key:
                return node
            node = node.next
        return None

    def __str__(self):
        songs = self.values()
        songs_string = ""
        for song in songs:
            songs_string = songs_string + str(song)
        return songs_string
        
        

    def __getitem__(self, key):
        node = self._find(self._head, key)
        if node == None:
            raise KeyError("Item does not exist")
        return node.value
    
    def _values(self, node, values_list):
        if node is not None:
            values_list.append(node.value)
            node = node.next
        return values_list
        
    def values(self):
        values_list=[]
        if self._head is not None:
            return self._values(self._head, values_list)
        return values_list
    
    
    def __setitem__(self, key, value):#Jonathan Cervantes - Set Item
        if self._head == None:#checks if the linked list is empty
            self._head = _LLNode(key, value)#creates the new node
            self._size += 1#adds to the collection to reflect the addition of the new node
        else:#else block
            self._insert(self._head, key, value)#calls _insert
   
    def _remove(self, key):#Jonathan Cervantes - Remove Item
        if not self._head:#checks if linked list is empty
            return
        if self._head.key == key:# Checks if the head node contains the key
            self._head = self._head.next#updates _head to the next node in the list
            self._size -= 1
            return
        current = self._head#initializes current to point to the next node
        prev = None#initializes current to point ot the head node
        while current: # Traverse the list to find the key
            if current.key == key:#checks if song_id of the current node matches the key
                if prev:
                    prev.next = current.next#updates the next pointer of the previous node to skip over the current node
                else:
                    self._head = current.next
                if current == self._tail:
                    self._tail = prev
                    self._size = 1
                return#removal completed
            prev = current#updates previous to current node
            current = current.next#moves current to the next node in the list

    def pop(self, key):#Jonathan Cervantes - Pop
        value = self._find(self._head, key)#calls _find, passes both head and key
        self._remove(key)#calls _remove to remove the node associated with the key
        self._size -= 1#decreases the size of the collection by one to reflect the nodes removal
        return value#returns value associated with removed node
    
    def _insert(self, head, key, new_data):#Jonathan Cervantes - Insert At Front
        new_node = _LLNode(key, new_data)#creates new instance of _LLNode and initializes it with provided key and data which is added to the list
        new_node.next = head#sets the next pointer of the new node to the current head
        self._head = new_node#updates the head of the list to be the new node
        return new_node#returns the newly made node