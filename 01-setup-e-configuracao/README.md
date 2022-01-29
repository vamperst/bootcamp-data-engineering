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
26. Vamos baixar o dataset na maquina com o comando `curl -o seattle-library-collection-inventory.zip "https://data-eng-16abd.s3.us-east-1.amazonaws.com/archive.zip?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXNhLWVhc3QtMSJGMEQCID0TatL0VxAzx8sZNJjOD%2BSA4viKZ1zMnjPqkRoVEjtGAiA5KyM3iRgC%2FB1A61gdu1TXoTbkKsDQDTcjZ5gZF4YgoCroAwjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDAzNjM0NTMwMzgxNCIMS39XwAcks7YcEinEKrwDKo47EgvaHBBRSBQzH3xnu1CzY0LNwdLm2JoaJ1oDl7OG5en4QJgOHivhqsZkNR99rt8UQ8CqYfL3dc9zQ2gW2NRBZDCar55H6tX3npNxfkFSXk7zXOopaWW0y8eTa9mYkSZuxYHvtdbfiNADMwenqiAC7xRZqt00wVFIw9BLwYsgYTNtdst80DqxZQjmLjorwicI0ijWqinZpjCe%2B0JHgcbSZU7kxJtjgIHnmUNGrcP64bRu%2FwGzNrFSoc2M65EWIXcgat8PqZ0BliNBT4D16BIU6gIdZV3WWB2s5h7kEv3E2TtgN8WInLxmrFWqYRt9gfNB4LqPqxhaRuY8JRE%2FRAPv8b2PQsPVLqoRK9lZVtbAxto2o8M1x7QirzL%2FCQGGSacsWVEKn7BsRmU%2FTyJ%2FGRHcdD7r4E0VDU2NpkIO1e%2FG%2BbrPYHD79cAMfd2qkFDAdKB0%2BSE3YbfbIFZ9agSpfCMNO8YEJOcxf5YaASt5brOvSc1uHFmroCk57poAEdo5frEIz3Jp4ZZ9XNCuL%2F0suFtqka1MtGiwpvJuuHBrhDSuMzgYCup38%2BUA9kf1fmsAzg92crErzHr%2BPdrXMPO70o8GOpUC4itkeXDFt5scfWMQEOZEm4rJh9s9UDZ7tBQZRuO1O1%2FGjkTzJDkESMOMJJdD8nbqZgGu6KlFGDfoA41p8SemCpaq3j%2BglnvIAjzMOm5x1KoFri3UpiSoH96K6W9JWDYHOlN1jAiWs5N79aYYmNhlZtfHhH%2Fu6VnOWgZ1dsP5acbwLFBkLrHZFRh87lcJJf98%2F9L9hCnDbiZegZ%2BRg5kaHFs%2BYBIClK6OdB%2FWhVJp8%2FSoNqOhfHe4EReZe1wBTpb3MLD0yGQjGhMgoXPs6Lajqe940qU3Pk2rI6I68%2B4QC7cnAHpYBN6AR%2BeG6GVcxwThweUDxX%2FwB93Wl7jqMgZxpG1ArYmtEHDGs%2B5N03zOH0ZoZMBNbA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220129T030438Z&X-Amz-SignedHeaders=host&X-Amz-Expires=172800&X-Amz-Credential=ASIAQQ5SZKMDIZYRMA4E%2F20220129%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=89eb3456aa07ff79bff3a73cbab6fc787c47c11a6cf0f96ca363036688a23eb8"
`
27. AO termino do download execute o comando `unzip seattle-library-collection-inventory.zip` para descompactar o conteúdo.
28. Apague o zip que baixou e já não é mais necessário com comando `rm seattle-library-collection-inventory.zip`

