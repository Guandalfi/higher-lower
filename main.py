import random
import data as celebrities
from art import logo, vs
from replit import clear

def random_person():
    '''return a random celebritie fom data.py'''
    person = random.choice(celebrities.data)
    return person

def more_followers(person_1_followers, person_2_followers):
    '''Take the number of 2 people followers, and return who has more'''
    if person_1_followers > person_2_followers:
        return 'A'
    elif person_2_followers > person_1_followers:
        return 'B'




random_person_1 = random_person()
player_score = 0
wining = True
while wining == True:

    random_person_2 = random_person()
    #Verifica se gerou a pessoa igual a anterior e então gera novamente se sim
    while random_person_2['name'] == random_person_1['name']:
        random_person_2 = random_person()
    #Verifica qual pessoa tem mais seguidores
    has_more_followers = more_followers(random_person_1['follower_count'], random_person_2['follower_count'])
  
    print(logo)
    
    if player_score > 0:
        print(f"You're right! Current score: {player_score}.")

    print(f"Compare A: {random_person_1['name']}, a {random_person_1['description']}, from {random_person_1['country']}.")
    print(vs)
    print(f"Against B: {random_person_2['name']}, a {random_person_2['description']}, from {random_person_2['country']}.")

    player_answer = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    #Verifica resposta do jogador
    #Se o jogador acertou, a pessoa 'B' se torna a pessoa 'A' e compara com a proxima 'B'
    if player_answer == has_more_followers:
      random_person_1 = random_person_2
      player_score += 1

    elif player_answer != has_more_followers:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {player_score}")
        wining = False
