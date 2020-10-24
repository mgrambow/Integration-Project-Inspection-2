#Programmer: Matthew Grambow
#Project: COP 1500 Integration Project - Fall 2020
#Professor: Scott VanSelow

#Description of Program: This program is a simple word game, similar to the "MadLibs" books.
#It prompts the user to input certain types of words and numbers, stores them, and outputs them into a pre-written story.
#The numbers that are requested and stored by the program are used to demonstrate basic computations and complete the story's "Restaurant Order" theme.

#Simple I/O: add a greeting/introduction to the user

print("Welcome to MattLibs")
print()
print("COP 1500's Greatest Phrasal Template Word Game!")
print("")

enter_prompt = input("<Press Enter to Begin>") 
print(enter_prompt)
print("Nice job! Keep following my directions, and you will be a MattLib pro in no time!")
print()
print("Though this isn't a quiz game application, we will start with a bit of a tricky question...")
print()
name = input("What is your name?\n")
print()
print("Welcome to MattLibs, ", name, "!", sep='')
print()
print("Just type in the type of word I request, and I'll build your MattLibs creation!")
print()
print("Let's get started!")
print()

#User Input Section of Program
#This section includes many Assignment Operators '=' to store string and integer information to output later in the program.

adjective_1 = input("Type in an Adjective: ")
color_1 = input("Type in a Color: ")
color_2 = input("Type in another Color: ")
adjective_2 = input("Type in another Adjective: ")
adverb_1 = input("Type in an Adverb: ")
adjective_3 = input("Type in another Adjective: ")
place_1 = input("Type in the name of a Place: ")
adjective_4 = input("Type in another Adjective: ")
adjective_5 = input("Type in another Adjective: ")
adjective_6 = input("Type in another Adjective: ")
noun_1 = input("Type in a Noun: ")
plural_noun_1 = input("Type in a Plural Noun: ")
adjective_7 = input("Type in another Adjective: ")
noun_2 =  input("Type in another Noun: ")
food_one = input("Type in a type of Food: ")
food_one_dollars = int(input("Type in a number between 0 and 99: "))
food_one_cents = int(input("Type in another number between 0 and 99: "))
food_two = input("Type in another type of Food: ")
food_two_dollars = int(input("Type in a number between 0 and 99: "))
food_two_cents = int(input("Type in another number between 0 and 99: "))
food_ingredient_1 = input("Type in a Food Indredient: ")
food_three_dollars = int(input("Type in a number between 0 and 99: "))
food_three_cents = int(input("Type in another number between 0 and 99: "))
size_1 = input("Type in a Size: ")
food_topping_1 = input("Type in a Food Topping: ")
curd_dollars = int(input("Type in a number between 0 and 99: "))
curd_cents = int(input("Type in another number between 0 and 99: "))
exclaimation_1 = input("Type in an Exclaimation: ")
verb_1 = input("Type in a Verb: ")
noun_3 = input("Type in a Noun: ")
number_people_1 = int(input("Enter a number between 1 and 10: "))

#Transition to MattLib Output

print()
print("Are you ready to see you MattLibs creation?!")
#Good location for a while and/or boolean operators section.

#Countdown Using Shortcut Operators
#This section of the program is a simple countdown, using shortcut operators, the 'for' and 'in' keywords, and the range() function.
#The function 'countdown' accepts the parameter 'user_count', which is inputed by the user prior to the definition of the function and through its call argument.
#The below lines create the function 'countdown', which is then immediately called.  This function could be reused at any point in the program to create another countdown.
#The 6th line of code below uses the key words 'for' and 'in' in combination with the range function to have the code run the code the 'user_number' amount of times.
#The shortcut operator reduces the value of 'user_count' by one, until it reaches 0.  Once at 0, the == relational operator causes the "OFF TO DELISCIOUSNESS!!" message to print, if TRUE.
#The if, elif, and else keywords change the outputted message, based on the value of 'count'.
user_count = int(input("How long would you like the Countdown to be?  Enter a positive integer of at least 1: "))
def countdown(user_count):
    for i in range(user_count):
        user_count -= 1
        print(user_count)
        print()
        if user_count > 5:
            print("Let's go!")
            print()
        #The line below uses the Boolean Operator 'and' to add an "Almost There!" message once the countdown reaches between 3 and 0.
        elif user_count <= 3 and user_count > 0:
            print("Almost There!")
            print()
        elif user_count == 0:
            print("OFF TO DELISCIOUSNESS!!")
        else:
            print()

countdown(user_count)
#Transition to completed MattLib

print("MattLib Number 1: The Perfect Culvers Order")
print()
print()
print("Just down the road in Gulf Coast Town Center, lies a", (adjective_1), "restaurant, painted in", (color_1), "and", (color_2)+".")
print()
print("This", (adjective_2), "place is", (adverb_1), "called Culvers and it comes from a", (adjective_3), "place, known as", (place_1)+".")
print()
print("The menu is", (adjective_4), "and it can be a little", (adjective_5), "so here is some advice on how to create a", (adjective_6), "Culvers", (noun_1)+".")
print()
print("There are a few", (plural_noun_1), "that are", (adjective_7), "in any Culvers", (noun_2)+":")
print()
print("There is the", (food_one), "which costs", (food_one_dollars), "dollars and", (food_one_cents), "cents.")
print("There is also the", (food_two), "which costs", (food_two_dollars), "dollars and", (food_two_cents), "cents.")

#The next two lines use the string operator '+' to create funny compound-words for two of the menu items: (food_ingredient_1)+"burger" and (food_topping_1)+"curds".
#The 2nd line also uses the string operator '*' to create a silly exclaimation to demonstrate Python's ability to multiply strings: ((exclaimation_1) * 3)
print("Finally, you just have to try the signature menu item, the", (food_ingredient_1)+"burger, which costs", (food_three_dollars), "dollars and", (food_three_cents), "cents.")
print("Of course, no Culvers order is complete without a", (size_1), "order of", (food_topping_1)+"curds", "which costs", (curd_dollars), "dollars and", (curd_cents), "cents, but will make everyone in your party say:", ((exclaimation_1) * 3) + "!")
print()
print("As the Culvers experience is social as well as culinary, it is best to", (verb_1), "with a", (noun_3), "of friends.")
print("Culvers food can be addicting, so you should plan to order enough food for everyone in your party!")
print()

#Calculations Section
print("With a group of", (number_people_1), "friends, you will want to order at least:")

#The '*' operator is used in the following 4 lines to calculate amounts of food through multiplication, based on the number of people inputted by the user: number_people_1 * 3
#The '**' operator is used in the 4th line below to calculate the amount of curds through exponetiation, based on the number of people inputted by the user: number_people_1 ** 2
number_food_one = (number_people_1 * 3)
number_food_two = (number_people_1 * 4)
number_food_three = (number_people_1 * 5)
number_curds_1 = (24 * ((number_people_1)**2))

print(number_food_one, "orders of the", (food_one))
print(number_food_two, "orders of the", (food_two))
print(number_food_three, "orders of the", (food_ingredient_1)+"burger")
print()

print("The", (food_topping_1)+"curds", "are where you want to be careful.")
print("In my opinion, your party of", (number_people_1), "should order at least", ((number_people_1)**2), "orders of", (food_topping_1)+"curds", "to share.")
print()
#The below line uses the '//' operator to perform floor division on the number of curds (number_curds_1) to calculate a minimum amount of curds per person (number_people_1).
print("As each order contains approximately 24", (food_topping_1)+"curds, this size of order ensures that everyone gets the recommended amount of", ((number_curds_1) // (number_people_1)), "curds.")
#The below line uses the '%' modulus operator to determine the number of remaining curds after dividing them equally amount the number of people (number_people_1).
print("Be sure to be the one to divide them up, so that you can take the", (24 % (number_people_1)), "that are leftover for yourself!")
print()
print("Now that you have placed your order, it is time to figure out how much this is all going to cost!")
print()
food_one_cost = (food_one_dollars) + (float((food_one_cents) / 100))
food_two_cost = (food_two_dollars) + (float((food_two_cents) / 100))
food_three_cost = (food_three_dollars) + (float((food_three_cents) / 100))
curd_cost = (curd_dollars) + (float((curd_cents) / 100))

#The below line uses the '+' operator to add the four food costs together into the pre_discount_cost
pre_discount_cost = food_one_cost + food_two_cost + food_three_cost + curd_cost

discount_amount = (pre_discount_cost) * .1

#The below line uses the '-' operator to subtract the discountAmount from the pre_discount_cost to calculate the final_cost.
final_cost = pre_discount_cost - discount_amount

#The below line uses the '/' operator to divide final_cost by number_people_1 to provide a per_person_cost.
per_person_cost = final_cost / number_people_1

print("All together, your perfect Culvers will cost: $", format(pre_discount_cost, "0.2f"), sep='')
print()
print("But wait!  Don't forget to use your 10% FGCU student discount, which will save your party: $", format(discount_amount, "0.2f"), sep='')
print()
print("With the discount, the real total will be: $", format(final_cost, "0.2f"), sep='')
print()
print("Each person in your party will need to pay their fair share of: $", format(per_person_cost, "0.2f"), sep='')

#The four lines of code below use conditional structures (if else), the relational operator '>', and the Boolean operator "or" to change the outputted text based on the value of per_person_cost or final_cost.
if per_person_cost > 15 or final_cost > 100:
    print("That is actually pretty expensive...")
else:
    print("Not a bad deal!")
print()
print("Enjoy your meal!")
print()
print()

#The below section uses a while loop and the "not" Boolean operator to encourage a better rating if the user-inputted rating is NOT greater than or equal to 5.
user_rating = int(input("How would you rate this MattLib, on a scale from 1 to 10?: "))
while not(user_rating >= 5):
    user_rating = int(input("That seems a bit low, can you go any higher, on a scale from 1 to 10?: "))
else:
    print("Thank you for your rating!")
