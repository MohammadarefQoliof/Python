import time
message = input("mesajı daxil edin: ")
attempt = int(input("say daxil edin: "))

while attempt > 0:
    print(message)
    attempt = attempt - 1
    time.sleep(0.2)