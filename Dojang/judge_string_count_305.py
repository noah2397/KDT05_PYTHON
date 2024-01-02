# 코딩도장 p.305 심사문제
msg=("the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside of the outside,"
     "and devote myself instead to geography, historym arithmetic, and grammer. That is why,  at the, age of six, I gave up what might have been a"
     "magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two."
     "Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.")
start=-1
the_count=0
while msg.find("the", start+1) != -1 :
    start=msg.find("the", start+1)
    if not start and (not 65<=ord(msg[start+len("the")]) <=90  and not 97<=ord(msg[start+len("the")]) <=122) :
        the_count+=1
    elif (not 65<=ord(msg[start+len("the")]) <=90  and not 97<=ord(msg[start+len("the")]) <=122) and (not 65<=ord(msg[start-1]) <=90  and not 97<=ord(msg[start-1]) <=122) :
        the_count += 1
print(the_count)

