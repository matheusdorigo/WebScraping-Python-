
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
url = "URL"  # Substitua por sua URL
driver.get(url)
time.sleep(3)
## Acessar a pagina inicial e clicar em "HREF"
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
        ##print("***** Ticket Aberto ***** em TEXTO - On going: "+e.text+"\n")
        toast = Notification(app_id="TEXTO - On going",title="Atenção",msg="TEXTO - On going: "+e.text,duration="long")
        toast.set_audio(audio.Mail, loop=True)
        toast.add_actions(label="Acessar fila",launch="TEXTOqueues/custom/2443")
        toast.show()
else:
       print("TEXTO - On going: "+e.text+"\n")
element4 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[42]/a/aui-badge')
for t in element4:   
  if int(t.text) != 0:
    toast3 = Notification(app_id="TEXTO TEXTO - Triagem",title="Atenção",msg="TEXTO TEXTO - Triagem: "+t.text,duration="long")
    toast3.set_audio(audio.Mail, loop=True)
    toast3.add_actions(label="Acessar fila",launch="TEXTOqueues/custom/2442")
    toast3.show()
else: 
       print("TEXTO TEXTO - Triagem: "+t.text+"\n")
element1 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[36]/a/aui-badge')
for m in element1:
    if int(m.text) != 0:
        ##print("*** Ticket aberto *** em [Enter] TEXTO - Triagem: "+m.text+"\n")
     toast4 = Notification(app_id="[Enter] TEXTO - Triagem",title="Atenção",msg="[Enter] TEXTO - Triagem: "+t.text,duration="long") 
     toast4.set_audio(audio.Mail, loop=True)
     toast4.add_actions(label="Acessar fila",launch="TEXTOqueues/custom/2209")
     toast4.show()
else:
        print("[Enter] TEXTO - Triagem: "+m.text+"\n")
element2 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[20]/a/aui-badge')


for n in element2:
    if int (n.text) != 0:
        ##print("***** Ticket aberto ***** em [Apps] TEXTO - TEXTO: "+n.text+"\n")
         toast5 = Notification(app_id="[Apps] TEXTO - TEXTO",title="Atenção",msg="[Apps] TEXTO - TEXTO: "+n.text,duration="long")
         toast5.set_audio(audio.Mail, loop=True)
         toast5.add_actions(label="Acessar fila",launch="TEXTOqueues/custom/2208")
         toast5.show()
else:
    print("[Apps] TEXTO - TEXTO: "+n.text+"\n")
    element3 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[2]/a/aui-badge')
for u in element3:
    if int (u.text) != 2:
      toast1 = Notification(app_id="Uncategorized TEXTO - Triagem",title="Atenção",msg="Uncategorized TEXTO - Triagem: "+u.text,duration="long")
      toast1.set_audio(audio.Mail, loop=True)
      toast1.add_actions(label="Acessar fila",launch="TEXTOqueues/custom/18")
      toast1.show()
else:
     print("Uncategorized TEXTO - Triagem: "+u.text+"\n")
element5 = driver.find_elements(By.XPATH, '//html/body/div[1]/div/div/section/div[1]/div[3]/div/div/ul/li[4]/a/aui-badge')
for t in element5:
    if int(t.text) != 5:
      toast2 = Notification(app_id="Abastible_apps",title="Atenção",msg="Abastible_apps: "+t.text,duration="long")
      toast2.set_audio(audio.Mail, loop=True)
      toast2.add_actions(label="Acessar fila",launch="TEXTOqueues/custom/2286")
      toast2.show()
else:
          print("Abastible_apps: "+t.text+"\n") 

          print(" *** Encerrando consulta *** \n")
           
