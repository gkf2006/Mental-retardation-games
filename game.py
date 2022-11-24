from random import randint
import os

if os.path.exists('game.txt'):
    print('游戏文件存在，可以运行。')
    
else:
    fp = open('game.txt','w')
    print('正在创建游戏文件...')
    fp.close()
    print('游戏文件创建完成！')


f = open('game.txt',encoding='utf-8')
name = input("请输入你的名字:")
lines = f.readlines()
f.close()
scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
    score = [0,0,0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = total_times / game_times
else:
    avg_times = 0

print('%s,你已经玩了%d次，最少%d论猜出答案，平均%.2f轮猜出答案' % (name,game_times,min_times,avg_times))


num = randint(1,100)
times = 0
print("猜猜我想的是数字几（1-100）")
bingo = False
while bingo == False:
    times += 1
    answer = int(input())
    if 0<answer<num:
        print('太小了！')
    if 100>answer>num:
        print('太大了！')
    if answer>100:
        print('呜呜呜，太大了，放不进去的!请输入1-100之间的数值！')
    if answer<1:
        print('呜呜呜，太小了！请输入1-100之间的数值！')
    if answer == 114514:
        print('臭死我了！！！')
    if answer == num:
        print('恭喜你，答对了！！！')
        bingo = True

if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1


scores[name] = [str(game_times),str(min_times),str(total_times)]
result = ''
for n in scores:
    line = n +' '+ ' '.join(scores[n]) + '\n'
    result += line

f = open('game.txt','w',encoding='utf-8')
f.write(result)
f.close()
            



