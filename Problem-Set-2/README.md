# Problem Set 2 

<h3> camelCase </h3>


In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (``_``), with all letters in lowercase. For instance, those same variables would be called ``name``, ``first_name``, and ``preferred_first_name``, respectively, in Python.

In a file called ``camel.py``, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.


<strong><ins> Expected Input/Output </strong></ins>

``Input: camelCase: berry``
``Output: snake_case: berry``

``Input: camelCase: bigBerry``
``Output: snake_case: big_berry``

``Input: camelCase: iAmBerry ``
``Output: snake_case: i_Am_Berry``

<h3> Coke Machine </h3>

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called ``coke.py``, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

<strong> <ins> Expected Output/Input:  </ins> </strong>

``Input: ``
``Insert Coin: 25``

``Output: ``
``Amount Due: 25``

``Input: ``
``Insert Coin: 26``

``Output: ``
``Amount Due: 25``

``Input: ``
``Insert Coin: 50``

``Output: ``
``Change Owed: 25``





