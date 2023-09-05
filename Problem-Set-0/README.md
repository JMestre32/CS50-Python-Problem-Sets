# Problem Set 0

<h2> Indoor.py </h2>
WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.


Example Input/Output:

Input: HELLO, WORLD
Output: hello, world

Input: THIS IS CS50
Output: this is cs50


<h2> Playback.py </h2>
Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

Example Input/Output: 

Input: Hi, I am Berry
Output: Hi,...I...am...Berry

<h2> Making Faces </h2>
Before there were emoji, there were emoticons, whereby text like :&#41; was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :&#x207D; converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

Example Input/Output:

Input: Hello! :&#41;
Output: Hello! 🙂

Input: Goodbye...:&#x207D;
Output: Goodbye...🙁