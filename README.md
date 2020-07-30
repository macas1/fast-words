# About
* A game where you type words quickly and cannot repeat words 
* A good mental exercise and harder than you may think

# Settings (Contained in main.py)
| Setting  | Description | Default |
| ------------- | ------------- | ------------- |
| seconds_for_each_word | How many seconds are given at the start of each word | 5 |
| bonus_for_each_char | Seconds added to your time for each character typed. This removes the disadvantage of typing longer words | 0.1 |
| bonus_for_backspace | This should be False as this mechanic is abusable for infinite time | False |
| word_min_length | Words with fewer letters than this will bot be accepted | 2 |
| ignored_characters | Character that the input will completely ignore | [39, 45] |
| dict_file | The path to the list of words to be used as correct | "en_dict.txt" |
| output_file | The path to the file where the results of the previous game will be stored to analysis. I always found this information quite interesting. Set to None or "" if you do not want to create an output file for each game. | "last game results.txt" |
