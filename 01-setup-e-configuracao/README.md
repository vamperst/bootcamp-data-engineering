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
curl -o seattle-library-collection-inventory.zip "https://data-eng-16abd.s3.us-east-1.amazonaws.com/archive.zip?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXNhLWVhc3QtMSJHMEUCIQDjMusCA8sjCcDKhA%2B4GIg62Cpuw1yozsJEfJHCylAfEwIgUY4RaOY1ZJhUx%2BZFFf%2FHnn6Rwz%2FJ48255iu8sepFQeoq3wMIFBAAGgwwMzYzNDUzMDM4MTQiDBtzFEk%2FRTvw0c%2BTbyq8A7TTDCPBTLfylvutCecHBpSln7CpbbAj6QHtJAstmg4WlHNgvxfyvkaWueORh8ul%2Bwtc1Y72i72g%2BSwX77Ao7Nmt8A%2FO3SEvEhONc7vtKX41Kpau2bf05SWGn4nrYKIEEKGcMhD4DpC4swuQBpId0Kj4CMVjx9sX3S6PId2I79AnyKKycFoHmTvHoNwN7TQJ4%2B3y8vnd%2BAE5dqpR3ABD02rgifREI1ETgbdHxSopHZSBceetzAe3Jbve9FL%2FSt3Eg3H3adAy3l1Eaegdit7KauUZRqu7gStJOD6r15djk4%2BXCFPttnmdiLHZE9BEEudG73In%2Fhb0gCcqxgsYgOBj5TOspcMuyxAV1EADttXaQ6hGEF3e3OGfl971E%2FmcEzuu2ztfyPOxxy01wuAhqio8KL8m6Tig6vU8FjgNMVRz8AtMiJRZH1kKVu1054UAqlO%2FfMRo9cTHQAMw3fHk%2BF8YHWuU8ThDAMwl6AYE32aqLMamhF4PXE9o4wSEpv7bKmhR3E0bcA6pq167OvGUlOaiOrg8NpXOCqb0rvejrgIuekJdpHRL7voeUHbLWtyKPiZsQwTSJlL%2FwXLCzTl7WjCxiuqhBjqUAj%2FMlz0E0eu%2FDvp762w2r6bojCP8QJjGKgFEgWCKOJKQ71wnolfdtdEyUXyOCcT%2FtlWJQpvT3W7y6q%2Bh%2BBqY6MNqxKhgUaWlp5WpQLV1tBDGV%2BD7Ry8kyzijPh8LemBLH3oJuKiPcL1AsZBKfBSbSZPb8mKq6JCAkQUbpJkicikECuz6n%2FEpn0iJvPG5fTO%2BLr56dY9YNgu2rzNqxGXS%2BpPe62dEo3efWCkCoNRa4I7u94EJsfiqGIV3IPYK0%2BLSSATcXmy9%2Bfe4fbY7vAZADZcXVTug3lHUU2JjnbgtGd3AuToI0uCO0uVvlvmSaTenh3v0d3BLNuGeRbekBstHaHLiy8byDgUmwJeqq9NBj2%2B35ZjtHA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230415T110737Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAQQ5SZKMDM2VLNBG6%2F20230415%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3bdc23226dcee88da047e6ec37fac4d0c6c5950190652d03b28add7c7377a5a2"
```
`
27. AO termino do download execute o comando `unzip seattle-library-collection-inventory.zip` para descompactar o conteúdo.
28. Apague o zip que baixou e já não é mais necessário com comando `rm seattle-library-collection-inventory.zip`

