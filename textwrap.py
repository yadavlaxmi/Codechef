# function in text wrap
def wrap(string, max_width):
        for i in range(0,len(string)+1,max_width):
            result = string[i:i+max_width]
            if len(result) == max_width:
                print(result)
            else:
                return("length is short")
string = input()
max_width=int(input())
print(wrap(string, max_width))



# without text wrap
string=input()
max_width=2
i=0
while i<len(string):
    result = string[i:i+max_width]
    i=i+1
    print(result)
