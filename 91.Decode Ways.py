class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def decode(s):
            
            prev_char = ''
            prev_way = 0
#            way = int(len(s)>0)
            if(len(s) > 0):
                way = 1
            else:
                way = 0

            for char in s:
                temp = way
                way = temp*(char!='0') + prev_way*(9<int(prev_char+char)<27)
                prev_way = temp
                prev_char = char
            
            return way
        return decode(s)    
        
            
             
#             ## try 2: time limit exceeded
#             if(len(s)==0):
#                 return 0
#             if(s[0]=='0'):
#                 return 0
#             r1 = 0
#             if(len(s[1:])==0):
#                 r1 = 1
#             else:
#                 r1 = decode(s[1:])
#             r2 = 0
#             if(9<int(s[0:2])<27):
#                 if(len(s[2:])==0):
#                     r2 = 1
#                 else:
#                     r2 = decode(s[2:])      
#             return r1+r2
            
#             ## try 1: time limit exceeded
#             if(len(s)==0):
#                 return 0
#             if(s[0]=='0'):
#                 return 0
#             return decode(s[1:])*(len(s[1:])>0)+1*(len(s[1:])==0) + decode(s[2:]*(len(s[2:])>0))*(9<int(s[0:2])<27)+1*(len(s[2:])==0)*(9<int(s[0:2])<27)
#             return decode(s)
