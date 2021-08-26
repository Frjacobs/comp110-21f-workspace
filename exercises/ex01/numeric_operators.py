"""The numeric operators program is designed to allow the user to input two numbers to then output 4 numeric expressions from the user input"""

__author__ = "730016032"

left_hand: str = input("Left-hand side: ")
right_hand: str = input("Right-hand side: ")
left_hand_int = int(left_hand)
right_hand_int = int(right_hand)
exponential_combined = left_hand_int ** right_hand_int
divide_combined = left_hand_int / right_hand_int
integerdivision_combined = left_hand_int // right_hand_int
remainder_combined = left_hand_int % right_hand_int


print(str(left_hand_int) + " ** " + str(right_hand_int) + " is " + str(exponential_combined))
print(str(left_hand_int) + " / " + str(right_hand_int) + " is " + str(divide_combined))
print(str(left_hand_int) + " // " + str(right_hand_int) + " is " + str(integerdivision_combined))
print(str(left_hand_int) + " % " + str(right_hand_int) + " is " + str(remainder_combined))