#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time
import pygame

def delay_print(message, delay=1):
  '''print a message with delay'''
  for char in message:
      print(char, end='', flush=True)
      time.sleep(delay)
  print()






gradient = {'name': 'gradient', 'type': 'room'}
mariana = {'name': 'mariana', 'type': 'furniture'}
jose = {'name': 'jose', 'type': 'furniture'}
doorA = {'name': 'doorA', 'type': 'door'}
keyA = {'name': 'keyA', 'type': 'key', 'target': doorA}
git = {'name': 'git', 'type': 'room'}
carolina = {'name': 'carolina', 'type': 'furniture'}
doorB = {'name': 'doorB', 'type': 'door'}
keyB = {'name': 'keyB', 'type': 'key', 'target': doorB}
doorC = {'name': 'doorC', 'type': 'door'}
boost = {'name': 'boost', 'type': 'room'}
fred = {'name': 'fred', 'type': 'furniture'}
keyC = {'name': 'keyC', 'type': 'key', 'target': doorC}
valeria = {'name': 'valeria', 'type': 'furniture'}
doorD = {'name': 'doorD', 'type': 'door'}
keyD = {'name': 'keyD', 'type': 'key', 'target': doorD}
comet = {'name': 'comet', 'type': 'room'}
pedro = {'name': 'pedro', 'type': 'furniture'}
outside = {'name': 'outside'}

all_rooms = [gradient, git, boost, comet, outside]
all_doors = [doorA, doorB, doorC, doorD]

connections = {
    'gradient': [mariana, jose, keyA, doorA],
    'git': [carolina, doorA, doorB, doorC, keyB],
    'boost': [fred, doorB, valeria, keyC, keyD],
    'comet': [pedro, doorC, doorD],
    'jose': [keyA],
    'doorA': [gradient, git],
    'carolina': [keyB],
    'doorB': [git, boost],
    'doorC': [git, comet],
    'fred': [keyC],
    'valeria': [keyD],
    'doorD': [comet, outside],
    'outside': [doorD]
}

target_room = outside
init_game_state = {
    'current_room': gradient,
    'keys_collected': [],
    'target_room': target_room
}


def play_room(room):
    game_state['current_room'] = room
    if game_state['current_room'] == game_state['target_room']:
        print('Congrats, you survived the bootcamp. ARE YOU HAPPY NOW?')
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'interact'? ").strip()
        if intended_action == "explore":
            explore(room)
            play_room(room)
        elif intended_action == "interact":
            interact_with_item(input("Who would you like to interact with? ").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'interact'.")
            play_room(room)


def explore(room):
    items = [i["name"] for i in connections[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))


def interact_with_item(item_name):
  current_room = game_state["current_room"]
  next_room = ""
  output = None

  for item in connections[current_room["name"]]:
      if item["name"].lower() == item_name.lower():
          output = "Trust the process! You interact with " + item_name + ". "
          if item["type"] == "door":
              have_key = False
              for key in game_state["keys_collected"]:
                  if "target" in key and key["target"] == item:
                      have_key = True
              if have_key:
                  output += "You unlock it with a key you have."
                  next_room = get_next_room_of_door(item, current_room)
              else:
                  output += "It is locked, but you don't have the key."
          elif item["name"] == "mariana":
              output += "She says, 'I'm from Azores.'"
              game_state["keys_collected"].append(item)
          elif item["name"] == "pedro":
              output += "He says, 'I'm in your heart, mind, and on Slack.'"
              game_state["keys_collected"].append(item)
          else:
              if item["name"] in connections and len(connections[item["name"]]) > 0:
                  item_found = connections[item["name"]].pop()
                  game_state["keys_collected"].append(item_found)
                  output += "You find " + item_found["name"] + "."
              else:
                  output += "There isn't anything interesting about it."
          print(output)
          break

  if output is None:
      print("The item you requested is not found in the current room.")

  if next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes':
      play_room(next_room)
  else:
      play_room(current_room)






def get_next_room_of_door(door, current_room):
    connected_rooms = connections[door["name"]]
    for room in connected_rooms:
        if not current_room == room:
            return room


def wake_up():
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/adi/Desktop/Shite/Open (Extended).mp3")  # Replace with the path to your music file
    pygame.mixer.music.play()
    delay_print("Survive Bootcamp",delay=0.05)
    delay_print("Welcome to 'Bootcamp Odyssey', an immersive narrative game that follows the journey of you embarking on a new course at the prestigious IronHack.",delay=0.05)
    delay_print("As an IronHacker, you will navigate the challenges and triumphs of Bootcamp, forming bonds with fellow students, overcoming obstacles, and unlocking the secrets of Data Analytics. Your choices will shape your character's destiny and determine their success in this scholarly adventure.",delay=0.05)

    start = input('Are you ready to trust the process? YES/NO ').upper()
    if start == 'YES':
        play_room(game_state['current_room'])
    elif start == 'NO':
        print("Come back when you're not too scared.")
    else:
        print('Please choose a valid option')
        wake_up()


game_state = init_game_state.copy()
wake_up()


# In[ ]:




