import telebot
from telebot import types
TOKEN='5620443990:AAH6bT7-L8ddBd4DB29xy8ScZtTWh4XoTwI'
bot=telebot.TeleBot(TOKEN)
from flask import Flask,request
secret = 'andijanchoyxonabot2305sdsd5555'
url = 'https://andjijonchoyxonabot.pythonanywhere.com/'+secret
bot.remove_webhook()
bot.set_webhook(url=url)
app = Flask(__name__)
@app.route('/',methods=['POST'])
def set_hook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok',200
############################################
contact= types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
reg_button = types.KeyboardButton(text="Telefon raqamingizni jo'nating", request_contact=True)
contact.add(reg_button)
#########################################################################################
manzil= types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,row_width=2)
manzil1 = types.KeyboardButton(text="📍Manzilingizni yuboring", request_location=True)
back=types.KeyboardButton('◀️Ortga')
manzil.add(manzil1,back)
#####################################################################################################
bekkiboy=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
bekkiboy1=types.KeyboardButton('🔔Buyurtma qilish')
bekkiboy2=types.KeyboardButton("🏃Olib ketish")
bekkiboy3=types.KeyboardButton("🔝Menu")
bekkiboy4=types.KeyboardButton("◀️Ortga")
bekkiboy.add(bekkiboy1,bekkiboy2,bekkiboy3,bekkiboy4)
#####################################################################################
bek=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
bek1=types.KeyboardButton('🔔Buyurtma qilish')
bek2=types.KeyboardButton("🏃Olib ketish")
bek3=types.KeyboardButton("🔙Orqaga")
bek.add(bek1,bek2,bek3)
#################################################################################
order=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
bir=types.KeyboardButton('🔔Buyurtma qilish')
ikki=types.KeyboardButton("🏃Olib ketish")
tort=types.KeyboardButton("🔙Ortga")
besh=types.KeyboardButton("🛒Xaridingiz")
olti=types.KeyboardButton("🗑Savatni bo'shatish")
yetti=types.KeyboardButton("💴Hisob")
sakkiz=types.KeyboardButton("🔝Menu")
order.add(bir,ikki,besh,olti,yetti,sakkiz,tort)
###############################################################################################################
payment=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
pay1=types.KeyboardButton('💶Naqd pul')
pay2=types.KeyboardButton('💳Click,Payme')
pay3=types.KeyboardButton("◀️Ortga")
payment.add(pay1,pay2,pay3)
#########################################################################################################
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = types.KeyboardButton("🛒Buyurtma berish")
btn2 = types.KeyboardButton("🏪Bizning manzillar")
btn3=types.KeyboardButton("🧑🏻‍💻Admin")
btn4=types.KeyboardButton("🛒Xaridingiz")
btn5=types.KeyboardButton("💴Hisob")
markup.add(btn1, btn2,btn3,btn4,btn5)
############################################################
menu=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
button=types.KeyboardButton('Osh')
button1=types.KeyboardButton('Jizz')
button2=types.KeyboardButton("Lag'mon")
button3=types.KeyboardButton("Sho'rva")
button4=types.KeyboardButton("Shashlik")
button5=types.KeyboardButton("Qozonkabob")
button8=types.KeyboardButton('Ichimliklar')
buttono=types.KeyboardButton("🛒Xaridingiz")
buttona=types.KeyboardButton("🗑Savatni bo'shatish")
buttonaa=types.KeyboardButton("💴Hisob")
button6=types.KeyboardButton("🔙Orqaga")
menu.add(button,button1,button2,button3,button4,button5,button8,buttono,buttona,buttonaa,button6)
##################################################################
osh =types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
osh1=types.KeyboardButton("1 kg osh")
osh2=types.KeyboardButton("0.75 kg osh")
osh3=types.KeyboardButton("0.5 kg osh")
osh4=types.KeyboardButton("1 pors osh")
osh5=types.KeyboardButton("🛒Xaridingiz")
osh6=types.KeyboardButton("🔙Ortga")
osh.add(osh1,osh2,osh3,osh4,osh5,osh6)
################################################################################
jizz =types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
jizz1=types.KeyboardButton("1 kg jizz")
jizz2=types.KeyboardButton("0.75 kg jizz")
jizz3=types.KeyboardButton("0.5 kg jizz")
jizz4=types.KeyboardButton("1 pors jizz")
jizz5=types.KeyboardButton("🛒Xaridingiz")
jizz6=types.KeyboardButton("🔙Ortga")
jizz.add(jizz1,jizz2,jizz3,jizz4,jizz5,jizz6)

#####################################################################################
lagmon =types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
lagmon1=types.KeyboardButton("Qovurma lag'mon")
lagmon2=types.KeyboardButton("Uyg'urcha lag'mon")
lagmon4=types.KeyboardButton("🛒Xaridingiz")
lagmon3=types.KeyboardButton("🔙Ortga")
lagmon.add(lagmon1,lagmon2,lagmon4,lagmon3)

####################################################################################
shorva =types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
shorva1=types.KeyboardButton("Tovuq sho'rva")
shorva2=types.KeyboardButton("No'xat sho'rva")
shorva3=types.KeyboardButton("Oddiy sho'rva")
shorva5=types.KeyboardButton("🛒Xaridingiz")
shorva4=types.KeyboardButton("🔙Ortga")
shorva.add(shorva1,shorva2,shorva3,shorva5,shorva4)

#################################################################################
shashlik =types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
shashlik1=types.KeyboardButton("1 pors shashlik")
shashlik2=types.KeyboardButton("2 pors shashlik")
shashlik3=types.KeyboardButton("Yarim pors shashlik")
shashlik5=types.KeyboardButton("🛒Xaridingiz")
shashlik4=types.KeyboardButton("🔙Ortga")
shashlik.add(shashlik1,shashlik2,shashlik3,shashlik5,shashlik4)
#########################################################################################
qozonkabob =types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
qozonkabob1=types.KeyboardButton("1 pors qozonkabob")
qozonkabob2=types.KeyboardButton("2 pors qozonkabob")
qozonkabob3=types.KeyboardButton("Yarim pors qozonkabob")
qozonkabob5=types.KeyboardButton("🛒Xaridingiz")
qozonkabob4=types.KeyboardButton("🔙Ortga")
qozonkabob.add(qozonkabob1,qozonkabob2,qozonkabob3,qozonkabob5,qozonkabob4)
######################################################################################################   
ichimlik =types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
ichimlik1=types.KeyboardButton("Coca Cola")
ichimlik2=types.KeyboardButton("Fanta")
ichimlik3=types.KeyboardButton("Sprite")
ichimlik4=types.KeyboardButton("🔙Ortga")
ichimlik.add(ichimlik1,ichimlik2,ichimlik3,ichimlik4)
######################################################################################
@bot.message_handler(commands=['start','yordam'])
def start(message):
    import sqlite3
    text=message.text
    id=message.chat.id
    connect=sqlite3.connect('delivery.db')
    cursor=connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS delivery(
               id INTEGER,
               ovqat TEXT
    
                             )
                                 """)
    chat_id=message.chat.id
    cursor.execute(f"DELETE from delivery WHERE id = {chat_id}")
    connect.commit()
    texto=f"<b>Assalomu aleykum aziz mijoz!</b>"
          
    bot.send_message(message.chat.id,texto,parse_mode='html',reply_markup=contact)
#######################################################################################################
@bot.message_handler(content_types=['contact'])
def main(message):
    a=message.text
    if a !='None':
        axborot=f"<b>🤖Men Andijon Choyxona telegram botiman</b>"
        bot.send_message(message.chat.id,axborot,parse_mode='html',reply_markup=markup)
    else:
        bot.send_message(message.chat.id,reply_markup=markup)

###################################################################################################################
@bot.message_handler(content_types=['text'])
def funksiya(message):
    import sqlite3
    text=message.text
    id=message.chat.id
    connect=sqlite3.connect('delivery.db')
    cursor=connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS delivery(
               id INTEGER,
               ovqat TEXT
    
                             )
                                 """)
    
   
    
    if text=="Fanta" or text=='bekkiboy' or text=="0.75 kg osh" or text=="1 kg osh" or text=="0.5 kg osh" or text=="1 pors osh" or text=="Yarim pors qozonkabob"  or text=="2 pors qozonkabob" or text=="1 pors qozonkabob" or text=="1 pors shashlik" or text=="2 pors shashlik" or text=="Yarim pors shashlik" or text=="Tovuq sho'rva" or text=="No'xat sho'rva" or text=="Oddiy sho'rva" or text=="Qovurma lag'mon" or text=="Uyg'urcha lag'mon" or text=="1 pors jizz" or text=="0.5 kg jizz" or text=="0.75 kg jizz" or text=="1 kg jizz" or text=='bekki' or text=="Coca Cola"  or text=="Sprite":
       
       id=message.chat.id
       ovqat=text
       users_list=[id,text]
       cursor.execute("INSERT INTO delivery VALUES(?,?);", users_list)
       connect.commit()
       matn=f"<b>Tanlov uchun rahmat!</b>"
       bot.send_message(id,matn,reply_markup=order,parse_mode='html')
    if text=='🛒Xaridingiz':
        chat_id=message.chat.id
        cursor.execute(f"SELECT ovqat from delivery WHERE id = {chat_id}")
        data=cursor.fetchall()
        database=data
        if database==[]:
            bad=f"<b>Siz hali hech narsa buyurtma qilmadingiz😔</b>"
            bot.send_message(message.chat.id,bad,parse_mode='html')
        else:
          import operator
          from functools import reduce
          datam=list(reduce(operator.concat, database))
          taomlar=''
          taomlar1=''
          ichimliklar=''
          ichimliklar1=''
          for i in datam:
             if i=='Coca Cola' or i=='Fanta' or i=="Sprite":
               ichimliklar+="✅ "+i+"\n" 
             else:
                taomlar+="✅ "+i+"\n" 
          if ichimliklar=='':
                  ichimliklar1="<b>Siz hali ichimlik buyurtma qilganiz yo'q</b>"
          else:
                   ichimliklar1=ichimliklar
          if taomlar=='':
                   taomlar1="<b>Siz hali ovqat buyurtma qilganiz yo'q</b>"
          else:
                   taomlar1=taomlar

          bekki='<b>🛒 Xaridingiz🛒</b>'
          meal='<b>🍽Taomlar🍽</b>'
          drinking='<b>🥤Ichimliklar🥤</b>'
          drink='<b>✅Bizning choyxonada aksiya ketyapti ichimliklar sizga tekinga beriladi</b>'
          informa=bekki +'\n'+'\n'+meal+"\n"+ taomlar1+'\n'+drinking+"\n"+ichimliklar1+"\n" +'\n'+ drink
          bot.send_message(message.chat.id,informa,parse_mode='html',reply_markup=bekkiboy)
    ############################################################################################################
    if text=="🗑Savatni bo'shatish":
        chat_id=message.chat.id
        cursor.execute(f"DELETE from delivery WHERE id = {chat_id}")
        connect.commit()
        savat=f"<b>Xarid savatchangiz bo'shatildi</b>\n"\
              f"<b>Tezroq narsa oling😊😊😊</b>"
        bot.send_message(message.chat.id,savat,parse_mode='html',reply_markup=menu)
    ############################################################################################################
    if text=="🔔Buyurtma qilish":
        chat_id=message.chat.id
        cursor.execute(f"SELECT ovqat from delivery WHERE id = {chat_id}")
        data=cursor.fetchall()
        database=data
        if database==[]:
            bad=f"<b>Siz hali hech narsa buyurtma qilmadingiz😔</b>"
            bot.send_message(message.chat.id,bad,parse_mode='html')
        else:
          import operator
          from functools import reduce
          datam=list(reduce(operator.concat, database))
          summa=0
          for data in datam:   
            if data=="1 kg osh":
                a=80
                summa+=a 
            if data=="0.75 kg osh":
                b=60
                summa+=b           
            if data=="0.5 kg osh":
                c=40
                summa+=c 
            if data=="1 pors osh":
                d=20
                summa+=d
            if data=="1 kg jizz":
                e=80
                summa+=e
            if data=="0.75 kg jizz":
                f=60
                summa+=f
            if data=="0.5 kg jizz":
               g=40
               summa+=g 
            if data=="1 pors jizz":
                h=20
                summa+=h
            if data=="Qovurma lag'mon":
                i=30
                summa+=i
            if data=="Uyg'urcha lag'mon":
                j=20
                summa+=j   
            if data=="Tovuq sho'rva":
                k=25
                summa+=k           
            if data=="No'xat sho'rva":
                l=20
                summa+=l
            if data=="Oddiy sho'rva":
                m=15
                summa+=m
            if data=="1 pors shashlik":
                n=58
                summa+=n
            if data=="2 pors shashlik":
                p=115
                summa+=p
            if data=="Yarim pors shashlik":
                q=30
                summa+=q
            if data=="1 pors qozonkabob":
                r=58
                summa+=r
            if datam=="2 pors qozonkabob":
                s=115
                summa+=s
            if data=="Yarim pors qozonkabob":
                t=30
                summa+=t
          texta="<b>Qilgan xarajatingiz:  </b>"+ str(summa) +"<b> ming so'm</b>"+'\n'
          tekst=f"<b>✅ Buyurtmangiz qabul qilindi mijoz</b>\n"\
                f"<b>🕔 20 minutda tayyor bo'ladi buyurtma</b>"
          texta1=texta + tekst
          bot.send_message(message.chat.id,texta1,parse_mode='html',reply_markup=manzil) 
    ################################################################################################################
    if  text=='💴Hisob':
        chat_id=message.chat.id
        cursor.execute(f"SELECT ovqat from delivery WHERE id = {chat_id}")
        data=cursor.fetchall()
        database=data
        if database==[]:
            bad=f"<b>Siz hali hech narsa buyurtma qilmadingiz😔</b>"
            bot.send_message(message.chat.id,bad,parse_mode='html')
        else:
          import operator
          from functools import reduce
          datam=list(reduce(operator.concat, database))
          summa=0
          for data in datam:   
            if data=="1 kg osh":
                a=80
                summa+=a 
            if data=="0.75 kg osh":
                b=60
                summa+=b           
            if data=="0.5 kg osh":
                c=40
                summa+=c 
            if data=="1 pors osh":
                d=20
                summa+=d
            if data=="1 kg jizz":
                e=80
                summa+=e
            if data=="0.75 kg jizz":
                f=60
                summa+=f
            if data=="0.5 kg jizz":
               g=40
               summa+=g 
            if data=="1 pors jizz":
                h=20
                summa+=h
            if data=="Qovurma lag'mon":
                i=30
                summa+=i
            if data=="Uyg'urcha lag'mon":
                j=20
                summa+=j   
            if data=="Tovuq sho'rva":
                k=25
                summa+=k           
            if data=="No'xat sho'rva":
                l=20
                summa+=l
            if data=="Oddiy sho'rva":
                m=15
                summa+=m
            if data=="1 pors shashlik":
                n=58
                summa+=n
            if data=="2 pors shashlik":
                p=115
                summa+=p
            if data=="Yarim pors shashlik":
                q=30
                summa+=q
            if data=="1 pors qozonkabob":
                r=58
                summa+=r
            if datam=="2 pors qozonkabob":
                s=115
                summa+=s
            if data=="Yarim pors qozonkabob":
                t=30
                summa+=t
          texta="<b>Qilgan xarajatingiz:  </b>"+ str(summa) +"<b> ming so'm</b>"+'\n'
          tekst=f"<b>✅ Buyurtmangiz qabul qilindi mijoz</b>\n"\
                f"<b>🕔 20 minutda tayyor bo'ladi buyurtma</b>"
          texta1=texta + tekst
          bot.send_message(message.chat.id,texta1,parse_mode='html',reply_markup=bek) 

    ################################################################################################################
    if text=="🏃Olib ketish":
        chat_id=message.chat.id
        cursor.execute(f"SELECT ovqat from delivery WHERE id = {chat_id}")
        data=cursor.fetchall()
        database=data
        if database==[]:
            bad=f"<b>Siz hali hech narsa buyurtma qilmadingiz😔</b>"
            bot.send_message(message.chat.id,bad,parse_mode='html')
        else:
          import operator
          from functools import reduce
          datam=list(reduce(operator.concat, database))
          summa=0
          for data in datam:   
            if data=="1 kg osh":
                a=80
                summa+=a 
            if data=="0.75 kg osh":
                b=60
                summa+=b           
            if data=="0.5 kg osh":
                c=40
                summa+=c 
            if data=="1 pors osh":
                d=20
                summa+=d
            if data=="1 kg jizz":
                e=80
                summa+=e
            if data=="0.75 kg jizz":
                f=60
                summa+=f
            if data=="0.5 kg jizz":
               g=40
               summa+=g 
            if data=="1 pors jizz":
                h=20
                summa+=h
            if data=="Qovurma lag'mon":
                i=30
                summa+=i
            if data=="Uyg'urcha lag'mon":
                j=20
                summa+=j   
            if data=="Tovuq sho'rva":
                k=25
                summa+=k           
            if data=="No'xat sho'rva":
                l=20
                summa+=l
            if data=="Oddiy sho'rva":
                m=15
                summa+=m
            if data=="1 pors shashlik":
                n=58
                summa+=n
            if data=="2 pors shashlik":
                p=115
                summa+=p
            if data=="Yarim pors shashlik":
                q=30
                summa+=q
            if data=="1 pors qozonkabob":
                r=58
                summa+=r
            if datam=="2 pors qozonkabob":
                s=115
                summa+=s
            if data=="Yarim pors qozonkabob":
                t=30
                summa+=t
          texta="<b>Qilgan xarajatingiz:  </b>"+ str(summa) +"<b> ming so'm</b>"+'\n'
          tekst=f"<b>✅ Buyurtmangiz qabul qilindi mijoz</b>\n"\
                f"<b>🕔 20 minutda tayyor bo'ladi buyurtma</b>"
          xabar="<b>Bizning manzil!</b>"
          texta1=texta + tekst
          lat=39.916667
          long=65.000000
          bot.send_message(message.chat.id,texta1,parse_mode='html',reply_markup=payment)
          bot.send_message(message.chat.id,xabar,parse_mode='html',reply_markup=payment)
          bot.send_location(message.chat.id,lat,long)  
    ###################################################################################################################### 
    ######################################################################################################################
    if text=="💶Naqd pul":
        tekst3=f"<b>✅Buyurtma manzilga borganga to'lov qilasiz!</b>"
              
        bot.send_message(message.chat.id,tekst3,parse_mode='html',reply_markup=menu)  
    ################################################################################################################
    if text=="💳Click,Payme":
        tekst4=f"<b>✅Bot sinov tariqasida ishlayapti!</b>"      
        bot.send_message(message.chat.id,tekst4,parse_mode='html',reply_markup=menu)
    #################################################################################################################
    if text=="◀️Ortga":
        tekst5=f"<b>◀️Ortga!</b>"      
        bot.send_message(message.chat.id,tekst5,parse_mode='html',reply_markup=order)  
    ########################################################################################
    if text=="🧑🏻‍💻Admin":
        admin=f"<b>🧑🏻‍💻 Admin: Asliddinov Behzod</b>\n"\
              f"<b>📞 Telefon : +998991160434</b>\n"\
              f"<b>💬 Telegram: @Bekhzod_Asliddinov</b>\n"\
              f"<b>🕔 Murojaat vaqti: 07:00 -23:00</b>"      
        bot.send_message(message.chat.id,admin,parse_mode='html',reply_markup=markup) 
    ############################################################################################
    if text=="🏪Bizning manzillar":
        adres=f"<b>1-Manzil: Asaka bank</b>\n"\
              f"<b>2- Manzil Turon kafesi oldi</b>\n"\
              f"<b>3-Manzil 'Hayot' mebel uyi yonida</b>"      
        bot.send_message(message.chat.id,adres,parse_mode='html',reply_markup=markup)  
    ############################################################################
    if text=='🛒Buyurtma berish':
        bot.send_message(message.chat.id,'🔝Menu',reply_markup=menu)
    ######################################################################################
    if text=='🔝Menu':
        bot.send_message(message.chat.id,'🔝Menu',reply_markup=menu)
    ##############################################################################################
    if text=='🔙Orqaga':
        tekst6=f"<b>◀️Orqaga!</b>" 
        bot.send_message(message.chat.id,tekst6,parse_mode='html',reply_markup=markup)
    ####################################################################################
    if text=='🔙Ortga':
       bot.send_message(message.chat.id,'🔝Menu',reply_markup=menu)
    #############################################################################################
    if text=='Osh':
        xabar=f"<b>Oshmisan?! Osh</b>\n" \
              f"<b>Haqiqiy Choyxona palov to'ra!!!</b>"          
        sti = open("osh.png", 'rb')  
        narxlarosh=f"<b>Eng arzon va eng shirin osh bizda</b>\n"\
                   f"<b>✅ 1 kg osh 80 ming</b>\n"\
                   f"<b>✅ 750 gramm osh 60 ming</b>\n"\
                   f"<b>✅ Yarim kg osh 40 ming</b>\n"\
                   f"<b>✅ 1 Pors osh 20 ming</b>\n"\
                   f"<b>Iltimos qancha miqdorda bo'lishini tanlang!!!</b>"
           
        bot.send_sticker(message.chat.id, sti,timeout=60)   
        bot.send_message(message.chat.id,xabar,reply_markup=osh,parse_mode='html')
        bot.send_message(message.chat.id,narxlarosh,parse_mode='html')
    ######################################################################################################
    if text=='Jizz':
        xabar=f"<b>Jizzmisan?! Jizz</b>\n" \
              f"<b>Haqiqiy O'zbek ovqati!!!</b>"        
        sti = open("jizz.png", 'rb')   
        narxlarjizz=f"<b>Eng arzon va eng shirin jizz bizda</b>\n"\
                    f"<b>✅ 1 kg jizz 80 ming</b>\n"\
                    f"<b>✅ 750 gramm jizz 60 ming</b>\n"\
                    f"<b>✅ Yarim kg jizz 40 ming</b>\n"\
                    f"<b>✅ 1 Pors jizz 20 ming</b>\n"\
                    f"<b>Iltimos qancha miqdorda bo'lishini tanlang!!!</b>"
        bot.send_sticker(message.chat.id, sti,timeout=60)   
        bot.send_message(message.chat.id,xabar,reply_markup=jizz,parse_mode='html')
        bot.send_message(message.chat.id,narxlarjizz,parse_mode='html')
    ########################################################################################################
    if text=="Lag'mon":
        xabar=f"<b>Lag'monmisan?! Lag'mon</b>\n" \
              f"<b>Haqiqiy O'zbek ovqati!!!</b>"          
        sti = open("lagmon.png", 'rb')
        narxlaruygur=f"<b>Eng arzon va eng shirin Lag'mon bizda</b>\n"\
                     f"<b>✅ Qovurma Lag'mon 30 ming</b>\n"\
                     f"<b>✅ Uyg'urcha lag'mon 20 ming</b>\n"\
                     f"<b>Iltimos qanaqa bo'lishini tanlang!!!</b>"    
        bot.send_sticker(message.chat.id, sti,timeout=60)   
        bot.send_message(message.chat.id,xabar,reply_markup=lagmon,parse_mode='html')
        bot.send_message(message.chat.id,narxlaruygur,parse_mode='html')
    #################################################################################################################
    if text=="Sho'rva":
        xabar=f"<b>Bay bay sho'rva!</b>\n" \
              f"<b>Haqiqiy O'zbek ovqati!!!</b>"
        sti = open("shorva.png",'rb')     
        bot.send_sticker(message.chat.id, sti,timeout=60)
        narxlarshorva=f"<b>Eng arzon va eng shirin sho'rva bizda</b>\n"\
                      f"<b>✅ Tovuq 25 ming</b>\n"\
                      f"<b>✅ No'xat  20 ming</b>\n"\
                      f"<b>✅ Oddiy sho'rva 15 ming</b>\n"\
                      f"<b>Iltimos turini tanlang!!!</b>"
        bot.send_message(message.chat.id,xabar,reply_markup=shorva,parse_mode='html')
        bot.send_message(message.chat.id,narxlarshorva,parse_mode='html')
    ##################################################################################################################
    if text=="Shashlik":
        xabar=f"<b>Tanlovda adashmadingiz!!!</b>\n" \
              f"<b>Haqiqiy O'zbek ovqati!!!</b>"     
        sti = open("shashlik.png",'rb')     
        bot.send_sticker(message.chat.id, sti,timeout=60)   
        narxlarshashlik=f"<b>Eng arzon va eng shirin qozonkabob bizda</b>\n"\
                        f"<b>✅ 1 Pors 58 ming</b>\n"\
                        f"<b>✅ 2 Pors 115 ming </b>\n"\
                        f"<b>✅ Yarim Pors 30 ming ming</b>\n"\
                        f"<b>Iltimos qancha miqdorda bo'lishini tanlang!!!</b>" 
        bot.send_message(message.chat.id,xabar,reply_markup=shashlik,parse_mode='html')
        bot.send_message(message.chat.id,narxlarshashlik,parse_mode='html')
    ################################################################################################################
    if text=="Qozonkabob":
        xabar=f"<b>Tanlovda adashmadingiz!!!</b>\n" \
              f"<b>Haqiqiy O'zbek ovqati!!!</b>"      
        sti = open("qozonkabob.png",'rb')     
        bot.send_sticker(message.chat.id, sti,timeout=60)  
        narxlarqozonkabob=f"<b>Eng arzon va eng shirin qozonkabob bizda</b>\n"\
                          f"<b>✅ 1 Pors 58 ming</b>\n"\
                          f"<b>✅ 2 Pors 115 ming </b>\n"\
                          f"<b>✅ Yarim Pors 30 ming ming</b>\n"\
                          f"<b>Iltimos qancha miqdorda bo'lishini tanlang!!!</b>" 
        bot.send_message(message.chat.id,xabar,reply_markup=qozonkabob,parse_mode='html')
        bot.send_message(message.chat.id,narxlarqozonkabob,parse_mode='html')
    ###############################################################################################################
    if text=="Ichimliklar":
        xabar=f"<b>Taomni salqin ichimlar bilan yeyishga nima yetibti?!</b>\n"\
              f"<b>Iltimos turini tanlang!!!</b>"
        sti = open("ichimliklar.png",'rb')  
        cola=f"<b>Taomni salqin ichimlar bilan yeyishga nima yetibti?!</b>\n"\
             f"<b>Ular sizga bonus tariqasida beriladi!!!</b>\n"\
             f"<b>Iltimos turini tanlang!!!</b>"  
        bot.send_sticker(message.chat.id, sti,timeout=60)
        bot.send_message(message.chat.id,xabar,reply_markup=ichimlik,parse_mode='html')   
        bot.send_message(message.chat.id,cola,parse_mode='html')    
@bot.message_handler(content_types=['location'])
def location(message):
    text=f"<b>✅Manzil qabul qilindi </b>\n"\
         f"<b>To'lovni qanday turda bo'lishini tanlang</b>"
         
    bot.send_message(message.chat.id,text,parse_mode='html',reply_markup=payment)
if  __name__=='__main__':
   bot.polling(none_stop=True)
