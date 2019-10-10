# coding:utf-8
import random
import itertools
c_leagu1 = ["巨人", "阪神", "広島", "ﾔｸﾙﾄ", "中日", "横浜"]
c_leagu2 = ["巨人", "阪神", "広島", "ﾔｸﾙﾄ", "中日", "横浜"]
p_leagu1 = ["ＯＢ", "西武", "ＳＢ", "千葉", "日ﾊﾑ", "楽天"]
p_leagu2 = ["ＯＢ", "西武", "ＳＢ", "千葉", "日ﾊﾑ", "楽天"]
all_teams = ["巨人", "阪神", "ﾔｸﾙﾄ", "広島", "中日", "横浜", "ＯＢ", "西武", "ＳＢ", "千葉", "日ﾊﾑ", "楽天"]

class Game(object):
    def __init__(self, name, strikes, balls, hits, b_3rd, b_2nd, b_1st, score, pi_hp):
        self.name = name
        self.strikes = strikes
        self.balls = balls
        self.hits = hits
        self.b_3rd = b_3rd
        self.b_2nd = b_2nd
        self.b_1st = b_1st
        self.score = score
        self.pi_hp = pi_hp

    # バッターの結果判定
    def hantei(self):
        self.strikes = random.randint(0, 3) # ストライク判定
        self.balls = random.randint(0, 4) # ボール判定
        self.hits = random.randint(0, 4)  # ヒット判定0:アウト 1:ヒット 2:ツーベース 3:スリーベース 4:ホームラン
        # print(" ⇨ ストライクカウント:" + str(self.strikes) + " ボールカウント:" + str(self.balls) + " ヒット判定:" + str(self.hits))

    # ピッチャーが5点取られた時の交代
    def pitcher(self):
        if self.pi_hp <= 0:
            # print("ピッチャー交代!")
            self.pi_hp = 5

    # 全7通りの残塁のシチュエーション
    def zanrui(self):
        # print("ランナー", end="")
        # print("満塁" if self.b_3rd == True and self.b_2nd == True and self.b_1st == True else
        #         "3塁2塁" if self.b_3rd == True and self.b_2nd == True and self.b_1st == False else
        #         "3塁1塁" if self.b_3rd == True and self.b_2nd == False and self.b_1st == True else
        #         "2塁1塁" if self.b_3rd == False and self.b_2nd == True and self.b_1st == True else
        #         "3塁" if self.b_3rd == True else
        #         "2塁" if self.b_2nd == True else
        #         "1塁" if self.b_1st == True else
        #         "なし")
        if self.b_3rd == True and self.b_2nd == True and self.b_1st == True:
            pass
            # print("満塁")
        elif self.b_3rd == False and self.b_2nd == False and self.b_1st == False:
            pass
            # print("なし")
        else:
            if self.b_3rd == True:
                pass
                 # print("3塁", end = "")
            if self.b_2nd == True:
                pass
                  # print("2塁", end = "")
            if self.b_1st == True:
                pass
                  # print("1塁", end = "")

    # メソッド5⇨攻撃時の関数
    def kougeki(self):
        self.b_3rd = False #1塁
        self.b_2nd = False #2塁
        self.b_1st = False #3塁
        out_cnt = 0
        while out_cnt < 3:
            self.hantei() # 同じクラスの中の他のメソッドを使うときは、self.で呼び出せる
            if self.strikes < 3 and self.balls < 4 and self.hits == 1:
                # print("シングルヒット!", end = "")
                if self.b_3rd == True:
                    self.score += 1
                    self.pi_hp -= 1
                    # print("得点!", end="")
                    self.b_3rd = False
                if self.b_2nd == True:
                    self.b_3rd = True
                    self.b_2nd = False
                if self.b_1st == True:
                    self.b_2nd = True
                    self.b_1st = False
                self.b_1st = True

            elif self.strikes < 3 and self.balls < 4 and self.hits == 2:
                # print("ツーベースヒット!", end="")
                if self.b_3rd == True :
                   self.score += 1
                   self.pi_hp -=1
                if self.b_2nd == True :
                   self.score += 1
                   self.pi_hp -=1
                if self.b_2nd == True or self.b_3rd == True:
                    pass
                    # print("得点!")
                self.b_2nd = True
                self.b_1st = False

            elif self.strikes < 3 and self.balls < 4 and self.hits == 3:
                # print("スリーベースヒット!", end = "")
                if self.b_3rd == True :
                   self.score += 1
                   self.pi_hp -=1
                if self.b_2nd == True :
                   self.score += 1
                   self.pi_hp -=1
                if self.b_1st == True :
                   self.score += 1
                   self.pi_hp -=1
                if self.b_1st == True or self.b_2nd == True or self.b_3rd == True:
                    pass
                   # print("得点!")
                self.b_3rd = True
                self.b_2nd = False
                self.b_1st = False

            elif self.strikes < 3 and self.balls < 4 and self.hits == 4:
                # print("ホームラン!得点!", end="")
                if self.b_3rd == True:
                   self.score += 1
                   self.pi_hp -= 1
                if self.b_2nd == True:
                   self.score += 1
                   self.pi_hp -= 1
                if self.b_1st == True:
                   self.score += 1
                   self.pi_hp -= 1

                self.b_3rd = False
                self.b_2nd = False
                self.b_1st = False
                self.score += 1
                self.pi_hp -= 1

            elif self.strikes < 3 and self.balls == 4: #フォアボール
                # print("フォアボール!", end="")
                if self.b_3rd == True:
                    if self.b_2nd == True:
                        if self.b_1st == True:
                            # print("押し出し!得点!", end="")
                            self.score += 1
                            self.pi_hp -= 1
                            self.b_2nd = True
                    elif self.b_2nd == False:
                        if self.b_1st == True:
                            self.b_2nd = True
                elif self.b_3rd == False:
                    if self.b_2nd == True:
                        if self.b_1st == True:
                            self.b_3rd = True
                    elif self.b_2nd == False:
                        if self.b_1st == True:
                            self.b_2nd = True
                self.b_1st = True

            elif self.strikes == 3 and self.balls < 4: #三振
                out_cnt += 1
                # print("バッターアウト:" + str(out_cnt) + "アウト ", end="" )

            else:  # strikes==3以外でのバッターアウトのケース（hits==0:ゴロ、フライ）
                out_cnt += 1
                # print("バッターアウト:" + str(out_cnt) +"アウト ", end="" )

            # player.pitcher()
            # player.zanrui()
            self.pitcher()
            self.zanrui()

        # print("チェンジ")
        return self.score

def game_result(leagu1, leagu2, dic_win, dic_lose, dic_draw):
    for senkou, koukou in itertools.product(leagu1, leagu2):
        if senkou != koukou:
            pass
            # print(senkou, koukou)
            for i in range(1, 14):
                player1 = False #away
                player2 = False #home
                # print("プレイボール!")
                player1_score = 0
                player2_score = 0
                player1_hp = 5
                player2_hp = 5

                inning = 1

                while inning < 13:
                    # print(str(inning) + "回表" + senkou + "の攻撃 スコア:" + senkou + str(player1_score) + "-" + koukou + str(player2_score))
                    player = Game("senkou", 0, 0, 0, False, False, False, 0, player1_hp) # strikes, balls, hits, b_3rd, b_2nd, b_1st, score, pi_hp
                    player1_score += player.kougeki()
                    player1_hp = player.pi_hp

                    if inning > 8 and player2_score > player1_score:   # 9回以降の条件分岐
                        # print(str(inning)+"回の裏はコールドのため実施せず。)
                        print("試合終了!" + senkou + ":" + str(player1_score) + "-" + koukou + ":" + str(player2_score) + " で" + koukou + "の勝利")
                        # 勝ちはTrue
                        player1 = False
                        player2 = True
                        break
                    # print(str(inning) + "回裏" + koukou + "の攻撃 スコア:" + senkou + str(player1_score) + "-" + koukou + str(player2_score))
                    player = Game("koukou", 0, 0, 0, False, False, False, 0, player2_hp) # strikes, balls, hits, b_3rd, b_2nd, b_1st,score, pi_hp
                    player2_score += player.kougeki()
                    player2_hp = player.pi_hp

                    if inning > 8 and player2_score > player1_score:
                        print("試合終了!" + senkou + ":" + str(player1_score) + "-" + koukou + ":" + str(player2_score) + " で" + koukou + "の勝利")
                        # 勝ちはTrue
                        player1 = False
                        player2 = True
                        break
                    elif inning > 8 and  player2_score < player1_score:
                        print("試合終了!" + senkou + ":" + str(player1_score) + "-" + koukou + ":" + str(player2_score) + " で" + senkou + "の勝利")
                        # 勝ちはTrue
                        player1 = True
                        player2 = False
                        break
                    elif inning == 12 and player1_score == player2_score:
                        print("試合終了!" + senkou + ":" + str(player1_score) + "-" + koukou + ":" + str(player2_score) + " で引き分け!")
                        # 引き分けは両方False
                        player1 = False
                        player2 = False
                        break
                    inning += 1
                # 試合後の、勝ち、負け、引き分けの割り振り
                for i in leagu1:
                    if senkou == i and player1 == True : # 先行の勝ち
                        dic_win[senkou] += 1
                        dic_lose[koukou] += 1
                    if koukou == i and player2 == True: # 後攻の勝ち
                        dic_win[koukou] += 1
                        dic_lose[senkou] += 1
                    if player1 == player2 == False: # 引き分け
                        dic_draw[senkou] += 1
                        dic_draw[koukou] += 1
    print("ペナントレース終了!")

# セリーグ辞書型
dic_win_cl = {"巨人":0, "中日":0, "阪神":0, "広島":0, "ﾔｸﾙﾄ":0, "横浜":0} # 勝利数
dic_lose_cl = {"巨人":0, "中日":0, "阪神":0, "広島":0, "ﾔｸﾙﾄ":0, "横浜":0} # 負け数
dic_draw_cl = {"巨人":0, "中日":0, "阪神":0, "広島":0, "ﾔｸﾙﾄ":0, "横浜":0} # 引き分け数
game_result(c_leagu1, c_leagu2, dic_win_cl, dic_lose_cl, dic_draw_cl) # セリーグペナント
# パリーグ辞書型
dic_win_pl = {"ＯＢ":0, "西武":0, "ＳＢ":0, "千葉":0, "日ﾊﾑ":0, "楽天":0} # 勝利数
dic_lose_pl = {"ＯＢ":0, "西武":0, "ＳＢ":0, "千葉":0, "日ﾊﾑ":0, "楽天":0} # 負け数
dic_draw_pl = {"ＯＢ":0, "西武":0, "ＳＢ":0, "千葉":0, "日ﾊﾑ":0, "楽天":0} # 引き分け数
game_result(p_leagu1, p_leagu2, dic_win_pl, dic_lose_pl, dic_draw_pl) # パリーグペナント
# 交流戦
dic_win_k = {"巨人":0, "中日":0, "阪神":0, "広島":0, "ﾔｸﾙﾄ":0, "横浜":0, "ＯＢ":0, "西武":0, "ＳＢ":0, "千葉":0, "日ﾊﾑ":0, "楽天":0} # 勝利数
dic_lose_k = {"巨人":0, "中日":0, "阪神":0, "広島":0, "ﾔｸﾙﾄ":0, "横浜":0, "ＯＢ":0, "西武":0, "ＳＢ":0, "千葉":0, "日ﾊﾑ":0, "楽天":0} # 負け数
dic_draw_k = {"巨人":0, "中日":0, "阪神":0, "広島":0, "ﾔｸﾙﾄ":0, "横浜":0, "ＯＢ":0, "西武":0, "ＳＢ":0, "千葉":0, "日ﾊﾑ":0, "楽天":0} # 引き分け数

for senkou, koukou in itertools.product(c_leagu1, p_leagu1):
    # if senkou != koukou:
    #     pass
        # print(senkou, koukou)
        for i in range(1, 4):
#####################試合########################################
            player1 = False # away
            player2 = False # home
            # print("プレイボール!")
            player1_score = 0
            player2_score = 0
            player1_hp = 5
            player2_hp = 5

            inning = 1
            while inning < 13:
                # print(str(inning) + "回表" + senkou + "の攻撃 スコア:" + senkou + str(player1_score) + "-" + koukou + str(player2_score))
                player = Game("senkou", 0, 0, 0, False, False, False, 0, player1_hp) # strikes,balls,hits,b_3rd,b_2nd,b_1st,score,pi_hp
                player1_score += player.kougeki()
                player1_hp = player.pi_hp

                if inning > 8 and player2_score > player1_score:   # 9回以降の条件分岐
                    # print(str(inning) + "回の裏はコールドのため実施せず。)
                    print("試合終了!" + senkou + ":" + str(player1_score) + "-" + koukou + ":" + str(player2_score) + " で" + koukou + "の勝利")
                    # 勝ちはTrue
                    player1 = False
                    player2 = True
                    break

                # print(str(inning) + "回裏" + koukou+"の攻撃 スコア:" + senkou + str(player1_score) + "-" + koukou + str(player2_score))
                player = Game("koukou", 0, 0, 0, False, False, False, 0, player2_hp) #strikes, balls, hits, b_3rd, b_2nd, b_1st, score, pi_hp
                player2_score += player.kougeki()
                player2_hp = player.pi_hp

                if inning > 8 and player2_score > player1_score:
                    print("試合終了!" + senkou + ":" + str(player1_score) + "-" + koukou + ":" + str(player2_score) + " で" + koukou + "の勝利")
                    # 勝ちはTrue
                    player1 = False
                    player2 = True
                    break
                elif inning > 8 and  player2_score < player1_score:
                    print("試合終了!" + senkou + ":" + str(player1_score) + "-" + koukou + ":" + str(player2_score) + " で" + senkou + "の勝利")
                    # 勝ちはTrue
                    player1 = True
                    player2 = False
                    break
                elif inning == 12 and player1_score == player2_score:
                    print("試合終了!" + senkou + ":" + str(player1_score) + "-" + koukou + ":" + str(player2_score) + " で引き分け!")
                    # 引き分けは両方False
                    player1 = False
                    player2 = False
                    break
                inning += 1

            # 交流戦 パリーグをリストから取り出す
            for i in p_leagu1:
                if senkou == i and player1 == True : # 先行の勝ち
                    dic_win_pl[senkou] += 1
                    dic_win_k[senkou] += 1
                    dic_lose_cl[koukou] += 1
                    dic_lose_k[koukou] += 1
                if koukou == i and player2 == True: # 後攻の勝ち
                    dic_win_pl[koukou] += 1
                    dic_win_k[koukou] += 1
                    dic_lose_cl[senkou] += 1
                    dic_lose_k[senkou] += 1
                if senkou == i and player1 == player2 == False: # 引き分け
                    dic_draw_pl[senkou] += 1
                    dic_draw_k[koukou] += 1

            # 交流戦 セリーグをリストから取り出す
            for i in c_leagu1:
                if senkou == i and player1 == True : # 先行の勝ち
                    dic_win_cl[senkou] += 1
                    dic_win_k[senkou] += 1
                    dic_lose_pl[koukou] += 1
                    dic_lose_k[koukou] += 1
                if koukou == i and player2 == True: # 後攻の勝ち
                    dic_win_pl[koukou] += 1
                    dic_win_k[koukou] += 1
                    dic_lose_cl[senkou] += 1
                    dic_lose_k[senkou] += 1
                if senkou == i and player1 == player2 == False: # 引き分け
                    dic_draw_cl[senkou] += 1
                    dic_draw_k[koukou] += 1
print("交流戦終了!")

dic_win_rate_cl = {} # セリーグ
dic_win_rate_pl = {} # パリーグ
dic_win_rate_k = {} # 交流戦
def win_r(dic_win_rate, leagu,dic_win, dic_lose):
    for k in leagu:
        dic_win_rate.setdefault(k,round(dic_win[k] / (dic_win[k]+dic_lose[k]), 2)) # 勝率の計算式 win/(win+lose)
    return dic_win_rate
dic_wain_rate_cl = win_r(dic_win_rate_cl, c_leagu1, dic_win_cl, dic_lose_cl)
dic_wain_rate_pl = win_r(dic_win_rate_pl, p_leagu1, dic_win_pl, dic_lose_pl)
dic_wain_rate_k = win_r(dic_win_rate_k, all_teams, dic_win_k, dic_lose_k)

dic_game_dif_cl = {} # セリーグ
dic_game_dif_pl = {} # パリーグ
dic_game_dif_k = {} # 交流戦
def getgamedif(dic_game_dif, leagu, dic_win, dic_lose): # ゲーム差, リーグ, 勝ち数, 負け数
    for k in leagu:
        # ゲーム差 = (上位チームの勝利数 - 上位チームの敗戦数) - (下位チームの勝利数 - 下位チームの敗戦数) ) / 2
        dic_game_dif.setdefault(k, (max(dic_win.values()) - min(dic_lose.values()) - (dic_win[k]-dic_lose[k])) / 2)
    return dic_game_dif

dic_game_dif_cl = getgamedif(dic_game_dif_cl, c_leagu1, dic_win_cl, dic_lose_cl)
dic_game_dif_pl = getgamedif(dic_game_dif_pl, p_leagu1, dic_win_pl, dic_lose_pl)
dic_game_dif_k = getgamedif(dic_game_dif_k, all_teams, dic_win_k, dic_lose_k)

list_cl = [] # セリーグリスト化リストに複数の要素を追加する場合はappendではなく、extend
list_pl = []
list_k = []
def get_list_all(list, leagu, dic_win, dic_lose, dic_draw, dic_win_rate, dic_game_dif):
    for i in leagu:
        # リーグの 名前、勝ち数、負け数、引き分け数、勝率のリスト化
        list.extend([[i, dic_win[i], dic_lose[i], dic_draw[i], dic_win_rate[i], dic_game_dif[i]]])
    return list
list_cl = get_list_all(list_cl, c_leagu1, dic_win_cl, dic_lose_cl, dic_draw_cl, dic_win_rate_cl, dic_game_dif_cl)
list_pl = get_list_all(list_pl, p_leagu1, dic_win_pl, dic_lose_pl, dic_draw_pl, dic_win_rate_pl, dic_game_dif_pl)
list_k = get_list_all(list_k, all_teams, dic_win_k, dic_lose_k, dic_draw_k, dic_win_rate_k, dic_game_dif_k)

final_result = [list_cl, list_pl, list_k] # セリーグ、パリーグ、交流戦のリスト
for i in final_result:
    if i == list_cl:
        print("セリーグ順位表")
    elif i == list_pl:
        print("パリーグ順位表")
    else :
        print("交流戦順位表")
    rank = lambda val: val[4] # 勝率の降順
    i.sort(key=rank, reverse=True) # 降順にソートしたい場合は引数reverseをTrueとする
    print("  TEAM  ", "勝", " 負", " 引", " 率", "   差")
    for k in i :
        print(k)
    if i[0][4] == i[1][4]:
        print("勝率が同じ!勝ち数が多い方が優勝!")
        rank_1 = lambda val: val[1] # 勝ち数での降順
        i.sort(key=rank_1, reverse=True) # 降順にソートしたい場合は引数reverseをTrueとする
        for j in i:
            print(j)
        if i[0][1] == i[1][1]:
            print("勝率も勝ち数も同じ。優勝決定戦!優勝決定戦はくじ引きです。")
            result = random.randint(0,1)
            print(result)
            if result == 0:
                print("優勝は" + str(i[0][0]))
            else :
                print("優勝は" + str(i[1][0]))
