import time

# we want to find the computers epoch time
# this can be thoght of as the number of seconds since January 1, 1970, or when the computer thinks time began
# this is useful for measuring time intervals and for debugging
# we can use the time module to find the epoch time
# the time module is part of the Python Standard Library


print(time.ctime(0)) # the ctime method converts the epoch time to a human readable format
print(time.time()) # the time method returns the current epoch time in seconds

#retrieve the current time
print(time.ctime(time.time()))

# using the local time method to get the current time
local_time = time.localtime(time.time())
#print(local_time) # this will return a time.struct_time object 

thai_time = time.strftime("%B %d %Y %H:%M:%S", local_time) # the strftime method converts the time.struct_time object to a string
print(f"The time here is {thai_time}")


# using string formatting to display the current time
time_string = "20 April 2022 12:30:00"
time_object = time.strptime(time_string, "%d %B %Y %H:%M:%S") # the strptime method converts a string to a time.struct_time object
print(time_object)

time.asctime(time_object) # this function accepts an object or a tuple and returns a human readable time string
time_tuple = (2022, 4, 20, 12, 30, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

# using mktime to convert a time.struct_time object to epoch time
epoch_time = time.mktime(time_object)
print(epoch_time)

# using gmc to get the current time in UTC
utc_time = time.gmtime()
print(utc_time) # this will return a time objectt that is related to the UTC timezone and is not affected by daylight savings time
# convert the UTC object into human readable format
utc_string = time.asctime(utc_time)
print(utc_string)
