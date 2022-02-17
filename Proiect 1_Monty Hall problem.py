import random
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def get_non_prize_doors(host, num_doors, player_choice):
    l=[0 for i in range(num_doors)]
    nr=0
    while(nr!=num_doors-2):
        i = random.randint(0, num_doors - 1)
        if (i != host and i != player_choice and l[i]!=1):
            l[i]=1
            nr+=1

    return l


def switch(l, num_doors, player_choice):
    for i in range(0,num_doors):
        if (i != player_choice and l[i]==0):
            return i

def monty_hall_game(num_tests):
    win_switch = 0
    win_no_switch = 0
    num_doors = 3

    for i in range(0, num_tests):
        host = random.randint(0, num_doors - 1)
        first_player_choice = random.randint(0, num_doors - 1)
        shown_doors = get_non_prize_doors(host, num_doors, first_player_choice)
        player_choice = switch(shown_doors, num_doors, first_player_choice)

        if player_choice == host :
            win_switch+= 1

        if first_player_choice==host:
            win_no_switch+= 1


    return  win_switch, win_no_switch, num_tests


x = monty_hall_game(200000)
print('Win after switch %: ', x[0]/ x[2])
print('win no switch %: ', x[1]/ x[2])


num_tests = []
win_percentage = []
for i in range(1,2000):
  num_tests.append(i)
  y = monty_hall_game(i)
  win_percentage.append(y[0]/ y[2])


plt.figure(figsize=(12.2,4.5))
plt.plot( num_tests, win_percentage  )
plt.title('Monty Hall Problem')
plt.xlabel('Number of Tests',fontsize=18)
plt.ylabel('Win Percentage',fontsize=18)
plt.show()
