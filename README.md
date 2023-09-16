<a name="readme-top"></a>

<div align="center">
  <a href="https://github.com/Fabrizzio20k/Proyecto_DBP">
  </a>
  <h1>👾 GPT VIDEOGAMES 👾</h1>
  
  <p>
  Este proyecto ha sido desarrollado por estudiantes del curso de Desarrollo Basado en Plataformas
de la Universidad de Ingeniería y Tecnología 💙🤍. Esperemos les guste. 🎮
    
  </p>
</div>

<details open>
  <summary>Índice:</summary>
  <ol>
    <li><a href="#integrantes">
      Integrantes
    </a></li>
    <li><a href="#acerca-del-proyecto">
      Acerca del proyecto
      <ul>
        <li><a href="#descripción">Descripción</a></li>
        <li><a href="#objetivos-principales">Objetivos Principales</a></li>
        <li><a href="#librerías-framworks-y-plugins">Librerías, Frameworks y Plugins</a></li>
        <li><a href="#script">Script</a></li>
        <li><a href="#api">API</a></li>
        <li><a href="#hosts">Hosts</a></li>
        <li><a href="#manejo-de-errores-http">Manejo de Errores HTTP</a></li>
        <li><a href="#ejecución-del-sistema">Ejecución del Sistema</a></li>
        <li><a href="#recursos-extra">Recursos extra</a></li>
        <li><a href="#equipo">Equipo</a></li>
        <li><a href="#notas-extra">Notas extra</a></li>
      </ul>
    </a></li>
  </ol>
</details>

---

## Integrantes

- Piero Jesus Guerrero Jimenez
- Fabrizzio Nicolay Vilchez Espinoza
- Manuel Jesus Silva
- Ariana Vega Huamán

## Acerca del proyecto

### Descripción

Este proyecto consiste en el desarrollo de una aplicación virtual llamada GPT VIDEOGAMES,
la cual consiste en comprar y vender videojuegos de manera virtual, ya sea por marcas, plataformas o categorías.

### Objetivos Principales

#### Misión

Esta página tiene como misión llegar a ser de total comodidad para el cliente y cumplirlo ofreciendo videojuegos de verdaderos y de alta calidad.

#### Visión

La visión de esta página es ser una de las plataformas líderes en la industria de entretenimiento electrónico y afines en el Perú.

### Librerías, Frameworks y Plugins

Front-end:

- Bootstrap: Bootstrap es un framework de desarrollo web gratuito y de código abierto. Está diseñado para facilitar el proceso de desarrollo de los sitios web responsivos y orientados a los dispositivos móviles, proporcionando una colección de sintaxis para diseños de plantillas.
- Slidy: Libreria de JS para mostrar un slide responsivo de manera fácil.
- SweetAlert2: Libreria de JS para mostrar alertas de forma más atractiva y con poco código.
- Axios: Libreria de JS para hacer diferentes peticiones al backend.

Back-end:

- Flask: Flask es un framework ligero de desarrollo web en Python que permite crear aplicaciones web rápidas y eficientes. Proporciona herramientas y bibliotecas para manejar solicitudes HTTP, enrutar URL, generar respuestas dinámicas y gestionar bases de datos. Flask es altamente personalizable y fácil de aprender, lo que lo convierte en una elección popular para desarrolladores de backend. Se usa en este proyecto para manejar las solicitudes a la base de datos y algunas operaciones de verificación.

- SQLAlchemy: SQLAlchemy es una biblioteca de mapeo objeto-relacional en Python que facilita la interacción con bases de datos relacionales. Proporciona una capa de abstracción que permite interactuar con la base de datos utilizando objetos y consultas en lugar de escribir consultas SQL directamente. SQLAlchemy simplifica el manejo de la persistencia de datos y la creación de consultas complejas.
- SMTPLIB: La biblioteca smtplib de Python se utiliza para enviar correos electrónicos a través de un servidor SMTP. Primero, se establece una conexión con el servidor utilizando smtplib.SMTP, luego se autentica con credenciales y se envía el correo utilizando sendmail. Todo esto se usa para enviar correos al usuario al final de la compra.

Base de Datos:

- Flask_migrate
- SQLAlchemy

### Script

Para cargar el backend se ejecuta:

```sh
./ejecutar.sh
```

- Se debe estar dentro de la carpeta llamada backend, en el mismo nivel que la carpeta app.
- Después, se usa ejecuta el código de los sql scripts encontrados dentro de la carpete /sql. Estos añaden la exensión uuid-ossp en la base de datos.
- Finalmente, se inicia el servidor.
- Debe existir una base de datos con el nombre de "project_dbp".

Para cargar el frontend se ejecuta:

```sh
npm install
npm run serve
```

- Se debe estar dentro de la carpeta llamada frontedn, en el mismo nivel que la carpeta src.

### Testing

Para realizar el testing del backend se ejecuta:

```sh
python -m unittest Test.py
```

- Se debe estar dentro de la carpeta llamada backend, en el mismo nivel que la carpeta app.

### API

La API que se está utilizando se llama IGDB.com, el cual sirve para obtener información sobre videojuegos individuales y poder realizar búsquedas de videojuegos.

### Hosts

Local host 5000

### Manejo de Errores HTTP

- Para la sección del login del usuario:
  El servidor responde con código 400 si el usuario no existe o la contraseña es incorrecta, y 200 si es que todo ha ido bien.
- Para la sección de recuperar constraseña:
  El servidor responde con código 400 si al momento de verificar las credenciales del usuario estas no coinciden, o con código 200 si pasa lo contrario.
- Para la sección de crear usuario:
  El servidor responde con código 400 (BAD_REQUEST) si se trata de ingresar un correo ya registrado, o con código, o con código 200 si el registro es exitoso.
- Para la sección de busqueda:
  El servidor siempre responde con código 200, ya que el que encuentre resultados o no, no indica que la petición de busqueda no se haya realizado correctamente.
- Para la sección de compra:
  El servidor siempre responde con código 200, ya que lo único que se hace es una inserción de datos dentro de la base de datos con datos verificados en pasos anteriores.
- Para la sección de editar datos:
  El servidor siempre responde con código 200, ya que el único dato relevante para definir si hay un error o no al insertar datos en la base de datos es el correo, el cual ya esta restringido para edición desde el principio.
- Para la sección de compras realizadas por el usuario:
  El servidor siempre responde con código 200, ya que la petición de busqueda siempre se hace con los datos obtenido anteriormente, y lo único que varia es el contenido dentro del JSON que se devuelve.

### Ejecución del Sistema

Para ejecutar el sistema se tiene que correr server.py

### Recursos extra

[Modelo entidad-relación de la base de datos implementada](extra/Diagrama.png)
![diagrama de clases](https://github.com/Fabrizzio20k/Proyecto_DBP/blob/main/extra/Diagrama.png?raw=true)

![Diseño Básico de la Página](https://github.com/Fabrizzio20k/Proyecto_DBP/blob/main/extra/Dise%C3%B1o%20B%C3%A1sico%20de%20la%20P%C3%A1gina.png).

### Equipo

| Fabrizzio Vilchez                                          | Piero Guerrero                                                   | Manuel Silva                                               | Ariana Vega                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------- |
| ![](https://avatars.githubusercontent.com/u/115495332?v=4) | ![](https://avatars.githubusercontent.com/u/102132128?s=400&v=4) | ![](https://avatars.githubusercontent.com/u/78549698?v=4)  | ![](https://avatars.githubusercontent.com/u/88595171?v=4) |
| [github.com/Fabrizzio20k](https://github.com/Fabrizzio20k) | [github.com/pieroGJ121](https://github.com/JLeandroJM).          | [github.com/Manueljsilva](https://github.com/Manueljsilva) | [github.com/ArianaVega](https://github.com/ArianaVega)    |

### Notas extra

El token de la API de IGDB tiene una fecha de expiracion del 10 de noviembre. Pasado esa fecha se debe de renovar el token.
