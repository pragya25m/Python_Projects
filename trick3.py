import os
for i in range(1,255):
    ip="192.168.1."+str(i)
    print("Pinging ",ip,".....")
    os.system("ping "+ip)
print("Finished Pinging, THANK YOU!!")