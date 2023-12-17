# Function to print all facts
def print_facts(fact_list):
    print("\nFacts:")
    for fact in fact_list:
        print(fact)
        
# Function to print all rules
def print_rules(rule_list):
    print("\nRules:")
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

    print("\nNew Facts: ")
    new_facts = []
    while True:
        newly_derived_facts = []

        for rule in rules:
            premise, conclusion = rule
            if is_condition_satisfied(premise, facts) and conclusion not in facts:
                newly_derived_facts.append(conclusion)
                facts.append(conclusion)
                
        new_facts.extend(newly_derived_facts)
            

        if not newly_derived_facts:
            break   

    print("\n".join(map(str, new_facts)))
    return facts # To update facts


if __name__ == "__main__":
    # Initialize facts and rules
    facts = []
    rules = []

    while True:
        print("\n-----------------------------------------")
        print("[1] Add facts\n[2] Add rules\n[3] Done Adding \n[4] Generate and display new facts\n[5] Exit")
        choice = input("\n")

        # To exit
        if choice == '5':
            break
        
        # Add Facts
        elif choice == '1':
            ctr_fact = 1
            print("\nAdding Fact(s)...")
            while True:
                fact_input = input(f"Fact {ctr_fact}: ")
                if not fact_input:
                    print("Invalid input.")
                    continue
                if fact_input == '3':
                    break
                ctr_fact += 1
                facts.append(fact_input)
            print("\nFact(s) added.\n")
            print_facts(facts)
            print_rules(rules)
            
        # Add Rules
        elif choice == '2':
            ctr_rule = 1
            print("\nAdding Rule(s)...")
            while True:
                rule_input = input(f"Rule {ctr_rule}: ")
                if rule_input == '3':
                    break
                if "if" in rule_input and ", then" in rule_input:
                    premise, conclusion = rule_input.split(", then ")
                    premise = premise.replace("if", "").strip()
                    rules.append((premise, conclusion))
                    ctr_rule += 1
                else:
                    print("Invalid rule format. [if {premise}, then {conclusion}")
            print("\nRule(s) added.\n")
            print_facts(facts)
            print_rules(rules)
        
        # Generate and display new facts    
        elif choice == '4':
            print_facts(forward_chaining(facts, rules))
        else:
            print("Invalid choice.")

    
    


