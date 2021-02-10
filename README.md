# dockersheet1
Criação de contêiner com Docker.

Os caminhos para gerar as credenciais, foram simples e diretos, acessando o console de API's do Google, foram geradas as credenciais necessárias para o desenvolvimento da aplicação. A API utilizada leva o nome de Sheets API, onde é possível executar a documentação do gspread, sendo possível realizar as alterações no script. 

O script em questão 'app.py', foi testado, de duas maneiras: no Ubuntu LS 20 04 focal e no ambiente Windows 10 pro, foram notados erros de log após a execução do Dockerfile no Ubuntu, porém, os mesmos erros aparentes não ocorrem no Windows. Testados separadamente, com a alteração dos caminhos nos diretórios e atualização para a ambientação em .JSON, o dockerfile executa o script automaticamente, dessa forma, app.py se torna uma dependência arquivo dockerfile, sendo executado somente através dele.

A maior dificuldade do projeto em si, foi a junção das credenciais para que o script funcionasse e posteriormente a aplicação junto ao dockerfile, o que exigiu mais pesquisa na documentação, e que no fim, trouxe um código mais "limpo".

O arquivo client_secret.json possui as credenciais do autor do script, portanto não acompanha a aplicação.

Container creation with Docker.

The paths to generate the credentials, were simple and straightforward, accessing google's API console, were generated the credentials necessary for the development of the application. The API used is called the Sheets API, where you can run the gspread documentation, and you can make the changes to the script.

The script in question 'app.py', was tested in two ways: in Ubuntu LS 20 04 focal and in the Windows 10 pro environment, log errors were noticed after running Dockerfile on Ubuntu, however, the same apparent errors do not occur in Windows. Tested separately, by changing the paths in the directories and upgrading to the setting in . JSON, the dockerfile runs the script automatically, so app.py becomes a dockerfile file dependency, running only through it.

The biggest difficulty of the project itself was the joining of credentials for the script to work and later the application next to the dockerfile, which required more research in the documentation, and that in the end, brought a cleaner code.

The file client_secret.json has the credentials of the script author, so it does not accompany the application.
