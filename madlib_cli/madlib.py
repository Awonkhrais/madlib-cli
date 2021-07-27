def print_mes():
    print ("""Welcome to my game you will have much fun.You will be provided with a series of prompts to enter a word that satisfies the requested word type
    
            """)


def read_template(file_path):
    try:
        with open(file_path) as file:
            content=file.read()
    except FileNotFoundError :
        # raise FileNotFoundError('The path file not correct')
        return 'The path file not correct'
    return content.strip()


import re
# import regex

def parse_template(template_string):
    text = tuple(re.findall('{(.*?)}',template_string)) 
    # use tuble to convert [] to ()
    new_text = re.sub('{.*?}','{}',template_string)

    # print(text)
    # print(new_text)

    return new_text,text

def user_input(words):
    responses=[]

    for i in words:
        responses.append(input(f'insert a {i}:'))
    # print(responses)
    return(responses)



def merge(new_text,input_words):
    
    # Merging process : Replace the { } with the user input

    merged_text = new_text.format(*input_words)
    print (merged_text)
    return (merged_text)

def madlib_game():
    print_mes()
    read=read_template('assets/test.txt')
    parse_template(read)
    new_text,text=parse_template(read)
    input_words=user_input(text)
    merge(new_text,input_words)

if __name__ == "__main__":
    # print(__name__)
    madlib_game()