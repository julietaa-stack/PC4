# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
#  your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona la sección que deseas ver', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>¡MI BLOG!:Paso a paso, código a código💻✨☺️</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("foto.jpeg", caption='¡Una foto mía!', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = """
    Soy Julieta Tamariz Tapia😀, tengo 22 años y nací el 29 de junio. Vivo en Lima, Perú y actualmente estudio Publicidad en la PUCP.<br><br>
    Antes pensé seguir Psicología, pero con el tiempo me di cuenta de que lo que realmente me motiva es el proceso creativo: pensar ideas, comunicar y conectar desde distintos formatos😌👌. En mi carrera disfruto especialmente la parte creativa, la generación de conceptos y la posibilidad de transformar ideas en mensajes.<br><br>
    A futuro, me gustaría trabajar en una agencia de publicidad, aunque también me interesa la idea de independizarme y desarrollar proyectos propios⭐. Me llaman mucho la atención el marketing, la moda y también la fotografía, como forma de observar y narrar la realidad desde lo visual.<br><br>
    En mi tiempo libre me encanta ir a la playa, montar bicicleta, salir a comer y ver películas, sobre todo en el cine y muchas veces acompañada de mi hermana🍿😆🎥. Escucho música todo el tiempo y disfruto mucho los conciertos, aunque últimamente no haya ido tanto🥲. Amo el verano, salir con mis amigas y pasar tiempo con mi familia, con quienes vivo: mis papás, mi hermana y mi perrito Tony, al que siempre suelo sacar a pasear🐕💕.<br><br>
    También me gusta la repostería, especialmente hacer galletas y postres en general, sobre todo aquellos que llevan arándanos. Entre mis favoritos está el helado de menta😋. Disfruto estos pequeños momentos cotidianos como una forma de desconectarme y seguir creando desde otros espacios.
    """

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Experiencia':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar💻😮</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2 = """
    Al inicio, la programación me generó confusión y un poco de temor 😬. Todo era completamente nuevo para mí: nunca había llevado clases relacionadas con este tema y me sentía mareada y extraña frente a algo que no entendía del todo. Aun así, también me resultaba interesante pensar en todo lo que se podía crear✨, aunque el proceso fuera difícil. Era necesario seguir los pasos con mucha precisión y mantener una alta concentración🧠💪<br><br>
    Con el tiempo, la programación me ha enseñado la importancia de la paciencia🧘‍♀️ y la constancia. Aprendí que cuando algo no resulta a la primera, es necesario volver a intentarlo y revisar los errores con atención. También descubrí que detrás de elementos que usamos cotidianamente, como gráficos , mapas o incluso juegos interactivos , existe todo un proceso que antes desconocía y que ahora puedo entender y aplicar🤓<br><br>
    Lo que más me gusta de programar es que ofrece herramientas que ayudan a optimizar el tiempo y simplificar tareas. Me parece muy funcional en distintos contextos, ya que permite crear, organizar y diseñar soluciones útiles ✅. Aunque requiere práctica y experiencia, el proceso de creación resulta motivador al ver cómo una idea puede transformarse en algo concreto💡.<br><br>
    A futuro, me gustaría seguir utilizando la programación como una herramienta complementaria para mi desarrollo académico y profesional 🎯, especialmente dentro del campo de las comunicaciones. Estas plataformas son útiles al momento de idear una web 💻, trabajar con datos📈 o desenvolverse en entornos digitales, lo que representa una ventaja en el ámbito laboral. Además, valoro mucho el acompañamiento recibido durante el curso 🤍, en especial el apoyo constante y la paciencia de la profe Luisa, lo cual facilitó el aprendizaje y generó un ambiente de confianza.<br><br>
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Explicación sencilla!🤓➡️ Diferencias entre los condicionales If, Elif, Else</h2>", unsafe_allow_html=True)
    
    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    st.video("https://www.youtube.com/watch?v=p8go9vagWfs&t=144s")
    st.markdown("<h2 style='text-align: center;'>Lo básico de los bucles for y while🤓➡️</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=CzKspWQA1fg&t=11s")
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://www.youtube.com/watch?v=X_Z7d04x9-E".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.

    # O creamos un botón para ir al enlace del video con button
    # st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 
    
    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>¡Mis primeras gráficas en programación!👀</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Histograma de goles de Barcelona', 'Gráfico de barras de tarjetas rojas en equipos', 'Gráfico circular sobre resultados del Real Madrid como visitante', 'Mapa interactivo de mis películas favoritas']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Histograma de goles de Barcelona':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Este histograma fue realizado como parte de un ejercicio de la Práctica 3, en el que debíamos escoger un equipo de la liga española y calcular la frecuencia de goles anotados como local y como visitante. En este caso, el equipo analizado fue Barcelona, y el gráfico corresponde a los goles anotados como visitante.<br><br>En el eje horizontal se muestra la cantidad de goles, mientras que en el eje vertical se representa la frecuencia, es decir, cuántas veces se repite cada rango de goles. El gráfico permite observar que la mayor concentración de partidos se da entre los 2 y 3 goles anotados, lo que indica que este es un resultado frecuente cuando Barcelona juega fuera de casa.<br><br>Asimismo, se puede notar que anotar 0 o 1 gol como visitante es menos común, mientras que marcar 4 o más goles ocurre con menor frecuencia. En conjunto, el histograma permite identificar patrones en el rendimiento ofensivo del equipo cuando juega fuera de su estadio.</div>", unsafe_allow_html=True)
        st.image("histograma.png", caption='Histograma de goles de Barcelona', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de barras de tarjetas rojas en equipos':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Este gráfico es un gráfico de barras que muestra el promedio de tarjetas rojas por equipo cuando juega como local.<br><br>Cada barra representa a un equipo de fútbol y su altura indica cuántas tarjetas rojas recibe en promedio.<br><br>Esto permite comparar de forma visual qué equipos suelen tener más expulsiones y cuáles menos.<br><br>Los equipos con barras más altas registran un mayor promedio de tarjetas rojas, mientras que los de barras más bajas presentan un comportamiento más disciplinado cuando juegan en casa.</div>", unsafe_allow_html=True)
        st.image("barras.png", caption='Gráfico de barras de tarjetas rojas en equipos', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico circular sobre resultados del Real Madrid como visitante':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Este es un gráfico circular son los resultados del Real Madrid cuando juega como visitante.<br><br>Cada sector representa un tipo de resultado: A = partidos ganados; D = partidos; empatados; H = partidos perdidos<br><br>El tamaño de cada sector indica la proporción de cada resultado.<br><br>Como se observa, el Real Madrid gana la mayoría de sus partidos como visitante (52.6%), seguido de empates (26.3%) y, en menor proporción, derrotas (21.1%). Este gráfico permite visualizar de manera clara el rendimiento del equipo fuera de casa.</div>", unsafe_allow_html=True)
        st.image("pastel.png", caption='Gráfico circular sobre resultados del Real Madrid como visitante', width=500)
        pass
    elif grafico_seleccionado == 'Mapa interactivo de mis películas favoritas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>En este mapa interactivo ubiqué los lugares asociados a mis cinco películas favoritas 🎬, considerando principalmente en donde fueron grabadas. El objetivo es relacionar el cine con espacios reales del mundo y explorar cómo estos lugares contribuyen a la atmósfera y narrativa de cada historia. Por ejemplo, en Shutter Island, marqué el estado de Massachusetts (Estados Unidos), donde se ambienta la historia del hospital psiquiátrico en una isla aislada, espacio que refuerza el suspenso psicológico de la película. En Relatos Salvajes, señalé Salta (Argentina), una de las regiones que representa los escenarios cotidianos donde se desarrollan los distintos relatos que componen la película.<br><br>Asimismo, en La Guerra de los Mundos, ubiqué Nueva York, ciudad clave en el contexto de la invasión extraterrestre y símbolo de caos y resistencia. En el caso de Supercool, marqué Alabama (Estados Unidos) como referencia al contexto suburbano donde se desarrolla la historia de los personajes. Finalmente, en Pearl, indiqué Whanganui (Nueva Zelanda), lugar donde se filmó la película y que aporta una estética rural inquietante acorde al terror psicológico del filme.<br><br>En cada punto del mapa se puede encontrar información básica de las películas, como el director, año de estreno, género y actores principales, lo que permite tener una visión general de cada obra a partir de su ubicación geográfica.</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_peliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)

    


