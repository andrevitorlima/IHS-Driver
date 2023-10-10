# IHS-Driver
Como projeto final da disciplina de Interface Hardware Software decidi fazer um driver de mouse no espaço do usuário para ajudar pessoas que não conseguem utilizar um mouse, como por exemplo pessoas com tetraplegia, com braços amputados e com doenças neuro degenerativas.

O driver funciona da seguinte forma: com a webcam centralizada, com poucos movimentos corporais é possível mover o mouse, é preciso ficar de frente para a webcam e trasladar a cabeça, sem rotacioná-la, para a direção que deseja que o mouse vá, para um melhor conforto é aconselhavel que o usuário calibre alguns parâmetros como os limites de valores das direções em que deseja que o mouse mova e a velocidade  do mesmo.

# Configutacao da maquina para rodar o projeto:

### Python 3.10.12 
### Sistema Operacional Linux
### OpenCV
### UInput

# Instalacao:

Abra o terminal e execute os seguintes comandos:

## $ sudo apt-get install python3

## $ sudo apt-get install python3-opencv

## $ sudo pip install python-uinput

# Executar:

Para executao o projeto você deve: baixar o arquivo, extraí-lo e executá-lo usando o seguinte comando no terminal no diretório em que se encontra o arquivo.

## $ sudo python3 driver.py
