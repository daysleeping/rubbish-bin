answer = ['cultural traditions','beauty trends','plump','attractive','desirable','poverty','prosperity','afford','popularity','multicultural','evolve','tattooing','expand','a fashionable trend','a sign of beauty','body piercings','status and wealth','doubtless to say','beliefs','define','in danger','preserve','landmarks','future generations','safeguard','unique','identity','historical buildings','impact','rural villages','entire','united people','symbolic','urban areas','historical importance','rituals','worship','ancestor','convenient','adapt']
user_answer = []
a = answer.copy()

print(len(answer))

def get_user():
    a = 1
    while a != len(answer) + 1:
        user_answer.append(input(f'{a} : '))
        a += 1

def check_without_order(user_answer,answer):
    a = 0
    b = 0
    correct = []
    while a != len(user_answer):
        while b != len(answer):
            if user_answer[a] == None:
                break
            if user_answer[a] == answer[b]:
                print(f'your answer {a} : {user_answer[a]} == correct answer {b} : {answer[b]}')
                correct.append(user_answer[a])
                answer.pop(b)
                break
            else:
                b += 1
        a += 1
        b = 0
    return [answer,correct]


get_user()
list = check_without_order(user_answer,answer)

print(f'Not answered : {list[0]} \nAnswered successfully : {list[1]} \nYour answer : {user_answer} \nCorrect answer : {a}')
print(f'Your score : {len(list[1])} / {len(a)}')
