'''Madlibs is a game of concatenation. It's about how to put strings together... So, here's my version of it...'''

#way's of doing it... P.S. --> I'm going for the 3rd one as it's much cleaner syntax
#print('abracad' + 'abra')
#print('abracad {}'.format('abra'))
#print(f'abracad{'abra'}')
name = input('Your Name: ')
age = input('Your Age: ')
country = input('Your Country: ')
number = input('Your Number: ')
email = input('Your Email Address: ')

madlib = f"Hi, my name is {name}. I\'m {age} years old. I live in {country}. You can contact me on {number} or {email}. That\'s it for this project. Have a good day!"

print(madlib)