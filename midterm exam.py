#question 1

a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2
print(a)  #9


#question 2
print(2+3*6/2) #11


#question 3
import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)   #abcabcabc

#question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

numbers = [
"6593036601359343374664733439531066303956",
"7489617719749244646336564429479177169847",
"5485839837501070045005400701057389385845",
"8025833559061079503003059701609553385208"]

for num in numbers:
    if palindrome(num):
        print(f'{num} is a palindrome')
    else:
        print(f'{num} not a palindrome')

#7489617719749244646336564429479177169847 not a palindrome

#question 5


import requests
text = ["unban, i unlovean to uncoodean"]
unique_words = {}
punctuation = ", . ' ? - = ()"

for line in text:
    for p in punctuation:
        line = line.replace(p, " ")
    words = line.split()
    for word in words:
        word = word.lower()
        unique_words[word] = unique_words.get(word, 0) + 1

matching_words = [word for word in unique_words if word.startswith("un") and word.endswith("an")]

print("Matching words:", matching_words)

#result
#Matching words: ['unban', 'unlovean', 'uncoodean']


#question 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)
    else:
        random_numbers[i] = "XX"

    print(random_numbers)


#question 8
import validators
def is_valid_link(url):
    return validators.url(url)
links = [
    "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwj97rnji9CLAxVwTKQEHbR7PTIQPAgI:" "A", "google.com:" "B"
]
for url in links:
    if is_valid_link(url):
        print(f'is a valid: {url}')
    else:
        print(f'is not valid: {url}')

#is a valid: https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwj97rnji9CLAxVwTKQEHbR7PTIQPAgI:A
#is not valid: google.com:B


#question 9

def is_a_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_since_birthday(birthday):
    day, month, birth_year = map(int, birthday.split('-'))
    current_year = 2025
    total_days = 0

    for year in range(birth_year + 1, current_year):
        total_days += 366
        if def is_a_leap_year(year):(year) else 365

    return total_days

print(calculate_day_since_bday(bday))
