from random import choice

def choose_a_door(doors):
    return choice(doors)

def door_with(doors, prize):
    for d in doors:
        if d['prize'] == prize:
            return d

def run_game(keep = False):
    doors = [{"door": 1, "prize": 'goat'},
            {"door": 2, "prize":'car'},
            {"door": 3, "prize":'goat'}]

    choosed_d = choose_a_door(doors)

    doors.remove(choosed_d)
    door_with_goat = door_with(doors, 'goat')
    doors.remove(door_with_goat)

    if not(keep):
        choosed_d = doors[0]

    if choosed_d['prize'] == 'car':
        return True
    else:
        return False

def main():
    keep_win = 0.0;
    keep_los = 0.0;

    nkeep_win = 0.0;
    nkeep_los = 0.0;

    num_rounds = 100000;

    for i in range(0,num_rounds):
        if run_game(True):
            keep_win += 1
        else:
            keep_los += 1

        if run_game(False):
            nkeep_win += 1
        else:
            nkeep_los += 1
    keep_win /= num_rounds
    keep_los /= num_rounds
    nkeep_win /= num_rounds
    nkeep_los /= num_rounds

    print("Cenario: Sempre manter a porta escolhida")
    print("probabilidade de vencer: {}".format(keep_win))
    print("probabilidade de perder: {}".format(keep_los))
    print("\nCenario: Sempre mudar a porta escolhida")
    print("probabilidade de vencer: {}".format(nkeep_win))
    print("probabilidade de perder: {}".format(nkeep_los))
main()
