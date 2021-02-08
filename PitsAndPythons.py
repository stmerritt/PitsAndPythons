#Empty shell for initial development
import math

error_msg_sm = [0,'']
num_ctype = 4   # 0 = Fighter, 1 = Wizard, 2 = Cleric, 3 = Rogue
num_rtype = 2   # 0 = Human, 1 = Elf
num_cstats = 7  #     Class, Str, Con, Dex, Int, Wis, Cha
class_types =   [['FIGHTER',  15,  14,  13,   8,  12,  10],
                 ['WIZARD' ,   8,  10,  14,  15,  13,  12],
                 ['CLERIC' ,  12,  13,   8,  10,  15,  14],
                 ['ROGUE'  ,  10,  12,  15,  14,   8,  13]]
#--------------------------------------------------------
race_types =    [['HUMAN'  ,   1,   1,   1,   1,   1,   1],
                 ['ELF'    ,   0,   0,   2,   1,   0,   0]]
#--------------------------------------------------------
enemy_types =   [['GOBLIN' ,  10,  12,  14,   8,   8,   8],
                 ['POOF'   ,  14,  14,  14,  14,  14,  14]]
#--------------------------------------------------------
active_PCs = []

def pits_and_pythons(finput):
    # Code to change
    return finput
    
def get_classes():
    char_classes = []
    for i in range(num_ctype):
        char_classes.append(class_types[i][0])
    return char_classes
    
def get_races():
    char_races = []
    for i in range(num_rtype):
        char_races.append(race_types[i][0])
    return char_races
    
def start_encounter():
    cur_enemy_list = gen_enemies(0,1)
    battle_list = gen_battle_stats(cur_enemy_list, active_PCs)
    print(battle_list)
    
def gen_battle_stats(cur_enemy_list, cur_PC_list):
    battle_list = []
    # ordered list with designation, list type (enemy or PC), list index, initiative, AC, health, consciousness/capacity
    for i in range(len(cur_enemy_list)):
        initiative = roll_die(20) + get_mod(cur_enemy_list[i][3])   # 3 == Dex
        ac = 10 + get_mod(cur_enemy_list[i][3])                     # 3 == Dex
        health = 10 + get_mod(cur_enemy_list[i][2])                 # 2 == Con
        #print(cur_enemy_list[i][2])
        battle_list.append([cur_enemy_list[i][0], 0, i, initiative, ac, health, 1])
    for n in range(len(cur_PC_list)):
        initiative = roll_die(20) + get_mod(cur_PC_list[n][5])   # 3 == Dex
        ac = 10 + get_mod(cur_PC_list[n][5])                     # 3 == Dex
        health = 20 + get_mod(cur_PC_list[n][4])                 # 2 == Con
        #print(cur_PC_list[n][2])
        battle_list.append([cur_PC_list[n][0], 1, n, initiative, ac, health, 1])
    # sort by initiative, then return
    return battle_list
    
def get_mod(raw_stat):
    mod = int(math.floor((raw_stat-10)/2))
    return mod

def gen_enemies(etype,cnt):
    gen_enemy_list = []
    for i in range(cnt):
        enemy = gen_enemy(etype)
        enemy[0] = enemy[0] + str(i)
        gen_enemy_list.append(enemy)
    return gen_enemy_list
        
def gen_enemy(etype):
    gen_enemy = enemy_types[etype]
    return gen_enemy
    
def create_character():
    char_races = get_races()
    char_classes = get_classes()
    print('Character name?: ')
    name = input()
    print('Character race?: ')
    race_sel = select_option(char_races)
    print('Character class?: ')
    class_sel = select_option(char_classes)
    if error_msg_sm[0] == 0:
        new_char_stats = [name]
        new_char_stats.append(char_races[race_sel])
        new_char_stats.append(char_classes[class_sel])
        for i in range(1,num_cstats):
            new_char_stats.append(class_types[class_sel][i] + race_types[race_sel][i])
        active_PCs.append(new_char_stats)
        print('New character added: ' + get_char_stats_str(len(active_PCs)-1) + '!')
        
def get_char_stats_str(i):
    char_stats_str = 'Name: {0}, Race: {1}, Class: {2}, Str: {3}, Con: {4}, Dex: {5}, Int: {6}, Wis: {7}, Cha: {8}'
    char_stats_str = char_stats_str.format(active_PCs[i][0],active_PCs[i][1],active_PCs[i][2],active_PCs[i][3],active_PCs[i][4],active_PCs[i][5],
                                active_PCs[i][6],active_PCs[i][7],active_PCs[i][8])
    return char_stats_str
    
def print_party_stats():
    print('Active party:')
    for i in range(len(active_PCs)):
        print(get_char_stats_str(i))
    print('')

def roll_advantage(adv):
    if adv == true:
        return max(roll_die(20),roll_die(20))
    else:
        return min(roll_die(20),roll_die(20))

def roll_dice(num, size):
    total = 0
    for n in num:
        total += roll_die(size)
    return total

def roll_die(size):
    # For now, return max, random number added later
    # In the future, it'll be range from 1 to size, needs to be equal chance of each possibility
    return size
    
def select_option(options):
    valid = 0
    timeout = 0
    selection = 0
    valid_options = str(options[0])
    if len(options) > 1:
        for i in range(1,len(options)):
            valid_options = valid_options + ', ' + str(options[i])
    while (valid == 0 and timeout < 3):
        print('(Valid options: ' + valid_options + ')')
        str_selection = input()
        str_selection = str_selection.upper()
        for i in range(len(options)):
            if str_selection == options[i]:
                valid = 1
                selection = i
        if valid == 0:
            timeout += 1
            print('Invalid selection')
        elif timeout >= 3:
            print('Timed out')
            error_msg_sm = [1, 'Timed out']
    print('')
    return selection
    
def get_menu_options():
    return ['CREATE','START','EXIT']

# Debugging function
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(prefix + ' got: ' + repr(got) + ' expected: ' + repr(expected))


# Calls sample_code
def main():
    state_option = 0
    print('Welcome to Pits_and_Pythons!')
    
    while state_option != 2:
        if len(active_PCs) <= 0:
            print('You have no active party members.')
        else:
            print_party_stats()
        
        print('What would you like to do?')
        state_option = select_option(get_menu_options())
        if state_option == 0:
            create_character()
        elif state_option == 1:
            if len(active_PCs) <= 0:
                print('You cannot start a mission without a party!')
            else:
                start_encounter()
        else:
            print('Thanks for playing!')
    
    print(active_PCs)
    print(roll_die(10))
    test(pits_and_pythons('testing'), 'testing')
    test(pits_and_pythons('testing'), 'tested')
  
# Default main
if __name__ == '__main__':
    main()
