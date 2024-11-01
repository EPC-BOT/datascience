#importação do opencv-python
import cv2
import mediapipe as mp # importação do mediapipe para usar o facemesh



#criar uma variável para camera
cap = cv2.VideoCapture(0)

#usando uma solução de desenho
mp_drawing = mp.solutions.drawing_utils

# usando uma solução para Face Mesh Detection
mp_face_mesh = mp.solutions.face_mesh
# liberação automática
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as facemesh:
    # enquanto a camera estiver aberta
    while cap.isOpened():
        # sucesso-booleana (verificar se o frame esta vazio)
        # frame - captura
        sucesso, frame = cap.read()
        # realizar a verificação
        # sucesso = 1   fracaso = 0
        if not sucesso:
            print("ignorando o frame vazio da camêra")
            continue
        # transformando de BGR para RGV
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        #criar variável   dados processados(ex. pontos do rosto)
        saida_facemesh = facemesh.process(frame)
        # O OpenCV - entende BGR
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

        """
            1- Mostrar os pontos da nossa face
            2- O process - processar dos dados
            3- face_landmarks (COORDENADAS)


        """
        try:    
            for face_landmarks in saida_facemesh.multi_face_landmarks:
                #desenhar
                 mp_drawing.draw_landmarks(frame,face_landmarks,mp_face_mesh.FACEMESH_CONTOURS)   

        except: 
            print("Algo deu errado")
        finally:    
            print("Encerrando o processo")




        # carregar nosso frame - com título
        cv2.imshow('Camera',frame)
        # bitwise - tabela ASC II
        # 10 milissegundos
        # ord() - retorna o valor Unicode (ou ASC II)
        # o valor 0xFF é tabela ASC II estendida
        if cv2.waitKey(10) & 0xFF == ord('c'):
            break
    # fechando a captura
    cap.release()
    # fechando todas janelas
    cv2.destroyAllWindows()

