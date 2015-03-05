from random import choice, random


# Decorator function to instantiate list to sample from
def hit(hit_dict):
    hit_list = ['flat'] * hit_dict['flat'] + ['slice'] * hit_dict['slice'] + \
        ['topspin'] * hit_dict['topspin'] + \
        ['unreturnable'] * hit_dict['unreturnable']
    # This will make it so I only have to create this list once

    def specific_hitter():
        return choice(hit_list)
    return specific_hitter


def returned(ret_dict, shot):
    if random() < ret_dict[shot]:
        return True
    else:
        return False


def run_volley(server_hit, server_dict, receiver_hit, receiver_dict):
    volley = True
    serve = True
    score = ''
    while(volley):
        # first hit
        if serve:
            if returned(receiver_dict, server_hit()):
                # additional %10 chance of missing return from a serve
                if random() > .9:
                    score = 'server'
                    volley = False
                else:
                    if not (returned(server_dict, receiver_hit())):
                        score = 'receiver'
                        volley = False
            else:
                score = 'server'
                volley = False
        # regular play
        else:
            if returned(receiver_dict, server_hit()):
                if not (returned(server_dict, receiver_hit())):
                    score = 'receiver'
                    volley = False
            else:
                score = 'server'
                volley = False
        serve = False
    return score


def run_game(p1, p2, names):
    server = ()
    receiver = ()
    scores = {'p1': 0, 'p2': 0}
    scores = {names[0]: 0, names[1]: 0}
    players = {}
    # For who serves first
    if random() < .5:
        print('first serve {}'.format(names[0]))
        server = p1
        receiver = p2
        players = {'server': names[0], 'receiver': names[1]}
    else:
        print('first serve {}'.format(names[1]))
        server = p2
        receiver = p1
        players = {'server': names[1], 'receiver': names[0]}
    score_p1 = 0
    score_p2 = 0
    while(scores[names[0]] < 21 and scores[names[1]] < 21):

        # 5 serves each
        for x in range(5):

            # These return a random shot
            server_hit = hit(server[0])
            receiver_hit = hit(receiver[0])

            # dictionaries with likelihood of returning each shot
            server_dict = server[1]
            receiver_dict = receiver[1]

            # server is p1, receiver is p2
            scored = run_volley(server_hit, server_dict, receiver_hit, receiver_dict)
            print('{}:{} serving to {}:{}'.format(players['server'], scores[players['server']], players['receiver'], scores[players['receiver']]))
            scores[players[scored]] += 1
            if (scores[players[scored]] == 21):
                break
        # Switch server and receiver
        receiver, server = server, receiver
        players['server'], players['receiver'] = players['receiver'], players['server']

    if scores[names[0]] == 21:
        return 0
    else:
        return 1
    # return 1 if p1 wins and 2 if p2 wins


def main():
    # Bruce Leeds
    b_hits = {'flat': 47, 'slice': 25, 'topspin': 25, 'unreturnable': 3}
    b_rets = {'flat': .80, 'slice': .45, 'topspin': .75, 'unreturnable': 0}
    b = (b_hits, b_rets)

    # Serena Williamson
    s_hits = {'flat': 10, 'slice': 20, 'topspin': 66, 'unreturnable': 4}
    s_rets = {'flat': .65, 'slice': .50, 'topspin': .85, 'unreturnable': 0}
    s = (s_hits, s_rets)

    # Jean Claude Van Dime
    j_hits = {'flat': 70, 'slice': 10, 'topspin': 15, 'unreturnable': 5}
    j_rets = {'flat': .90, 'slice': .25, 'topspin': .85, 'unreturnable': 0}
    j = (j_hits, j_rets)

    # Natan Lailari
    n_hits = {'flat': 0, 'slice': 95, 'topspin': 0, 'unreturnable': 5}
    n_rets = {'flat': .6, 'slice': .4, 'topspin': 1, 'unreturnable': 0}
    n = (n_hits, n_rets)

    choose = {'js': (j, s), 'jb': (j, b), 'sb': (s, b), 'nj': (n, j), 'ns': (n, s), 'nb': (n, b)}

    # Competitors
    competitors = {'js': ('Jean', 'Serena'), 'jb': ('jean', 'bruce'),
                    'sb': ('serena', 'bruce'), 'ns': ('Natan', 'Serena'), 
                    'nj': ('Natan', 'Jean'), 'nb': ('Natan', 'Bruce')}
    print("'js' for Jean vs. Serena, 'jb' for Jean vs. Bruce, and 'sb' for Serena vs. Bruce")
    print("'nj' for Natan vs. Jean, 'ns' for Natan vs. Serena, 'nb' for Natan vs. Bruce:")
    c = input()

    runs = int(input("number of runs?"))
    wins = {competitors[c][0]: 0, competitors[c][1]: 0}
    for x in range(runs):
        # Run a game
        winner = run_game(choose[c][0], choose[c][1], competitors[c])
        # Increment score accordingly
        wins[competitors[c][winner]] += 1
    # Print results
    print('{}:{}, {}:{}'.format(competitors[c][0], wins[competitors[c][0]], competitors[c][1], wins[competitors[c][1]]))


if __name__ == '__main__':
    main()
