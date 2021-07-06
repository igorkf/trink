## Trink

### Um encurtador de links

Clique na imagem abaixo para ver uma demonstração.   

<div align="center">
  <a href="https://www.youtube.com/watch?v=TMeFudIt3gQ"><img src="https://imgur.com/yKHD9RU.png" alt="IMAGE ALT TEXT"></a>
</div>


## Como testar localmente
Clone o repositório e acesse a pasta:
```shell
git clone https://github.com/igorkf/trink.git
cd trink
```

Crie um ambiente virtual e ative-o:
```shell
python3 -m venv venv
source venv/bin/activate 
```

Instale as bibliotecas:
```shell
pip3 install -r requirements.txt
```

Inicie o *webserver*:
```shell
python3 manage.py runserver
```

Vá para `http://localhost:8000/` e utilize.
