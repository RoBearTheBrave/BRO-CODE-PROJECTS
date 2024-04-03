import time


# my_time = int(input("Enter the time in seconds: "))
# print("-------begin countdown-------")

# for counter in range(0, my_time):#count down low to high
#     print(counter)
#     time.sleep(1)
# print("Time's up!")


# my_time = int(input("Enter the time in seconds: "))
# print("-------begin countdown-------")

# for counter in range(my_time, 0, -1):#count down high to low
#     print(counter)
#     time.sleep(1)
# print("Time's up!")


#create a clock timer
my_time = int(input("Enter the time in seconds: "))

for counter in range(my_time, 0, -1):#count down high to low
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)
print("Time's up!")