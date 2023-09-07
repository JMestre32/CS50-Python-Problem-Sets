# Problem Set 2 

<h3> camelCase </h3>


In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (``_``), with all letters in lowercase. For instance, those same variables would be called ``name``, ``first_name``, and ``preferred_first_name``, respectively, in Python.

In a file called ``camel.py``, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.


<strong><ins> Expected Input/Output </strong></ins>

``Input: camelCase: berry`` <br>
``Output: snake_case: berry``<br>

``Input: camelCase: bigBerry``<br>
``Output: snake_case: big_berry``

``Input: camelCase: iAmBerry ``<br>
``Output: snake_case: i_Am_Berry``

<h3> Coke Machine </h3>

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called ``coke.py``, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

<strong> <ins> Expected Output/Input:  </ins> </strong>

``Input: ``<br>
``Insert Coin: 25``

``Output: ``<br>
``Amount Due: 25``

``Input: ``<br>
``Insert Coin: 26``

``Output: ``<br>
``Amount Due: 25``

``Input: ``<br>
``Insert Coin: 50``

``Output: ``<br>
``Change Owed: 25``





<h3> Just setting up my twttr </h3>

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

<strong> <ins> Expected input/output: </ins> </strong>

``Input: twitter``
``Output: twttr``

``Input: What's your name?``
``Output: Wht's yr nm?``

``Input: CS50``
``Output: CS50``