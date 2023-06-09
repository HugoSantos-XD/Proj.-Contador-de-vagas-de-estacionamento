import cv2 #importando a biblioteca do OpenCv 
import pickle #importando bibliteca que irá salvar as vagas de estacionamento

img = cv2.imread('estacionamento.png')

vagas = [] #lista vazia 

for x in range(69): #69 vagas no estacionamento
    vaga = cv2.selectROI('vagas',img,False) #pegando precisamente a imagem 
    cv2.destroyWindow('vagas') #destruindo a janela 
    vagas.append((vaga)) #adicionando um item a uma lista

    for x,y,w,h in vagas: #função para o usuário selecionar as vagas e armazenar
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

#salvando os campos selecionados das vagas
with open('vagas.pkl','wb') as arquivo:
    pickle.dump(vagas,arquivo)