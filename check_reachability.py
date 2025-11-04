#Check if a website is reachable (socket ping)

#Concept: try/except + sockets

#Interview ask: Write a small Python script to check if a website’s port 80 is reachable.



import socket
try:
    socket.create_connection(("example.com", 80), 1)
    print("Reachable")
except:
    print("Not reachable")
