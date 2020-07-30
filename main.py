# ====================================================================
# OPTIONS
# ====================================================================
seconds_for_each_word = 5
bonus_for_each_char = 0.1
bonus_for_backspace = False
word_min_length = 2

ignored_characters = [39, 45]

dict_file = "en_dict.txt"
output_file = "last game results.txt"

# ====================================================================
# IMPORTS
# ====================================================================
import os, sys, time, msvcrt 

# ====================================================================
# GLOBALS
# ====================================================================
dict_words = frozenset([line.rstrip('\n') for line in open(dict_file)])
used_words = []

# ====================================================================
# FUNCTIONS
# ====================================================================
def fixString(string):
    string = string.lower()
    for c in ignored_characters:
        string = string.replace(chr(c), "")
    return string

def checkString(string):
    if len(string) < word_min_length:
        return "'" + string + "' is less than the minimum length ("+str(word_min_length)+")."
    if string not in dict_words:
        return "'" + string + "' is not in the dictionary."
    return ""

def readInput(caption, timeout, keypress_bonus):
    os.system('clear||cls')
    sys.stdout.write("\nTime: " + "%.16f"%timeout + "\n" + caption)
    sys.stdout.flush()
    start_time = time.time()
    string = ""
    err = ""
    while True:        
        if msvcrt.kbhit():
            # Get input data
            byte_arr = msvcrt.getche()
            char = ord(byte_arr)
           
            # Act accordinly
            if char == 13: # enter_key
                out = fixString(string)
                current_err = checkString(out)
                if current_err:
                    err = current_err
                else:
                    if out in used_words:
                        return '-2'+out
                    return out
            elif char == 8: # backspace
                string = string[:-1]
                if bonus_for_backspace:
                    timeout += keypress_bonus
            elif (char >= 97 and char <= 122) or (char >= 65 and char <= 90) or char in ignored_characters:   
                string += "".join(map(chr,byte_arr))
                timeout += keypress_bonus

            # Print new string
            os.system('clear||cls')
            sys.stdout.write(err + "\nTime: " + "%.16f"%(timeout-(time.time()-start_time))+ "\n" + caption + string)
            sys.stdout.flush()
            
        if (time.time() - start_time) > timeout: # Return nothing for unfinished string
            return '-1'+string

# ====================================================================
# MAIN
# ====================================================================
def main():
    # Quiz loop
    ans = ""
    while True:
        ans = readInput('Word: ', seconds_for_each_word, bonus_for_each_char)
        if ans.startswith("-"): break
        used_words.append(ans)

    # Result
    os.system('clear||cls')
    result_string = "Game over.\nScore: " + str(len(used_words)) + "."
    if ans[1] == "1":
        err = checkString(ans[2:])
        x = ""
        if ans[2:] and err:
            x = " Note: " + err
        result_string += ("\nYou ran out of time." + x)
    elif ans[1] == "2":
        result_string += ("\nYou have already used the word '" + ans[2:] + "'.")
    print(result_string)

    # Write reult to file
    if output_file:
        with open(output_file, 'w') as f:
            f.write(result_string+"\n\n")
            for word in used_words:
                f.write(word + "\n")
            if ans[2:]:
                f.write("> '" + ans[2:] + "'")

if __name__ == "__main__":
    # Printing the error like this allows it to show without the cmd closing
    try:
        main()
    except Exception as e:
        print("ERROR:\n", e)

    input("\nProgram complete. Press enter twice to close.")
    input("One more time.")
    
