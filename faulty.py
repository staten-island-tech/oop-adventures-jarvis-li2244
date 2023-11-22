class turn():
    def player_turn():
        print("Options")
    def enemy_turn():
        egg = 1
    def equal_rate():
        while enemy_alive == False or player_alive == False:
            if turnvara == "player":
                turn.player_turn()
                health_check()
                turn.enemy_turn()
                health_check()
            elif turnvara == "enemy":
                turn.enemy_turn()
                health_check()
                turn.player_turn()
                health_check()

class Enemy_stats():
    class attack():
        def crit_check():
            if crit == True:
                Enemy_stats.attack.crit()
        def crit():
            print(edamage * ecrit)
    class atkspd():
        def roa():
            if eatkspd == atkspd:
                turnvara = "player"
            if eatkspd < atkspd:
                turnvara = "enemy"
            turn.equal_rate()
class health_check():
    if health == 0:
        enemy_alive == False
    if ehealth == 0:
        enemy_alive == True 