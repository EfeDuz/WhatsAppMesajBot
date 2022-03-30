import pywhatkit as kit

try :
  kit.sendwhatmsg("+905432199668", "Bu Mesaj Efe Tarafından Gönderilmemiştir", 21,6)
except :
 print("Hata Oluştu")
finally :
 print("A")