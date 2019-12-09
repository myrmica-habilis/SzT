# coding: utf-8

from collections import OrderedDict

from player import Player
import world


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Inventář")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 's', player.move_north, "Jít na sever")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 'j', player.move_south, "Jít na jih")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'v', player.move_east, "Jít na východ")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'z', player.move_west, "Jít na západ")
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


def main():
    print("Escape from Cave Terror!")
    world.parse_world_dsl()
    player = Player()

    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)

        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("Your journey has come to an early end!")


if __name__ == '__main__':
    main()
