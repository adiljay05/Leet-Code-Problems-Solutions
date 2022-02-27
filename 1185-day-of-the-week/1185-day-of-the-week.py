class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:  
        x = datetime.datetime(year, month, day)
        dic = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
        return dic[x.weekday()]