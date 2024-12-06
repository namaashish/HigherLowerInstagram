from game_data import data 
import random


def format_data(account):

    account_name = account["name"]
    account_descri = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descri}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers ):

    if a_followers > b_followers :
        if user_guess == "a" :
            return True
        




score = 0
account_b = random.choice(data)
game_continue = True
while game_continue :
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        random_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(f"Compare B : {format_data(account_b)}")


    guess = input("who has more followers ? Type 'A' or 'B' :").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"right,{score}")
    else:
        print("sorry")
        game_continue = False
        