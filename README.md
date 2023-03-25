# ChatGPT on Graphics

### Name0: Rafayet Hossain
### Name1: Olivia Zheng
### Name2: Josiah Moltz 

---

## Background
Your goal is to get ChatGPT to create a program that meets all the requirements of our graphics engine up to the latest assignment. This includes:
* Drawing lines
* Drawing circles, and Bezier and Hermite curves.
* Maintining an edge list of points.
* Being able to perform & potentially combine transformations, rotations and dilations.
* Being able to save and display the images.
* Being able to correctly read in files using the graphics scripting language we've developed.

Some Notes:
* Please stick to C, Python or Java as the language of choice.
* Don't let ChatGPT use an existing graphics engine, it's got to work as hard as you have!
* If the program has multiple files, feel free to get ChatGPT to create a makefile for you.
* If you get it to create a useable grpahics engine, see if it can generate an image that shows off its capabilities.



## Task 0: Setup
Only one member of your group needs to have an account to use ChatGPT, if someone has one already, go ahead and use that. If not, pick one person to sign up, the simplest method to sign up would be to authenticate with google and use your stuy.edu email address. Authentication will require recieving a text message, so pick someone that has easy access to their phone.

You can find ChatGPT here: <https://chat.openai.com/chat>

## Task 1: The First Program
### Your Prompt
Provide below the first description you gave ChatGPT:

"Make a graphics engine in Python that can draw lines and create a .ppm file with the lines."

### The Code
Crate a folder in this repository called __0-program__ containing all the relevant code initially created by ChatGPT.

### Your Analysis
Answer the Following Questions after seeing the initial program.

#### Question 0
Overall, how well did ChatGPT do?

YOUR ANSWER HERE

#### Question 1
What did ChatGPT get right?

YOUR ANSWER HERE

#### Question 2
What did ChatGPT get wrong?

YOUR ANSWER HERE

#### Question 3:
How much of the code generated by ChatGPT do you understand?

YOUR ANSWER HERE

#### Question 4:
How does ChatGPT's approach differe from yours?

YOUR ANSWER HERE


## Task 2: Refinement
if possible, run the code made by ChatGPT. Based on your answers the questions above, and your observations about how the program runs, ask ChatGPT to improve the code. ChatGPT will generally understand that you are asking to make changes to your inital prompt, so you don't need to restate the enire problem, instead, ask for specific changes or improvements.

Provide each prompt you gave ChatGPT bellow. Give each prompt a header like this :`#### Prompt X` where X is a counter starting at 1.

Prompt 1: Rewrite the code to store an edge matrix of points
Prompt 2: Add a function to draw a circle in the image.
Prompt 3: Create an example code for the above code
Prompt 4: The draw_circle() function causes an IndexError: bytearray index out of range, can you fix it?
Prompt 5: How can i fix the "bytes" object has no attribute "format" error?
Prompt 6: (Given full traceback message for bytearray out of range since it still couldn't fix it)

## Task 3: The Final Program
Include the final program created by ChatGPT in this repository in a folder called __1-program__.



