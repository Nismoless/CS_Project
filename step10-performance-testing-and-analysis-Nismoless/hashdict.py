from dictabs import DictAbstract
from lldict import LLDict

class HashDict(DictAbstract):
    def __init__(self):
        self._buckets = [LLDict() for _ in range(1301)]
        self._size = 0

    def __contains__(self, key):#Jonathan Cervantes
        """Check if the key exists in the hash dict."""
        return self._find(key) != None#Returns if key is found and none if it isnt found
        
    def _find(self, key):#Jonathan Cervantes
        """Return the node if it exists, else None."""
        bucket = key % 1301#computes the hash value for the key
        cur_node = self._buckets[bucket]._head#Gets first item in selected bucket
        while cur_node != None:#while loop checks items in bucket until there is none
            if cur_node.key == key:#checks if the item we're looking at has the same key we're looking for
                return cur_node#Returns value associated with the key if it is found
            cur_node = cur_node.next
        return None#if the key isn't found it returns none
    
    def pop(self, key):#Jonathan Cervantes
        """Remove and return the value associated with the key."""
        node = self._find(key)#searches for the key in the data structure
        if node == None:#if the key isn't found
            raise KeyError(f"Key {key} not found")#Error is raised with a print statement
        bucket = key % 1301#calculates where the key should be
        self._buckets[bucket].pop(key)#Removes the key from selected bucket and removes the value associated with the key
        return node.value#Returns value associated with the key that was removed

    def __setitem__(self, key, value): # Rob Eusanio
        node = self._find(key) # check if key already exists
        if node != None: # if it exists 
            node.value = value # change to new value
        # if key doesn't exist
        bucket_index = key % 1301 # hash key to bucket_index
        self._buckets[bucket_index][key] = value # add value to bucket (LLdict)
        self._size += 1 # increase size

    def __str__(self):
        song_list = self.values()
        songs_string = ""
        for song in song_list:
            songs_string = songs_string + str(song)
        return songs_string
    
    def __len__(self):
        return self._size

    # Fabian V.  
    def __getitem__(self, key):
           node = self._find(key) # use the _find method to find the index of the key
           if node is None: # key not found
               raise KeyError("Item does not exist")
           return node # return the node
    
    # Fabian V.  
    def values(self):
        # Return a list of all values 
        values_list = [] # empty list to put values into
        for bucket in self._buckets: # Iterate through each bucket
            cur_node = bucket._head # Get the head of the linked list for the bucket
            while cur_node is not None: 
                values_list.append(cur_node.value) # Add the value to the list
                cur_node = cur_node.next # Move on to the next node and append again
        return values_list # Returns the list 
    
    # # Fabian V.  
    # def _values(self, node, values_list): # This function collects values
    #     if node is None:
    #         return values_list # Empty list
    #     values_list.append(node.value)
    #     return self._values(node.next, values_list) # Next node (recursive)