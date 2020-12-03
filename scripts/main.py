import os 
import keyboard 
while True:
       try:
           if keyboard.is_pressed('-'):
                kapat = ["firefox.exe"]   
                for x in kapat:         
                    os.system('taskkill /f /im ' + x)
                    print("Uygulama kapatıldı, terminale dönülüyor!")
                break
           else:
               pass
       except:
           break