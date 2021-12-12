import re

#Mad Lib: User is asked to provide several different parts of speech and numbers. Their input is used to create a funny message based on their choices!

#User may then save the message to new text file if they choose.

def read_template(path):
  '''
  Opens a filepath and returns its contents as a stripped string

  Input: file path
  Output: string
  '''
  try:
    with open(path) as file:
      contents = file.read()
      return contents.strip()
  except:
    raise FileNotFoundError('\nNo Such File Exists At This Path!')


def parse_template(template):
  '''
  Finds substrings within curly braces from a given string using a regex statement and outputs a list of all strings found.

  Input: string
  Output: list
  '''
  parts = re.findall(r"\{([A-Za-z0-9_\'\- ]+)\}", template)

  for word in parts:
    if word in template:
      template = template.replace(word, '', 1)
  parts = tuple(parts)

  return template, parts


def merge(template, words):
  '''
  Given a list of input strings from the user. Loops through the list, finding the first instance of two curly braces inside of a larger string. Replaces the curly braces with each word from the list. After the loop is finished, returns the new string.

  Input: string, list
  Output: string
  '''
  for word in words:
    template = template.replace(f'{{}}', word, 1)    

  return template


def user_input_func(words):
  '''
  Given a list of strings requesting parts of speech and numbers, asks the user to input a string for each item in the list. User inputs are returned.

  Input: list
  Output: list
  '''
  user_inputs = []

  for word in words:
    user_input = input(f'\nEnter a Unique {word}\n>: ')
    user_input = validate(word, user_input)
    user_inputs.append(user_input)

  user_inputs = tuple(user_inputs)

  return user_inputs


def user_new_input(word):
  '''
  Given a string requesting a part of speech or number, ask the user to input a new string. User input is returned.

  Input: string
  Output: string
  '''
  user_input = input(f'\nEnter a Unique {word}\n>: ')
  user_input = validate(word, user_input)

  return user_input


def validate(word, user_input):
  '''
  Given a string which requests either a Number or anything else, ensures user entered a string when asked for words and a number when asked for numbers. If not, raises a Value Error exception and requests input again.

  Input: string, string
  Output: string
  '''  
  if 'Number' in word:
    try:
      if user_input.isnumeric() == True:
        return user_input
      else:
        raise ValueError('Not a NUMBER!')
        print(f'\nYou Must Enter ONLY a Enter a Unique {word}:\n')
      return user_new_input(word)
    except ValueError as e:
      print(e)
      user_input = input(f'\nYou Must Enter ONLY a Enter a Unique {word}:\n')
      return user_new_input(word, user_input)

  else:       
    try:       
      if user_input.isdigit() == True:
        raise ValueError('\nNot a ENTER ONLY THE REQUESTED INPUT!!')      
      else:
        return user_input
    except ValueError as e:
      print(f'\nENTER ONLY THE REQUESTED INPUT!\n')
      return user_new_input(word)


def wrapper(text):
  '''
  Wraps a given string in a border and spaces. Returns the wrapped string.

  Input: string
  Output: string
  '''
  ret_str = f'\n\n<>============================================================<>\n{text}\n<>============================================================<>\n\n'

  return ret_str


def save_file(template):
  '''
  Given a string: requests whether or not the user would like to create a new file, write the string to the file, then save the file to the local directory. If no, the program exits.

  Input: string
  Output: .txt file
  '''
  user_res = input(f'\nWould you like to save your Mad Lib?\n \nYes or No?\n>: ')
  user_res = user_res.lower()

  if user_res == 'yes' or user_res == 'y':
    filename = input('\nEnter a filename\n>: ')
    try:
      file = open(filename, 'x')
    except:
      print('\nFilename already exists or selected drive is Full!')
      return save_file(template)

    try:
      file.write(template)
      file.close()
      print(f'\n{filename} was saved to local directory! \n\nThanks for Playing! :D')
    except:
      print('File Not Found!')
  elif user_res == 'no' or user_res == 'n':
    print('\n\nThanks for Playing! :D')
    quit()
  else:
    print('\n\nYou MUST respond YES or NO!')
    return save_file(template)


if __name__ == '__main__':
  '''
  Begins Program
  - a,b: the output of parse_template(path) 
    a: a string with a words between curly braces removed
    b: a list of all words that were removed
  - c: the output of user_input_func(b): a list of user responses
  - user_template: the output of merge(a,c): a string of the completed Mad Lib
  - user_template is then printed to the console inside a wrapper and the user is then requested as to whether they would like to save their text to a new file
  '''
  a, b = parse_template(read_template('../assets/dark_and_stormy_night_template.txt'))
  c = user_input_func(b)  
  user_template = merge(a,c)

  print(wrapper(user_template))
  save_file(user_template)
