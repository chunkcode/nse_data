import threading

def printit():
  threading.Timer(1, printit).start()
  print ("Hello, World!")

printit()