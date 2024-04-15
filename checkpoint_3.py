#Exercise 1:
string = "Hello, this is a string!"
integer = 100
myList = ["the first item", 123, 'Amrad', "any"]
boolean = True #it can be False also

#Exercise 2:
first_three_letters = string[0:3]
print(first_three_letters)

#Exercise 3:
print(myList[0])

#Exercise 4: 
add_ten_to_integer = integer + 10
print(add_ten_to_integer)

#Exercise 5:
element = myList[-1]
last_element = myList.index(element)
print(last_element)

#Exercise 6:
names = 'harry,alex,susie,jared,gail,conner'
convert_to_list = names.split(',')
print(convert_to_list)

#Exercise 7:
word = string.split()
first_word = word[0].upper()
print(first_word)
new_string = first_word, word[1:]
print(new_string)


#Exercise 8:
sentence = "my number:"
print(f"hi, this {sentence} {integer}")

#Exercise 9:
print('Hello World!')

#------------------------

cadena = ['Hola', 'Buenos días', 'buenas noches']
cadena.pop(0)
cadena.insert(0,'Adios')
print(cadena)
