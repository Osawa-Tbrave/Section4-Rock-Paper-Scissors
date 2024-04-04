import streamlit as st
import random

st.title("Rock-Paper-Scissors")



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

#Write your code below this line 👇
import random
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpu_choice = random.randint(0,2) # int
# 選択肢の表示
choices = [rock, paper, scissors]
if your_choice not in [0,1,2]:
  print("You typed an invalid number, you lose!")
elif your_choice == cpu_choice:
  print(f"Your choice:{choices[your_choice]} \n CPU choice:{choices[cpu_choice]}")
  print("Draw")
elif (your_choice == 0 and cpu_choice == 1) or (your_choice == 1 and cpu_choice == 2) or (your_choice == 2 and cpu_choice == 0):
  print(f"Your choice:{choices[your_choice]} \n CPU choice:{choices[cpu_choice]}")
  print("You lose")
elif your_choice >= 3 or your_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(f"Your choice:{choices[your_choice]} \n CPU choice:{choices[cpu_choice]}")
  print("You win")

print("---")
print("リストとインデックスの扱いとランダムを用いました。 \n デバッグを含めた条件分岐。入力が数字以外、文字列の場合の対処。")
