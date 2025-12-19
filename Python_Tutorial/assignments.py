# FSM to check divisibility by 3 for binary numbers

# State representation:
# 0 -> remainder 0 (divisible by 3)
# 1 -> remainder 1
# 2 -> remainder 2

# Transition table: state[row][col] -> next state
# col=0 means reading '0', col=1 means reading '1'
state_transition = [
    [0, 1],  # From S0: 0 -> S0, 1 -> S1
    [2, 0],  # From S1: 0 -> S2, 1 -> S0
    [1, 2]   # From S2: 0 -> S1, 1 -> S2
]

def is_divisible_by_3(binary_str):
    state = 0  # Start at remainder 0 (S0)
    
    for bit in binary_str:
        if bit not in ('0', '1'):
            raise ValueError("Invalid binary number")
        
        state = state_transition[state][int(bit)]
    
    return state == 0

# Driver code
binary_num = input("Enter a binary number: ").strip()
if is_divisible_by_3(binary_num):
    print(f"{binary_num} is divisible by 3")
else:
    print(f"{binary_num} is NOT divisible by 3")
    
