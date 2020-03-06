'''
hello pyhunters your mation is : 
make two functions : 
1st function : 
Caesar cipher Encode 
2nd function : 
Caesar cipher decode

مرحبا مجددًا مشروعنا الجديد ينقل بنا الى عالم التشفير 
التشفير كان احد اقدم العلوم الانسانية ويطلق عليه التعمية وهو علم تحويل المعلومات من معلومات  مقروءة الى معلومات سرية 
واستخدم منذ الأزل 

مهمتكم هو عمل دالة تقوم بالتشفير الى شيفرة قيصر ودالة اخرى تقوم بفك  شيفرة قيصر 


وتذكروا دائمًا لن تبلغوا المجد حتى تلعقوا الصبرا 
best of luck 

''''
#------------------ @start:zaid------------------------------



def nc(text,k):
  ntext=""
  for i in text:
    n=ord(i)+k
    nl=chr(n)
    ntext+=nl
  print("your encrypted text is:",ntext)
text1=str(input("insert the word you want to encrypt it here: "))
key1=int(input("insert your key here: "))
nc(text1,key1)
print('\n\n\n')
def dc(text,k):
  dtext=""
  for i in text:
    d=ord(i)-k
    dl=chr(d)
    dtext+=dl
  print("your decrypted text is:",dtext)
text2=str(input("insert the word you want to decrypt it here: "))
key2=int(input("insert your key here: "))
dc(text2,key2)




#-------------------- @end:zaid------------------------------





#------------------ @start:khalid------------------------------












#-------------------- @end:khalid------------------------------



#------------------ @start:عبدالرحمن------------------------------











#-------------------- @end:عبدالرحمن------------------------------


#------------------ @start:ممدوح------------------------------










#-------------------- @end:ممدوح------------------------------
