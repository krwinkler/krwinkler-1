def hawkid():
    return(["Katelyn Winkler", "krwinkler"])
if (not hawkid()[0] or not hawkid()[1]) or (hawkid()[1] == "hawkid"):
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
    print('### Otherwise, the Autograder will assign 0 points.')
    exit(-1)
else:
    info = hawkid()
    print(info[0])
    print(info[1])
#
#
#
#
#
mode=input('Enter mode:')
list = []
list.len()
n = int(input('Enter # of values'))
for i in range(0,n):
	 x = float(input('Enter Values' + str(i)))
	 list.append(x)
print(mode)
print(len)
print(n)
print(list)
if mode == 'min':
    list.sort()
    print(list[0])
if mode == 'max':
    list.sort()
    print(list[-1])
if mode == 'avg':
    def sum_of_list(l):
        total = 0
        for val in l:
            total = total + val
        return total
print(sum_of_list(mylist)/len)


    
