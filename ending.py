

#-------------ASCII ART AND ENDING SCREEN-------------------


import os
ascii = """ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█       █      █  █▄█  █       █  █       █  █ █  █       █   ▄  █  
█   ▄▄▄▄█  ▄   █       █    ▄▄▄█  █   ▄   █  █▄█  █    ▄▄▄█  █ █ █  
█  █  ▄▄█ █▄█  █       █   █▄▄▄   █  █ █  █       █   █▄▄▄█   █▄▄█▄ 
█  █ █  █      █       █    ▄▄▄█  █  █▄█  █       █    ▄▄▄█    ▄▄  █
█  █▄▄█ █  ▄   █ ██▄██ █   █▄▄▄   █       ██     ██   █▄▄▄█   █  █ █
█▄▄▄▄▄▄▄█▄█ █▄▄█▄█   █▄█▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█
"""

def ending(Score:int):
    
    return f"Final score: {Score}"
    
def art():
    os.system('cls')
    print(ascii)
    


    