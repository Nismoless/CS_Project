class Song:
    def __init__(self, track_name="", artist_name=[], artist_count=0, streams=0, in_apple_charts=0, bpm=0, release_year=0, release_month=0, in_spotify_chart=0, song_id=0):
        self._track_name = track_name
        self._artist_name = artist_name
        self._artist_count = artist_count
        self._streams = streams
        self._in_apple_charts = in_apple_charts
        self._bpm = bpm
        self._release_year = release_year
        self._release_month = release_month
        self._in_spotify_chart = in_spotify_chart
        self._song_id = song_id

    @property # track_name getter/setter - Rob Eusanio
    def track_name(self):
        return self._track_name
    
    @track_name.setter
    def track_name(self, track_name):
        if track_name:
            self._track_name = track_name
        else:
            raise ValueError("Track name cannot be empty.")
    
    @property # artist_name getter/setter - Rob Eusanio
    def artist_name(self):
        return self._artist_name
    
    @artist_name.setter
    def artist_name(self, artist_name):
        if artist_name:
            self._artist_name = artist_name
        else:
            raise ValueError("Artist(s) name cannot be empty.")
        
    @property # track_name getter/setter - Rob Eusanio
    def artist_count(self):
        return self._artist_count
    
    @artist_count.setter
    def artist_count(self, artist_count):
        if artist_count > 0:
            self._artist_count = artist_count
        else:
            raise ValueError("Artist count must be greater than 0.")
        
    @property # release_year getter/setter - Jonathan Cervantes
    def release_year(self):#returns the value of the attribute in _release_year
        return self._release_year

    @release_year.setter
    def release_year(self, release_year):
        if release_year > 0:#sets a new value if the value is greater than 0
            self._release_year = release_year
        else:
            raise ValueError("Song Release Year must be greater than 0.")
    
    @property # release_month getter/setter - Jonathan Cervantes
    def release_month(self):#returns the value of the attribute in _release_month
        return self._release_month

    @release_month.setter
    def release_month(self, release_month):
        if release_month > 0 and release_month < 13:#sets a new value if the value is greater than 0 but less than 13
            self._release_month = release_month
        else:
            raise ValueError("Song Release Month must be greater than 0 and less than 12.")#if the input value isn't greater than 0 and less than 12 an error occurs

    @property # in_spotify_chart getter/setter - Jonathan Cervantes
    def in_spotify_chart(self):#returns the value of the attribute in in_spotify_chart
        return self._in_spotify_chart
    
    @in_spotify_chart.setter
    def in_spotify_chart(self, in_spotify_chart):
        if in_spotify_chart >= 0:#sets a new value if the value is greater than 0
            self._in_spotify_chart = in_spotify_chart
        else:
            raise ValueError("Chart Placement for song must be greater than 0.")#raises an error if the input value isn't greater than 0
        
    # Streams getter/setter: Fabian Villasenor
    @property
    def streams(self):
        return self._streams
    
    @streams.setter
    def streams(self, streams):
        if streams > 0:
            self._streams = streams
        else:
            raise ValueError("Streams must be a number.")
        
    @property # Apple charts getter/setter - Fabian Villasenor
    def in_apple_charts(self):
        return self._in_apple_charts
    
    @in_apple_charts.setter
    def in_apple_charts(self, in_apple_charts):
        if in_apple_charts >= 0:
            self._in_apple_charts = in_apple_charts
        
    @property #bpm getter/setter - Fabian Villasenor
    def bpm(self):
        return self._bpm
    
    @bpm.setter
    def bpm(self, bpm):
        if bpm > 0:
            self._bpm = bpm
        else: 
            bpm = None # BPM is set to None, but we may want to handle it differently
                       # TODO: Do we want unfilled columns to be set to null?
    
    @property #song_id getter/setter - Jonathan Cervantes
    def song_id(self):#returns the value of the attribute in song_id
        return self._song_id
    
    @song_id.setter
    def song_id(self, song_id):
        if song_id > 0:#sets a new value if the value is greater than 0
            self._song_id = song_id
        else:
            raise ValueError("Song ID must be greater than 0.")#raises an error if the input value isn't greater than 0

    # Define __str__ to give a readable representation of the object
    def __str__(self):
        """String representation of the Song object."""
        return f"\nTrack Name: {self._track_name}, \nArtist(s) Name: {self._artist_name}, \nArtist Count: {self._artist_count}, \nArtist streams: {self._streams}, \nIn Apple Charts: {self._in_apple_charts}, \nBPM: {self._bpm}, \nRelease Year: {self._release_year}, \nRelease Month: {self._release_month}, \nSpotify Chart Placement: {self._in_spotify_chart}, \nSong ID: {self._song_id}"