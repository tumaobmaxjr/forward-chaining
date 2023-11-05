# CSci 144 - Intelligent Systems | Coursework 2
## Rule-Based Expert System Operating on Forward Chaining Reasoning Method

This documentation describes a simple forward chaining inference engine implemented in Python. Forward chaining is a method used in artificial intelligence and expert systems to infer new facts based on a set of initial facts and a set of rules. This implementation allows you to input facts, rules, and generate new facts based on the rules using forward chaining.

## Table of Contents

1. [Overview](#overview)
2. [Functions](#functions)
    - [print_facts](#print-facts)
    - [print_rules](#print-rules)
    - [is_condition_satisfied](#is-condition-satisfied)
    - [forward_chaining](#forward-chaining)
3. [Usage](#usage)
4. [Example](#example)


## Overview
<a id="overview"></a>

The provided Python code includes the following components:

- Functions to print existing facts and rules.
- A function to check if a rule's premises are satisfied based on the current set of facts.
- A function to perform forward chaining and derive new facts based on the rules and existing facts.
- A command-line interface for adding new facts, rules, and generating and displaying new facts.

## Functions
<a id="functions"></a>

### print_facts
<a id="print-facts"></a>

This function prints a list of facts.

```python
def print_facts(fact_list):
    for fact in fact_list:
        print(fact)
```

### print_rules
<a id="print-rules"></a>

This function prints a list of rules. Each rule consists of premises and a conclusion.

```python
def print_rules(rule_list):
    for rule in rule_list:
        premise, conclusion = rule
        print(f"if {premise}, then {conclusion}")
```

### is_condition_satisfied
<a id="is-condition-satisfied"></a>

This function checks if a rule's premises are satisfied based on the current set of facts. It splits the premises using 'and' and checks if all conditions are satisfied.

```python
def is_condition_satisfied(premise, facts):
    premises = premise.split(' and ')
    all_premises_satisfied = True
    for cond in premises:
        if cond not in facts:
            all_premises_satisfied = False
            break

    return all_premises_satisfied
```

### forward_chaining
<a id="forward-chaining"></a>
This function performs forward chaining using the given set of initial facts and rules. It iteratively applies the rules to generate new facts until no more facts can be derived.

```python
def forward_chaining(initial_facts, rules):
    facts = initial_facts.copy()

    while True:
        newly_derived_facts = []
        
        for rule in rules:
            premise, conclusion = rule
            if is_condition_satisfied(premise, facts) and conclusion not in facts:
                newly_derived_facts.append(conclusion)
                facts.append(conclusion)

        if not newly_derived_facts:
            break

    return facts # To update facts
```

## Usage
<a id="usage"></a>

To use the forward chaining inference engine, follow these steps:

1. Initialize existing facts and rules.
2. Use the command-line interface to add new facts and rules.
3. Generate and display new facts based on the rules and existing facts.

The script will continue running until you choose to exit.

## Example
<a id="example"></a>

An example of how to use the forward chaining inference engine is provided in the code. You can add facts, rules, and generate new facts based on the rules. For example:

- Add new facts by choosing 'f'.
- Add new rules by choosing 'r' and following the format: if <premises>, then <conclusion>.
- Generate and display new facts by choosing 'g'.
You can run the script and interact with it through the command line.