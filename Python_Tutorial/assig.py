from automata.fa.dfa import DFA

# Define the DFA
dfa_div_by_3 = DFA(
    states={'S0', 'S1', 'S2'},
    input_symbols={'0', '1'},
    transitions={
        'S0': {'0': 'S0', '1': 'S1'},
        'S1': {'0': 'S2', '1': 'S0'},
        'S2': {'0': 'S1', '1': 'S2'}
    },
    initial_state='S0',
    final_states={'S0'}
)

# Driver code
binary_num = input("Enter a binary number: ").strip()
if dfa_div_by_3.accepts_input(binary_num):
    print(f"{binary_num} is divisible by 3")
else:
    print(f"{binary_num} is NOT divisible by 3")
