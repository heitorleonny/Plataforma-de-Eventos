# Plataforma-de-Eventos
 Esse projeto foi desenvolvido na PYSTACK WEEK 6.0 com o intuito de criar uma plataforma de eventos com a linguagem Python e o framework Django. Através da plataforma desenvolvida é possível criar eventos bem como se inscrever em eventos criados por outras pessoas, tendo acesso a lista de participantes exportada em csv(planilha) e também à certificados gerados automaticamente.

## Índice

1. [Visão Geral](#visão-geral)
2. [Configuração](#configuração)
   - [Instalação](#instalação)
   - [Configuração do Ambiente](#configuração-do-ambiente)
3. [Dúvidas e Contribuições](#dúvidas-e-contribuições)
4. [Referências e Links Úteis](#referências-e-links-úteis)

## Visão Geral

O propósito dessa plataforma é facilitar a criação e gerenciamento de eventos, onde os usuários podem criar seus próprios eventos e se inscrever em eventos criados por outras pessoas. De forma intuitiva, a plataforma tem funcionalidades como gerar planilhas com o nome e email de todos aqueles que estão inscritos em um evento e também permite que o usuário gere um certificado de participação de forma automática.
![image](https://github.com/heitorleonny/Plataforma-de-Eventos/assets/108541219/f8691935-0e2f-47d6-a4f7-5384a173a49d)
![image](https://github.com/heitorleonny/Plataforma-de-Eventos/assets/108541219/ab8a0195-3bb9-4d37-a245-2cacf9190846)
![image](https://github.com/heitorleonny/Plataforma-de-Eventos/assets/108541219/0cb1c326-a134-49e6-a900-50fa5c5e3b52)
![image](https://github.com/heitorleonny/Plataforma-de-Eventos/assets/108541219/4e416ff7-2718-4c1a-90dd-e347287fb9aa)
![image](https://github.com/heitorleonny/Plataforma-de-Eventos/assets/108541219/41be6aef-f6c9-4628-982f-373681f86311)
![image](https://github.com/heitorleonny/Plataforma-de-Eventos/assets/108541219/1786d827-0b8c-4d46-9011-03e4595192b3)
![image](https://github.com/heitorleonny/Plataforma-de-Eventos/assets/108541219/7c62838b-7aee-45f4-a36a-5648f64ea1ca)


## Configuração

### Instalação

1. Para poder instalar o projeto e roda-lo é necessário ter instalado em sua máquina o python, git e alguma IDE de sua preferência.
2. Escolha a pasta onde deseja ter o repositório e abra seu terminal nessa pasta.
3. Efetue o clone com o seguinte comando ```git clone https://github.com/heitorleonny/Plataforma-de-Eventos.git```

### Configuração do Ambiente

Com o repositório clonado será necessário efetuar alguns passos para conseguir rodar o projeto:
1. Mude para a branch master onde está localizado os arquivos do projeto com o comando ```git checkout master```
2. Abra o repositório em alguma IDE (se estiver utilizando o VSCODE pode usar o atalho no terminal ```code .```)
3. Já na sua IDE abra um terminal e crie um ambiente virtual com o comando ```python -m venv env``` (caso queira pode substituir env pelo nome que preferir).
4. Sempre que você for rodar o site vai precisar ativar o ambiente virtual, podemos fazer isso com o seguinte comando ```env\Scripts\Activate``` no Windows. Se estiver usando Linux utilize ```source env/bin/activate```
5. Agora instale as dependencias do arquivo com o comando ```pip install -r requirements.txt```
6. Tudo certo!!! Agora é só rodar o projeto utilizando ```python manage.py runserver```


## Dúvidas e contribuições

O projeto é totalmente Open Source, logo você pode clona-lo e adicionar alterações que contribuam com o projeto que eu irei análisar e aceitar!😊
Caso tenha alguma dúvida pode entrar em contato comigo pelo meu [Linkedin](https://www.linkedin.com/in/heitor-leonny-24b564240/) ou [Instagram](https://www.instagram.com/heitor.leonny/)!

## Referências e Links Úteis

- [Django Official Documentation](https://docs.djangoproject.com/)





