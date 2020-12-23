import random
# below the program takes an integer value from the user in order to throwing the coins to the chambers.
number_of_coins = int(input("Please enter the number of coins that you are going to throw:"))
# below, by the random module's choices method, everytime the program is made run, the distrubition of coins
# will be unique for that time. This method returns a random choice sequence by the probability weights.
# @param sequence: here the sequence is a list of the ten chambers that are seen in the problem.
# @param weights: the possibility weight of each of the chamber. That comes from the Pascal triangle's 10.level
# since there are ten chambers.
# @param k: k here is the length of the list that will be created in terms of possibility weights. This is the
# user input for the number of the coins that are going to be thrown into the chambers.
coins = random.choices([1,2,3,4,5,6,7,8,9,10],weights=[1,9,36,84,126,126,84,36,9,1],k=number_of_coins)
# the_max_occcurence variable is to determine the height of the chambers. It depends on the maximum occurrence
# of coins in a chamber. If we think of the probability theoretically, chambers in the middle will be
# determinative for the max occurrence. By finding the max occurred amount of coin in a chamber it is being assigned to the
# max occurrence variable.
the_max_occurrence = 0
for i in range(1,11):
    if coins.count(i) > the_max_occurrence:
        the_max_occurrence = coins.count(i)
# code below is used to print number of coins in a chamber
for i in range(1,11):
    print("Number of coins in chamber {} is...: {}".format(i, coins.count(i)))
#the outside for loop below (whose iterator variable called i) is used to print the enumeration of the number
# of the coins for each chamber. i variable varies in a descending order
for i in range(the_max_occurrence,0,-1):
    # r.just() method is used for arranging the enumeration of the number of coins in a proper way.
    # @param end: is used not to pass into the new line
    print(str(i).rjust(3) + "|", end="")
    # the for loop below is used nested. Because it will be used for placing the coins in the table.
    # in order to do that there is an iterator variable called a, every time through the loop it represents
    # the number of the chamber. And it places the coins into the chambers if the coin in that height level of
    # chamber exists. For example if the max occurrence of coins in a chamber is 13. It will be started to
    # check whether there is any chamber that has a 13rd coin in it or not. If it's not there will be a space for
    # that height level in the chamber and so on.
    for a in range(1,11):
        print(" o |" if coins.count(a) >= i else "   |",end="")
    # the print function below is used to pass onto a new line because when a height level for all of the
    # chambers is done checking, it has to print for another height level.
    print()
#the print function below simply prints a line in order to print the number of the chambers at the bottom.
print(" --+"+"---+"*10+"\n   |",end="")
#the for loop below prints the number of chambers and "|" is used to separate them
for i in range(1,11):
    print(" {} |".format(i),end="")


# YUSUF EREN KAYA 190709054





