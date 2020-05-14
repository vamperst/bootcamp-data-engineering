# 02 - Ingestão Manual

![](img/arch-ingestao-manual.png)

1. Primeiro vamos criar 4 filas no SQS, para isso abre o console e no canto esquerdo superior clique em `serviços`, digite `sqs` e selecione para abrir.
   ![](img/sqs1.png)
2. Inicialmente vamos criar as 2 filas DLQ: `raw-json-dlq` e `small-files-csv-dlq`. 'Clique em criar uma nova fila', apenas coloque os nomes, mantenha as opções padrão e clique em 'Criar fila rápido'.
   ![](img/sqs2.png)
3. Agora vamos as filas principais: `raw-json` e `small-files-csv`. Clique novamente em 'Clique em criar uma nova fila' coloque o nome e clique em 'configurar fila'. Em `Configurações da Fila de mensagens mortas` deixe como na imagem. Lembrando que cada fila tem sua respectiva DLQ. E clique em `Criar fila`
   ![](img/sqs3.png)
4. Ao final devem haver 4 filas:
   ![](img/sqs4.png)
5. Para não precisar lidar com um arquivo muito grande vamos dividir em varias partes, para tal vá ao terminal do cloud9.
6. Entre na pasta do dataset com o comando `cd ~/environment/seattle-library-collection-inventory/`
7. Crie a pasta para os arquivos menores com o comando `mkdir files-small`
8. Vamos criar arquivos de 100.000 linhas cada com o comando`split -d -l 100000 library-collection-inventory.csv files-small/inventory.part.` 
9. Pode ser que o comando demore um pouco para executar
10. Enquanto o código executa vamos criar o bucket que será utilizado no bootcamp. Para isso vá ao console do S3.
11. No canto supeiror direito clique em `Criar bucket`
12. Os nomes no S3 são unicos em toda a AWS não somente sua conta, vamos nomear seu bucket como `bootcamp-data-engineering-<SEU RM>` e clique em criar bucket
    ![](img/s3-1.png)
13. Devolta ao terminal do CLoud9, agora vamos retirar o cabeçalho do primeiro arquivo para que não atrapalhe na ingestão. Para tal utilize o comando `sed -i '$d' files-small/inventory.part.00`
    ![](img/sed1.png)
15. Execute o comando `rm files-small/inventory.part.9*` para deixar apenas 90 arquivos gerando um total de 4.5Gb deixando as fases do bootcamp mais rápidas.
16. Agora é hora de colocar os arquivos no S3, para isso execute o comando: `aws s3 cp --recursive ~/environment/seattle-library-collection-inventory/files-small/ s3://bootcamp-data-engineering-<SEU RM>/files-small/`
17. Vá para a pasta do projeto que baixou do git com o comando `cd ~/environment/bootcamp-data-engineering/02-ingestao-manual/`
18. No IDE navegue até o arquivo `list-from-s3-send-to-sqs.py` e altere o valor da variavel `bucket` pelo nome do bucket que criou, a variável `urlSQS` pela URL da fila `files-small-csv` que criou e a variável `keyprefix` com o conteudo 'files-small/'. 
    ![](img/ide1.png)
    ![](img/sqs5.png)
19. Execute o arquivo no terminal com o comando `python3 list-from-s3-send-to-sqs.py`
20. Se for ao painel do sqs e atualizar verá que a fila files-small-csv tem 90 itens disponiveis. Um para que arquivo no S3. Essa é uma maneira segura de consumir os arquivos e garantir que caso tenha uma falha o registro vá para a fila de DLQ, sendo facilmente restreavel.
21. Agora é necessário consumir a fila, converter e salvar os jsons no S3. Para isso altere as variaveis `bucket` e `urlSQS` como fez no passo 16 no arquivo `read-sqs-convert-csv-to-json.py`.
22. Execute o comando `python3 read-sqs-convert-csv-to-json.py` para executar o arquivo e iniciar o processo.
23. O processo pode demorar, para acelerar pode abrir até 4 terminais. Até 4 porque seria o limite da maquina já que essa operação consome bastante IO e CPU. É possivel acompanhar o progresso atualizando o painel do SQS.
24. Após o fim da execução vamos precisar novamente do arquivo `list-from-s3-send-to-sqs.py`, dessa vez altere a variável `urlSQS` para a URL da fila `raw-json` e a variável `keyprefix` para o conteúdo 'json/'
    ![](img/ide3.png)
25. No terminal execute o comando `python3 list-from-s3-send-to-sqs.py`. Isso irá preencher a fila `raw-json` com 90 registros correspondentes aos arquivos na pasta json.
26. Vamos criar o kinesis firehose que vamos utilizar nesse bootcamp. Em outra aba vá para o console do kinesis. CLique em `Criar stream de entrega`
    ![](img/kinesis1.png)
27. De o nome de `ingest-json` e clique em 'next'
    ![](img/kinesis2.png)
28. Clique em `Next` novamente.
29. Na seção 'S3 destination' escolha o bucket que acabou de criar.
30. Na seção 'S3 prefix' coloque os valores `ingested-json/` em 'Prefix - optional', `ingested-json-error/` em 'Error prefix - optional'.
31. Na secão 'S3 backup' escolha o bucket que criou e popule `source_records_ingested/` em 'Prefix - optional' e clique em 'Next'
    ![](img/kinesis4.png)
32. Na seção 'S3 buffer conditions' coloque o valor `100` em 'Buffer size' e `300` em 'Buffer interval'.
    ![](img/kinesis5.png)
33. Na seção 'Permissions' clique em 'Create new or choose'
34. Na aba que abriu apenas clique em 'permitir' no canto infeiror direito para criar o IAM do firehose.
    ![](img/kinesis7.png)
35. Clique em 'Next'
36. Revise as informações e clique em `Create delivery stream`
37. Vamos alterar um parametro da fila `raw-json`. Vá até o painel do sqs, selecione a fila e clique em 'Açoes de fila'. Clique na opção `Configurar fila`
38. Altere o valor de 'Tempo limite de visibilidade padrão' para `2 MINUTOS` e 'Atraso de entrega' para `20 segundos`. O primeiro parametro é o tempo que o consumidor tem para deletar o registro da fila após ler. O segundo é o tempo de atraso da primeira entrega do registro na fila, ele é interessante pois o S3 é assincrono e pode demorar alguns poucos segundos para o objeto ficar disponível.
    ![](img/sqs6.png)
39. De volta ao cloud9, altere o arquivo `read-sqs-send-to-firehose.py` colocando a URL da fila `raw-json` na variável `urlSQS`
    ![](img/kinesis8.png)
40. Após 20 segundos da inserção, execute o comando `python3 read-sqs-send-to-firehose.py` para ler os arquivos do S3 que estão listados no SQS e mandar para o Firehose.
41. É possivel ver os arquivos sendo criados no S3 dentro da pasta ingested-json