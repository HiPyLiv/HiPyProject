import multiprocessing as mp
import time

def sender(connection):
    connection.send("A string object")
    connection.send("Another string")
    print(connection.recv())
    print("Sent a string")
    connection.close()

def receiver(connection):
    print("Received:", connection.recv(), connection.recv())
    connection.close()

if __name__ == '__main__':
    endA, endB = mp.Pipe()
    Alice = mp.Process(target=sender, args=(endA,))
    Bob = mp.Process(target=receiver, args=(endB,)) 
    Alice.start()
    Bob.start()


