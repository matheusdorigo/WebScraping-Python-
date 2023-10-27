
import time
from email.mime import audio
from winsound import PlaySound

from playsound import playsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from winotify import Notification, audio

options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
##options.add_argument('headless')
options.add_argument("window-size=300,300")


 # Configura o driver do Edge
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=options)
# Abre a URL
url = "https://tickets.sinch.com/projects/APPS/queues/custom/19"  # Substitua por sua URL
driver.get(url)
time.sleep(3)
## Acessar a pagina inicial e clicar em "Sinch Employees"
acessar = driver.find_elements(By.XPATH, '/html/body/div/div/section/div/div/section/div/p[1]/a')
for i in acessar:
    print("\n")
    print("Acessando... "+i.text)
    print("\n")
    i.click()
time.sleep(10)
print("Lendo os valores... \n")

print("Iniciando consulta... \n")
print("\n")
# Acessar fila pelo elemento e exibir valor 
print("Lista das filas monitoradas:\n")
elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[43]/a/aui-badge')
for e in elements:
    if int(e.text) != 0:
        ##print("***** Ticket Aberto ***** em [24x7] - On going: "+e.text+"\n")
        toast = Notification(app_id="[24x7] - On going",title="Atenção",msg="[24x7] - On going: "+e.text,duration="long")
        toast.set_audio(audio.Mail, loop=True)
        toast.add_actions(label="Acessar fila",launch="https://tickets.sinch.com/projects/APPS/queues/custom/2443")
        toast.show()
else:
       print("[24x7] - On going: "+e.text+"\n")
element4 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[42]/a/aui-badge')
for t in element4:   
  if int(t.text) != 0:
    toast3 = Notification(app_id="[24x7] News - Triagem",title="Atenção",msg="[24x7] News - Triagem: "+t.text,duration="long")
    toast3.set_audio(audio.Mail, loop=True)
    toast3.add_actions(label="Acessar fila",launch="https://tickets.sinch.com/projects/APPS/queues/custom/2442")
    toast3.show()
else: 
       print("[24x7] News - Triagem: "+t.text+"\n")
element1 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[36]/a/aui-badge')
for m in element1:
    if int(m.text) != 0:
        ##print("*** Ticket aberto *** em [Enter] News - Triagem: "+m.text+"\n")
     toast4 = Notification(app_id="[Enter] News - Triagem",title="Atenção",msg="[Enter] News - Triagem: "+t.text,duration="long") 
     toast4.set_audio(audio.Mail, loop=True)
     toast4.add_actions(label="Acessar fila",launch="https://tickets.sinch.com/projects/APPS/queues/custom/2209")
     toast4.show()
else:
        print("[Enter] News - Triagem: "+m.text+"\n")
element2 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[20]/a/aui-badge')


for n in element2:
    if int (n.text) != 0:
        ##print("***** Ticket aberto ***** em [Apps] News - Screening: "+n.text+"\n")
         toast5 = Notification(app_id="[Apps] News - Screening",title="Atenção",msg="[Apps] News - Screening: "+n.text,duration="long")
         toast5.set_audio(audio.Mail, loop=True)
         toast5.add_actions(label="Acessar fila",launch="https://tickets.sinch.com/projects/APPS/queues/custom/2208")
         toast5.show()
else:
    print("[Apps] News - Screening: "+n.text+"\n")
    element3 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[2]/a/aui-badge')
for u in element3:
    if int (u.text) != 2:
      toast1 = Notification(app_id="Uncategorized News - Triagem",title="Atenção",msg="Uncategorized News - Triagem: "+u.text,duration="long")
      toast1.set_audio(audio.Mail, loop=True)
      toast1.add_actions(label="Acessar fila",launch="https://tickets.sinch.com/projects/APPS/queues/custom/18")
      toast1.show()
else:
     print("Uncategorized News - Triagem: "+u.text+"\n")
element5 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[4]/a/aui-badge')
for t in element5:
    if int(t.text) != 5:
      toast2 = Notification(app_id="Abastible_apps",title="Atenção",msg="Abastible_apps: "+t.text,duration="long")
      toast2.set_audio(audio.Mail, loop=True)
      toast2.add_actions(label="Acessar fila",launch="https://tickets.sinch.com/projects/APPS/queues/custom/2286")
      toast2.show()
else:
          print("Abastible_apps: "+t.text+"\n") 

          print(" *** Encerrando consulta *** \n")
           


