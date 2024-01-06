#27번

msg="Merry Christmas HaPPy New YEaR"
msg2="".join([i.lower() if i.isupper() else i.upper() for i in msg ])
print(msg2)