import streamlit as st
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

st.title("Rock-Paper-Scissors2")

your_choice = st.selectbox("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.", options=[("Rock", 0), ("Paper", 1), ("Scissors", 2)])
cpu_choice = random.randint(0,2)

if your_choice not in [0,1,2]:
  st.write("You typed an invalid number, you lose!")
elif your_choice == cpu_choice:
  st.write(f"Your choice:\n{choices[your_choice]} \n CPU choice:\n{choices[cpu_choice]}")
  st.write("Draw")
elif (your_choice == 0 and cpu_choice == 1) or (your_choice == 1 and cpu_choice == 2) or (your_choice == 2 and cpu_choice == 0):
  st.write(f"Your choice:\n{choices[your_choice]} \n CPU choice:\n{choices[cpu_choice]}")
  st.write("You lose")
else:
  st.write(f"Your choice:\n{choices[your_choice]} \n CPU choice:\n{choices[cpu_choice]}")
  st.write("You win")
