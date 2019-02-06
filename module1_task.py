# task 1 
f = open('running-config','rt')
fin = file.read()
interface_list = list()
last_list = list()

 def list_ifname_ip():
  global vlancheck
   for value in f:
     if 'interface'in value:
       value = value.split()
       interface = list.append(value[1])
     if 'nameif'in value:
       value = value.split()
       if "no"in value[0]:
       interface_list.append("null")
     else:
       interface_list.append(value[1])
       last_list.append(interface_list)
     return final_list
#task 2
with open('running-config')as f:
 secondtext = f.read().replace('192','10')
 secondtext = f.read().replace('172','10')
with open('running-config')as f:
f.write(secondtext)


#task 3
with open('running-config')as in f:
 a = f.read()
 b = a.split("!")
print(b) 
 

def list_ifname_ip(nameif,Ipaddress,NetMask):
