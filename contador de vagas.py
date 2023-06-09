import cv2 #importando bibliotecas 
import pickle
import numpy as np 

vagas = []

with open ('vagas.pkl','rb') as arquivo:
    vagas = pickle.load(arquivo) #abrindo todas as vagas salvas 

#print (vagas) #printando todas as coordenadas das vagas

video = cv2.VideoCapture('video.mp4') #armazenando o video na variavel 

while True:
    ckeck,img = video.read() #colocando o video para rodar 
    imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #video em cinza 
    imgTh = cv2.adaptiveThreshold(imgCinza,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16) #modificando o video para escala preto e branco
    imgMedian = cv2.medianBlur(imgTh,5)#limpando os ruidos da imagem preto e branco(Threshold)
    Kernel = np.ones((3,3),np.int8) #expandindo os pixels para assim ficar mais facil de indentificar qual onde tem vaga no estacionamento
    imgDil = cv2.dilate(imgMedian,Kernel)
    
    vagasDisp = 0 #variavel contadoras das vagas disponiveis
    for x,y,w,h in vagas: #verificando se as coordenadas dos retangulos batem com o video
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        vaga = imgDil[y:y+h,x:x+w]
        count = cv2.countNonZero(vaga)#calcula a quantidade de pixels 
        cv2.putText(img,str(count),(x,y+h-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1) #mostrandos os valores dos pixels nas vagas 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        if count <900:  #verificando se há vagas ou não 
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            vagasDisp +=1
        else:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            

        
        cv2.rectangle(img,(95,0),(800,60),(0,255,0),-1)
        cv2.putText(img,f'Vagas Livres:{vagasDisp}/69',(95,45),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3) #exibindo a quantidade de vagas disponiveis no estacionamento 
    
    cv2.imshow('video',img) #rodando o video 
    cv2.imshow('video Threshold',imgDil) #rodando o video em Threshold
    cv2.waitKey(1)#10 milessegundos