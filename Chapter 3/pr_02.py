
# Print Invitation Letter template  :-->

letter = '''Dear <|NAME|>,
Greeting From Bhardwaj.
You are Invited.

Date: <|DATE|> '''

name = input("Enter Name ")
date = input("Enter Date ")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)
