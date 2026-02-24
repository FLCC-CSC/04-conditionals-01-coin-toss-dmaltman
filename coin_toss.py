# FILE NAME - coin_toss.py
# NAME: Dawn Maltman
# DATE: February 23, 2026
# BRIEF DESCRIPTION:  Determine output of random coin toss

# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience
########## ENTER YER CODE BELOW THIS LINE ##########
import random

def main():
    random_flip()

def random_flip():
    random_number = random.randint(1,100)

    print('===== Coin Flipper =====')
    
    if random_number >= 51:
        print("Tails")
    if random_number < 51:
        print("Heads")

main()









########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
The hardest part of the lab was remembering how to generate a random number.






'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[x] I'm solid. Totally got it.
'''
