import streamlit as st
import random

st.title("Rock-Paper-Scissors1")

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

your_choice = st.radio("What do you choose?", options=["選択してください", "Rock", "Paper", "Scissors"])
if your_choice == "選択してください":
    st.write("Please make a choice.")
else:
    your_choice_index = ["Rock", "Paper", "Scissors"].index(your_choice)
    cpu_choice_index = random.randint(0,2) # int

    # ユーザーの選択を表示
    st.write("Your choice:")
    st.code(choices[your_choice_index])

    # CPUの選択を表示
    st.write("CPU choice:")
    st.code(choices[cpu_choice_index])

    if your_choice_index == cpu_choice_index:
      st.write("Draw")
    elif (your_choice_index == 0 and cpu_choice_index == 1) or (your_choice_index == 1 and cpu_choice_index == 2) or (your_choice_index == 2 and cpu_choice_index == 0):
      st.write("You lose")
    else:
      st.write("You win")
