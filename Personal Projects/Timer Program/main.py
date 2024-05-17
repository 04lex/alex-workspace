import time

timer = int(input("Enter the time in seconds: "))

# reversed(range(0, timer)) or reverse timer with 0 and increment backwards
for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")