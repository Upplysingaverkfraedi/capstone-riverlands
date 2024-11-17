class LengdKeppna:
    def __init__(self, year, show, songs, entertainment, voting, first_song, last_song, first_vote, last_vote):
        self.__year = year
        self.__show = show
        self.__songs = songs
        self.__entertainment = entertainment
        self.__voting = voting
        self.__first_song = first_song
        self.__last_song = last_song
        self.__first_vote = first_vote
        self.__last_vote = last_vote

    def get_year(self):
        return self.__year
    
    def get_show(self):
        return self.__show
    
    def get_songs(self):
        return self.__songs
    
    def get_entertainment(self):
        return self.__entertainment
    
    def get_voting(self):
        return self.__voting
    
    def get_first_song(self):
        return self.__first_song

    def get_last_song(self):
        return self.__last_song
    
    def get_first_vote(self):
        return self.__first_vote
    
    def get_last_vote(self):
        return self.__last_vote