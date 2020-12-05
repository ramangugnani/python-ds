# https://leetcode.com/problems/meeting-rooms/

'''
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),
determine if a person could attend all meetings.
'''

# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


class Solution(object):
    def canAttendMeetings(self, intervals):
        new_list = list()
        for interval in intervals:
            new_list.append([interval.start,1])
            new_list.append([interval.end, -1])

        print(new_list)
        new_list.sort()
        print(new_list)

        meeting_start = False
        for interval in new_list:
            if interval[1] == 1 and meeting_start == False:
                meeting_start = True
            elif interval[1] == -1 and meeting_start == True:
                meeting_start = False
            else:
                return False

        return True


my_list = list()
my_list.append(Interval(0,20))
my_list.append(Interval(5,10))
my_list.append(Interval(15,20))
sol = Solution()
print(sol.canAttendMeetings(my_list))