from abc import abstractmethod
from abc import ABC

class IRSystemAbstract(ABC):

    @abstractmethod
    def search_by_id(self, item_id):
        """Return a song object matching the given unique identifier, or None if not found."""
        pass

    @abstractmethod
    def search_by_name(self, track_name):
        """Return all song objects matching the given track name, or None if not found."""
        pass

    @abstractmethod
    def search_by_artist(self, artist_name):
        """Returns all song objects matching the given artist name, or None if not found."""
        pass

    @abstractmethod
    def search_by_streams(self, streams_lower, streams_higher):
        """Return all song objects within range of streams, or None if not found."""
        pass

    @abstractmethod
    def load_data(self, item_information_file):
        """Load item data from a file and populate the item list."""
        pass
    
    @abstractmethod
    def add_item(self, song):
        pass
    
    @abstractmethod
    def edit_item(self, key, song):
        pass

    @abstractmethod
    def delete_item(self, item_id):
        """Delete item from a file"""
        pass

    @abstractmethod
    def _write_back(self, item_information_file):
        """(To be implemented) Write the updated list of items back to the file."""
        pass


    @abstractmethod
    def __str__(self):
        """Return a string representation of all items in the system."""
        pass            