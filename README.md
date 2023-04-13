# AdoPet
![em desenvolvimento](https://img.shields.io/badge/STATUS-EM%20DESENVOLVIMENTO-brightgreen)

API para gerir os recursos de um sistema de adoção de animais de estimação

# 🔨Ferramentas Utilizadas
* Django 4.1.7
* Django Rest Framework 3.14.0
* Postgresql 15

# Recursos disponíveis
* Tutor (tutor)
* Abrigo (shelter)
* Animal de estimação (Pet)

# Segue as etapas para utilização local:
LEMBRE-SE:
* Você precisa utilizar um banco de dados postegres;
* Foi disponibilizado um arquivo docker para gerar um container Postegres e um pg-admin;

Comando para subir os containers:
```
docker-compose up
```

Crie uma pasta pasta:
```
mkdir my-project
```
E em seguida, acesse-a:
```
cd my-project
```

No seu terminal *git bash* digite:
``` 
git clone https://github.com/BunoQueiroz/adopet-alura.git .
```

E em seguida, crie um ambiente virtual:

```
python -m venv venv
```

Entre no ambiente:

* COMANDO WINDOWS
```
venv/Scripts/activate
```

* COMANDO LINUX / MAC

```
source venv/bin/activate
```

Instale as bibliotecas Python necessárias:

```
python -m pip install -r requirements.txt
```

*Por fim crie, na raiz do seu projeto um arquivo .env e defina dentro dele suas variáveis de ambiente. Igual o .env.exemple*

<br>
Para Similar seu banco de dados ao projeto rode o comando:

```
python manage.py migrate
```

Depois de tudo isso, rode o comando:

```
python manage.py runserver
```
E seja feliz ; )

*Dúvidas ou  erros fale diretamente comigo, boa sorte com tudo*