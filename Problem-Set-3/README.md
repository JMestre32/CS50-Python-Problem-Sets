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