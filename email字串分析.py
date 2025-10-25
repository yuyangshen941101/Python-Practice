#類似篩選
email = "yc54806@gmail.com"
index = email.index("@")
# print(email[0:index])

#不想包含@ 可直接+1跳過
print(email[index+1:])