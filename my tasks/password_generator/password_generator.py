import random
usual_sim = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
special_sim = '!@#$%^&*/.'
str = ""
pas = ""
long_pass = int(input("enter password length"))
need_special_sim = int(input("1 : yes, 0 : no"))
for i in range(0, long_pass):
    if need_special_sim == 1 and i % 2 == 0:
        str = random.choice(special_sim)
        pas += str
    else:
        str = random.choice(usual_sim)
        pas += str
print(pas)

