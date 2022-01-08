import random
from typing import List, Dict

#FUNCTIONS--------------------------------------------------------------------------

def avoid_my_neck(my_head: Dict[str, int], my_body: List[dict
], possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """
    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        possible_moves.remove("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        possible_moves.remove("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        possible_moves.remove("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        possible_moves.remove("up")

    return possible_moves



def avoid_borders(my_head: Dict[str, int], board_height: int, board_width: int, possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'border' direction removed
    """
    if my_head["x"] == 0 and my_head["y"] == 0:  #head at bottom left corner
        possible_moves.remove("left")
        possible_moves.remove("down")
    elif my_head["x"] == (board_width - 1) and my_head["y"] == 0: #head is at bottom right corner
        possible_moves.remove("right")
        possible_moves.remove("down")
    elif my_head["x"] == 0 and my_head["y"] == (board_height - 1) :  # head is at top left corner
        possible_moves.remove("left")
        possible_moves.remove("up")
    elif my_head["x"] == (board_width - 1) and my_head["y"] == (board_height - 1):#head at top right corner
        possible_moves.remove("right")
        possible_moves.remove("up")
    elif my_head["x"] == 0:               # head is along left border wall
        possible_moves.remove("left")   
    elif my_head["x"] == board_width - 1:            # head is along right border wall
        possible_moves.remove("right")
    elif my_head["y"] == 0:             # head is along bottom border wall
        possible_moves.remove("down")
    elif my_head["y"] == board_height - 1:            # head is along top border wall
        possible_moves.remove("up")

    return possible_moves 

def avoid_my_body(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
  """
  The head cannot hit itself, and is already programmed to avoid the neck, and the head cannot physically hit the third body section, so testing begins at the fourth body section ie: index 3
  """
  body_sections = 3

  while body_sections < len(my_body):
    if my_head["x"]  == my_body[body_sections]["x"] and my_head["y"] == my_body[body_sections]["y"] + 1:
      possible_moves.remove("down")
    print(f"Checking for head above Body Section {body_sections + 1}")
    print(possible_moves)

    if my_head["x"] == my_body[body_sections]["x"] and my_head["y"] == my_body[body_sections]["y"] - 1:
      possible_moves.remove("up")
    print(f"Checking for head below Body Section {body_sections + 1}")
    print(possible_moves)

    if my_head["x"] == my_body[body_sections]["x"] - 1 and my_head["y"] == my_body[body_sections]["y"]:
      possible_moves.remove("right")
    print(f"Checking for head left of Body Section {body_sections + 1}")
    print(possible_moves)

    if my_head["x"] == my_body[body_sections]["x"] + 1 and my_head["y"] == my_body[body_sections]["y"]:
      possible_moves.remove("left")
    print(f"Checking for head right of Body Section {body_sections + 1}")
    print(possible_moves)

    body_sections += 1

  return possible_moves
  
def avoid_other_snakes(my_head: Dict[str, int], other_snakes: List[dict], data: dict, possible_moves: List[str]) -> List[str]:
  snake_num = 0
  body_sections = 0

  while snake_num < len(other_snakes):
    while body_sections < len(other_snakes[snake_num]["body"]):
      print(f"current Body Sections Value: {body_sections}")
      print(f"current snake_num value: {snake_num}")
      print(f"Their are a total of {len(other_snakes) - 1} other snakes on the board")
      print(f"About to check snake named: {other_snakes[snake_num]['name']}")

      if data["you"]["id"] == other_snakes[snake_num]["id"]:
        break

      if my_head["x"] == other_snakes[snake_num]["body"][body_sections]["x"] and my_head["y"] == other_snakes[snake_num]["body"][body_sections]["y"] + 1:
        possible_moves.remove("down")
      print(f"Checking for body section {body_sections + 1} of Other Snake Named: {other_snakes[snake_num]['name']} below my head.")
      print(possible_moves)

      if my_head["x"] == other_snakes[snake_num]["body"][body_sections]["x"] and my_head["y"] == other_snakes[snake_num]["body"][body_sections]["y"] - 1:
        possible_moves.remove("up")
      print(f"Checking for body section {body_sections + 1} of Snake {snake_num} above my head.")
      print(possible_moves)

      if my_head ["x"] == other_snakes[snake_num]["body"][body_sections]["x"] - 1 and my_head["y"] == other_snakes[snake_num]["body"][body_sections]["y"]:
        possible_moves.remove("right")
      print(f"Checking for body section {body_sections + 1} of Snake {snake_num} to the right of my head.")
      print(possible_moves)

      if my_head["x"] == other_snakes[snake_num]["body"][body_sections]["x"] + 1 and my_head["y"] == other_snakes[snake_num]["body"][body_sections]["y"]:
        possible_moves.remove("left")
      print(f"Checking for body section {body_sections + 1} of Snake {snake_num} to the left of my head.")
      print(possible_moves)

      body_sections += 1

    snake_num += 1
    body_sections = 0

  return possible_moves

def closest_food (food_coords: List[dict], my_head: Dict[str, int], my_list: List[list]) -> List[list]:
  for item in food_coords:
    distance = abs(my_head["x"] - item["x"]) + abs(my_head["y"] - item["y"])
    for items in my_list:
      if distance == items[0]:
        break
    else: my_list.append([distance, item])

    print (distance)
    print(my_list)
    my_list.sort()
    print(my_list)

  return my_list

def move_to_food (my_list: List[list], my_head: Dict[str, int], possible_moves: List[str]) -> List[str]:
  for item in my_list:
    if len(possible_moves) <= 1:
      print(f"Breaking out of move_to_food as possible moves are only {possible_moves}.")
      break
    for items in possible_moves:
      print("starting loop")
      if items == "left" and item[1]["x"] < my_head["x"]:
        possible_moves = ["left"]
      elif items == "right" and item[1]["x"] > my_head["x"]:
        possible_moves = ["right"]
      elif items == "up" and item[1]["y"] > my_head["y"]:
        possible_moves = ["up"]
      elif items == "down" and item[1]["y"] < my_head["y"]:
        possible_moves = ["down"]

      if len(possible_moves) <= 1:
        print(f"Some moves were removed")
        break

  print(possible_moves)
  return possible_moves

def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see ]https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """
    my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]other_snakes = data["board"]["snakes"]
    other_snakes = data["board"]["snakes"] # A list of all battlesnake objects on the board including your own snake

    '''
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]
    '''
    
    
    board_height = data["board"]["height"] # An integer, the number of rows in the y-axis of the game board.
    board_width = data["board"]["width"] # An integer, the number of columns in the x-axis of the game board.

    food_coords = data["board"]["food"]


    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    print(f"All board data this turn: {data}")
    print(f"My Battlesnakes head this turn is: {my_head}")
    print(f"My Battlesnakes body this turn is: {my_body}")
    
    my_list = []

    possible_moves = ["up", "down", "left", "right"]

    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)
    
    possible_moves = avoid_borders(my_head, board_height, board_width, possible_moves)

    possible_moves = avoid_my_body(my_head, my_body, possible_moves)
    
    possible_moves = avoid_other_snakes(my_head, other_snakes, data, possible_moves)

    my_list = closest_food(food_coords, my_head, my_list)

    print(f"Final list {my_list}")

    possible_moves = move_to_food(my_list, my_head, possible_moves)

    print(f"The remaining move(s) is/are: {possible_moves}")
  
    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    move = random.choice(possible_moves)
    # TODO: Explore new strategies for picking a move that are better than random

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves} and hi.")

    return move
