def add_two_numbers(num_one, num_two):
    number_to_return = num_one + num_two
    return number_to_return

my_added_numbers = add_two_numbers(1, 1)

print(my_added_numbers) # will print 2


nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Globals to observe name masking (same-name local variables hides the global variable so use different variable names inside the function). Do not rename these.
count = 999
summary = "unset"
result = "unset"

def count_above(nums, limit):
    count = 0
    for num in nums:
        if num > limit:
            count += 1
        else:
            count += 0
    return(count)

counts = count_above(nums, limit)
print(counts)

def text_summarise(s:str):
    assert isinstance(s, str), 'Strings only!'
    dictm = dict({'digits':0, 'letters':0, 'other':0})
    for a in s:
        if a.isdigit() == True:
            dictm['digits'] += 1
        elif a.isalpha() == True:
            dictm['letters'] += 1
        elif a.isdigit() == False and s.isalpha() == False:
            dictm['other'] += 1
    return(dictm)

given_text = text_summarise(text)
print(given_text)

def aggregate(seq, mode, threshold):
    if mode == "sum":
        result = 0
        for n in seq:
            if n >= threshold:
            #import pdb; pdb.set_trace()
                if mode == "sum":
                    if n >= 0:
                        result += n 
    elif mode == "count":
        result = 0
        for n in seq:
            if n >= threshold:
                if mode == "count":
                    if n <= 0:
                        continue
                    elif n > 0:
                        if mode == "count":
                            result += 1 
    elif mode == "max":
        result = None
        for n in seq:
            if n >= threshold:
            #import pdb; pdb.set_trace()
                if mode == "max":
                    if n <= 0:
                        continue
                    elif n > 0:
                        if result is None or result < n:
                            result = n
                        else:
                            continue
    return(result)

sum1 = aggregate(nums, "sum", limit)
print(sum1)

count1 = aggregate(nums, "count", limit)
print(count1)

max1 = aggregate(nums, "max", limit)
print(max1)


