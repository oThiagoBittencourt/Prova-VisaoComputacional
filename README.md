# Prova-VisaoComputacional

Arquivo Jpynb do treinamento da CNN:
[CNN-Colab](https://colab.research.google.com/drive/1ZSA4OOmnCzm1aSd4dkiSlirTrIeMGu0E?usp=sharing)

## Descrição do Problema:
### CNN
O objetivo deste projeto foi treinar uma rede neural para reconhecer imagens do conjunto CIFAR-10, que contém 10 categorias, "avião", "automóvel", "pássaro", "gato", "cervo", "cachorro", "sapo", "cavalo", "navio" e "caminhão".
### Pré-Processamento
A meta deste do pré-processamento é executar um tratamento inicial em fotos de duas classes distintas (gatos e cachorros).

## Por que escolhi essas técnicas
### CNN
Usei uma rede neural convolucional (CNN) por se tratar de uma boa opção para o processamento de imagens, devido às suas convoluções. Para melhorar a generalização do modelo e evitar overfitting, apliquei data augmentation. Quanto ao otimizador Adam, foi escolhido por ser rápido e estável. Como função de perda escolhi prosseguir com sparse categorical crossentropy. E por fim, adicionei uma matriz de confusão para entender melhor como o modelo se saiu em cada classe.
### Pré-Processamento
As técnicas foram escolhidas para padronizar as imagens: o redimensionamento facilita o uso em modelos de IA, o filtro Gaussiano reduz ruídos e a equalização de histograma aumenta o contraste, destacando detalhes das imagens.

## Etapas do projeto
### CNN
- Normalização das imagens.
- Modelagem da CNN.
- Aplicação do data augmentation no conjunto de treino.
- Treinamento do modelo, junto da avaliação do conjunto de teste.
- Análise dos resultados com gráficos de acurácia e a matriz de confusão.
![image](https://github.com/user-attachments/assets/76b34fe9-2a77-4f30-928b-76920250a798)
### Pré-Processamento
- Criação da estrutura de pastas.
- Implementação do script.
- Testes finais com as seis imagens.

## Resultados
### CNN
- O modelo atingiu 70,81% de acurácia.
- O gráfico de desempenho mostra que o modelo aprendeu de forma crescente.
- A matriz de confusão revelou que ele teve mais dificuldade para diferenciar algumas classes parecidas, como gato e cachorro, ou automóvel e caminhão.
- Classes como avião, navio e caminhão foram bem classificadas.
![image](https://github.com/user-attachments/assets/8b6d6b59-57f2-4a0f-bb12-1320f3e54bf3)
### Pré-Processamento
As seis imagens foram processadas com sucesso, apresentando tamanho uniforme, menos ruído e maior contraste.

## Tempo investido
### CNN
Em média 1 hora. Sendo 25 minutos de treinamento.
### Pré-Processamento
Aproximadamente 30 minutos para toda a implementação, testes e documentação.

## Dificuldades encontradas
### CNN
- O overfitting foi resolvido com o data augmentation.
- Algumas classes muito semelhantes entre si causaram confusões na classificação.
- Foi preciso experimentar diferentes parâmetros para chegar em um resultado satisfatório.
### Pré-Processamento
- Problemas com caminhos ao trabalhar com diferentes diretórios.
- Ajustes no tamanho do kernel do filtro Gaussiano para não suavizar demais.
