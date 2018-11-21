# DJANGO

# GRADE DE PROGRAMAÇÃO

Construa uma API REST em Django, que será responsável por entregar a grade de programação das rádios e alimentar o conteúdo dos sites e Apps do SGR.

# BASE A:
 - extremamente sensível e deve ser protegida com os maiores níveis de segurança.
Para proteção de uma base de informação e dados deve-se seguir alguns conceitos na proteção de dados, onde destaco abaixo alguns conceitos mais relevantes e usuais.

### Controle de Acesso
- Controle de acesso feito quanto ao acesso ao BD, impondo regras de restrição, através das contas dos usuários, e autenticação via TOKEN. Exemplos, JWT.

### Controle de Fluxo
- É um mecanismo que previne que as informações fluem por canais secretos e violem a política de segurança ao alcançarem usuários não autorizados


### Controle contra SQL Injection
- É um tipo de ameaça relacionado a segurança, que se aproveita de falhas em sistemas que interagem com bases de dados para inserir trechos de código SQL para realizar ações não desejadas e  para manipular, roubar ou danificar a estrutura ou dados contidos no banco de dados.

### Criptografia de Dados
- É uma medida de controle final, utilizada para proteger dados sigilosos que são transmitidos por meio de algum tipo de rede de comunicação. Ela também pode ser usada para oferecer proteção adicional para que partes confidenciais de um banco de dados não sejam acessadas por usuários não autorizados

##### Minha proposta para esse microsserviço está descrita a baixo:

1. MySql
2. Django-Rest-Framawork
3. Json Web Token

## Modelo proposta para solução da BASE A

![BASE A](https://github.com/asafepy/desafio-api-bureau/blob/develop/files/base-a.png)


# BASE B:
 - Também possui dados críticos, o acesso precisa ser um pouco mais rápido, além de consultas ela é utilizada para extração de dados por meio de algoritmos de aprendizado de máquina.

### Mantendo a arquitetura Base A

- Para a Base B, manter os mesmos critérios de segurança para as informações junto com o MySQL.

### Serveless
- A computação sem servidor é um modelo de execução de computação em nuvem no qual o provedor de nuvem atua como o servidor gerenciando dinamicamente a alocação de recursos da máquina. 

### Web Crawler
Web Crawler, utilizado como um programa de computador que navega pela Web de uma forma metódica e automatizada, bastante comum ver a utilização destes sistemas autômatos para buscar alguma informação e extração de dados pela Web. 

## Modelo proposta para solução da BASE B

![BASE B](https://github.com/asafepy/desafio-api-bureau/blob/develop/files/base-b.png)
