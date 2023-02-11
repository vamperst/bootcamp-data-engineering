# 01 - Setup e Configuração de ambiente


 1. Abra o console da AWS e va para o serviço `Cloud 9`.
   ![img/acharcloud9.png](img/acharcloud9.png)
1. garanta que a região que esta utilizando é `us-east-1/ Norte da Virgínia`. Você consegue ver isso no canto superior direiro da tela.
    ![img/regiao.png](img/regiao.png)
 2. Clique em `create environment`.
 3. Coloque o nome `lab-fiap` e avance.
 ![img/nomelab.png](img/nomelab.png)
 5. Deixe as configurações como na imagem a seguir. Se atente ao tipo da maquina que deve ser t2.medium:
![img/config.png](img/config.png)
 6. Caso os parametros estejam como na imagem a seguir clique em `Create Environment`
   ![img/review.png](img/review.png)
 7. A criação do ambiente pode levar alguns minutos.
![img/criando.png](img/criando.png)
 8. Após a criação clique em `abrir IDE`, caso o IDE não tenha aberto automaticamente.
   ![img/abriride.png](img/abriride.png)
9. Para os próximos comandos utilize o console bash que fica no canto inferior do seu IDE.
   ![img/bash.png](img/bash.png)
10. Execute o comando `npm install -g serverless` para instalar o serverless framework.
    ![img/installserverless.png](img/installserverless.png)
11. Execute o comando `sudo apt  install jq -y` para instalar o software que irá nos ajudar a ler e manipular Jsons no terminal
12. Execute o comando `git clone https://github.com/vamperst/bootcamp-data-engineering.git` para clonar o repositório com os exercicios.
13. Execute o comando `cd bootcamp-data-engineering/` para entrar na pasta criada pelo git
14. Execute o comando `cd 01-setup-e-configuracao/` para entrar na pasta com os scripts de Configuração.
15. Precisamos aumentar o tamanho do volume(HD) do cloud9. Para isso execute o comando  `sh resize.sh`
   ![img/resizeEBS](img/resizeEBS.png)
16. Para utilizar o SDK em python da AWS instale com o comando `pip3 install boto3`
17. Iremos utilizar um dataset do kaggle para fazer o bootcamp, instale o sdk da api para conseguir fazer o download via terminal `pip install kaggle`
25. Vamos criar o lugar onde ficarão os dados na maquina. Para isso crie a pasta com o comando ` mkdir ~/environment/seattle-library-collection-inventory` e entre nela `cd ~/environment/seattle-library-collection-inventory`
26. Vamos baixar o dataset na maquina com o comando 
``` shell 
curl -o seattle-library-collection-inventory.zip "https://data-eng-16abd.s3.us-east-1.amazonaws.com/archive.zip?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXNhLWVhc3QtMSJHMEUCIAdu0Gr6wjFOup4k2MxhKrO3NAm9nE1zAj3zsHM2TdrxAiEAoqnmV6VGGOQp12CuRwq7B2KQsWhOO9%2Bnl2btujEU9fYq6AMIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwwMzYzNDUzMDM4MTQiDGfCT7z7%2FrsLxQ6s%2FCq8A1iwuqDt5eG2IVjE2jsm2VtYIdJdkvI2iUjVFw8dArN0th%2BuPYMW0m6f8rgejDEbsZrvL0Vl4p8XsyAC2r%2BcNpf9f6QIgbH7JhPXrJ028lhTDWeruDGytKNRDl4wZIaBGqP0r6FhYZq%2Bbp%2Bq7tHTcjuUES%2Bye8jYJU1pKZebXRsOEAsClgQ7hQvmx6GGa2yYuK8GiPkvyiTKP9z09%2Fy4GdGalh0Lm8MOCzxeZlWXEUR5ELKESxbRZc3IsQ2S8GfjnLx7hD7jXuBjGa8EUp8Uw4YGRwtse1B%2BeX04JpC7yo58pTRIGMLw4niVrWFzOtAHdI%2B1DIu%2BU0xVNvPqv6unn9PwR6s6Llp93LzQah7%2Bx%2BkU%2FrVGiPZjIAx6uyuA2Cl1gY%2FfNp6Z72vsbJiZ81VKtAQ8TBMDN01UqfTZOxbS0gVuoozrPikDDACzECeUGVnEKdnBPyFx5HkIwMYcp%2BUjVcPjFktwUzcTkz2P3lxCz5Zpn96A4Y48swot1w3a7WLadE5KOhdM6AMDdT1mFnuholiGJLERvNv5d2vzaBK8Dtv43H%2FVChRF0Cxw5J%2F6FAjkqNuILml1IOOg0l3%2BODC19J2fBjqUAmrVHp1v%2FcfY7oBJgXoo2JcZUPv4TnclyEVGHaeZGhIChZn7YwTK%2Blv9JBFDy63RNtd8Nzq5nxVOVM7wtqANZWElFbIJs6JdOirCrKy%2FjLZ37WuUfvtelh4FOK6%2Ff%2FffzoFgpW42QWq6PS%2FIEYW37i4aaT1A5Erb1Wcv7Xc1cphsOMGItOdj3ifD0i%2FG65453kdxkOBqxmJrEQ6%2BRxxtNyPXrOODQJ%2B1JEMJmaVN0f0VGUyHsEc%2F6SdBMfZnKnPNdiz%2FjacuDTZvXaqrj4BkZ%2FKvUCQodC7O5bTDFGSo1WXH7WSsb7UAKsp32GUDB%2FyRsdZfBIowjYd9KIAWBp2FCV%2BONPGd67dlnEZ9vd3Xb6taKyKZSQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230211T115044Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAQQ5SZKMDKLAQSJOI%2F20230211%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=40bac41bbfb640c393ec3ce52ac1ae6b9ba815ac3161ca0d618323159128e078"
```
`
27. AO termino do download execute o comando `unzip seattle-library-collection-inventory.zip` para descompactar o conteúdo.
28. Apague o zip que baixou e já não é mais necessário com comando `rm seattle-library-collection-inventory.zip`

