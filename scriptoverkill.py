#MDR 
from miio import Vacuum
import os
import requests
import time
import datetime  

telephone1 = "<ipAppareil1>" #Mon téléphone
telephone2 = "<ipAppareil2>" #Un autre téléphone

isVacuumedToday = 0 #L'aspirateur est-il passé aujourd'hui ?

vac = Vacuum("<ipAspirateur>", "<tokenAspirateur>")

def isConnected():
  telephone1IsConnected = os.system("ping -c 1 " + telephone1)
  telephone2IsConnected = os.system("ping -c 1 " + telephone2)

  if telephone1IsConnected == 0 or telephone2IsConnected == 0:
      return 0
  else:
      return 1
      
def vacuumStart():
  if isConnected() == 1 :
      print("Trying to start the vacuum.")
      print(vac.start())
  else:
      return 0    
    
while 1:
  current_time = datetime.datetime.now()  
  if current_time.hour == <heure> and current_time.minute == <minutes> and isVacuumedToday == 0: #1er essai à une heure donnée
      vacuumStart()
      isVacuumedToday = 1
  elif current_time.hour == <heure> and current_time.minute == <minutes> and isVacuumedToday == 0: #2eme essai si l'aspirateur n'a pas démarré au premier horaire
      vacuumStart()
      isVacuumedToday = 1
  elif current_time.hour == 0 and current_time.minute == 0:
      isVacuumedToday = 0 #On réinitialise à minuit
  else:
      print("Wait 30 seconds")
      print(isVacuumedToday)
  time.sleep(30)