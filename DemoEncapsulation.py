
class FitnessTracker:
    user=[]
    __steps__=0
    def add_steps(self,n):
        self.__steps__+=n
        return self.__steps__
    def get_steps(self):
        return
    def reset_steps(self):
        self.__steps__=0
        return self.__steps__