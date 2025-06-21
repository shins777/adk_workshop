
import time
def count_up_to(max_number):
    number = 0
    while number < max_number:
        # Returns a number and suspends function execution, then resumes execution when processing is complete and returns.
        yield number  
        print("After yield in count_up_to:", number)
        number += 1

for num in count_up_to(5):
    print(num)  # print 0, 1, 2, 3, 4 
    time.sleep(1)  # wait 1 second
    print("Yielded in loop:", num)  # Yielded: 0, Yielded: 1, ... 