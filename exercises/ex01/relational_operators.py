"""The relational operator program allow the user to input two integers and demonstrates four relational operators based on the input"""

__author__ = "730016032"

left_hand: str = input("Left-hand side: ")
right_hand: str = input("Right-hand side: ")
left_hand_int = int(left_hand)
right_hand_int = int(right_hand)
less_than = left_hand_int < right_hand_int
greater_equal = left_hand_int >= right_hand_int
equal_to = left_hand_int == right_hand_int
not_equal = left_hand_int != right_hand_int


print(str(left_hand_int) + " < " + str(right_hand_int) + " is " + str(less_than))
print(str(left_hand_int) + " >= " + str(right_hand_int) + " is " + str(greater_equal))
print(str(left_hand_int) + " == " + str(right_hand_int) + " is " + str(equal_to))
print(str(left_hand_int) + " != " + str(right_hand_int) + " is " + str(not_equal))