# Problem Set 3

<h3> Fuel Gauge </h3>
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called ``fuel.py``, implement a program that prompts the user for a fraction, formatted as ``X/Y``, wherein each of ``X`` and ``Y`` is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output ``E`` instead to indicate that the tank is essentially empty. And if 99% or more remains, output ``F`` instead to indicate that the tank is essentially full.

If, though, ``X`` or ``Y`` is not an integer, ``X`` is greater than ``Y``, or ``Y`` is ``0``, instead prompt the user again. (It is not necessary for ``Y`` to be ``4``.) Be sure to catch any exceptions like ``ValueError`` or ``ZeroDivisionError``.

<strong><ins> Expected Input/Output: </ins> </strong>

``Fraction: 1/4 ``
``25%``

``Fraction: 1/2 ``
``50%``

``Fraction: 3/4 ``
``75%``


``Fraction: 4/4 ``
``F``

``Fraction: 1/0 ``
``Fractio: 0/1``
``E``

<h3> Felipe's Taqueria </h3>

One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

<code>
{ "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
</code>

In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.


Hints:
<ul>
<li> Note that you can detect when the user has inputted control-d by catching an EOFError with code like: </li>
<code>
try:
    item = input()
except EOFError:
    ...
</code>
You might want to print a new line so that the user’s cursor (and subsequent prompt) doesn’t remain on the same line as your program’s own prompt.


<li> You might want to print a new line so that the user’s cursor (and subsequent prompt) doesn’t remain on the same line as your program’s own prompt. </li>

<li> Note that a dict comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#mapping-types-dict, among them get, and supports operations like: </li>

``d[key]`` <br>
and 
``if key in d: ``
    ``...``
<li> Be sure to avoid or catch any KeyError </li>

<strong><ins> Expected Input/Output: </ins></strong>

``Item: burrito `` <br>
``Total: $7.50 `` <br>
``Item: large quesadilla`` <br>
``Item: super quesadilla `` <br>
``Total: $17.00`` <br>
``python taqueria.py ``
``Item: nachos`` <br>
``Total: $11.00`` <br>
``Item: taco`` <br>
``Total: $14.00 `` <br>
``Item: taco `` <br>
``Total: $17.00`` <br>
``Item: taco `` <br>
``Total: $20.00`` <br>

<h3> Grocery List </h3>
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called ``grocery.py``, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

Hint: You'll probably want to use a dict and be sure to avoid or catch ``Key Error``

<strong><ins> Expected Input/Output: </ins></strong>

<code>
python3 grocery.py
apple
banana
banana
ice cream

1 APPLE
2 BANANA
1 ICE CREAM
</code>

<code>
python3 grocery.py
lettuce
tomato
tomato
carrot
tomato

1 CARROT
1 LETTUCE
3 TOMATO
</code>

