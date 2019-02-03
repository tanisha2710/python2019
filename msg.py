import socket,thread
def send():
	rec_ip="192.168.10.105"
	rec_port=6500   
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	while  True:
		data=raw_input("type your message :  ")
         
		s.sendto(data,(rec_ip,rec_port))
		
def recv():
	rec_ip="192.168.10.235"
	rec_port=6500 
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((rec_ip,rec_port))            # proving  a way to connect 

	while  3  >  2	 :
		rec_data=s.recvfrom(100) 
		print   "data rec from  client :   ",rec_data[0]
thread.start_new_thread(send,())
thread.start_new_thread(recv,())
while True:
	pass

