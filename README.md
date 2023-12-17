# CSci 144 - Intelligent Systems | Coursework 2
## Rule-Based Expert System Operating on Forward Chaining Reasoning Method

This documentation describes a simple forward chaining inference engine implemented in Python. Forward chaining is a method used in artificial intelligence and expert systems to infer new facts based on a set of initial facts and a set of rules. This implementation allows you to input facts, rules, and generate new facts based on the rules using forward chaining.

## Overview

The provided Python code includes the following components:

- Functions to print existing facts and rules.
- A function to check if a rule's premises are satisfied based on the current set of facts.
- A function to perform forward chaining and derive new facts based on the rules and existing facts.
- A command-line interface for adding new facts, rules, and generating and displaying new facts.

## Usage

The rule-based system provides a menu-driven interface for users to interact with the system. Users can add facts, add rules, generate new facts, and exit the system.

1. Adding Facts:
- Choose [1] from the menu.
- Input each fact and press 'Enter'.
- Enter '3' when done to return to the main menu.
2. Adding Rules:
- Choose [2] from the menu.
- Input rules in the format "if {premise}, then {conclusion}" and press 'Enter'.
- Enter '3' when done to return to the main menu.
3. Generating New Facts:
- Choose [4] from the menu to see newly derived facts.
4. Exiting the System:
- Choose [5] from the menu to exit the system.
