from dictabs import DictAbstract

class _SLNode: # Rob Eusanio
    def __init__(self, key, value):
        self.key = key
        self.value = value

class SLDict(DictAbstract):
    def __init__(self):
        self._sortedlist = None
        self._size=0
    
    def __contains__(self, key):#Jonathan Cervantes
        """Check if the key exists in the sorted list."""
        return self._find(key) != None

    def _find(self, key):#Jonathan Cervantes
        """Return the index of the key if it exists, else -1."""
        # Binary search to find the element by key
        left, right = 0, len(self._sortedlist) - 1
        while left <= right:
            mid = (left + right) // 2
            if self._sortedlist[mid].key == key:
                return mid
            elif self._sortedlist[mid].key < key:
                left = mid + 1
            else:
                right = mid - 1
        return None    
    
    # Not needed for Sorted List
    
    def pop(self, key):#Jonthan Cervantes
        index = self._find(key)
        if index is None:
            raise KeyError("Item does not exist")
        deleted_song = self._sortedlist[index]
        del self._sortedlist[index]
        self._size -= 1
        return deleted_song
        
        
    # Fabian V. - Creating the values list which will display all values in the list
    # def _values(self, node, values_list): # Passing in the node with which we want to begin appending values. The node's value is appended to the list and then moves on to the next node
    #     if node is not None:
    #         values_list.append(node.value)
    #         node = node.next
    #     return values_list # The values_list will contain the values of all nodes that are passed through this function
    
    # Fabian V. - values function to display values
    def values(self):
        return [item for item in self._sortedlist] if self._sortedlist else [] # returns each song in the self._sortedlist, or an empty array if none
    
    # Fabian V. - Get item using the _find function
    def __getitem__(self, key):
        index = self._find(key)
        if index is None:
            raise KeyError("Item does not exist")
        return self._sortedlist[index]

    # Rob Eusanio - set item using insert
    def __setitem__(self, key, value):
        # insert if list empty
        if self._sortedlist == None:
            self._sortedlist = [_SLNode(key,value)]
            self._size += 1
        else:
            self._insert(key, value)

    # Rob Eusanio - Insert in sorted order
    def _insert(self, key, value):
        index = self._find(key) 
        node = _SLNode(key, value)
        # If DNE, insertion sort
        if index == None:
            i = self._size - 1
            # add to end of list if largest id
            if self._sortedlist[i].key < key:
                self._sortedlist.append(node)
                self._size += 1
                return
            # increase space in list by 1
            self._sortedlist.append(self._sortedlist[i])
            # find where to put list in sorted arr
            while i >= 0 and self._sortedlist[i].key > key:
                self._sortedlist[i+1] = self._sortedlist[i]
                i -= 1
            # insert at correct position
            self._sortedlist[i+1] = node
            self._size += 1
        # If exists, edit item
        else: 
            self._sortedlist[index] = node


    def __str__(self): # Rob Eusanio
        if self._size > 0:
            songs = self.values()
            songs_string = ""
            for song in songs:
                songs_string = songs_string + str(song)
            return songs_string
        return None
        
    def __len__(self): # Rob Eusanio
        return self._size