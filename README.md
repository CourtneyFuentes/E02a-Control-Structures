
# E02a-Control-Structures

This is my second assignment for my C220 class, it is helping me realize what problems to look out for when I'm coding in the future and giving me some good tips, as well as getting me more comfortable with the program. The game is a guessing game where you guess what the computer's favorite color is. Each file has a different response and gets slightly more advanced. In main10.py, for example, the game will either respond with "Sorry, try again" or "Correct!" It will tell you how many guesses it took for you to get the correct answer and see if you wish to play again. 

- Open main01.py. Before running it, what do you expect this program to do? I expect it to greet me and ask what I believe it's favorite color is.
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened. It just replied with the file name.
  - What do you think the program did with what you typed in answer to the question? It looked like it did nothing.
- Open main02.py. Before running it, describe how this is different than main01.py. This file has print(color) as the next line
  - What do you think the color = input() will do? I believe it will repeat my response to me.
  - Run the program in the terminal and answer the question. Did the program do what you expected? Yes.
- Open main03.py. Before running it, describe how this is different than main02.py. This one tells me if I guessed correctly (Red) and if not to try again.
  - What is happening on lines 9–12? It will tell me if I guessed correctly with Red and if not it tells me to try again.
  - Why are lines 10 and 12 indented? They are what to respond if lines 9 or 11 are what the player responded with.
  - Run the program and answer the question. What happens if you don’t capitalize Red? It counts it as incorrect and asks the player to try again.
  - What does this tell you about "color"? it only knows color by what the creater input it as, it's just a string of letters to the program.
- Open main04.py. Before running it, describe how this is different than main03.py. It will count red or Red as correct this time.
  - What problem is this trying to solve? It won't say incorrect just because the first letter is lower cased.
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)? It counts it as incorrect and asks you to try again.
- Open main05.py. What do you expect line 9 to do? If red is written in with capitals or lower cased letters it will still count as correct.
  - What problem is it trying to solve? It won't count red as wrong just because of a capital or lower cased letter.
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)? It counts it as incorrect and asks the player to try again.
 - Open main06.py. How is line 9 different than in main05.py? it adds .strip() after what is already there in main05.py
   - What would you guess .strip() is doing? Disregards any spaces before or after the response
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic? Not that I'm aware. perhaps the user will use a different name, like maroon, instead of just saying red. 
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py? If i guess pink it will tell me that I'm close instead of just asking me to try again.
   - What is happening on line 12? If I guess pink it will tell me that I am close.
   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9? After saying to try again it loops around again and asks the question "What is my favorite color?" again, giving the player another chance to answer.
   - Why are lines 10–17 indented? It tells the program where to loop back to.
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)? It doesn't say correct after guessing correctly, it just ends. If I guess pink it says "Close!" on repeat and doesn't let me guess again. If I guess another color it says "Sorry, try again." on repeat and doesn't let me type another response.
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
 - Open main09.py. What is happening on line 13? It counts how many times the player guessed an answer.
   - What is the purpose of “count”? It counts how many times the player guessed an answer before getting the correct one.
   - What is happening on line 22? There isn't a line 22 but line 21 tells the player the amount of guesses it took them to get the correct answer.
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]). Done
 - *Extra credit:* open main11.py. What is happening on lines 6-11? The program picks a color from the list that is not the same as the last color.
  

 

