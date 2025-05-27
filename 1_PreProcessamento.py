import os
import cv2
import numpy as np

# Diretórios
dir_imagens = os.path.join(os.path.dirname(__file__), 'imagens')
dir_saida = os.path.join(os.path.dirname(__file__), 'preprocessadas')

os.makedirs(dir_saida, exist_ok=True)

# Parâmetros de pré-processamento
tamanho = (128, 128)
kernel_gauss = (5, 5)

def processar_imagem(nome_arquivo):
    caminho = os.path.join(dir_imagens, nome_arquivo)
    img = cv2.imread(caminho)
    if img is None:
        print(f"Falha ao carregar {nome_arquivo}")
        return

    # Redimensiona
    img_resized = cv2.resize(img, tamanho, interpolation=cv2.INTER_AREA)

    # Converte para tons de cinza
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

    # Aplica filtro Gaussiano
    img_blur = cv2.GaussianBlur(img_gray, kernel_gauss, 0)

    # Equalização de histograma
    img_eq = cv2.equalizeHist(img_blur)

    # Salvamento
    nome_saida = os.path.splitext(nome_arquivo)[0] + '_pre.jpg'
    caminho_saida = os.path.join(dir_saida, nome_saida)
    cv2.imwrite(caminho_saida, img_eq)
    print(f"Processado e salvo: {nome_saida}")


def main():
    arquivos = [f for f in os.listdir(dir_imagens)
                if os.path.isfile(os.path.join(dir_imagens, f))
                and f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for arquivo in arquivos:
        processar_imagem(arquivo)


if __name__ == '__main__':
    main()