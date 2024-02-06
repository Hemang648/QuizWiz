import requests as rp
import html
import random as rd
from category import categories_list
from ending import *

#----------------------------------------------------------GETTING QUESIONS------------------------------------------

def ques (amt, category, level) -> list:
    
    """
    Retrieve a list of questions from an API based on the specified parameters.

    Args:
        amt (int): The number of questions to retrieve.
        category (int): The category ID for the questions.
        level (str): The difficulty level for the questions.

    Returns:
        list: A list of questions retrieved from the API.
    """
    
    url = f"https://opentdb.com/api.php?amount={amt}&difficulty={level}&category={category}"
    res = rp.get(url)
    res_json = res.json()
    return  res_json["results"]


#--------------------------------------------------SHUFFLING OPTIONS-----------------------------------------

def shuffle_choice (choice) -> list:
    
    """
    Args:
        choice (list): List of choices for a question.

    Returns:
        list: Shuffled list of choices.
    """
    rd.shuffle(choice)
    return choice

#-----------------------------------------------SHOWING OPTIONS ON SCREEN---------------------------------------

def print_choice(choice) -> None:
    
    """
    Args:
        choice (list): List of choices for a question.
    
    """
    for choice_index, choice in enumerate(choice):
        print(f"{choice_index+1}. {html.unescape(choice)}")


#-------------------------------------------------GETTING USER INPUT----------------------------------------------
def get_input() -> int:
    
    """
    Returns:
        int: Index of the user's chosen answer.
    
    """
    while True:
        try:
            user_choice = int(input("Enter your chosen answer index: "))
            if user_choice in range(1,5):
                return user_choice-1
            else:
                print("Invalid Input!!. Please enter between range given options")
        except ValueError:
            print("WRONG LITERAL, BRUHH??? what are you doing")
         
            
#----------------------------------------------------------PLAYING-----------------------------------------------

def play_game(amt: int, category: int, dificulty:str)->None:
    
    """
    Args:
        amt (int): The number of questions to play.
        category (int): The category ID for the questions.
        difficulty (str): The difficulty level for the questions.
    
    """
    global point 
    ques101 = ques(amt, category,dificulty) 
    for question in ques101:
        ques_text = html.unescape(question['question'])
        print(ques_text)
        
        choice = question['incorrect_answers']
        choice.extend([question['correct_answer']])
        
        shuffled_options = shuffle_choice(choice)                                       
        print_choice(shuffled_options)
        
        get_input_index = get_input()
        get_choice_text = shuffled_options[get_input_index]
        
        correct_text = html.unescape(question['correct_answer'])
        
        if get_choice_text == correct_text:
            print(f"Nice, Your answer {correct_text}\n")
            point +=1     
        else:
            print(f"Wrong, Correct is {correct_text}\n")    



#------------------------------------MAIN CALL------------------------------------- 

if __name__ == "__main__":
    
    global rounds 
    global point 
    point = 0
    rounds = 1 
    Game_data = []    
    while True:
        print("******************************************* Welcome to the quiz game ***************************************\n")
        
        try:
            number_of_ques= int(input("Number of questions you want: "))
            
            if number_of_ques<=0:
                print("Number of questions should be positive integer")
                print("RESTART!!\n")
                continue
            
            diffi = input("Enter the difficulty level [Hard/Medium/Easy]: ").lower()
            
            if diffi == 'hard' or diffi == 'easy' or diffi == 'medium': 
                available_categories = categories_list()                                               # CATEGORIES LIST FUNCTION
                cate = int(input("Enter the ID of the your preffered category: ") )
            
            else:
                print("Error! Enter a valid difficulty level!!\n")
                continue    
        
            if cate >=9 and cate <=32:
                play_game(amt=number_of_ques, category=cate, dificulty=diffi)
            else:
                print("Error! Please select from the given IDs") 
                print("RESTART!!\n")
                continue   
        except ValueError:
            print("Error! Please enter a valid ID.")
            print("RESTART!!\n")
            continue
            
                    
        sets = input("Do you want to start again [Y/N]: ").lower()
        
#------------------------------GAME ROUND DATA ACCUMULATION AND PRINTINT THEM -------------------------        
        
        if sets=='y' and Game_data != None:
            data = f"Played in {diffi} mode, Round-{rounds}: {ending(point)}/{number_of_ques}"
            Game_data.append(data) 
            rounds +=1
           
            
        else:
            data = f"Played in {diffi} mode, Round-{rounds}: {ending(point)}/{number_of_ques}"
            Game_data.append(data) 
            
            break
 
 #------------------------------------------ASCII art will be printed---------------------------------------       
    art()                                                                               
    print("Scores for each game round: \n")
    for i in (Game_data):
        print(i)        
                                                                                               
    
                  
                  
                  
