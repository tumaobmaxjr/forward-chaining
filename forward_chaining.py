# Function to print all facts
def print_facts(fact_list):
    for fact in fact_list:
        print(fact)
        
# Function to print all rules
def print_rules(rule_list):
    for rule in rule_list:
        premise, conclusion = rule
        print(f"if {premise}, then {conclusion}")

# Function to check if a rule's premises are satisfied
def is_condition_satisfied(premise, facts):
    premises = premise.split(' and ')
    all_premises_satisfied = True
    for cond in premises:
        if cond not in facts:
            all_premises_satisfied = False
            break

    return all_premises_satisfied

# Function to perform forward chaining
def forward_chaining(initial_facts, rules):
    facts = initial_facts.copy()
    # print("\nNew Facts: ")
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


if __name__ == "__main__":
    # Initialize existing facts and rules
    facts = []
    rules = []

    print("------------------------------------------------------------------------------------------------------")
    print("\nFacts:")
    print_facts(facts)
    
    print("\nRules:")
    print_rules(rules)

    while True:
        print("------------------------------------------------------------------------------------------------------")
        choice = input("('f') add new fact, ('r') add new rule, ('g') generate and disp new fact(s), ('exit') to exit: ")
        if choice.lower() == 'exit':
            break
        
        # Add Facts
        elif choice.lower() == 'f':
            ctr_fact = 1
            print("\nAdding Fact(s)...")
            while True:
                fact_input = input(f"Fact {ctr_fact}: ")
                if not fact_input:
                    print("Invalid input.")
                    continue
                if fact_input.lower() == 'exit':
                    break
                ctr_fact += 1
                facts.append(fact_input)
            print("\nFact(s) added.\n")
            print("\nCurrent Facts:")
            print_facts(facts)
            print("\nCurrent Rules:")
            print_rules(rules)
            
        # Add Rules
        elif choice.lower() == 'r':
            ctr_rule = 1
            print("Adding Rule(s)...")
            while True:
                rule_input = input(f"Rule {ctr_rule}: ")
                if rule_input.lower() == 'exit':
                    break
                if "if" in rule_input and ", then" in rule_input:
                    premise, conclusion = rule_input.split(", then ")
                    premise = premise.replace("if", "").strip()
                    rules.append((premise, conclusion))
                    ctr_rule += 1
                else:
                    print("Invalid rule format.")
            print("Rule(s) added.\n")
            print("\nCurrent Facts:")
            print_facts(facts)
            print("\nCurrent Rules:")
            print_rules(rules)
        
        # Generate and display new facts    
        elif choice.lower() == 'g':
            print("\nAll Facts:")
            facts = forward_chaining(facts, rules)
            print_facts(facts)

            print("\nAll Rules:")
            print_rules(rules)
        else:
            print("Invalid choice.")

    
    


