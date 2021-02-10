# dockersheet1
Container creation with Docker.

Os caminhos para gerar as credenciais, foram simples e diretos, acessando o console de API's do Google, foram geradas as credenciais necessárias para o desenvolvimento da aplicação. A API utilizada leva o nome de Sheets API, onde é possível executar a documentação do gspread, sendo possível realizar as alterações no script. 

O script em questão 'app.py', foi testado, de duas maneiras: no Ubuntu LS 20 04 focal e no ambiente Windows 10 pro, foram notados erros de log após a execução do Dockerfile no Ubuntu, porém, os mesmos erros aparentes não ocorrem no Windows. Testados separadamente, com a alteração dos caminhos nos diretórios e atualização para a ambientação em .JSON, o dockerfile executa o script automaticamente, dessa forma, app.py se torna uma dependência arquivo dockerfile, sendo executado somente através dele.

A maior dificuldade do projeto em si, foi a junção das credenciais para que o script funcionasse e posteriormente a aplicação junto ao dockerfile, o que exigiu mais pesquisa na documentação, e que no fim, trouxe um código mais "limpo".

O arquivo client_secret.json possui as credenciais do autor do script, portanto não acompanha a aplicação.
