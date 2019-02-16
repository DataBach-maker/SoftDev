import socket
import pickle
import datetime


#BUFF=1024
port = 9999
BUFF = 1024
host = 'localhost'

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#open a connection to a certain port
s.connect((host, port))

def socket_sent_message(s, message):
	print message
	message = message+'\r\n'
	s.send(message)
	return

def socket_receive_massage(s):
	message = s.recv(BUFF)
	print message.rstrip('\r\n')
	return message


socket_receive_massage(s)

socket_sent_message(s, 'horbaje')

socket_receive_massage(s)

socket_sent_message(s, '41e944df4349ac0c8f222842a3489c1a')

socket_receive_massage(s)

min=0
max=10000

while (1):
    
	num=(min+max)/2
	socket_sent_message(s, str(num))
	message=(socket_receive_massage(s)).split()
    
	if (message[0]=='nope.'):
		if (message[3]=='bigger'):
			min=num
		elif (message[3]=='smaller'):
			max=num
	else:
		break


krikel_krackel = socket_receive_massage(s)

d={"3233323":0,"1221115":1,"5215117":2,"5215125":3,"1227111":4,"7115125":5,"5216225":6,"7211111":7,"5225225":8,"5226125":9}
splited = krikel_krackel.split('\n')[:-3]
indices = [(0,8),(15,23),(25,39)]

result = []
number = []
snd = []
your_bloody_number = []

for line in splited:
    r= [line[sp:e+1] for sp,e in indices]
    result.append(r)

def list_per_number(result, item_n):  
    number = [item[item_n] for item in result]
    return number

def char_count(number):   
    shape = []
    for i in number:
        shape.extend(str(i.count('#')))                                           
    return shape

def join_me(shape_count,joiner):
    snd = joiner.join(shape_count)
    return snd

def getter(snd):
    your_bloody_number = d.get(snd[0:7])
    return your_bloody_number

number_1 = list_per_number(result, 0)
number_2 = list_per_number(result, 1)
number_3 = list_per_number(result, 2)
#print number_1, number_2, number_3

shape_count_number_1 = char_count(number_1)
shape_count_number_2 = char_count(number_2)
shape_count_number_3 = char_count(number_3)
#print shape_count_number_1, shape_count_number_2, shape_count_number_3

snd_1 = join_me(shape_count_number_1, "")
snd_2 = join_me(shape_count_number_2, "")
snd_3 = join_me(shape_count_number_3, "")        
#print snd_1, snd_2, snd_3

one = getter(snd_1)
two = getter(snd_2)
three = getter(snd_3)

it_was_this = (one*100)+(two*10)+three
socket_sent_message(s, str(it_was_this))
socket_receive_massage(s)

pickeled_version_input = socket_receive_massage(s)

pickled=''

for l in pickeled_version_input.splitlines(True)[1:-2]:
	pickled += l

date_obj = pickle.loads(pickled)
         
socket_sent_message(s, str(date_obj.microsecond))
socket_receive_massage(s) 
            
when_list = socket_receive_massage(s)           
splited = when_list.split()
shorted = splited[5:8]
she = join_me(shorted, " ")   

dtdate = datetime.datetime.strptime(she[:-1], "%d %b %y")     
            
now = datetime.datetime.now()
delta = now -dtdate

converted_string = str(delta)
select_days = converted_string.split()

socket_sent_message(s, str(select_days[0]))         

secret = socket_receive_massage(s)
print secret.split('\n')[2]

s.close()


