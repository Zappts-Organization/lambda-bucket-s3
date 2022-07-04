<br />
<p align="center">
  <a href="https://www.zappts.com.br/">
    <img src="https://uploads-ssl.webflow.com/60d39ec767d1cd6ee3eb6f5e/6122c24c585295aac26de440_zappts-logo.svg" height="60">
  </a>

  <h3 align="center">Universizappts</h3>
</p>

## Sobre o Projeto

Este repositório contém uma função Lambda que extrai o conteúdo de arquivos .txt. A função e acionada ao adicionar um .txt ao bucket do Amazon S3.

## Requisitos

1. Para usar o Lambda e outros serviços da AWS, você precisa de uma conta da AWS. Se não tiver uma conta, acesse  [aws.amazon.com](http://aws.amazon.com/)  e escolha  **Create an AWS Account**  (Criar uma conta da AWS).
2.  Instalar Serverless Framework

## Instruções de instalação

1. [Crie uma conta da AWS](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) se ainda não tiver uma e faça login.

1. Clone o repositório em sua máquina de desenvolvimento local usando `git clone`.

1. E execute:
```
serverless deploy
```

## Como funciona

* Ao adicionar um arquivo TXT no bucket S3 da Amazon e acionada uma lambda que lê o conteúdo do arquivo.

### Estrutura de Arquivos
```bash
lambda-bucket-s3/  
┣ .gitignore  
┣ handler.py  
┗ serverless.yml
```
## Contato

Zappts - **zappts@zappts.com**
<br />
<p align="center">
  <a href="https://www.zappts.com.br/">
 <img src="https://uploads-ssl.webflow.com/60d39ec767d1cd6ee3eb6f5e/6122c24c585295aac26de440_zappts-logo.svg" height="60" alt="Logo">
  </a>
