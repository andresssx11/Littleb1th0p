#Importar Librería de flet
import flet as ft
from flet import*

#Función Principal: La que va a aparecer con la página
def main(page: ft.Page):
    page.scroll=False

    #Definición de La fuente de escritura
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    #Imagen Logo
    img = ft.Image(
        src="https://github.com/andresssx11/Littleb1th0p/blob/main/LOGO.png?raw=true",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

#Función que se va a ejecutar cuando se presione el botón de ayuda
    def ayuda(e):
        # Eliminar todos los elementos de la página
        for aa in page.controls:
            page.remove(aa)
            page.scroll=True
        # Agregar contenido nuevo
        ayuda_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=880),
        ft.Container(ft.Text("Ayuda",color="#3e8c69", selectable=True, font_family="RobotoSlab", 
                             style=ft.TextThemeStyle.HEADLINE_MEDIUM)),
        ft.Container(ft.Text("Al iniciar la aplicación, el usuario será dirigido automáticamente a la pestaña 'Home'. En la parte inferior, se desplegará un menú que consta de 5 pestañas. A continuación, se detalla el propósito de cada pestaña, de izquierda a derecha:",
                             color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=610), 
                             top=40),
        ft.Container (ft.Text("1. Info", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=120, left=20),
        ft.Container (ft.Text("Proporciona información fundamental sobre las bases numéricas implementadas por la aplicación, así como detalles específicos sobre los procesos de conversión entre bases y el código ASCII. Esta pestaña está concebida para abordar interrogantes básicos acerca del funcionamiento intrínseco de la aplicación.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=573,), top=140, left=35),
        ft.Container (ft.Text("2. ASCII", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=220, left=20),
        ft.Container (ft.Text("Muestra un menú doble en la parte superior de la pantalla. El primer menú es la biblioteca, que permite la entrada de un símbolo (encuéntrelos en info) o su correspondiente número decimal según el código ASCII extendido, muestra el resultado según lo que se haya ingresado añadiendo también la tecla a usar según la accesibilidad de Windows. En el segundo menú, se proporciona un codificador de palabras, donde puedes ingresar una cadena de bits para obtener la palabra traducida.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=573,), top=240, left=35),
        ft.Container (ft.Text("3. Home", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=360, left=20),
        ft.Container (ft.Text("Actúa como la pantalla principal de la aplicación, donde se visualizará el logotipo y el nombre de la aplicación.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=573,), top=380, left=35),
        ft.Container (ft.Text("4. Calculadora", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=425, left=20),
        ft.Container (ft.Text("Al acceder a esta pestaña, se observa un nuevo menú en la parte superior de la pantalla. Aquí puedes elegir el tipo de operación matemática deseada, como suma, multiplicación, división y resta. Debes seleccionar las bases con las cuales realizarás la operación y, en la parte inferior donde indica 'resultado', se mostrará la solución a la operación matemática.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=573,), top=445, left=35),
        ft.Container (ft.Text("5. Cambio de base", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=527, left=20),
        ft.Container (ft.Text("Similar a la pestaña de la calculadora, esta sección presenta un espacio para ingresar un número con un lugar para especificar su base. Justo debajo, hay otra sección para seleccionar la base a la cual se desea transformar el número ingresado. Y donde se encuentra la palabra 'resultado' se representará el número ya transformado a la nueva base.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=573,), top=547, left=35),
        ft.Container(ft.Text("Contacto",color="black", selectable=True, font_family="RobotoSlab", 
                             style=(ft.TextThemeStyle.TITLE_LARGE), weight=ft.FontWeight.W_500), top=670),
        ft.Container (ft.Text("» María Alejandra Arango Bocanegra. Celular: +57 312 554 3315. Correo: maarangob@udistrital.edu.co", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=537,), top=705, left=20),
        ft.Container (ft.Text("» Andres Santiago Rodríguez Lopez. Celular: +57 312 672 0831. Correo: ansrodriguezl@udistrital.edu.co", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=537,), top=745, left=20),
        ft.Container (ft.Text("» Luna Manuela Peña Cocco. Celular: +57 320 255 4122. Correo: lmpenac@udistrital.edu.co ", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=537,), top=785, left=20),
        ft.Container(ayuda_abajo, top=840, left=0)])
        page.add(ayuda_)
        page.scroll=True

#Función que se va a ejecutar cuando se oprimar el botón info
    def info(e):
        # Eliminar todos los elementos de la página
        for bb in page.controls:
            page.remove(bb)
            page.scroll=True
        # Agregar contenido nuevo
        info_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=16455),
        ft.Container(ft.Text("Sistemas de Numeración",color="#3e8c69", selectable=True, font_family="RobotoSlab", 
                             style=ft.TextThemeStyle.HEADLINE_MEDIUM)),
        ft.Container(ft.Text("Los sistemas de numeración son sistemas formales utilizados para representar y manipular cantidades numéricas. Cada sistema de numeración tiene reglas específicas para asignar símbolos a cantidades y proporciona un método estructurado para expresar números. Los más comunes son:",
                             color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=610), 
                             top=40),
        ft.Container (ft.Text("1. Sistema Binario (base 2)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=120, left=20),
        ft.Container (ft.Text("-Símbolos:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=140, left=35),
        ft.Container (ft.Text("-Detalles:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=160, left=35),
        ft.Container (ft.Text("0 y 1.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610), top=140, left=105),
        ft.Container (ft.Text("Cada posición en la representación binaria se denomina bit. Los números binarios son fundamentales en la informática, ya que los circuitos digitales y las computadoras operan internamente con señales eléctricas que pueden estar encendidas (1) o apagadas (0). Todas las instrucciones y datos en las computadoras se almacenan y procesan en formato binario.", 
                    color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=512), 
                    top=160, left=98),
        ft.Container (ft.Text("2. Sistema Octal (base 8)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=260, left=20),
        ft.Container (ft.Text("-Símbolos:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=280, left=35),
        ft.Container (ft.Text("-Detalles:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=300, left=35),
        ft.Container (ft.Text("0 al 7.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610), top=280, left=105),
        ft.Container (ft.Text("Cada posición en la representación octal tiene un valor que es una potencia de 8. Aunque hoy en día se utiliza con menos frecuencia que otros sistemas, el sistema octal ha sido históricamente útil en ciertas áreas de programación y en la representación compacta de conjuntos de bits.", 
                    color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=512), 
                    top=300, left=98),
        ft.Container (ft.Text("3. Sistema Decimal (base 10)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=380, left=20),
        ft.Container (ft.Text("-Símbolos:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=400, left=35),
        ft.Container (ft.Text("-Detalles:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=420, left=35),
        ft.Container (ft.Text("0 al 9.", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610), top=400, left=105),
        ft.Container (ft.Text("Es el sistema numérico más común en la vida cotidiana. Utilizado para contar, medir y realizar cálculos en general. Aplicaciones incluyen finanzas, comercio, ciencias sociales, ciencias exactas y cualquier otro contexto que requiera expresar cantidades cotidianas.", 
                    color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=512), 
                    top=420, left=98),
        ft.Container (ft.Text("4. Sistema Hexadecimal (base 16)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=500, left=20),
        ft.Container (ft.Text("-Símbolos:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=520, left=35),
        ft.Container (ft.Text("-Detalles:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=540, left=35),
        ft.Container (ft.Text("0 al 9 y las letras A al F (representando los valores del 10 al 15).", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610), top=520, left=105),
        ft.Container (ft.Text("Muy utilizado en programación y en ciencias de la computación. Permite representar grandes cantidades de datos de manera compacta y es comúnmente utilizado para representar direcciones de memoria y valores en programación de bajo nivel. También es empleado en la representación de colores en HTML y otros contextos.", 
                    color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=512), 
                    top=540, left=98),
        ft.Container(ft.Text("Operaciones Aritméticas",color="black", selectable=True, font_family="RobotoSlab", 
                             style=(ft.TextThemeStyle.TITLE_LARGE), weight=ft.FontWeight.W_500), top=650),
        ft.Container(ft.Text("Las operaciones aritméticas en decimal son las más familiares y siguen las reglas convencionales que todos conocemos. A pesar de que, en otros sistemas numéricos, como binario, octal y hexadecimal, las operaciones también se realizan de la misma forma es crucial tener en cuenta algunas reglas específicas. A continuación, se detallan las consideraciones fundamentales para realizar operaciones en los otros sistemas numéricos:",
                             color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=610), 
                             top=685),
        ft.Container (ft.Text("Tabla 1", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=795, left=20),
        ft.Container (ft.Text("Consideraciones para operaciones aritméticas entre números binarios", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610,), top=815, left=20),
        ft.Container(ft.DataTable(
            columns=[ft.DataColumn(ft.ElevatedButton("Operaciones", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))), 
                     ft.DataColumn(ft.ElevatedButton("Consideraciones en Binario", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))))],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text("Suma", selectable=True)),
                                    ft.DataCell(ft.Text("0+0=0, 1+0=1, 0+1=1, 1+1=0(lleva 1)", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Resta", selectable=True)),
                                  ft.DataCell(ft.Text("0-0=0,1-0=1,1-1=0, 0-1=1(lleva 1)", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Multiplicación", selectable=True)),
                                ft.DataCell(ft.Text("Estándar", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Divisón", selectable=True)),
                                ft.DataCell(ft.Text("Estándar (preferiblemente en forma de resta)", selectable=True)),],),],
                                show_bottom_border=True), top=835, left=20),
        ft.Container (ft.Text("Tabla 2", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=1105, left=20),
        ft.Container (ft.Text("Consideraciones para operaciones aritméticas entre números octales", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610,), top=1125, left=20),
        ft.Container(ft.DataTable(
            columns=[ft.DataColumn(ft.ElevatedButton("Operaciones", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))), 
                     ft.DataColumn(ft.ElevatedButton("Consideraciones en Octal", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))))],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text("Suma", selectable=True)),
                                    ft.DataCell(ft.Text("0+0=0, 1+0=1, …, 7+1=0(lleva 1) , …", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Resta", selectable=True)),
                                  ft.DataCell(ft.Text("Estándar", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Multiplicación", selectable=True)),
                                ft.DataCell(ft.Text("Estándar", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Divisón", selectable=True)),
                                ft.DataCell(ft.Text("Estándar (preferiblemente en forma de resta)", selectable=True)),],),],
                                show_bottom_border=True), top=1145, left=20),
        ft.Container (ft.Text("Tabla 3", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=1415, left=20),
        ft.Container (ft.Text("Consideraciones para operaciones aritméticas entre números hexadecimales", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610,), top=1435, left=20),
        ft.Container(ft.DataTable(
            columns=[ft.DataColumn(ft.ElevatedButton("Operaciones", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))), 
                     ft.DataColumn(ft.ElevatedButton("Consideraciones en Hexadecimal", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))))],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text("Suma", selectable=True)),
                                    ft.DataCell(ft.Text("0+0=0, 1+0=1, …, 9+7=10, A+1=B, …, F+1=0(lleva 1), … ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Resta", selectable=True)),
                                  ft.DataCell(ft.Text("Estándar", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Multiplicación", selectable=True)),
                                ft.DataCell(ft.Text("Estándar", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Divisón", selectable=True)),
                                ft.DataCell(ft.Text("Estándar (preferiblemente en forma de resta)", selectable=True)),],),],
                                show_bottom_border=True), top=1455, left=20),
        ft.Container(ft.Text("Manejo de Números Enteros",color="black", selectable=True, font_family="RobotoSlab", 
                             style=(ft.TextThemeStyle.TITLE_LARGE), weight=ft.FontWeight.W_500), top=1725),
        ft.Container(ft.Text("1. Sistema Decimal (base 10)", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,weight=ft.FontWeight.W_500), top=1760, left=20),
        ft.Container (ft.Text("La representación decimal es la forma estándar en la que expresamos los números en nuestra vida diaria. En este sistema, los enteros se presentan de la misma manera que estamos acostumbrados.", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=1780, left=35),
        ft.Container(ft.Text("2. Sistema Binario (base 2)", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,weight=ft.FontWeight.W_500), top=1842, left=20),
        ft.Container (ft.Text("En el sistema binario, los enteros se representan de manera similar a los enteros decimales, pero se utiliza un bit adicional para indicar el signo (positivo o negativo). Este se conoce como 'bit de signo' o 'bit de complemento a dos'.", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=1862, left=35),
        ft.Container (ft.Text("-Representación de Enteros Positivos", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=1930, left=70),
        ft.Container (ft.Text("Los enteros positivos se representan de manera directa en binario. Por ejemplo, 19₁₀ se representa como 10011₂", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=540,), top=1950, left=70),
        ft.Container (ft.Text("-Representación de Enteros Negativos (Complemento a Dos)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=1990, left=70),
        ft.Container (ft.Text("I. Representación Binaria del Valor Absoluto", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2010, left=78),
        ft.Container (ft.Text("» Encuentra la representación binaria del valor absoluto del número.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610), top=2030, left=93),
        ft.Container (ft.Text("» Por ejemplo, para representar -19₁₀, primero se encuentra la representación binaria de 19₁₀, que es 10011₂", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2050, left=93),
        ft.Container (ft.Text("II. Inversión de Bits (Complemento a Uno)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2090, left=78),
        ft.Container (ft.Text("» Invierte todos los bits (cambiar 0 a 1 y viceversa).", color="black", selectable=True, 
                              font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=610), top=2110, left=93),
        ft.Container (ft.Text("» En nuestro ejemplo, el complemento a uno de 10011₂ sería 01100₂.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2130, left=93),
        ft.Container (ft.Text("III. Suma de 1 al Complemento a Uno (Complemento a Dos)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2150, left=78),
        ft.Container (ft.Text("» Suma 1 al resultado del paso anterior. 01100₂ + 1₂ = 01101₂. Así, la representación binaria de -19₁₀ en complemento a dos es 01101₂.", color="black", selectable=True, 
                              font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=517), top=2170, left=93),
        ft.Container(ft.Text("3. Sistema Octal (base 8)", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,weight=ft.FontWeight.W_500), top=2213, left=20),
        ft.Container (ft.Text("En el sistema octal, la representación de enteros, tanto positivos como negativos, sigue un proceso similar al que se emplea en el sistema binario, pero con base 8.", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=2233, left=35),
        ft.Container (ft.Text("-Representación de Enteros Positivos", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2280, left=70),
        ft.Container (ft.Text("I. Descomposición en Potencias de 8", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2300, left=78),
        ft.Container (ft.Text("» Expresa el número en términos de potencias de 8. Por ejemplo, 57₁₀ se descompone como 5·8¹ + 7·8⁰.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2320, left=93),
        ft.Container (ft.Text("II. Representación Octal", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2360, left=78),
        ft.Container (ft.Text("» Convierte cada potencia de 8 a su equivalente en octal. En este caso, 57₁₀ = 71₈.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2380, left=93),
        ft.Container (ft.Text("-Representación de Enteros Negativos (Complemento a Dos)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2400, left=70),
        ft.Container (ft.Text("I. Representación Octal del Valor Absoluto", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2420, left=78),
        ft.Container (ft.Text("» Encuentra la representación octal del valor absoluto del número.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2440, left=93),
        ft.Container (ft.Text("II. Inversión de Dígitos (Complemento a Uno)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2460, left=78),
        ft.Container (ft.Text("» Invierte cada dígito (cambia 0 a 7, 1 a 6, etc.).", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2480, left=93),
        ft.Container (ft.Text("III. Suma de 1 al Complemento a Uno (Complemento a Dos)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2500, left=78),
        ft.Container (ft.Text("» Suma 1 al resultado obtenido en el paso anterior..", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2520, left=93),
        ft.Container (ft.Text("Por ejemplo, para representar -57₁₀ en octal:", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=2550, left=35),
        ft.Container(ft.Text("■ El valor absoluto de -57₁₀ en octal es 71₈.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=2570, left=55),
        ft.Container(ft.Text("■ El complemento a uno sería 06₈ (inversión de 71₈).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=2590, left=55),
        ft.Container(ft.Text("■ Sumando 1, obtenemos 07₈.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=2610, left=55),
        ft.Container (ft.Text("Entonces, la representación de -57₁₀ en octal sería 07₈ empleando el complemento a 2.", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=2630, left=35),
        ft.Container(ft.Text("4. Sistema Hexadecimal (base 16)", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,weight=ft.FontWeight.W_500), top=2660, left=20),
        ft.Container (ft.Text("La representación de enteros en el sistema hexadecimal, al igual que en sistemas binario y octal, implica considerar tanto los enteros positivos como los negativos.", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=2680, left=35),
        ft.Container (ft.Text("-Representación de Enteros Positivos", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2730, left=70),
        ft.Container (ft.Text("I. Descomposición en Potencias de 16", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2750, left=78),
        ft.Container (ft.Text("» Expresa el número en términos de potencias de 16. Por ejemplo, 112₁₀ se descompone como 6·16¹ + 14·16⁰.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2770, left=93),
        ft.Container (ft.Text("II. Representación Hexadecimal", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2810, left=78),
        ft.Container (ft.Text("» Convierte cada potencia de 16 a su equivalente en hexadecimal. En este caso, 112₁₀ = 70₁₆.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2830, left=93),
        ft.Container (ft.Text("-Representación de Enteros Negativos (Complemento a Dos)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2870, left=70),
        ft.Container (ft.Text("I. Representación Hexadecimal del Valor Absoluto", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2890, left=78),
        ft.Container (ft.Text("» Encuentra la representación hexadecimal del valor absoluto del número.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2910, left=93),
        ft.Container (ft.Text("II. Inversión de Dígitos (Complemento a Uno)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2930, left=78),
        ft.Container (ft.Text("» Invierte cada dígito (cambia 0 a F, 1 a E, etc.).", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2950, left=93),
        ft.Container (ft.Text("III. Suma de 1 al Complemento a Uno (Complemento a Dos)", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=2970, left=78),
        ft.Container (ft.Text("» Suma 1 al resultado obtenido en el paso anterior.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=517), top=2990, left=93),
        ft.Container (ft.Text("Por ejemplo, para representar -112₁₀ en hexadecimal:", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3020, left=35),
        ft.Container(ft.Text("■ El valor absoluto de -112₁₀ en hexadecimal es 70₁₆.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3040, left=55),
        ft.Container(ft.Text("■ El complemento a uno sería 8F₁₆ (inversión de 70₁₆).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3060, left=55),
        ft.Container(ft.Text("■ Sumando 1, obtenemos 90₁₆.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3080, left=55),
        ft.Container (ft.Text("Entonces, la representación de -112₁₀ en hexadecimal sería 90₁₆ empleando el complemento a 2.", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3100, left=35),
        ft.Container(ft.Text("Manejo de Números Reales",color="black", selectable=True, font_family="RobotoSlab", 
                             style=(ft.TextThemeStyle.TITLE_LARGE), weight=ft.FontWeight.W_500), top=3155),
        ft.Container(ft.Text("1. Sistema Decimal (base 10)", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,weight=ft.FontWeight.W_500), top=3190, left=20),
        ft.Container (ft.Text("La representación decimal es la forma estándar en la que expresamos los números en nuestra vida diaria. En este sistema, los enteros se presentan de la misma manera que estamos acostumbrados.", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3210, left=35),
        ft.Container(ft.Text("2. Sistema Binario (base 2)", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,weight=ft.FontWeight.W_500), top=3272, left=20),
        ft.Container (ft.Text("La representación de números reales en el sistema binario se realiza mediante una técnica conocida como punto flotante. Un número real se representa como una fracción binaria multiplicada por una potencia de 2. La forma general de un número en punto flotante es:", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3292, left=35),
        ft.Container (ft.Text("(-1)ˢ · M · 2ᴱ", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="CENTER", width=576), top=3372),
        ft.Container (ft.Text("Donde:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3392, left=35),
        ft.Container(ft.Text("■ s es el bit de signo (0 para positivo, 1 para negativo).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3412, left=55),
        ft.Container(ft.Text("■ M es la mantisa o fracción binaria normalizada.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3432, left=55),
        ft.Container(ft.Text("■ E es el exponente, que determina la potencia de 2 a la que se multiplica la mantisa.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3452, left=55),
        ft.Container (ft.Text("La mantisa se normaliza para tener un solo dígito antes del punto decimal (binario), y el exponente se representa utilizando un exceso de N para asegurar que tanto números positivos como negativos tengan representaciones consistentes. Por ejemplo, el número real -6.25 en binario podría representarse como sigue:", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3482, left=35),
        ft.Container (ft.Text("-6.25 = (-1)¹ · 1.1001 · 22", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="CENTER", width=576), top=3572),
        ft.Container (ft.Text("Donde:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3592, left=35),
        ft.Container(ft.Text("■ El bit de signo (s) es 1 porque el número es negativo.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3612, left=55),
        ft.Container(ft.Text("■ La mantisa (M) es 1.1001 (la parte fraccionaria binaria de 6.25 normalizada).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3632, left=55),
        ft.Container(ft.Text("■ El exponente (E) es 2 (porque 2² = 4).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3652, left=55),
        ft.Container(ft.Text("3. Sistema Octal (base 8)", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,weight=ft.FontWeight.W_500), top=3675, left=20),
        ft.Container (ft.Text("La representación de números reales en el sistema octal sigue un enfoque similar al de la representación binaria, pero emplea una notación octal. Al igual que en binario, los números reales en octal se representan en formato de punto flotante. La forma general de un número real en punto flotante en el sistema octal es:", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3695, left=35),
        ft.Container (ft.Text("(-1)ˢ · M · 8ᴱ", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="CENTER", width=576), top=3785),
        ft.Container (ft.Text("Donde:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3805, left=35),
        ft.Container(ft.Text("■ s es el bit de signo (0 para positivo, 1 para negativo).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3825, left=55),
        ft.Container(ft.Text("■ M es la mantisa o fracción octal normalizada.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3845, left=55),
        ft.Container(ft.Text("■ E es el exponente, que determina la potencia de 8 a la que se multiplica la mantisa.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=3865, left=55),
        ft.Container (ft.Text("La mantisa se normaliza para tener un solo dígito antes del punto octal, y el exponente se representa utilizando un exceso de N para asegurar que tanto números positivos como negativos tengan representaciones consistentes. Por ejemplo, el número real -13.75 en octal podría representarse como sigue:", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=3895, left=35),
        ft.Container (ft.Text("-13.75 = (-1)¹ · 15.6 · 8¹", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="CENTER", width=576), top=3985),
        ft.Container (ft.Text("Donde:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=4005, left=35),
        ft.Container(ft.Text("■ El bit de signo (s) es 1 porque el número es negativo.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4025, left=55),
        ft.Container(ft.Text("■ La mantisa (M) es 15.6 (la parte fraccionaria binaria de 13.75 normalizada).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4045, left=55),
        ft.Container(ft.Text("■ El exponente (E) es 1 (porque 8¹= 8).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4065, left=55),
        ft.Container(ft.Text("4. Sistema Hexadecimal (base 16)", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,weight=ft.FontWeight.W_500), top=4090, left=20),
        ft.Container (ft.Text("La representación de números reales en el sistema hexadecimal sigue el mismo principio que en binario y octal, pero utiliza una notación hexadecimal. Al igual que en binario y octal, los números reales en hexadecimal se representan en formato de punto flotante. La forma general de un número real en punto flotante en el sistema hexadecimal es:", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=4110, left=35),
        ft.Container (ft.Text("(-1)ˢ · M · 16ᴱ", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="CENTER", width=576), top=4200),
        ft.Container (ft.Text("Donde:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=4220, left=35),
        ft.Container(ft.Text("■ s es el bit de signo (0 para positivo, 1 para negativo).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4240, left=55),
        ft.Container(ft.Text("■ M es la mantisa o fracción hexadecimal normalizada.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4260, left=55),
        ft.Container(ft.Text("■ E es el exponente, que determina la potencia de 16 a la que se multiplica la mantisa.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4280, left=55),
        ft.Container (ft.Text("La mantisa se normaliza para tener un solo dígito antes del punto hexadecimal, y el exponente se representa utilizando un exceso de N para asegurar que tanto números positivos como negativos tengan representaciones consistentes. Por ejemplo, el número real -AB.C en hexadecimal podría representarse como sigue:", 
                              color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=4310, left=35),
        ft.Container (ft.Text("-AB.C = (-1)¹ · 10.12 · 16¹", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="CENTER", width=576), top=4400),
        ft.Container (ft.Text("Donde:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=4420, left=35),
        ft.Container(ft.Text("■ El bit de signo (s) es 1 porque el número es negativo.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4440, left=55),
        ft.Container(ft.Text("■ La mantisa (M) es 10.12 (la parte fraccionaria binaria de 13.75 normalizada).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4460, left=55),
        ft.Container(ft.Text("■ El exponente (E) es 1 (porque 16¹= 16).", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4480, left=55),
        ft.Container(ft.Text("Conversiones (Teorema Fundamental de la Numeración)",color="black", selectable=True, font_family="RobotoSlab", 
                             style=(ft.TextThemeStyle.TITLE_LARGE), weight=ft.FontWeight.W_500), top=4515),
        ft.Container(ft.Text("El Teorema Fundamental de la Enumeración establece una relación entre cantidades expresadas en cualquier sistema de enumeración y su equivalente en el sistema decimal. La fórmula asociada a este teorema utiliza una sumatoria, donde cada dígito de la cantidad en la base está representado por un subíndice que indica su posición en relación con el punto decimal. La posición se numera desde 0 hacia la izquierda y desde 0 hacia la derecha, utilizando índices negativos.",
                             color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=610), 
                             top=4550),
        ft.Container (ft.Text("ᵢ₌ᵣ", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, width=576), top=4688, left=245),
        ft.Container (ft.Text("ⁿ", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, width=576), top=4672, left=246),
        ft.Container (ft.Text("Nᵢ = Σ (dígito)ᵢ · (base)ⁱ", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="CENTER", width=576), top=4680),
        ft.Container (ft.Text("Donde:", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=576), top=4718),
        ft.Container(ft.Text("■ i = Posición respecto la coma.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4738),
        ft.Container(ft.Text("■ Dígito = Número según la posición.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4758),
        ft.Container(ft.Text("■ Base = Base del sistema de enumeración.", color="black", selectable=True, font_family="RobotoSlab", size=13, 
                             text_align="JUSTIFY", width=610,), top=4778),
        ft.Container(ft.Text("Cabe resaltar que, si se quiere hacer la conversión de decimal a otras bases, se divide el número decimal por la base que se busca, esto se hace sucesivamente hasta que el cociente resulte en 0. La unión de todos los residuos obtenidos, ordenados desde el último hasta el primero, nos proporciona el número expresado en el nuevo sistema.",
                             color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=610), 
                             top=4808),
        ft.Container (ft.Text("Tabla 4", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=4900, left=20),   
        ft.Container (ft.Text("Representación de los primeros 16 dígitos de los sistemas de numeración decimal, binario, octal y hexadecimal.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=585,), top=4920, left=20), 
        ft.Container(ft.DataTable(
            columns=[ft.DataColumn(ft.ElevatedButton("Decimal", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))), 
                ft.DataColumn(ft.ElevatedButton("Binario", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))),
                ft.DataColumn(ft.ElevatedButton("Octal", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))),
                ft.DataColumn(ft.ElevatedButton("Hexadecimal", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))))],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text("0", selectable=True)),
                                    ft.DataCell(ft.Text("0000", selectable=True)),
                                    ft.DataCell(ft.Text("0", selectable=True)),
                                    ft.DataCell(ft.Text("0", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("1", selectable=True)),
                                    ft.DataCell(ft.Text("0001", selectable=True)),
                                    ft.DataCell(ft.Text("1", selectable=True)),
                                    ft.DataCell(ft.Text("1", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("2", selectable=True)),
                                    ft.DataCell(ft.Text("0010", selectable=True)),
                                    ft.DataCell(ft.Text("2", selectable=True)),
                                    ft.DataCell(ft.Text("2", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("3", selectable=True)),
                                    ft.DataCell(ft.Text("0011", selectable=True)),
                                    ft.DataCell(ft.Text("3", selectable=True)),
                                    ft.DataCell(ft.Text("3", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("4", selectable=True)),
                                    ft.DataCell(ft.Text("0100", selectable=True)),
                                    ft.DataCell(ft.Text("4", selectable=True)),
                                    ft.DataCell(ft.Text("4", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("5", selectable=True)),
                                    ft.DataCell(ft.Text("0101", selectable=True)),
                                    ft.DataCell(ft.Text("5", selectable=True)),
                                    ft.DataCell(ft.Text("5", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("6", selectable=True)),
                                    ft.DataCell(ft.Text("0110", selectable=True)),
                                    ft.DataCell(ft.Text("6", selectable=True)),
                                    ft.DataCell(ft.Text("6", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("7", selectable=True)),
                                    ft.DataCell(ft.Text("0111", selectable=True)),
                                    ft.DataCell(ft.Text("7", selectable=True)),
                                    ft.DataCell(ft.Text("7", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("8", selectable=True)),
                                    ft.DataCell(ft.Text("1000", selectable=True)),
                                    ft.DataCell(ft.Text("10", selectable=True)),
                                    ft.DataCell(ft.Text("8", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("9", selectable=True)),
                                    ft.DataCell(ft.Text("1001", selectable=True)),
                                    ft.DataCell(ft.Text("11", selectable=True)),
                                    ft.DataCell(ft.Text("9", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("10", selectable=True)),
                                    ft.DataCell(ft.Text("1010", selectable=True)),
                                    ft.DataCell(ft.Text("12", selectable=True)),
                                    ft.DataCell(ft.Text("A", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("11", selectable=True)),
                                    ft.DataCell(ft.Text("1011", selectable=True)),
                                    ft.DataCell(ft.Text("13", selectable=True)),
                                    ft.DataCell(ft.Text("B", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("12", selectable=True)),
                                    ft.DataCell(ft.Text("1100", selectable=True)),
                                    ft.DataCell(ft.Text("14", selectable=True)),
                                    ft.DataCell(ft.Text("C", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("13", selectable=True)),
                                    ft.DataCell(ft.Text("1101", selectable=True)),
                                    ft.DataCell(ft.Text("15", selectable=True)),
                                    ft.DataCell(ft.Text("D", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("14", selectable=True)),
                                    ft.DataCell(ft.Text("1110", selectable=True)),
                                    ft.DataCell(ft.Text("16", selectable=True)),
                                    ft.DataCell(ft.Text("E", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("15", selectable=True)),
                                    ft.DataCell(ft.Text("1111", selectable=True)),
                                    ft.DataCell(ft.Text("17", selectable=True)),
                                    ft.DataCell(ft.Text("F", selectable=True)),],),],
                                show_bottom_border=True, column_spacing=40, data_row_max_height=40), top=4960, left=20),
        ft.Container(ft.Text("Código ASCII Extendido",color="#3e8c69", selectable=True, font_family="RobotoSlab", 
                             style=ft.TextThemeStyle.HEADLINE_MEDIUM), top=5680),
        ft.Container(ft.Text("El código ASCII extendido es una variante del estándar ASCII (American Standard Code for Information Interchange) que incluye un conjunto más amplio de carácteres. Mientras que el estándar ASCII original utiliza 7 bits para representar un total de 128 caracteres, el código ASCII extendido utiliza 8 bits, permitiendo la representación de 256 caracteres. La extensión del conjunto de caracteres en el código ASCII extendido permite incluir símbolos adicionales, letras acentuadas, caracteres especiales, y otros elementos que no estaban presentes en el ASCII estándar. Al utilizar 8 bits en lugar de 7, se añade una capacidad adicional para representar más carácteres y símbolos siendo útil para idiomas que utilizan carácteres acentuados, como el español, francés, alemán, entre otros. Además, incluye caracteres especiales, signos de puntuación extendidos y símbolos matemáticos.",
                             color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=610), 
                             top=5720),
        ft.Container (ft.Text("Codificación", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=5920, left=20),
        ft.Container(ft.Text("La codificación en el código ASCII extendido sigue el mismo principio básico que el estándar ASCII, pero en este caso, se utiliza un byte completo (8 bits) en lugar de 7 bits. El código ASCII extendido, asigna valores numéricos a un conjunto de carácteres. Estos se representan mediante un número decimal entre 0 y 255. Por ejemplo, el valor decimal 65 (correspondiente a la letra 'A') se representa como '1000001' en binario, pero al ser una cadena de 7 bits se rellenaría de '0s' para completar la cadena de 8 bits '01000001'",
                             color="black", selectable=True, font_family="RobotoSlab", size=13, text_align="JUSTIFY", width=590), 
                             top=5940, left=20), 
        ft.Container (ft.Text("Tabla 5", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=610, weight=ft.FontWeight.W_500), top=6070, left=20),   
        ft.Container (ft.Text("Carácteres de código ASCII con su respectivo símbolo y representación decimal.", color="black", selectable=True, font_family="RobotoSlab", 
                              size=13, text_align="JUSTIFY", width=585,), top=6090, left=20),
        ft.Container(ft.DataTable(
            columns=[ ft.DataColumn(ft.ElevatedButton("№", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))),
                ft.DataColumn(ft.ElevatedButton("Carácter", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))),
                ft.DataColumn(ft.ElevatedButton("Simbolo", bgcolor="#9cc4b2", color="black",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))))],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text("0", selectable=True)),
                                    ft.DataCell(ft.Text("Carácter nulo (NULL)", selectable=True)),
                                    ft.DataCell(ft.Text("NULL/null", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("1", selectable=True)),
                                    ft.DataCell(ft.Text("Inicio de encabezado (SOH)", selectable=True)),
                                    ft.DataCell(ft.Text("SOH/soh", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("2", selectable=True)),
                                    ft.DataCell(ft.Text("Inicio de texto (STX)", selectable=True)),
                                    ft.DataCell(ft.Text("STX/stx", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("3", selectable=True)),
                                    ft.DataCell(ft.Text("Fin de texto (ETX)", selectable=True)),
                                    ft.DataCell(ft.Text("ETX/etx", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("4", selectable=True)),
                                    ft.DataCell(ft.Text("Fin de transmisión (EOT)", selectable=True)),
                                    ft.DataCell(ft.Text("EOT/eot", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("5", selectable=True)),
                                    ft.DataCell(ft.Text("Consulta (ENQ)", selectable=True)),
                                    ft.DataCell(ft.Text("ENQ/enq", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("6", selectable=True)),
                                    ft.DataCell(ft.Text("Reconocimiento (ACK)", selectable=True)),
                                    ft.DataCell(ft.Text("ACK/ack", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("7", selectable=True)),
                                    ft.DataCell(ft.Text("Timbre (BEL)", selectable=True)),
                                    ft.DataCell(ft.Text("BEL/bel", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("8", selectable=True)),
                                    ft.DataCell(ft.Text("Retroceso (BS)", selectable=True)),
                                    ft.DataCell(ft.Text("BS/bs", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("9", selectable=True)),
                                    ft.DataCell(ft.Text("Tabulador horizontal (HT)", selectable=True)),
                                    ft.DataCell(ft.Text("HT/ht", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("10", selectable=True)),
                                    ft.DataCell(ft.Text("Nueva línea (LF)", selectable=True)),
                                    ft.DataCell(ft.Text("LF/lf", selectable=True)),],),
                 ft.DataRow(cells=[ft.DataCell(ft.Text("11", selectable=True)),
                                    ft.DataCell(ft.Text("Tabulador vertical (VT)", selectable=True)),
                                    ft.DataCell(ft.Text("VT/vt", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("12", selectable=True)),
                                    ft.DataCell(ft.Text("Nueva página (FF)", selectable=True)),
                                    ft.DataCell(ft.Text("FF/ff", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("13", selectable=True)),
                                    ft.DataCell(ft.Text("ENTER (CR)", selectable=True)),
                                    ft.DataCell(ft.Text("CR/cr", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("14", selectable=True)),
                                    ft.DataCell(ft.Text("Desplazamiento hacia afuera (SO)", selectable=True)),
                                    ft.DataCell(ft.Text("SO/so", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("15", selectable=True)),
                                    ft.DataCell(ft.Text("Desplazamiento hacia adentro (SI)", selectable=True)),
                                    ft.DataCell(ft.Text("SI/si", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("16", selectable=True)),
                                    ft.DataCell(ft.Text("Escape de vínculo de datos (DLE)", selectable=True)),
                                    ft.DataCell(ft.Text("DLE/dle", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("17", selectable=True)),
                                    ft.DataCell(ft.Text("Control dispositivo 1 (DC1)", selectable=True)),
                                    ft.DataCell(ft.Text("DC1/dc1", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("18", selectable=True)),
                                    ft.DataCell(ft.Text("Control dispositivo 1 (DC2)", selectable=True)),
                                    ft.DataCell(ft.Text("DC2/dc2", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("19", selectable=True)),
                                    ft.DataCell(ft.Text("Control dispositivo 1 (DC3)", selectable=True)),
                                    ft.DataCell(ft.Text("DC3/dc3", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("20", selectable=True)),
                                    ft.DataCell(ft.Text("Control dispositivo 1 (DC4)", selectable=True)),
                                    ft.DataCell(ft.Text("DC4/dc4", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("21", selectable=True)),
                                    ft.DataCell(ft.Text("Confirmación negativa (NAK)", selectable=True)),
                                    ft.DataCell(ft.Text("NAK/nak", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("22", selectable=True)),
                                    ft.DataCell(ft.Text("Inactividad sincrónica (SYN)", selectable=True)),
                                    ft.DataCell(ft.Text("SYN/syn", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("23", selectable=True)),
                                    ft.DataCell(ft.Text("Fin del bloque de transmisión (ETB)", selectable=True)),
                                    ft.DataCell(ft.Text("ETB/etb", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("24", selectable=True)),
                                ft.DataCell(ft.Text("Cancelar (CAN)", selectable=True)),
                                ft.DataCell(ft.Text("CAN/can", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("25", selectable=True)),
                                ft.DataCell(ft.Text("Fin del medio (EM)", selectable=True)),
                                ft.DataCell(ft.Text("EM/em", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("26", selectable=True)),
                                ft.DataCell(ft.Text("Sustitución (SUB)", selectable=True)),
                                ft.DataCell(ft.Text("SUB/sub", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("27", selectable=True)),
                                  ft.DataCell(ft.Text("Escape (ESC)", selectable=True)),
                                  ft.DataCell(ft.Text("ESC/esc", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("28", selectable=True)), 
                                  ft.DataCell(ft.Text("Separador de archivos (FS)", selectable=True)),
                                  ft.DataCell(ft.Text("FS/fs", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("29", selectable=True)),
                                ft.DataCell(ft.Text("Separador de grupos (GS)", selectable=True)),
                                ft.DataCell(ft.Text("GS/gs", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("30", selectable=True)),
                                  ft.DataCell(ft.Text("Separador de registros (RS)", selectable=True)),
                                  ft.DataCell(ft.Text("RS/rs", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("31", selectable=True)),
                                  ft.DataCell(ft.Text("Separador de unidades (US)", selectable=True)),
                                  ft.DataCell(ft.Text("US/us", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("32", selectable=True)),
                                  ft.DataCell(ft.Text("Espacio (Espacio en blanco)", selectable=True)),
                                  ft.DataCell(ft.Text("Espacio", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("33", selectable=True)),
                                  ft.DataCell(ft.Text("Signo de exclamación (Cierre)", selectable=True)),
                                  ft.DataCell(ft.Text("!", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("34", selectable=True)),
                                  ft.DataCell(ft.Text("Comillas dobles", selectable=True)),
                                  ft.DataCell(ft.Text('"', selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("35", selectable=True)),
                                    ft.DataCell(ft.Text("Signo numeral", selectable=True)),
                                    ft.DataCell(ft.Text("#", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("36", selectable=True)),
                                    ft.DataCell(ft.Text("Signo pesos", selectable=True)),
                                    ft.DataCell(ft.Text("$", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("37", selectable=True)),
                                    ft.DataCell(ft.Text("Signo de porcentaje", selectable=True)),
                                    ft.DataCell(ft.Text("%", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("38", selectable=True)),
                                    ft.DataCell(ft.Text("Ampersand ", selectable=True)),
                                    ft.DataCell(ft.Text("&", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("39", selectable=True)),
                                    ft.DataCell(ft.Text("Comillas simples", selectable=True)),
                                    ft.DataCell(ft.Text("'", selectable=True)),],), 
                ft.DataRow(cells=[ft.DataCell(ft.Text("40", selectable=True)),
                                    ft.DataCell(ft.Text("Abre paréntesis", selectable=True)),
                                    ft.DataCell(ft.Text("(", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("41", selectable=True)),
                                    ft.DataCell(ft.Text("Cierra paréntesis", selectable=True)),
                                    ft.DataCell(ft.Text(")", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("42", selectable=True)),
                                    ft.DataCell(ft.Text("Asterisco", selectable=True)),
                                    ft.DataCell(ft.Text("*", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("43", selectable=True)),
                                    ft.DataCell(ft.Text("Signo más", selectable=True)),
                                    ft.DataCell(ft.Text("+", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("44", selectable=True)),
                                    ft.DataCell(ft.Text("Coma", selectable=True)),
                                    ft.DataCell(ft.Text(",", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("45", selectable=True)),
                                    ft.DataCell(ft.Text("Signo menos", selectable=True)),
                                    ft.DataCell(ft.Text("-", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("46", selectable=True)),
                                    ft.DataCell(ft.Text("Punto", selectable=True)),
                                    ft.DataCell(ft.Text(".", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("47", selectable=True)),
                                    ft.DataCell(ft.Text("Barra Inclinada", selectable=True)),
                                    ft.DataCell(ft.Text("/", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("48", selectable=True)),
                                    ft.DataCell(ft.Text("Número cero", selectable=True)),
                                    ft.DataCell(ft.Text("0", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("49", selectable=True)),
                                    ft.DataCell(ft.Text("Número uno", selectable=True)),
                                    ft.DataCell(ft.Text("1", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("50", selectable=True)),
                                    ft.DataCell(ft.Text("Número dos", selectable=True)),
                                    ft.DataCell(ft.Text("2", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("51", selectable=True)),
                                    ft.DataCell(ft.Text("Número tres", selectable=True)),
                                    ft.DataCell(ft.Text("3", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("52", selectable=True)),
                                    ft.DataCell(ft.Text("Número cuatro", selectable=True)),
                                    ft.DataCell(ft.Text("4", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("53", selectable=True)),
                                    ft.DataCell(ft.Text("Número cinco", selectable=True)),
                                    ft.DataCell(ft.Text("5", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("54", selectable=True)),
                                    ft.DataCell(ft.Text("Número seis", selectable=True)),
                                    ft.DataCell(ft.Text("6", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("55", selectable=True)),
                                    ft.DataCell(ft.Text("Número siete", selectable=True)),
                                    ft.DataCell(ft.Text("7", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("56", selectable=True)),
                                    ft.DataCell(ft.Text("Número ocho", selectable=True)),
                                    ft.DataCell(ft.Text("8", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("57", selectable=True)),
                                    ft.DataCell(ft.Text("Número nueve", selectable=True)),
                                    ft.DataCell(ft.Text("9", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("58", selectable=True)),
                                    ft.DataCell(ft.Text("Dos puntos", selectable=True)),
                                    ft.DataCell(ft.Text(":", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("59", selectable=True)),
                                    ft.DataCell(ft.Text("Punto y coma", selectable=True)),
                                    ft.DataCell(ft.Text(";", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("60", selectable=True)),
                                    ft.DataCell(ft.Text("Menor que", selectable=True)),
                                    ft.DataCell(ft.Text("<", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("61", selectable=True)),
                                    ft.DataCell(ft.Text("Signo gual", selectable=True)),
                                    ft.DataCell(ft.Text("=", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("62", selectable=True)),
                                    ft.DataCell(ft.Text("Mayor que", selectable=True)),
                                    ft.DataCell(ft.Text(">", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("63", selectable=True)),
                                    ft.DataCell(ft.Text("Signo interrogación (cierre)", selectable=True)),
                                    ft.DataCell(ft.Text("?", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("64", selectable=True)),
                                    ft.DataCell(ft.Text("Arroba", selectable=True)),
                                    ft.DataCell(ft.Text("@", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("65", selectable=True)),
                                    ft.DataCell(ft.Text("Letra A mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("A", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("66", selectable=True)),
                                    ft.DataCell(ft.Text("Letra B mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("B", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("67", selectable=True)),
                                    ft.DataCell(ft.Text("Letra C mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("C", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("68", selectable=True)),
                                    ft.DataCell(ft.Text("Letra D mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("D", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("69", selectable=True)),
                                    ft.DataCell(ft.Text("Letra E mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("E", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("70", selectable=True)),
                                    ft.DataCell(ft.Text("Letra F mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("F", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("71", selectable=True)),
                                    ft.DataCell(ft.Text("Letra G mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("G", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("72", selectable=True)),
                                    ft.DataCell(ft.Text("Letra H mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("H", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("73", selectable=True)),
                                    ft.DataCell(ft.Text("Letra I mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("I", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("74", selectable=True)),
                                    ft.DataCell(ft.Text("Letra J mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("J", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("75", selectable=True)),
                                    ft.DataCell(ft.Text("Letra K mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("K", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("76", selectable=True)),
                                    ft.DataCell(ft.Text("Letra L mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("L", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("77", selectable=True)),
                                    ft.DataCell(ft.Text("Letra M mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("M", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("78", selectable=True)),
                                    ft.DataCell(ft.Text("Letra N mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("N", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("79", selectable=True)),
                                    ft.DataCell(ft.Text("Letra O mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("O", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("80", selectable=True)),
                                    ft.DataCell(ft.Text("Letra P mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("P", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("81", selectable=True)),
                                    ft.DataCell(ft.Text("Letra Q mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("Q", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("82", selectable=True)),
                                    ft.DataCell(ft.Text("Letra R mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("R", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("83", selectable=True)),
                                    ft.DataCell(ft.Text("Letra S mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("S", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("84", selectable=True)),
                                    ft.DataCell(ft.Text("Letra T mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("T", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("85", selectable=True)),
                                    ft.DataCell(ft.Text("Letra U mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("U", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("86", selectable=True)),
                                    ft.DataCell(ft.Text("Letra V mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("V", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("87", selectable=True)),
                                    ft.DataCell(ft.Text("Letra W mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("W", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("88", selectable=True)),
                                    ft.DataCell(ft.Text("Letra X mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("X", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("89", selectable=True)),
                                    ft.DataCell(ft.Text("Letra Y mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("Y", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("90", selectable=True)),
                                    ft.DataCell(ft.Text("Letra Z mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("Z", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("91", selectable=True)),
                                    ft.DataCell(ft.Text("Abre corchetes", selectable=True)),
                                    ft.DataCell(ft.Text("[", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("92", selectable=True)),
                                    ft.DataCell(ft.Text("Contrabarra", selectable=True)),
                                    ft.DataCell(ft.Text("\\", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("93", selectable=True)),
                                    ft.DataCell(ft.Text("Cierra corchetes", selectable=True)),
                                    ft.DataCell(ft.Text("]", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("94", selectable=True)),
                                    ft.DataCell(ft.Text("Intercalación", selectable=True)),
                                    ft.DataCell(ft.Text("^", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("95", selectable=True)),
                                    ft.DataCell(ft.Text("Guión bajo", selectable=True)),
                                    ft.DataCell(ft.Text("_", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("96", selectable=True)),
                                    ft.DataCell(ft.Text("Acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("`", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("97", selectable=True)),
                                    ft.DataCell(ft.Text("Letra a minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("a", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("98", selectable=True)),
                                    ft.DataCell(ft.Text("Letra b minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("b", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("99", selectable=True)),
                                    ft.DataCell(ft.Text("Letra c minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("c", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("100", selectable=True)),
                                    ft.DataCell(ft.Text("Letra d minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("d", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("101", selectable=True)),
                                    ft.DataCell(ft.Text("Letra e minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("e", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("102", selectable=True)),
                                    ft.DataCell(ft.Text("Letra f minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("f", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("103", selectable=True)),
                                    ft.DataCell(ft.Text("Letra g minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("g", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("104", selectable=True)),
                                    ft.DataCell(ft.Text("Letra h minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("h", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("105", selectable=True)),
                                    ft.DataCell(ft.Text("Letra i minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("i", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("106", selectable=True)),
                                    ft.DataCell(ft.Text("Letra j minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("j", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("107", selectable=True)),
                                    ft.DataCell(ft.Text("Letra k minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("k", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("108", selectable=True)),
                                    ft.DataCell(ft.Text("Letra l minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("l", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("109", selectable=True)),
                                    ft.DataCell(ft.Text("Letra m minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("m", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("110", selectable=True)),
                                    ft.DataCell(ft.Text("Letra n minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("n", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("111", selectable=True)),
                                    ft.DataCell(ft.Text("Letra o minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("o", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("112", selectable=True)),
                                    ft.DataCell(ft.Text("Letra p minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("p", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("113", selectable=True)),
                                    ft.DataCell(ft.Text("Letra q minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("q", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("114", selectable=True)),
                                    ft.DataCell(ft.Text("Letra r minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("r", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("115", selectable=True)),
                                    ft.DataCell(ft.Text("Letra s minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("s", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("116", selectable=True)),
                                    ft.DataCell(ft.Text("Letra t minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("t", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("117", selectable=True)),
                                    ft.DataCell(ft.Text("Letra u minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("u", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("118", selectable=True)),
                                    ft.DataCell(ft.Text("Letra v minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("v", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("119", selectable=True)),
                                    ft.DataCell(ft.Text("Letra w minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("w", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("120", selectable=True)),
                                    ft.DataCell(ft.Text("Letra x minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("x", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("121", selectable=True)),
                                    ft.DataCell(ft.Text("Letra y minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("y", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("122", selectable=True)),
                                    ft.DataCell(ft.Text("Letra z minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("z", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("123", selectable=True)),
                                    ft.DataCell(ft.Text("Abre llave", selectable=True)),
                                    ft.DataCell(ft.Text("{", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("124", selectable=True)),
                                    ft.DataCell(ft.Text("Barra vertical", selectable=True)),
                                    ft.DataCell(ft.Text("|", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("125", selectable=True)),
                                    ft.DataCell(ft.Text("Cierra llave", selectable=True)),
                                    ft.DataCell(ft.Text("}", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("126", selectable=True)),
                                    ft.DataCell(ft.Text("Virgulilla", selectable=True)),
                                    ft.DataCell(ft.Text("~", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("127", selectable=True)),
                                    ft.DataCell(ft.Text("Borrar (DEL)", selectable=True)),
                                    ft.DataCell(ft.Text("DEL/del", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("128", selectable=True)),
                                    ft.DataCell(ft.Text("Letra C cedilla mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("Ç", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("129", selectable=True)),
                                    ft.DataCell(ft.Text("Letra u minúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("ü", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("130", selectable=True)),
                                    ft.DataCell(ft.Text("Letra e minúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("é", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("131", selectable=True)),
                                    ft.DataCell(ft.Text("Letra a minúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("â", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("132", selectable=True)),
                                    ft.DataCell(ft.Text("Letra a minúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("ä", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("133", selectable=True)),
                                    ft.DataCell(ft.Text("Letra a minúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("à", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("134", selectable=True)),
                                    ft.DataCell(ft.Text("Letra a minúscula con anillo", selectable=True)),
                                    ft.DataCell(ft.Text("å", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("135", selectable=True)),
                                    ft.DataCell(ft.Text("Letra c cedilla minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("ç", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("136", selectable=True)),
                                    ft.DataCell(ft.Text("Letra e minúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("ê", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("137", selectable=True)),
                                    ft.DataCell(ft.Text("Letra e minúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("ë", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("138", selectable=True)),
                                    ft.DataCell(ft.Text("Letra e minúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("è", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("139", selectable=True)),
                                    ft.DataCell(ft.Text("Letra i minúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("ï", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("140", selectable=True)),
                                    ft.DataCell(ft.Text("Letra i minúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("î", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("141", selectable=True)),
                                    ft.DataCell(ft.Text("Letra i minúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("ì", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("142", selectable=True)),
                                    ft.DataCell(ft.Text("Letra A mayúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("Ä", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("143", selectable=True)),
                                    ft.DataCell(ft.Text("Letra A mayúscula con anillo", selectable=True)),
                                    ft.DataCell(ft.Text("Å", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("144", selectable=True)),
                                    ft.DataCell(ft.Text("Letra E mayúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("É", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("145", selectable=True)),
                                    ft.DataCell(ft.Text("Diptongo latino ae minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("æ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("146", selectable=True)),
                                    ft.DataCell(ft.Text("Diptongo latino AE mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("Æ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("147", selectable=True)),
                                    ft.DataCell(ft.Text("Letra o minúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("ô", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("148", selectable=True)),
                                    ft.DataCell(ft.Text("Letra o minúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("ö", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("149", selectable=True)),
                                    ft.DataCell(ft.Text("Letra o minúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("ò", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("150", selectable=True)),
                                    ft.DataCell(ft.Text("Letra u minúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("û", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("151", selectable=True)),
                                    ft.DataCell(ft.Text("Letra u minúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("ù", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("152", selectable=True)),
                                    ft.DataCell(ft.Text("Letra y minúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("ÿ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("153", selectable=True)),
                                    ft.DataCell(ft.Text("Letra O mayúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("Ö", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("154", selectable=True)),
                                    ft.DataCell(ft.Text("Letra U mayúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("Ü", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("155", selectable=True)),
                                    ft.DataCell(ft.Text("Letra o minúscula con barra inclinada", selectable=True)),
                                    ft.DataCell(ft.Text("ø", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("156", selectable=True)),
                                    ft.DataCell(ft.Text("Signo libra esterlina", selectable=True)),
                                    ft.DataCell(ft.Text("£", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("157", selectable=True)),
                                    ft.DataCell(ft.Text("Letra O mayúscula con barra inclinada", selectable=True)),
                                    ft.DataCell(ft.Text("Ø", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("158", selectable=True)),
                                    ft.DataCell(ft.Text("Signo de multiplicación", selectable=True)),
                                    ft.DataCell(ft.Text("×", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("159", selectable=True)),
                                    ft.DataCell(ft.Text("Signo de función", selectable=True)),
                                    ft.DataCell(ft.Text("ƒ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("160", selectable=True)),
                                    ft.DataCell(ft.Text("Letra a minúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("á", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("161", selectable=True)),
                                    ft.DataCell(ft.Text("Letra i minúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("í", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("162", selectable=True)),
                                    ft.DataCell(ft.Text("Letra o minúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("ó", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("163", selectable=True)),
                                    ft.DataCell(ft.Text("Letra u minúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("ú", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("164", selectable=True)),
                                    ft.DataCell(ft.Text("Letra ñ minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("ñ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("165", selectable=True)),
                                    ft.DataCell(ft.Text("Letra Ñ mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("Ñ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("166", selectable=True)),
                                    ft.DataCell(ft.Text("Ordinal femenino", selectable=True)),
                                    ft.DataCell(ft.Text("ª", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("167", selectable=True)),
                                    ft.DataCell(ft.Text("Ordinal masculino", selectable=True)),
                                    ft.DataCell(ft.Text("º", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("168", selectable=True)),
                                    ft.DataCell(ft.Text("Signo interrogación (apertura)", selectable=True)),
                                    ft.DataCell(ft.Text("¿", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("169", selectable=True)),
                                    ft.DataCell(ft.Text("Signo de marca registrada", selectable=True)),
                                    ft.DataCell(ft.Text("®", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("170", selectable=True)),
                                    ft.DataCell(ft.Text("Signo de negación", selectable=True)),
                                    ft.DataCell(ft.Text("¬", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("171", selectable=True)),
                                    ft.DataCell(ft.Text("Fracción 1/2", selectable=True)),
                                    ft.DataCell(ft.Text("½", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("172", selectable=True)),
                                    ft.DataCell(ft.Text("Fracción 1/4", selectable=True)),
                                    ft.DataCell(ft.Text("¼", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("173", selectable=True)),
                                    ft.DataCell(ft.Text("Signo de exclamación (Apertura)", selectable=True)),
                                    ft.DataCell(ft.Text("¡", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("174", selectable=True)),
                                    ft.DataCell(ft.Text("Comillas bajas (apertura)", selectable=True)),
                                    ft.DataCell(ft.Text("«", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("175", selectable=True)),
                                    ft.DataCell(ft.Text("Comillas bajas (cierre)", selectable=True)),
                                    ft.DataCell(ft.Text("»", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("176", selectable=True)),
                                    ft.DataCell(ft.Text("Bloque color tramado densidad baja", selectable=True)),
                                    ft.DataCell(ft.Text("░", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("177", selectable=True)),
                                    ft.DataCell(ft.Text("Bloque color tramado densidad media", selectable=True)),
                                    ft.DataCell(ft.Text("▒", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("178", selectable=True)),
                                    ft.DataCell(ft.Text("Bloque color tramado densidad alta", selectable=True)),
                                    ft.DataCell(ft.Text("▓", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("179", selectable=True)),
                                    ft.DataCell(ft.Text("Línea simple vertical de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("│", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("180", selectable=True)),
                                    ft.DataCell(ft.Text("Línea vertical con empalme de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("┤", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("181", selectable=True)),
                                    ft.DataCell(ft.Text("Letra A mayúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("Á", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("182", selectable=True)),
                                    ft.DataCell(ft.Text("Letra A mayúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("Â", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("183", selectable=True)),
                                    ft.DataCell(ft.Text("Letra A mayúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("À", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("184", selectable=True)),
                                    ft.DataCell(ft.Text("Símbolo Copyright", selectable=True)),
                                    ft.DataCell(ft.Text("©", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("185", selectable=True)),
                                    ft.DataCell(ft.Text("Doble línea vertical empalme izquierdo", selectable=True)),
                                    ft.DataCell(ft.Text("╣", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("186", selectable=True)),
                                    ft.DataCell(ft.Text("Líneas doble vertical de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("║", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("187", selectable=True)),
                                    ft.DataCell(ft.Text("Línea doble esquina superior derecha de recuadro", selectable=True)),
                                    ft.DataCell(ft.Text("╗", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("188", selectable=True)),
                                    ft.DataCell(ft.Text("Línea doble esquina inferior derecha de recuadro", selectable=True)),
                                    ft.DataCell(ft.Text("╝", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("189", selectable=True)),
                                    ft.DataCell(ft.Text("Signo centavo", selectable=True)),
                                    ft.DataCell(ft.Text("¢", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("190", selectable=True)),
                                    ft.DataCell(ft.Text("Signo YUAN chino", selectable=True)),
                                    ft.DataCell(ft.Text("¥", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("191", selectable=True)),
                                    ft.DataCell(ft.Text("Línea simple esquina de recuadro gráfico (1)", selectable=True)),
                                    ft.DataCell(ft.Text("┐", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("192", selectable=True)),
                                    ft.DataCell(ft.Text("Línea simple esquina de recuadro gráfico (2)", selectable=True)),
                                    ft.DataCell(ft.Text("└", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("193", selectable=True)),
                                    ft.DataCell(ft.Text("Línea horizontal con empalme de recuadro gráfico (1)", selectable=True)),
                                    ft.DataCell(ft.Text("┴", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("194", selectable=True)),
                                    ft.DataCell(ft.Text("Línea horizontal con empalme de recuadro gráfico (2)", selectable=True)),
                                    ft.DataCell(ft.Text("┬", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("195", selectable=True)),
                                    ft.DataCell(ft.Text("Línea vertical con empalme de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("├", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("196", selectable=True)),
                                    ft.DataCell(ft.Text("Línea simple horizontal de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("─", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("197", selectable=True)),
                                    ft.DataCell(ft.Text("Líneas simples empalmes de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("┼", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("198", selectable=True)),
                                    ft.DataCell(ft.Text("Letra a minúscula con virgulilla", selectable=True)),
                                    ft.DataCell(ft.Text("ã", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("199", selectable=True)),
                                    ft.DataCell(ft.Text("Letra A mayúscula con virgulilla", selectable=True)),
                                    ft.DataCell(ft.Text("Ã", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("200", selectable=True)),
                                    ft.DataCell(ft.Text("Línea doble esquina inferior izquierda de recuadro", selectable=True)),
                                    ft.DataCell(ft.Text("╚", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("201", selectable=True)),
                                    ft.DataCell(ft.Text("Línea doble esquina superior izquierda de recuadro", selectable=True)),
                                    ft.DataCell(ft.Text("╔", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("202", selectable=True)),
                                    ft.DataCell(ft.Text("Doble línea horizontal empalme arriba de recuadro", selectable=True)),
                                    ft.DataCell(ft.Text("╩", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("203", selectable=True)),
                                    ft.DataCell(ft.Text("Doble línea horizontal empalme abajo de recuadro", selectable=True)),
                                    ft.DataCell(ft.Text("╦", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("204", selectable=True)),
                                    ft.DataCell(ft.Text("Doble línea vertical empalme derecho de recuadro", selectable=True)),
                                    ft.DataCell(ft.Text("╠", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("205", selectable=True)),
                                    ft.DataCell(ft.Text("Líneas dobles horizontales de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("═", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("206", selectable=True)),
                                    ft.DataCell(ft.Text("Líneas dobles cruce de líneas de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("╬", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("207", selectable=True)),
                                    ft.DataCell(ft.Text("Símbolo de unidad monetaria", selectable=True)),
                                    ft.DataCell(ft.Text("¤", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("208", selectable=True)),
                                    ft.DataCell(ft.Text("Letra eth latina minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("ð", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("209", selectable=True)),
                                    ft.DataCell(ft.Text("Letra eth latina mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("Ð", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("210", selectable=True)),
                                    ft.DataCell(ft.Text("Letra E mayúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("Ê", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("211", selectable=True)),
                                    ft.DataCell(ft.Text("Letra E mayúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("Ë", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("212", selectable=True)),
                                    ft.DataCell(ft.Text("Letra E mayúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("È", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("213", selectable=True)),
                                    ft.DataCell(ft.Text("Letra minuscula i sin punto", selectable=True)),
                                    ft.DataCell(ft.Text("ı", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("214", selectable=True)),
                                    ft.DataCell(ft.Text("Letra I mayúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("Í", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("215", selectable=True)),
                                    ft.DataCell(ft.Text("Letra I mayúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("Î", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("216", selectable=True)),
                                    ft.DataCell(ft.Text("Letra I mayúscula con diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("Ï", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("217", selectable=True)),
                                    ft.DataCell(ft.Text("Línea simple esquina de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("┘", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("218", selectable=True)),
                                    ft.DataCell(ft.Text("Línea simple esquina de recuadro gráfico", selectable=True)),
                                    ft.DataCell(ft.Text("┌", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("219", selectable=True)),
                                    ft.DataCell(ft.Text("Rectángulo relleno", selectable=True)),
                                    ft.DataCell(ft.Text("█", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("220", selectable=True)),
                                    ft.DataCell(ft.Text("Media mitad inferior de rectángulo relleno", selectable=True)),
                                    ft.DataCell(ft.Text("▄", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("221", selectable=True)),
                                    ft.DataCell(ft.Text("Barra vertical partida", selectable=True)),
                                    ft.DataCell(ft.Text("¦", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("222", selectable=True)),
                                    ft.DataCell(ft.Text("Letra I mayúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("Ì", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("223", selectable=True)),
                                    ft.DataCell(ft.Text("Media mitad superior de rectángulo relleno", selectable=True)),
                                    ft.DataCell(ft.Text("▀", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("224", selectable=True)),
                                    ft.DataCell(ft.Text("Letra O mayúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("Ó", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("225", selectable=True)),
                                    ft.DataCell(ft.Text("Letra alemana eszett", selectable=True)),
                                    ft.DataCell(ft.Text("ß", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("226", selectable=True)),
                                    ft.DataCell(ft.Text("Letra O mayúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("Ô", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("227", selectable=True)),
                                    ft.DataCell(ft.Text("Letra O mayúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("Ò", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("228", selectable=True)),
                                    ft.DataCell(ft.Text("Letra o minúscula con virgulilla", selectable=True)),
                                    ft.DataCell(ft.Text("õ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("229", selectable=True)),
                                    ft.DataCell(ft.Text("Letra O minúscula con virgulilla", selectable=True)),
                                    ft.DataCell(ft.Text("Õ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("230", selectable=True)),
                                    ft.DataCell(ft.Text("Signo micro", selectable=True)),
                                    ft.DataCell(ft.Text("µ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("231", selectable=True)),
                                    ft.DataCell(ft.Text("Letra latina thorn minúscula", selectable=True)),
                                    ft.DataCell(ft.Text("þ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("232", selectable=True)),
                                    ft.DataCell(ft.Text("Letra latina thorn mayúscula", selectable=True)),
                                    ft.DataCell(ft.Text("Þ", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("233", selectable=True)),
                                    ft.DataCell(ft.Text("Letra U mayúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("Ú", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("234", selectable=True)),
                                    ft.DataCell(ft.Text("Letra U mayúscula con acento circunflejo", selectable=True)),
                                    ft.DataCell(ft.Text("Û", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("235", selectable=True)),
                                    ft.DataCell(ft.Text("Letra U mayúscula con acento grave", selectable=True)),
                                    ft.DataCell(ft.Text("Ù", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("236", selectable=True)),
                                    ft.DataCell(ft.Text("Letra y minúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("ý", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("237", selectable=True)),
                                    ft.DataCell(ft.Text("Letra y mayúscula con tilde", selectable=True)),
                                    ft.DataCell(ft.Text("Ý", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("238", selectable=True)),
                                    ft.DataCell(ft.Text("Guión alto", selectable=True)),
                                    ft.DataCell(ft.Text("¯", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("239", selectable=True)),
                                    ft.DataCell(ft.Text("Tilde", selectable=True)),
                                    ft.DataCell(ft.Text("´", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("240", selectable=True)),
                                    ft.DataCell(ft.Text("Símbolo equivalencia lógica", selectable=True)),
                                    ft.DataCell(ft.Text("≡", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("241", selectable=True)),
                                    ft.DataCell(ft.Text("Símbolo más menos", selectable=True)),
                                    ft.DataCell(ft.Text("±", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("242", selectable=True)),
                                    ft.DataCell(ft.Text("Doble línea baja", selectable=True)),
                                    ft.DataCell(ft.Text("‗", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("243", selectable=True)),
                                    ft.DataCell(ft.Text("Fracción 3/4", selectable=True)),
                                    ft.DataCell(ft.Text("¾", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("244", selectable=True)),
                                    ft.DataCell(ft.Text("Calderón", selectable=True)),
                                    ft.DataCell(ft.Text("¶", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("245", selectable=True)),
                                    ft.DataCell(ft.Text("Signo de sección", selectable=True)),
                                    ft.DataCell(ft.Text("§", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("246", selectable=True)),
                                    ft.DataCell(ft.Text("Signo de división", selectable=True)),
                                    ft.DataCell(ft.Text("÷", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("247", selectable=True)),
                                    ft.DataCell(ft.Text("Cedilla", selectable=True)),
                                    ft.DataCell(ft.Text("¸", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("248", selectable=True)),
                                    ft.DataCell(ft.Text("Grado", selectable=True)),
                                    ft.DataCell(ft.Text("°", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("249", selectable=True)),
                                    ft.DataCell(ft.Text("Diéresis", selectable=True)),
                                    ft.DataCell(ft.Text("¨", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("250", selectable=True)),
                                    ft.DataCell(ft.Text("Punto medio", selectable=True)),
                                    ft.DataCell(ft.Text("·", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("251", selectable=True)),
                                    ft.DataCell(ft.Text("Superíndice 1", selectable=True)),
                                    ft.DataCell(ft.Text("¹", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("252", selectable=True)),
                                    ft.DataCell(ft.Text("Superíndice 3", selectable=True)),
                                    ft.DataCell(ft.Text("³", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("253", selectable=True)),
                                    ft.DataCell(ft.Text("Superíndice 2", selectable=True)),
                                    ft.DataCell(ft.Text("²", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("254", selectable=True)),
                                    ft.DataCell(ft.Text("Cuadrado relleno", selectable=True)),
                                    ft.DataCell(ft.Text("■", selectable=True)),],),
                ft.DataRow(cells=[ft.DataCell(ft.Text("255", selectable=True)),
                                    ft.DataCell(ft.Text("Espacio sin separación (nbsp)", selectable=True)),
                                    ft.DataCell(ft.Text("NBSP/nbsp", selectable=True)),],),], show_bottom_border=True,
    column_spacing=10, data_row_max_height=40), top=6110, left=20),
        ft.Container(info_abajo, bottom=0, left=0)])
        page.add(info_)

#Función que se va a ejecutar cuando se oprima ascii
    def ascii(e):
        # Eliminar todos los elementos de la página
        for cc in page.controls:
            page.remove(cc)
            page.scroll=False
        # Agregar contenido nuevo
        ascii_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(ft.Text("ASCII", size=60, color="#3e8c69", text_align="CENTER",
                             weight=ft.FontWeight.BOLD, italic=True, selectable=True), top=90, left=224),
        ft.Container(ft.Text("Para continuar, seleccione una opción", size=15, 
                             color="black",
                             weight=ft.FontWeight.NORMAL, selectable=True, text_align="CENTER"), top=500, left=170),
        ft.Container(ascii_abajo, bottom=30, left=0),
        ft.Container(ascii_arriba, top=4, left=1), ft.Container(img, top=190, left=150),])
        page.add(ascii_)

#Función que se va a ejecutar cuando se oprima codificador ascii extendido
    def codificador_ascii_extendido(e):
        # Eliminar todos los elementos de la página
        for zz in page.controls:
            page.remove(zz)
            page.scroll=False
        # Agregar contenido nuevo
        codificador_ascii_extendido_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(ascii_abajo, bottom=30, left=0),
        ft.Container(codificador_ascii_extendido_abajo, top=4, left=1), 
        ft.Container(ft.Text("Ingrese un Carácter", size=10), top=140), ft.Container(cuadro_texto_1, top=180), 
        ft.Container(boton_codificar_1, top=270), ft.Container(cuadro_resultado_binario_50, top=340,)])
        page.add(codificador_ascii_extendido_)

#Función que se va a ejecutar cuando se oprima calculadora
    def calculadora(e):
        # Eliminar todos los elementos de la página
        for dd in page.controls:
            page.remove(dd)
            page.scroll=False
        # Agregar contenido nuevo
        calculadora_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(ft.Text("Calculadora", size=60, color="#3e8c69",
                             weight=ft.FontWeight.BOLD, italic=True, selectable=True), top=90, left=120),
        ft.Container(ft.Text("Para continuar, seleccione la operación que desea realizar", size=15, 
                             color="black",
                             weight=ft.FontWeight.NORMAL, selectable=True,), left=110, top=500,),
        ft.Container(img, top=190, left=150),
        ft.Container(calculadora_abajo, bottom=30, left=0),
        ft.Container(calculadora_arriba, top=4, left=1)])
        page.add(calculadora_)

#Función que se va a ejecutar cuando se oprimar home
    def home(e):
        # Eliminar todos los elementos de la página
        for ff in page.controls:
            page.remove(ff)
            page.scroll=False
        # Agregar contenido nuevo
        page.add(fondo)

#ALGORITMO SUMA-----------------------------------------------------------------------------------------------------------------
    desplegable_suma_todo = ft.Dropdown(
    options=[
        ft.dropdown.Option("Binario"),
        ft.dropdown.Option("Octal"),
        ft.dropdown.Option("Decimal"),
        ft.dropdown.Option("Hexadecimal")
    ],
    width=330, focused_bgcolor="#9cc4b2",
    filled=True,
    autofocus=True,
    focused_color="black",
    text_size=16,
    border_color="#3e8c69",
    border_radius=20,
    hint_text="Seleccione Sistema de Numeración (+)"
)
    def mostrar_seccion_segun_opcion_suma(opcion_seleccionada_suma):
    # Eliminar todos los controles existentes
        for control_suma in page._controls.copy():
            page.remove(control_suma)

    # Mostrar la sección correspondiente a la opción seleccionada
        if opcion_seleccionada_suma == "Decimal":
            contenedor_decimal_suma = ft.Stack([ft.Container(row_suma_decimal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(suma_arriba, top=4, left=1), 
                                           ft.Container(desplegable_suma_todo, top=100)])
            page.add(contenedor_decimal_suma)
        elif opcion_seleccionada_suma == "Hexadecimal":
            contenedor_hexadecimal_suma = ft.Stack([ft.Container(row_suma_hexadecimal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(suma_arriba, top=4, left=1), 
                                           ft.Container(desplegable_suma_todo, top=100)])
            page.add(contenedor_hexadecimal_suma)
        elif opcion_seleccionada_suma == "Binario":
            contenedor_binario_suma = ft.Stack([ft.Container(row_suma_binario, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(suma_arriba, top=4, left=1), 
                                           ft.Container(desplegable_suma_todo, top=100)])
            page.add(contenedor_binario_suma)
        elif opcion_seleccionada_suma == "Octal":
            contenedor_octal_suma = ft.Stack([ft.Container(row_suma_octal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(suma_arriba, top=4, left=1), 
                                           ft.Container(desplegable_suma_todo, top=100)])
            page.add(contenedor_octal_suma)

    def oprimir_sistema_suma(e):
        sistema_seleccionado_suma = desplegable_suma_todo.value
        if sistema_seleccionado_suma in {"Binario", "Octal", "Decimal", "Hexadecimal"}:
            mostrar_seccion_segun_opcion_suma(sistema_seleccionado_suma)

    desplegable_suma_todo.on_change = oprimir_sistema_suma

    def suma(e):
    # Eliminar todos los controles existentes
        for control_suma_2 in page._controls.copy():
            page.remove(control_suma_2)

    # Agregar contenido nuevo
        suma_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(desplegable_suma_todo, top=100),
        ft.Container(calculadora_abajo, bottom=30, left=0),
        ft.Container(suma_arriba, top=4, left=1)
    ])

    # Agregar la sección correspondiente según la opción seleccionada en el desplegable

        page.add(suma_)
    
    digite_numeros = ft.Row([
        ft.Text("Digitar Número 1", color="black", size=10),
        ft.Text("Digitar Número 2", color="black", size=10)
    ], spacing=245)

    signo_suma = ft.Text("+", size=60)

    def conv_binario_entero(e):
        try:
            conv_binario_entero_ = int(e.control.value, 2)
            e.control.value = bin(conv_binario_entero_)[2:]
        except ValueError:
            pass

    def conv_octal_entero(e):
        try:
            conv_octal_entero_ = int(e.control.value, 8)
            e.control.value = oct(conv_octal_entero_)[2:]
        except ValueError:
            pass
    
    def conv_hexadecimal_entero(e):
        try:
            conv_hexadecimal_entero_ = int(e.control.value, 16)
            e.control.value = hex(conv_hexadecimal_entero_)[2:]
        except ValueError:
            pass
    
    def conv_decimal_float(e):
        try:
            conv_decimal_float_ = float(e.control.value)
            e.control.value = str(conv_decimal_float_)
        except ValueError:
            pass

    operador_1_suma_binario = ft.TextField(on_change=conv_binario_entero, width=260)
    operador_2_suma_binario = ft.TextField(on_change=conv_binario_entero, width=260)

    operador_1_suma_octal = ft.TextField(on_change=conv_octal_entero, width=260)
    operador_2_suma_octal = ft.TextField(on_change=conv_octal_entero, width=260)

    operador_1_suma_hexadecimal = ft.TextField(on_change=conv_hexadecimal_entero, width=260)
    operador_2_suma_hexadecimal = ft.TextField(on_change=conv_hexadecimal_entero, width=260)

    operador_1_suma_decimal = ft.TextField(on_change=conv_decimal_float, width=260)
    operador_2_suma_decimal = ft.TextField(on_change=conv_decimal_float, width=260)

    row_operadores_binarios = ft.Row([
        operador_1_suma_binario,
        signo_suma,
        operador_2_suma_binario
    ], spacing=10)

    row_operadores_octales = ft.Row([
        operador_1_suma_octal,
        signo_suma,
        operador_2_suma_octal
    ], spacing=10)

    row_operadores_hexadecimales = ft.Row([
        operador_1_suma_hexadecimal,
        signo_suma,
        operador_2_suma_hexadecimal
    ], spacing=10)

    row_operadores_decimales = ft.Row([
        operador_1_suma_decimal,
        signo_suma,
        operador_2_suma_decimal
    ], spacing=10)

    resultado_suma_binario = ft.TextField(bgcolor="#9cc4b2", width=605)

    def suma_binario(e):
        try:
            suma_binario_ = int(operador_1_suma_binario.value, 2) + int(operador_2_suma_binario.value, 2)
            resultado_suma_binario.value = f"{bin(suma_binario_)[2:]}"
        except ValueError:
            resultado_suma_binario.value = "Error: Ingrese números binarios naturales"
        page.update()

    mostrar_resultado_suma_binario = ft.OutlinedButton("♗ Mostrar Resultado ♗", tooltip="Mostrar Resultado",
                                  on_click=suma_binario,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)

    resultado_suma_octal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def suma_octal(e):
        try:
            suma_octal_ = int(operador_1_suma_octal.value, 8) + int(operador_2_suma_octal.value, 8)
            resultado_suma_octal.value = f"{oct(suma_octal_)[2:]}"
        except ValueError:
            resultado_suma_octal.value = "Error: Ingrese números octales naturales"
        page.update()

    mostrar_resultado_suma_octal = ft.OutlinedButton("♗ Mostrar Resultado ♗", tooltip="Mostrar Resultado",
                                  on_click=suma_octal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)
    
    resultado_suma_hexadecimal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def suma_hexadecimal(e):
        try:
            suma_hexadecimal_ = int(operador_1_suma_hexadecimal.value, 16) + int(operador_2_suma_hexadecimal.value, 16)
            resultado_suma_hexadecimal.value = f"{hex(suma_hexadecimal_)[2:]}"
        except ValueError:
            resultado_suma_hexadecimal.value = "Error: Ingrese números hexadecimales naturales"
        page.update()

    mostrar_resultado_suma_hexadecimal = ft.OutlinedButton("♗ Mostrar Resultado ♗", tooltip="Mostrar Resultado",
                                  on_click=suma_hexadecimal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)
    
    resultado_suma_decimal = ft.TextField(bgcolor="#9cc4b2", width=605)
    
    def suma_decimal(e):
        try:
            suma_decimal_ = float(operador_1_suma_decimal.value) + float(operador_2_suma_decimal.value)
            resultado_suma_decimal.value = f"{suma_decimal_}"
        except ValueError:
            resultado_suma_decimal.value = "Error: Ingrese números decimales naturales"
        page.update()
    
    mostrar_resultado_suma_decimal = ft.OutlinedButton("♗ Mostrar Resultado ♗", tooltip="Mostrar Resultado",
                                  on_click=suma_decimal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)

    row_suma_binario = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_binarios, top=90, left=0),
        ft.Container(mostrar_resultado_suma_binario, top=190, left=1),
        ft.Container(resultado_suma_binario, top=260)])

    row_suma_octal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_octales, top=90, left=0),
        ft.Container(mostrar_resultado_suma_octal, top=190, left=1),
        ft.Container(resultado_suma_octal, top=260)])
    
    row_suma_hexadecimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_hexadecimales, top=90, left=0),
        ft.Container(mostrar_resultado_suma_hexadecimal, top=190, left=1),
        ft.Container(resultado_suma_hexadecimal, top=260)])
    
    row_suma_decimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_decimales, top=90, left=0),
        ft.Container(mostrar_resultado_suma_decimal, top=190, left=1),
        ft.Container(resultado_suma_decimal, top=260)])
    
#ALGORITMO RESTA-----------------------------------------------------------------------------------------------------------------
    desplegable_resta_todo = ft.Dropdown(
    options=[
        ft.dropdown.Option("Binario"),
        ft.dropdown.Option("Octal"),
        ft.dropdown.Option("Decimal"),
        ft.dropdown.Option("Hexadecimal")
    ],
    width=330, focused_bgcolor="#9cc4b2",
    filled=True,
    autofocus=True,
    focused_color="black",
    text_size=16,
    border_color="#3e8c69",
    border_radius=20,
    hint_text="Seleccione Sistema de Numeración (-)"
)
    def mostrar_seccion_segun_opcion_resta(opcion_seleccionada_resta):
    # Eliminar todos los controles existentes
        for control_resta in page._controls.copy():
            page.remove(control_resta)

    # Mostrar la sección correspondiente a la opción seleccionada
        if opcion_seleccionada_resta == "Decimal":
            contenedor_decimal_resta = ft.Stack([ft.Container(row_resta_decimal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(resta_arriba, top=4, left=1), 
                                           ft.Container(desplegable_resta_todo, top=100)])
            page.add(contenedor_decimal_resta)
        elif opcion_seleccionada_resta == "Hexadecimal":
            contenedor_hexadecimal_resta = ft.Stack([ft.Container(row_resta_hexadecimal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(resta_arriba, top=4, left=1), 
                                           ft.Container(desplegable_resta_todo, top=100)])
            page.add(contenedor_hexadecimal_resta)
        elif opcion_seleccionada_resta == "Binario":
            contenedor_binario_resta = ft.Stack([ft.Container(row_resta_binario, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(resta_arriba, top=4, left=1), 
                                           ft.Container(desplegable_resta_todo, top=100)])
            page.add(contenedor_binario_resta)
        elif opcion_seleccionada_resta == "Octal":
            contenedor_octal_resta = ft.Stack([ft.Container(row_resta_octal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(resta_arriba, top=4, left=1), 
                                           ft.Container(desplegable_resta_todo, top=100)])
            page.add(contenedor_octal_resta)

    def oprimir_sistema_resta(e):
        sistema_seleccionado_resta = desplegable_resta_todo.value
        if sistema_seleccionado_resta in {"Binario", "Octal", "Decimal", "Hexadecimal"}:
            mostrar_seccion_segun_opcion_resta(sistema_seleccionado_resta)

    desplegable_resta_todo.on_change = oprimir_sistema_resta

    def resta(e):
    # Eliminar todos los controles existentes
        for control_resta_2 in page._controls.copy():
            page.remove(control_resta_2)

    # Agregar contenido nuevo
        resta_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(desplegable_resta_todo, top=100),
        ft.Container(calculadora_abajo, bottom=30, left=0),
        ft.Container(resta_arriba, top=4, left=1)
    ])

    # Agregar la sección correspondiente según la opción seleccionada en el desplegable

        page.add(resta_)

    signo_resta = ft.Text("-", size=60)

    operador_1_resta_binario = ft.TextField(on_change=conv_binario_entero, width=260)
    operador_2_resta_binario = ft.TextField(on_change=conv_binario_entero, width=260)

    operador_1_resta_octal = ft.TextField(on_change=conv_octal_entero, width=260)
    operador_2_resta_octal = ft.TextField(on_change=conv_octal_entero, width=260)

    operador_1_resta_hexadecimal = ft.TextField(on_change=conv_hexadecimal_entero, width=260)
    operador_2_resta_hexadecimal = ft.TextField(on_change=conv_hexadecimal_entero, width=260)

    operador_1_resta_decimal = ft.TextField(on_change=conv_decimal_float, width=260)
    operador_2_resta_decimal = ft.TextField(on_change=conv_decimal_float, width=260)

    row_operadores_binarios_2 = ft.Row([
        operador_1_resta_binario,
        signo_resta,
        operador_2_resta_binario
    ], spacing=10)

    row_operadores_octales_2 = ft.Row([
        operador_1_resta_octal,
        signo_resta,
        operador_2_resta_octal
    ], spacing=10)

    row_operadores_hexadecimales_2 = ft.Row([
        operador_1_resta_hexadecimal,
        signo_resta,
        operador_2_resta_hexadecimal
    ], spacing=10)

    row_operadores_decimales_2 = ft.Row([
        operador_1_resta_decimal,
        signo_resta,
        operador_2_resta_decimal
    ], spacing=10)

    resultado_resta_binario = ft.TextField(bgcolor="#9cc4b2", width=605)

    def resta_binario(e):
        try:
            resta_binario_ = int(operador_1_resta_binario.value, 2) - int(operador_2_resta_binario.value, 2)
            resultado_resta_binario.value = f"{bin(resta_binario_)[2:]}"
        except ValueError:
            resultado_resta_binario.value = "Error: Ingrese números binarios naturales"
        page.update()

    mostrar_resultado_resta_binario = ft.OutlinedButton("♙ Mostrar Resultado ♙", tooltip="Mostrar Resultado",
                                  on_click=resta_binario,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)

    resultado_resta_octal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def resta_octal(e):
        try:
            resta_octal_ = int(operador_1_resta_octal.value, 8) - int(operador_2_resta_octal.value, 8)
            resultado_resta_octal.value = f"{oct(resta_octal_)[2:]}"
        except ValueError:
            resultado_resta_octal.value = "Error: Ingrese números octales naturales"
        page.update()

    mostrar_resultado_resta_octal = ft.OutlinedButton("♙ Mostrar Resultado ♙", tooltip="Mostrar Resultado",
                                  on_click=resta_octal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)
    
    resultado_resta_hexadecimal =  ft.TextField(bgcolor="#9cc4b2", width=605)

    def resta_hexadecimal(e):
        try:
            resta_hexadecimal_ = int(operador_1_resta_hexadecimal.value, 16) - int(operador_2_resta_hexadecimal.value, 16)
            resultado_resta_hexadecimal.value = f"{hex(resta_hexadecimal_)[2:]}"
        except ValueError:
            resultado_resta_hexadecimal.value = "Error: Ingrese números hexadecimales naturales"
        page.update()

    mostrar_resultado_resta_hexadecimal = ft.OutlinedButton("♙ Mostrar Resultado ♙", tooltip="Mostrar Resultado",
                                  on_click=resta_hexadecimal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)
    
    resultado_resta_decimal = ft.TextField(bgcolor="#9cc4b2", width=605)
    
    def resta_decimal(e):
        try:
            resta_decimal_ = float(operador_1_resta_decimal.value) - float(operador_2_resta_decimal.value)
            resultado_resta_decimal.value = f"{resta_decimal_}"
        except ValueError:
            resultado_resta_decimal.value = "Error: Ingrese números decimales naturales"
        page.update()
    
    mostrar_resultado_resta_decimal = ft.OutlinedButton("♙ Mostrar Resultado ♙", tooltip="Mostrar Resultado",
                                  on_click=resta_decimal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)

    row_resta_binario = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_binarios_2, top=90, left=0),
        ft.Container(mostrar_resultado_resta_binario, top=190, left=1),
        ft.Container(resultado_resta_binario, top=260)])

    row_resta_octal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_octales_2, top=90, left=0),
        ft.Container(mostrar_resultado_resta_octal, top=190, left=1),
        ft.Container(resultado_resta_octal, top=260)])
    
    row_resta_hexadecimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_hexadecimales_2, top=90, left=0),
        ft.Container(mostrar_resultado_resta_hexadecimal, top=190, left=1),
        ft.Container(resultado_resta_hexadecimal, top=260)])
    
    row_resta_decimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_decimales_2, top=90, left=0),
        ft.Container(mostrar_resultado_resta_decimal, top=190, left=1),
        ft.Container(resultado_resta_decimal, top=260)])

#ALGORITMO MULTIPLICACIÓN-------------------------------------------------------------------------------------------------
    desplegable_multiplicacion_todo = ft.Dropdown(
    options=[
        ft.dropdown.Option("Binario"),
        ft.dropdown.Option("Octal"),
        ft.dropdown.Option("Decimal"),
        ft.dropdown.Option("Hexadecimal")
    ],
    width=330, focused_bgcolor="#9cc4b2",
    filled=True,
    autofocus=True,
    focused_color="black",
    text_size=16,
    border_color="#3e8c69",
    border_radius=20,
    hint_text="Seleccione Sistema de Numeración (·)"
)
    def mostrar_seccion_segun_opcion_multiplicacion(opcion_seleccionada_multiplicacion):
    # Eliminar todos los controles existentes
        for control_multiplicacion in page._controls.copy():
            page.remove(control_multiplicacion)

    # Mostrar la sección correspondiente a la opción seleccionada
        if opcion_seleccionada_multiplicacion == "Decimal":
            contenedor_decimal_multiplicacion = ft.Stack([ft.Container(row_multiplicacion_decimal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(multiplicacion_arriba, top=4, left=1), 
                                           ft.Container(desplegable_multiplicacion_todo, top=100)])
            page.add(contenedor_decimal_multiplicacion)
        elif opcion_seleccionada_multiplicacion == "Hexadecimal":
            contenedor_hexadecimal_multiplicacion = ft.Stack([ft.Container(row_multiplicacion_hexadecimal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(multiplicacion_arriba, top=4, left=1), 
                                           ft.Container(desplegable_multiplicacion_todo, top=100)])
            page.add(contenedor_hexadecimal_multiplicacion)
        elif opcion_seleccionada_multiplicacion == "Binario":
            contenedor_binario_multiplicacion = ft.Stack([ft.Container(row_multiplicacion_binario, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(multiplicacion_arriba, top=4, left=1), 
                                           ft.Container(desplegable_multiplicacion_todo, top=100)])
            page.add(contenedor_binario_multiplicacion)
        elif opcion_seleccionada_multiplicacion == "Octal":
            contenedor_octal_multiplicacion = ft.Stack([ft.Container(row_multiplicacion_octal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(multiplicacion_arriba, top=4, left=1), 
                                           ft.Container(desplegable_multiplicacion_todo, top=100)])
            page.add(contenedor_octal_multiplicacion)

    def oprimir_sistema_multiplicacion(e):
        sistema_seleccionado_multiplicacion = desplegable_multiplicacion_todo.value
        if sistema_seleccionado_multiplicacion in {"Binario", "Octal", "Decimal", "Hexadecimal"}:
            mostrar_seccion_segun_opcion_multiplicacion(sistema_seleccionado_multiplicacion)

    desplegable_multiplicacion_todo.on_change = oprimir_sistema_multiplicacion

    def multiplicacion(e):
    # Eliminar todos los controles existentes
        for control_multiplicacion_2 in page._controls.copy():
            page.remove(control_multiplicacion_2)

    # Agregar contenido nuevo
        multiplicacion_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(desplegable_multiplicacion_todo, top=100),
        ft.Container(calculadora_abajo, bottom=30, left=0),
        ft.Container(multiplicacion_arriba, top=4, left=1)
    ])

    # Agregar la sección correspondiente según la opción seleccionada en el desplegable

        page.add(multiplicacion_)

    signo_multiplicacion = ft.Text("·", size=60)

    operador_1_multiplicacion_binario = ft.TextField(on_change=conv_binario_entero, width=260)
    operador_2_multiplicacion_binario = ft.TextField(on_change=conv_binario_entero, width=260)

    operador_1_multiplicacion_octal = ft.TextField(on_change=conv_octal_entero, width=260)
    operador_2_multiplicacion_octal = ft.TextField(on_change=conv_octal_entero, width=260)

    operador_1_multiplicacion_hexadecimal = ft.TextField(on_change=conv_hexadecimal_entero, width=260)
    operador_2_multiplicacion_hexadecimal = ft.TextField(on_change=conv_hexadecimal_entero, width=260)

    operador_1_multiplicacion_decimal = ft.TextField(on_change=conv_decimal_float, width=260)
    operador_2_multiplicacion_decimal = ft.TextField(on_change=conv_decimal_float, width=260)

    row_operadores_binarios_3 = ft.Row([
        operador_1_multiplicacion_binario,
        signo_multiplicacion,
        operador_2_multiplicacion_binario
    ], spacing=10)

    row_operadores_octales_3 = ft.Row([
        operador_1_multiplicacion_octal,
        signo_multiplicacion,
        operador_2_multiplicacion_octal
    ], spacing=10)

    row_operadores_hexadecimales_3 = ft.Row([
        operador_1_multiplicacion_hexadecimal,
        signo_multiplicacion,
        operador_2_multiplicacion_hexadecimal
    ], spacing=10)

    row_operadores_decimales_3 = ft.Row([
        operador_1_multiplicacion_decimal,
        signo_multiplicacion,
        operador_2_multiplicacion_decimal
    ], spacing=10)

    resultado_multiplicacion_binario = ft.TextField(bgcolor="#9cc4b2", width=605)

    def multiplicacion_binario(e):
        try:
            multiplicacion_binario_ = int(operador_1_multiplicacion_binario.value, 2) * int(operador_2_multiplicacion_binario.value, 2)
            resultado_multiplicacion_binario.value = f"{bin(multiplicacion_binario_)[2:]}"
        except ValueError:
            resultado_multiplicacion_binario.value = "Error: Ingrese números binarios naturales"
        page.update()

    mostrar_resultado_multiplicacion_binario = ft.OutlinedButton("♣ Mostrar Resultado ♣", tooltip="Mostrar Resultado",
                                  on_click=multiplicacion_binario,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)

    resultado_multiplicacion_octal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def multiplicacion_octal(e):
        try:
            multiplicacion_octal_ = int(operador_1_multiplicacion_octal.value, 8) * int(operador_2_multiplicacion_octal.value, 8)
            resultado_multiplicacion_octal.value = f"{oct(multiplicacion_octal_)[2:]}"
        except ValueError:
            resultado_multiplicacion_octal.value = "Error: Ingrese números octales naturales"
        page.update()

    mostrar_resultado_multiplicacion_octal = ft.OutlinedButton("♣ Mostrar Resultado ♣", tooltip="Mostrar Resultado",
                                  on_click=multiplicacion_octal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)
    
    resultado_multiplicacion_hexadecimal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def multiplicacion_hexadecimal(e):
        try:
            multiplicacion_hexadecimal_ = int(operador_1_multiplicacion_hexadecimal.value, 16) * int(operador_2_multiplicacion_hexadecimal.value, 16)
            resultado_multiplicacion_hexadecimal.value = f"{hex(multiplicacion_hexadecimal_)[2:]}"
        except ValueError:
            resultado_multiplicacion_hexadecimal.value = "Error: Ingrese números hexadecimales naturales"
        page.update()

    mostrar_resultado_multiplicacion_hexadecimal = ft.OutlinedButton("♣ Mostrar Resultado ♣", tooltip="Mostrar Resultado",
                                  on_click=multiplicacion_hexadecimal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)
    
    resultado_multiplicacion_decimal = ft.TextField(bgcolor="#9cc4b2", width=605)
    
    def multiplicacion_decimal(e):
        try:
            multiplicacion_decimal_ = float(operador_1_multiplicacion_decimal.value) * float(operador_2_multiplicacion_decimal.value)
            resultado_multiplicacion_decimal.value = f"{multiplicacion_decimal_}"
        except ValueError:
            resultado_multiplicacion_decimal.value = "Error: Ingrese números decimales naturales"
        page.update()
    
    mostrar_resultado_multiplicacion_decimal = ft.OutlinedButton("♣ Mostrar Resultado ♣", tooltip="Mostrar Resultado",
                                  on_click=multiplicacion_decimal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)

    row_multiplicacion_binario = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_binarios_3, top=90, left=0),
        ft.Container(mostrar_resultado_multiplicacion_binario, top=190, left=1),
        ft.Container(resultado_multiplicacion_binario, top=260)])

    row_multiplicacion_octal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_octales_3, top=90, left=0),
        ft.Container(mostrar_resultado_multiplicacion_octal, top=190, left=1),
        ft.Container(resultado_multiplicacion_octal, top=260)])
    
    row_multiplicacion_hexadecimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_hexadecimales_3, top=90, left=0),
        ft.Container(mostrar_resultado_multiplicacion_hexadecimal, top=190, left=1),
        ft.Container(resultado_multiplicacion_hexadecimal, top=260)])
    
    row_multiplicacion_decimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_decimales_3, top=90, left=0),
        ft.Container(mostrar_resultado_multiplicacion_decimal, top=190, left=1),
        ft.Container(resultado_multiplicacion_decimal, top=260)])

#ALGORITMO DIVISIÓN-------------------------------------------------------------------------------------------------------------
    desplegable_division_todo = ft.Dropdown(
    options=[
        ft.dropdown.Option("Binario"),
        ft.dropdown.Option("Octal"),
        ft.dropdown.Option("Decimal"),
        ft.dropdown.Option("Hexadecimal")
    ],
    width=330, focused_bgcolor="#9cc4b2",
    filled=True,
    autofocus=True,
    focused_color="black",
    text_size=16,
    border_color="#3e8c69",
    border_radius=20,
    hint_text="Seleccione Sistema de Numeración (÷)"
)
    def mostrar_seccion_segun_opcion_division(opcion_seleccionada_division):
    # Eliminar todos los controles existentes
        for control_division in page._controls.copy():
            page.remove(control_division)

    # Mostrar la sección correspondiente a la opción seleccionada
        if opcion_seleccionada_division == "Decimal":
            contenedor_decimal_division = ft.Stack([ft.Container(row_division_decimal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(division_arriba, top=4, left=1), 
                                           ft.Container(desplegable_division_todo, top=100)])
            page.add(contenedor_decimal_division)
        elif opcion_seleccionada_division == "Hexadecimal":
            contenedor_hexadecimal_division = ft.Stack([ft.Container(row_division_hexadecimal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(division_arriba, top=4, left=1), 
                                           ft.Container(desplegable_division_todo, top=100)])
            page.add(contenedor_hexadecimal_division)
        elif opcion_seleccionada_division == "Binario":
            contenedor_binario_division = ft.Stack([ft.Container(row_division_binario, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(division_arriba, top=4, left=1), 
                                           ft.Container(desplegable_division_todo, top=100)])
            page.add(contenedor_binario_division)
        elif opcion_seleccionada_division == "Octal":
            contenedor_octal_division = ft.Stack([ft.Container(row_division_octal, top=150), 
                                           ft.Container(calculadora_abajo, top=550, left=0),
                                           ft.Container(division_arriba, top=4, left=1), 
                                           ft.Container(desplegable_division_todo, top=100)])
            page.add(contenedor_octal_division)

    def oprimir_sistema_division(e):
        sistema_seleccionado_division = desplegable_division_todo.value
        if sistema_seleccionado_division in {"Binario", "Octal", "Decimal", "Hexadecimal"}:
            mostrar_seccion_segun_opcion_division(sistema_seleccionado_division)

    desplegable_division_todo.on_change = oprimir_sistema_division

    def division(e):
    # Eliminar todos los controles existentes
        for control_division_2 in page._controls.copy():
            page.remove(control_division_2)

    # Agregar contenido nuevo
        division_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(desplegable_division_todo, top=100),
        ft.Container(calculadora_abajo, bottom=30, left=0),
        ft.Container(division_arriba, top=4, left=1)
    ])

    # Agregar la sección correspondiente según la opción seleccionada en el desplegable

        page.add(division_)

    signo_division = ft.Text("÷", size=60)

    operador_1_division_binario = ft.TextField(on_change=conv_binario_entero, width=260)
    operador_2_division_binario = ft.TextField(on_change=conv_binario_entero, width=260)

    operador_1_division_octal = ft.TextField(on_change=conv_octal_entero, width=260)
    operador_2_division_octal = ft.TextField(on_change=conv_octal_entero, width=260)

    operador_1_division_hexadecimal = ft.TextField(on_change=conv_hexadecimal_entero, width=260)
    operador_2_division_hexadecimal = ft.TextField(on_change=conv_hexadecimal_entero, width=260)

    operador_1_division_decimal = ft.TextField(on_change=conv_decimal_float, width=260)
    operador_2_division_decimal = ft.TextField(on_change=conv_decimal_float, width=260)

    row_operadores_binarios_4 = ft.Row([
        operador_1_division_binario,
        signo_division,
        operador_2_division_binario
    ], spacing=10)

    row_operadores_octales_4 = ft.Row([
        operador_1_division_octal,
        signo_division,
        operador_2_division_octal
    ], spacing=10)

    row_operadores_hexadecimales_4 = ft.Row([
        operador_1_division_hexadecimal,
        signo_division,
        operador_2_division_hexadecimal
    ], spacing=10)

    row_operadores_decimales_4 = ft.Row([
        operador_1_division_decimal,
        signo_division,
        operador_2_division_decimal
    ], spacing=10)


    def float_to_binary_division(float_number_binario_division, precision=8):
        integer_part_binario_division = bin(int(float_number_binario_division))[2:]
        fractional_part_binario_division = float_number_binario_division - int(float_number_binario_division)
        binary_fractional_part_binario_division = ""
        for _ in range(precision):
            fractional_part_binario_division *= 2
            binary_fractional_part_binario_division += str(int(fractional_part_binario_division))
            fractional_part_binario_division -= int(fractional_part_binario_division)
        binary_representation = f"{integer_part_binario_division}.{binary_fractional_part_binario_division}"
        return binary_representation
    resultado_division_binario = ft.TextField(bgcolor="#9cc4b2", width=605)

    def division_binario(e):
        try:
            division_binario_ = float(int(operador_1_division_binario.value, 2)) / float(int(operador_2_division_binario.value, 2))
            binary_result_division = float_to_binary_division(division_binario_)
            resultado_division_binario.value = f"{binary_result_division}"
        except ValueError:
            resultado_division_binario.value = "Error: Ingrese números binarios naturales"
        page.update()

    mostrar_resultado_division_binario = ft.OutlinedButton("♠ Mostrar Resultado ♠", tooltip="Mostrar Resultado",
                                  on_click=division_binario,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)

    def float_to_octal_division(float_number_octal_division, precision=8):
        integer_part_octal_division = oct(int(float_number_octal_division))[2:]
        fractional_part_octal_division = float_number_octal_division - int(float_number_octal_division)
        octal_fractional_part_octal_division = ""
        for _ in range(precision):
            fractional_part_octal_division *= 8
            octal_fractional_part_octal_division += str(int(fractional_part_octal_division))
            fractional_part_octal_division -= int(fractional_part_octal_division)
        octal_representation_division = f"{integer_part_octal_division}.{octal_fractional_part_octal_division}"
        return octal_representation_division
    
    resultado_division_octal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def division_octal(e):
        try:
            division_octal_ = float(int(operador_1_division_octal.value, 8)) / float(int(operador_2_division_octal.value, 8))
            octal_result_division = float_to_octal_division(division_octal_)
            resultado_division_octal.value = f"{octal_result_division}"
        except ValueError:
            resultado_division_octal.value = "Error: Ingrese números octales naturales"
        page.update()

    mostrar_resultado_division_octal = ft.OutlinedButton("♠ Mostrar Resultado ♠", tooltip="Mostrar Resultado",
                                  on_click=division_octal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)
    
    def float_to_hexadecimal_division(float_number_hexadecimal_division, precision=8):
        integer_part_hexadecimal_division = hex(int(float_number_hexadecimal_division))[2:]
        fractional_part_hexadecimal_division = float_number_hexadecimal_division - int(float_number_hexadecimal_division)
        hexadecimal_fractional_part_hexadecimal_division = ""
        for _ in range(precision):
            fractional_part_hexadecimal_division *= 16
            hexadecimal_fractional_part_hexadecimal_division += format(int(fractional_part_hexadecimal_division), 'x')
            fractional_part_hexadecimal_division -= int(fractional_part_hexadecimal_division)
        hexadecimal_representation_division = f"{integer_part_hexadecimal_division}.{hexadecimal_fractional_part_hexadecimal_division}"
        return hexadecimal_representation_division
    
    resultado_division_hexadecimal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def division_hexadecimal(e):
        try:
            division_hexadecimal_ = float(int(operador_1_division_hexadecimal.value, 16)) / float(int(operador_2_division_hexadecimal.value, 16))
            hexadecimal_result_division = float_to_hexadecimal_division(division_hexadecimal_)
            resultado_division_hexadecimal.value = f"{hexadecimal_result_division}"
        except ValueError:
            resultado_division_hexadecimal.value = "Error: Ingrese números hexadecimales naturales"
        page.update()

    mostrar_resultado_division_hexadecimal = ft.OutlinedButton("♠ Mostrar Resultado ♠", tooltip="Mostrar Resultado",
                                  on_click=division_hexadecimal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)
    
    resultado_division_decimal = ft.TextField(bgcolor="#9cc4b2", width=605)
    
    def division_decimal(e):
        try:
            division_decimal_ = float(operador_1_division_decimal.value) / float(operador_2_division_decimal.value)
            resultado_division_decimal.value = f"{division_decimal_}"
        except ValueError:
            resultado_division_decimal.value = "Error: Ingrese números decimales naturales"
        page.update()
    
    mostrar_resultado_division_decimal = ft.OutlinedButton("♠ Mostrar Resultado ♠", tooltip="Mostrar Resultado",
                                  on_click=division_decimal,
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=210)

    row_division_binario = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_binarios_4, top=90, left=0),
        ft.Container(mostrar_resultado_division_binario, top=190, left=1),
        ft.Container(resultado_division_binario, top=260)])

    row_division_octal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_octales_4, top=90, left=0),
        ft.Container(mostrar_resultado_division_octal, top=190, left=1),
        ft.Container(resultado_division_octal, top=260)])
    
    row_division_hexadecimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_hexadecimales_4, top=90, left=0),
        ft.Container(mostrar_resultado_division_hexadecimal, top=190, left=1),
        ft.Container(resultado_division_hexadecimal, top=260)])
    
    row_division_decimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numeros, top=70),
        ft.Container(row_operadores_decimales_4, top=90, left=0),
        ft.Container(mostrar_resultado_division_decimal, top=190, left=1),
        ft.Container(resultado_division_decimal, top=260)])

#ALGORITMO BASE-------------------------------------------------------------------------------------------------------------------------------------
    desplegable_base_original = ft.Dropdown(hint_text="Seleccione Base Original", options=[ft.dropdown.Option("Decimal"), ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"), ft.dropdown.Option("Hexadecimal")],
        focused_bgcolor="#9cc4b2", filled=True, autofocus=True, focused_color="black", text_size=16, border_color="#3e8c69", border_radius=20, width=250)

    desplegable_base_destino = ft.Dropdown(hint_text="Seleccione Base de Destino", options=[ft.dropdown.Option("Decimal"), ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"), ft.dropdown.Option("Hexadecimal")], focused_bgcolor="#9cc4b2", filled=True, autofocus=True, focused_color="black",
        text_size=16, border_color="#3e8c69", border_radius=20, width=250)

    def mostrar_seccion_segun_opcion_base_1(opcion_seleccionada_base_1, opcion_seleccionada_base_destino):
    # Eliminar todos los controles existentes
        for control_base_1 in page._controls.copy():
            page.remove(control_base_1)

    # Mostrar la sección correspondiente a la opción seleccionada
        if opcion_seleccionada_base_1 == "Octal" and opcion_seleccionada_base_destino == "Decimal":
            contenedor_octal_base_1 = ft.Stack([ft.Container(poner_en_funcion_octal_decimal, top=30),
                                        ft.Container(desplegable_base_destino, top=280), 
                                        ft.Container(base_abajo, top=550, left=0), 
                                        ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_octal_base_1)
        elif opcion_seleccionada_base_1 == "Binario" and opcion_seleccionada_base_destino == "Decimal":
            contenedor_binario_base_1 = ft.Stack([ft.Container(poner_en_funcion_binario_decimal, top=30),
                                          ft.Container(desplegable_base_destino, top=280), 
                                          ft.Container(base_abajo, top=550, left=0), 
                                          ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_binario_base_1)
        
        elif opcion_seleccionada_base_1 == "Hexadecimal" and opcion_seleccionada_base_destino == "Decimal":
            contenedor_hexadecimal_base_1 = ft.Stack([ft.Container(poner_en_funcion_hexadecimal_decimal, top=30),
                                          ft.Container(desplegable_base_destino, top=280), 
                                          ft.Container(base_abajo, top=550, left=0), 
                                          ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_hexadecimal_base_1)
        
        elif opcion_seleccionada_base_1 == "Decimal" and opcion_seleccionada_base_destino == "Decimal":
            contenedor_decimal_base_1 = ft.Stack([ft.Container(poner_en_funcion_decimal_decimal, top=30),
                                          ft.Container(desplegable_base_destino, top=280), 
                                          ft.Container(base_abajo, top=550, left=0), 
                                          ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_decimal_base_1)
        
        elif opcion_seleccionada_base_1 == "Binario" and opcion_seleccionada_base_destino == "Octal":
            contenedor_binario_base_2 = ft.Stack([ft.Container(poner_en_funcion_binario_octal, top=30),
                                          ft.Container(desplegable_base_destino, top=280), 
                                          ft.Container(base_abajo, top=550, left=0), 
                                          ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_binario_base_2)
        
        elif opcion_seleccionada_base_1 == "Binario" and opcion_seleccionada_base_destino == "Hexadecimal":
            contenedor_binario_base_3 = ft.Stack([ft.Container(poner_en_funcion_binario_hexadecimal, top=30),
                                          ft.Container(desplegable_base_destino, top=280), 
                                          ft.Container(base_abajo, top=550, left=0), 
                                          ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_binario_base_3)
        
        elif opcion_seleccionada_base_1 == "Binario" and opcion_seleccionada_base_destino == "Binario":
            contenedor_binario_base_4 = ft.Stack([ft.Container(poner_en_funcion_binario_binario, top=30),
                                          ft.Container(desplegable_base_destino, top=280), 
                                          ft.Container(base_abajo, top=550, left=0), 
                                          ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_binario_base_4)
        
        elif opcion_seleccionada_base_1 == "Octal" and opcion_seleccionada_base_destino == "Binario":
            contenedor_octal_base_2 = ft.Stack([ft.Container(poner_en_funcion_octal_binario, top=30),
                                      ft.Container(desplegable_base_destino, top=280), 
                                      ft.Container(base_abajo, top=550, left=0), 
                                      ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_octal_base_2)
        
        elif opcion_seleccionada_base_1 == "Octal" and opcion_seleccionada_base_destino == "Hexadecimal":
            contenedor_octal_base_3 = ft.Stack([ft.Container(poner_en_funcion_octal_hexadecimal, top=30),
                                      ft.Container(desplegable_base_destino, top=280), 
                                      ft.Container(base_abajo, top=550, left=0), 
                                      ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_octal_base_3)
        
        elif opcion_seleccionada_base_1 == "Octal" and opcion_seleccionada_base_destino == "Octal":
            contenedor_octal_base_4 = ft.Stack([ft.Container(poner_en_funcion_octal_octal, top=30),
                                      ft.Container(desplegable_base_destino, top=280), 
                                      ft.Container(base_abajo, top=550, left=0), 
                                      ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_octal_base_4)
        
        elif opcion_seleccionada_base_1 == "Hexadecimal" and opcion_seleccionada_base_destino == "Binario":
            contenedor_hexadecimal_base_2 = ft.Stack([ft.Container(poner_en_funcion_hexadecimal_binario, top=30),
                                      ft.Container(desplegable_base_destino, top=280), 
                                      ft.Container(base_abajo, top=550, left=0), 
                                      ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_hexadecimal_base_2)
        
        elif opcion_seleccionada_base_1 == "Hexadecimal" and opcion_seleccionada_base_destino == "Octal":
            contenedor_hexadecimal_base_4 = ft.Stack([ft.Container(poner_en_funcion_hexadecimal_octal, top=30),
                                      ft.Container(desplegable_base_destino, top=280), 
                                      ft.Container(base_abajo, top=550, left=0), 
                                      ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_hexadecimal_base_4)
        
        elif opcion_seleccionada_base_1 == "Hexadecimal" and opcion_seleccionada_base_destino == "Hexadecimal":
            contenedor_hexadecimal_base_3 = ft.Stack([ft.Container(poner_en_funcion_hexadecimal_hexadecimal, top=30),
                                      ft.Container(desplegable_base_destino, top=280), 
                                      ft.Container(base_abajo, top=550, left=0), 
                                      ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_hexadecimal_base_3)
        
        elif opcion_seleccionada_base_1 == "Decimal" and opcion_seleccionada_base_destino == "Binario":
            contenedor_decimal_base_2 = ft.Stack([ft.Container(poner_en_funcion_decimal_binario, top=30),
                                      ft.Container(desplegable_base_destino, top=280), 
                                      ft.Container(base_abajo, top=550, left=0), 
                                      ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_decimal_base_2)
        
        elif opcion_seleccionada_base_1 == "Decimal" and opcion_seleccionada_base_destino == "Octal":
            contenedor_decimal_base_3 = ft.Stack([ft.Container(poner_en_funcion_decimal_octal, top=30),
                                      ft.Container(desplegable_base_destino, top=280), 
                                      ft.Container(base_abajo, top=550, left=0), 
                                      ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_decimal_base_3)

        elif opcion_seleccionada_base_1 == "Decimal" and opcion_seleccionada_base_destino == "Hexadecimal":
            contenedor_decimal_base_4 = ft.Stack([ft.Container(poner_en_funcion_decimal_hexadecimal, top=30),
                                      ft.Container(desplegable_base_destino, top=280), 
                                      ft.Container(base_abajo, top=550, left=0), 
                                      ft.Container(desplegable_base_original, top=50)])
            page.add(contenedor_decimal_base_4)


    def oprimir_sistema_base_1(e):
        sistema_seleccionado_base_1 = desplegable_base_original.value
        sistema_seleccionado_base_destino = desplegable_base_destino.value
        if sistema_seleccionado_base_1 in {"Binario", "Octal", "Decimal", "Hexadecimal"} and \
            sistema_seleccionado_base_destino in {"Binario", "Octal", "Decimal", "Hexadecimal"}:
                mostrar_seccion_segun_opcion_base_1(sistema_seleccionado_base_1, sistema_seleccionado_base_destino)
    
    desplegable_base_destino.on_change = oprimir_sistema_base_1
    desplegable_base_original.on_change = oprimir_sistema_base_1
    

    def base(e):
    # Eliminar todos los controles existentes
        for control_base_total in page._controls.copy():
            page.remove(control_base_total)
            page.scroll=False
        
        base_ = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(desplegable_base_original, top=50),  ft.Container(desplegable_base_destino, top=280),
    ft.Container(base_abajo, bottom=30, left=0)])
        page.add(base_)

    #Texto cuando se oprime la base seleccionada
    digite_numero_base=ft.Text("Digitar Número", color="black", size=10)

    #Cuadro de texto de los números cuando se oprime base original
    numero_binario_base = ft.TextField(on_change=conv_binario_entero, width=260)
    numero_octal_base = ft.TextField(on_change=conv_octal_entero, width=260)
    numero_decimal_base = ft.TextField(on_change=conv_decimal_float, width=260)
    numero_hexadecimal_base = ft.TextField(on_change=conv_hexadecimal_entero, width=260)

    #DE BINARIO A DECIMAL &&&&&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_binario_decimal = ft.TextField(width=605, bgcolor="#9cc4b2")
    def binario_decimal(numero_binario_decimal):
        try:
            partes = numero_binario_decimal.split('.')

        # Verificar que la parte entera y fraccionaria contengan solo '0' y '1'
            if any(digito not in {'0', '1'} for digito in partes[0]) or (len(partes) == 2 and any(digito not in {'0', '1'} for digito in partes[1])):
                raise ValueError("Ingrese números binarios reales positivos")

        # Convertir la parte entera a entero en base 2
            parte_entera = int(partes[0], 2)

        # Incluir la parte fraccionaria si existe
            parte_fraccionaria = f".{partes[1]}" if len(partes) == 2 else ''

        # Convertir la parte fraccionaria a decimal
            parte_fraccionaria_decimal = sum(int(digit) * 2**(-i-1) for i, digit in enumerate(partes[1])) if parte_fraccionaria else 0

        # Devolver el número decimal original
            resultado_decimal = parte_entera + parte_fraccionaria_decimal
            return resultado_decimal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: {str(e)}"


    def mostrar_resultado_conversion_binario_decimal():
        try:
            valor_binario_decimal = numero_binario_base.value if numero_binario_base.value is not None else ""
            resultado_binario_decimal = binario_decimal(valor_binario_decimal)
            resultado_base_binario_decimal.value = f"{resultado_binario_decimal}"
        except ValueError:
            resultado_base_binario_decimal.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_binario_decimal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=140,
                                                      on_click=lambda _: mostrar_resultado_conversion_binario_decimal())
    poner_en_funcion_binario_decimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numero_base, top=120), ft.Container(numero_binario_base, top=140), 
        ft.Container(mostrar_resultado_base_binario_decimal_, top=350, left=1),
        ft.Container(resultado_base_binario_decimal, top=390)])

    #DE OCTAL A DECIMAL &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_octal_decimal = ft.TextField(bgcolor="#9cc4b2", width=605)
    def octal_a_decimal(numero_octal_decimal):
        try:
            partes = numero_octal_decimal.split('.')

        # Verificar que la parte entera y fraccionaria contengan solo dígitos en el rango 0-7
            if any(digito not in {'0', '1', '2', '3', '4', '5', '6', '7'} for digito in partes[0]) or (len(partes) == 2 and any(digito not in {'0', '1', '2', '3', '4', '5', '6', '7'} for digito in partes[1])):
                raise ValueError("Ingrese números octales reales positivos")

        # Convertir la parte entera a entero en base 8
            parte_entera = int(partes[0], 8)

        # Incluir la parte fraccionaria si existe
            parte_fraccionaria = f".{partes[1]}" if len(partes) == 2 else ''

        # Convertir la parte fraccionaria a decimal
            parte_fraccionaria_decimal = sum(int(digit) * 8**(-i-1) for i, digit in enumerate(partes[1])) if parte_fraccionaria else 0

        # Devolver el número decimal original
            resultado_decimal = parte_entera + parte_fraccionaria_decimal
            return resultado_decimal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: {str(e)}"

    def mostrar_resultado_conversion_octal_decimal():
        try:
            valor_octal_decimal = numero_octal_base.value if numero_octal_base.value is not None else ""
            resultado_octal_decimal = octal_a_decimal(valor_octal_decimal)
            resultado_base_octal_decimal.value = f"{resultado_octal_decimal}"
        except ValueError:
            resultado_base_octal_decimal.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_octal_decimal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=140,
                                                      on_click=lambda _: mostrar_resultado_conversion_octal_decimal())
    poner_en_funcion_octal_decimal = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(digite_numero_base, top=120), ft.Container(numero_octal_base, top=140), 
        ft.Container(mostrar_resultado_base_octal_decimal_, top=350, left=1),
        ft.Container(resultado_base_octal_decimal, top=390)])
    
    #DE HEXADECIMAL A DECIMAL &&&&&&&&&&&&&&&&&&&&&&
    resultado_base_hexadecimal_decimal = ft.TextField(bgcolor="#9cc4b2", width=605)
    def hexadecimal_decimal(numero_hexadecimal_decimal):
        try:
        # Convierte el número hexadecimal a decimal
            partes_hexadecimal_decimal = numero_hexadecimal_decimal.split('.')
    
            parte_entera_hexadecimal_decimal = int(partes_hexadecimal_decimal[0], 16)
            parte_fraccionaria_hexadecimal_decimal = 0
            if len(partes_hexadecimal_decimal) == 2:
                parte_fraccionaria_hexadecimal_decimal = sum(int(digit, 16) * 16**(-i-1) for i, digit in enumerate(partes_hexadecimal_decimal[1]))
            resultante_hexadecimal_decimal = parte_entera_hexadecimal_decimal + parte_fraccionaria_hexadecimal_decimal
            return resultante_hexadecimal_decimal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: Ingrese números hexadecimales reales positivos"

    def mostrar_resultado_conversion_hexadecimal_decimal():
        try:
            valor_hexadecimal_decimal = numero_hexadecimal_base.value if numero_hexadecimal_base.value is not None else ""
            resultado_hexadecimal_decimal = hexadecimal_decimal(valor_hexadecimal_decimal)
            resultado_base_hexadecimal_decimal.value = f"{resultado_hexadecimal_decimal}"
        except ValueError:
            resultado_base_hexadecimal_decimal.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_hexadecimal_decimal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=140,
                                                      on_click=lambda _: mostrar_resultado_conversion_hexadecimal_decimal())
    poner_en_funcion_hexadecimal_decimal = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_hexadecimal_base, top=140), 
    ft.Container(mostrar_resultado_base_hexadecimal_decimal_, top=350, left=1),
    ft.Container(resultado_base_hexadecimal_decimal, top=390)])

    #DE DECIMAL A DECIMAL&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_decimal_decimal = ft.TextField(bgcolor="#9cc4b2", width=605)
    def mostrar_resultado_conversion_decimal_decimal():
        try:
            valor_decimal_decimal = numero_decimal_base.value if numero_decimal_base.value is not None else ""
        
        # Verificar que la cadena contenga solo dígitos numéricos
            if not valor_decimal_decimal.replace('.', '').isdigit():
                raise ValueError("Ingrese números decimales reales positivos")

        # Convertir la cadena a un número decimal
            resultado_base_decimal_decimal.value = f"{float(valor_decimal_decimal)}"
        except ValueError as e:
            resultado_base_decimal_decimal.value = f"Error: {str(e)}"
        page.update()


    mostrar_resultado_base_decimal_decimal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=140,
                                                      on_click=lambda _: mostrar_resultado_conversion_decimal_decimal())
    poner_en_funcion_decimal_decimal = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_decimal_base, top=140), 
    ft.Container(mostrar_resultado_base_decimal_decimal_, top=350, left=1),
    ft.Container(resultado_base_decimal_decimal, top=390)])

    #DE BINARIO A OCTAL&&&&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_binario_octal = ft.TextField(bgcolor="#9cc4b2", width=605)
    def binario_a_octal(numero_binario):
        try:
        # Agregar ".0" si no hay parte fraccionaria
            numero_binario = numero_binario + ".0" if '.' not in numero_binario else numero_binario

            partes_binario = numero_binario.split('.')

            parte_entera_binario = partes_binario[0].lstrip('0')
            parte_fraccionaria_binario = partes_binario[1]

        # Completa con ceros a la derecha en la parte fraccionaria
            while len(parte_fraccionaria_binario) % 3 != 0:
                parte_fraccionaria_binario += '0'

            parte_entera_octal = oct(int(parte_entera_binario, 2))[2:]
        
        # Convertir la parte fraccionaria a octal, tomando en cuenta los valores de izquierda a derecha
            parte_fraccionaria_octal = ''
            for i in range(0, len(parte_fraccionaria_binario), 3):
                grupo_binario = parte_fraccionaria_binario[i:i+3]
                parte_fraccionaria_octal += str(int(grupo_binario, 2))

            resultado_octal = parte_entera_octal + ('.' + parte_fraccionaria_octal if parte_fraccionaria_octal else '')
            return resultado_octal
        except ValueError as e:
            return f"Error: Ingrese números binarios reales positivos"

        
    def mostrar_resultado_conversion_binario_octal():
        try:
            valor_binario_octal = numero_binario_base.value if numero_binario_base.value is not None else ""
            resultado_binario_octal = binario_a_octal(valor_binario_octal)
            resultado_base_binario_octal.value = f"{resultado_binario_octal}"
        except ValueError:
            resultado_base_binario_octal.value = "Error de conversión"
        page.update()
    
    mostrar_resultado_base_binario_octal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=140,
                                                      on_click=lambda _: mostrar_resultado_conversion_binario_octal())
    poner_en_funcion_binario_octal = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_binario_base, top=140), 
    ft.Container(mostrar_resultado_base_binario_octal_, top=350, left=1),
    ft.Container(resultado_base_binario_octal, top=390)])

    #DE BINARIO A HEXADECIMAL&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_binario_hexadecimal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def binario_a_hexadecimal(numero_binario):
        try:
        # Agregar ".0" si no hay parte fraccionaria
            numero_binario = numero_binario + ".0" if '.' not in numero_binario else numero_binario

            partes_binario = numero_binario.split('.')

            parte_entera_binario = partes_binario[0].lstrip('0')
            parte_fraccionaria_binario = partes_binario[1]

        # Completa con ceros a la derecha en la parte fraccionaria
            while len(parte_fraccionaria_binario) % 4 != 0:
                parte_fraccionaria_binario += '0'

            parte_entera_hexadecimal = hex(int(parte_entera_binario, 2))[2:]
        
        # Convertir la parte fraccionaria a hexadecimal, tomando en cuenta los valores de izquierda a derecha
            parte_fraccionaria_hexadecimal = ''
            for i in range(0, len(parte_fraccionaria_binario), 4):
                grupo_binario = parte_fraccionaria_binario[i:i+4]
                parte_fraccionaria_hexadecimal += hex(int(grupo_binario, 2))[2:]

            resultado_hexadecimal = parte_entera_hexadecimal + ('.' + parte_fraccionaria_hexadecimal if parte_fraccionaria_hexadecimal else '')
            return resultado_hexadecimal.upper()  # Convierte a mayúsculas para consistencia

        except ValueError as e:
            return f"Error: Ingrese números binarios reales positivos"

    def mostrar_resultado_conversion_binario_hexadecimal():
        try:
            valor_binario_hexadecimal = numero_binario_base.value if numero_binario_base.value is not None else ""
            resultado_binario_hexadecimal = binario_a_hexadecimal(valor_binario_hexadecimal)
            resultado_base_binario_hexadecimal.value = f"{resultado_binario_hexadecimal}"
        except ValueError:
            resultado_base_binario_hexadecimal.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_binario_hexadecimal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=140,
                                                      on_click=lambda _: mostrar_resultado_conversion_binario_hexadecimal())
    poner_en_funcion_binario_hexadecimal = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_binario_base, top=140), 
    ft.Container(mostrar_resultado_base_binario_hexadecimal_, top=350, left=1),
    ft.Container(resultado_base_binario_hexadecimal, top=390)])

    #DE BINARIO A BINARIO&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_binario_binario = ft.TextField(bgcolor="#9cc4b2", width=605)

    def binario_a_binario(numero_binario_binario):
        try:
        # Agregar ".0" si no hay parte fraccionaria
            numero_binario_binario = numero_binario_binario + ".0" if '.' not in numero_binario_binario else numero_binario_binario
            partes_binario_binario = numero_binario_binario.split('.')

            parte_entera_binario = partes_binario_binario[0]
            parte_fraccionaria_binario = partes_binario_binario[1] if len(partes_binario_binario) == 2 else ''

        # Validar que los dígitos de la parte entera y fraccionaria estén en el rango del 0 al 1 (sistema binario)
            if any(int(digito, 2) > 1 for digito in parte_entera_binario) or any(int(digito, 2) > 1 for digito in parte_fraccionaria_binario):
                raise ValueError("Los dígitos en el sistema binario deben estar en el rango del 0 al 1.")

        # En este ejemplo, simplemente devolveremos el mismo valor
            resultado_binario = parte_entera_binario + ('.' + parte_fraccionaria_binario if parte_fraccionaria_binario else '')
            return resultado_binario
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: Ingrese números binarios reales positivos"



    def mostrar_resultado_conversion_binario_binario():
        try:
            valor_binario_binario = numero_binario_base.value if numero_binario_base.value is not None else ""
            resultado_binario_binario = binario_a_binario(valor_binario_binario)
            resultado_base_binario_binario.value = f"{resultado_binario_binario}"
        except ValueError:
            resultado_base_binario_binario.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_binario_binario_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                                  style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                      color="Black", bgcolor="#9cc4b2"), width=200,
                                                      on_click=lambda _: mostrar_resultado_conversion_binario_binario())

    poner_en_funcion_binario_binario = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_binario_base, top=140), 
    ft.Container(mostrar_resultado_base_binario_binario_, top=350, left=1),
    ft.Container(resultado_base_binario_binario, top=390)])

    #DE OCTAL A BINARIO&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_octal_binario = ft.TextField(bgcolor="#9cc4b2", width=605)
    def octal_binario(numero_octal_binario):
        try:
            partes_octal_binario = numero_octal_binario.split('.')

            parte_entera_octal_binario = bin(int(partes_octal_binario[0], 8))[2:]

            parte_fraccionaria_octal_binario = ''
            if len(partes_octal_binario) == 2:
                parte_fraccionaria_octal_binario_1 = partes_octal_binario[1]

            # Convertir la parte fraccionaria a binario
                parte_fraccionaria_binario = bin(int(parte_fraccionaria_octal_binario_1, 8))[2:]

                parte_fraccionaria_octal_binario = parte_fraccionaria_binario.zfill(len(parte_fraccionaria_binario) + (3 - len(parte_fraccionaria_binario) % 3) % 3)

            resultado_octal_binario = parte_entera_octal_binario + ('.' + parte_fraccionaria_octal_binario if parte_fraccionaria_octal_binario else '')
            return resultado_octal_binario
        except ValueError as e:
            return f"Error: Ingrese números octales reales positivos"

    def mostrar_resultado_conversion_octal_binario():
        try:
            valor_octal_binario = numero_octal_base.value if numero_octal_base.value is not None else ""
            resultado_octal_binario = octal_binario(valor_octal_binario)
            resultado_base_octal_binario.value = f"{resultado_octal_binario}"
        except ValueError:
            resultado_base_octal_binario.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_octal_binario_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                              style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                  color="Black", bgcolor="#9cc4b2"), width=140,
                                                  on_click=lambda _: mostrar_resultado_conversion_octal_binario())
    poner_en_funcion_octal_binario = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_octal_base, top=140), 
    ft.Container(mostrar_resultado_base_octal_binario_, top=350, left=1),
    ft.Container(resultado_base_octal_binario, top=390)])

    #DE OCTAL A HEXADECIMAL&&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_octal_hexadecimal = ft.TextField (bgcolor="#9cc4b2", width=605)

    def octal_a_decimal_dos(numero_octal_decimal_dos):
        try:
            partes = numero_octal_decimal_dos.split('.')

        # Verificar que la parte entera y fraccionaria contengan solo dígitos en el rango 0-7
            if any(digito not in {'0', '1', '2', '3', '4', '5', '6', '7'} for digito in partes[0]) or (len(partes) == 2 and any(digito not in {'0', '1', '2', '3', '4', '5', '6', '7'} for digito in partes[1])):
                raise ValueError("Ingrese números octales reales positivos")

        # Convertir la parte entera a entero en base 8
            parte_entera = int(partes[0], 8)

        # Incluir la parte fraccionaria si existe
            parte_fraccionaria = f".{partes[1]}" if len(partes) == 2 else ''

        # Convertir la parte fraccionaria a decimal
            parte_fraccionaria_decimal = sum(int(digit) * 8**(-i-1) for i, digit in enumerate(partes[1])) if parte_fraccionaria else 0

        # Devolver el número decimal original
            resultado_decimal = parte_entera + parte_fraccionaria_decimal
            return resultado_decimal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: {str(e)}"

    def decimal_a_hexadecimal_dos(numero_decimal_hexadecimal_dos):
        try:
        # Dividir el número en parte entera y fraccionaria
            partes = str(numero_decimal_hexadecimal_dos).split('.')

        # Convertir la parte entera a hexadecimal
            parte_entera_hexadecimal = hex(int(partes[0]))[2:]

        # Convertir la parte fraccionaria a hexadecimal si existe
            parte_fraccionaria_hexadecimal = ''
            if len(partes) == 2:
                parte_fraccionaria_decimal = float('0.' + partes[1])
                precision = 12  # Puedes ajustar la precisión según tus necesidades
                for _ in range(precision):
                    parte_fraccionaria_decimal *= 16
                    parte_fraccionaria_hexadecimal += hex(int(parte_fraccionaria_decimal))[2:]
                    parte_fraccionaria_decimal -= int(parte_fraccionaria_decimal)

        # Unir la parte entera y fraccionaria si es necesario
            resultado_hexadecimal = parte_entera_hexadecimal + ('.' + parte_fraccionaria_hexadecimal if parte_fraccionaria_hexadecimal else '')
            return resultado_hexadecimal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: Ingrese números octales reales positivos"

    def octal_a_hexadecimal(numero_octal_dos):
        try:
            resultado_decimal = octal_a_decimal_dos(numero_octal_dos)
            resultado_hexadecimal = decimal_a_hexadecimal_dos(resultado_decimal)
            return resultado_hexadecimal
        except ValueError as e:
            return f"Error: {str(e)}"


    def mostrar_resultado_conversion_octal_hexadecimal():
        try:
            valor_octal_hexadecimal = numero_octal_base.value if numero_octal_base.value is not None else ""
            resultado_octal_hexadecimal = octal_a_hexadecimal(valor_octal_hexadecimal)
            resultado_base_octal_hexadecimal.value = f"{resultado_octal_hexadecimal}"
        except ValueError:
            resultado_base_octal_hexadecimal.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_octal_hexadecimal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                            style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                color="Black", bgcolor="#9cc4b2"), width=140,
                                                on_click=lambda _: mostrar_resultado_conversion_octal_hexadecimal())

    poner_en_funcion_octal_hexadecimal = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_octal_base, top=140), 
    ft.Container(mostrar_resultado_base_octal_hexadecimal_, top=350, left=1),
    ft.Container(resultado_base_octal_hexadecimal, top=390)])

    #DE OCTAL A OCTAL&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_octal_octal = ft.TextField(bgcolor="#9cc4b2", width=605)
    def octal_a_octal(numero_octal_octal):
        try:
        # Agregar ".0" si no hay parte fraccionaria
            numero_octal_octal = numero_octal_octal + ".0" if '.' not in numero_octal_octal else numero_octal_octal

            partes_octal_octal = numero_octal_octal.split('.')
        
            parte_entera_octal = partes_octal_octal[0]
            parte_fraccionaria_octal = partes_octal_octal[1] if len(partes_octal_octal) == 2 else ''

        # Validar que los dígitos de la parte entera y fraccionaria estén en el rango del 0 al 7
            if any(int(digito, 8) > 7 for digito in parte_entera_octal) or any(int(digito, 8) > 7 for digito in parte_fraccionaria_octal):
                raise ValueError("Los dígitos en el sistema octal deben estar en el rango del 0 al 7.")

        # En este ejemplo, simplemente devolveremos el mismo valor
            resultado_octal = parte_entera_octal + ('.' + parte_fraccionaria_octal if parte_fraccionaria_octal else '')
            return resultado_octal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: Ingrese números octales reales positivos"

    def mostrar_resultado_conversion_octal_octal():
        try:
            valor_octal_octal = numero_octal_base.value if numero_octal_base.value is not None else ""
            resultado_octal_octal = octal_a_octal(valor_octal_octal)
            resultado_base_octal_octal.value = f"{resultado_octal_octal}"
        except ValueError:
            resultado_base_octal_octal.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_octal_octal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                            style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                color="Black", bgcolor="#9cc4b2"), width=140,
                                                on_click=lambda _: mostrar_resultado_conversion_octal_octal())

    poner_en_funcion_octal_octal = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_octal_base, top=140), 
    ft.Container(mostrar_resultado_base_octal_octal_, top=350, left=1),
    ft.Container(resultado_base_octal_octal, top=390)])

    #DE HEXADECIMAL A BINARIO&&&&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_hexadecimal_binario = ft.TextField(bgcolor="#9cc4b2", width=605)
    def hexadecimal_a_binario(numero_hexadecimal_binario):
        try:
            partes_hexadecimal_binario = numero_hexadecimal_binario.split('.')

        # Convertir la parte entera a binario
            parte_entera_hexadecimal_binario = bin(int(partes_hexadecimal_binario[0], 16))[2:]

        # Inicializar la parte fraccionaria binaria
            parte_fraccionaria_binario = ''

        # Verificar si hay parte fraccionaria
            if len(partes_hexadecimal_binario) == 2:
                parte_fraccionaria_hexadecimal_binario_1 = partes_hexadecimal_binario[1]

            # Convertir la parte fraccionaria a binario
                parte_fraccionaria_binario = ''.join(format(int(digit, 16), '04b') for digit in parte_fraccionaria_hexadecimal_binario_1)

        # Combinar la parte entera y fraccionaria binaria
            resultado_hexadecimal_binario = parte_entera_hexadecimal_binario + ('.' + parte_fraccionaria_binario if parte_fraccionaria_binario else '')

            return resultado_hexadecimal_binario
        except ValueError as e:
            return f"Error: Ingrese números hexadecimales reales positivos"


    def mostrar_resultado_conversion_hexadecimal_binario():
        try:
            valor_hexadecimal_binario = numero_hexadecimal_base.value if numero_hexadecimal_base.value is not None else ""
            resultado_hexadecimal_binario = hexadecimal_a_binario(valor_hexadecimal_binario)
            resultado_base_hexadecimal_binario.value = f"{resultado_hexadecimal_binario}"
        except ValueError:
            resultado_base_hexadecimal_binario.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_hexadecimal_binario_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                                style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                    color="Black", bgcolor="#9cc4b2"), width=140,
                                on_click=lambda _: mostrar_resultado_conversion_hexadecimal_binario())
    poner_en_funcion_hexadecimal_binario = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_hexadecimal_base, top=140), 
    ft.Container(mostrar_resultado_base_hexadecimal_binario_, top=350, left=1),
    ft.Container(resultado_base_hexadecimal_binario, top=390)])

    #DE HEXADECIMAL A OCTAL&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_hexadecimal_octal=ft.TextField(bgcolor="#9cc4b2", width=605)

    def decimal_a_octal_dos(numero_decimal_octal_dos):
        try:
        # Dividir el número en parte entera y fraccionaria
            partes = str(numero_decimal_octal_dos).split('.')

        # Convertir la parte entera a octal
            parte_entera_octal = oct(int(partes[0]))[2:]

        # Convertir la parte fraccionaria a octal si existe
            parte_fraccionaria_octal = ''
            if len(partes) == 2:
                parte_fraccionaria_decimal = float('0.' + partes[1])
                precision = 12  # Puedes ajustar la precisión según tus necesidades
                for _ in range(precision):
                    parte_fraccionaria_decimal *= 8
                    parte_fraccionaria_octal += str(int(parte_fraccionaria_decimal))
                    parte_fraccionaria_decimal -= int(parte_fraccionaria_decimal)

        # Unir la parte entera y fraccionaria si es necesario
            resultado_octal = parte_entera_octal + ('.' + parte_fraccionaria_octal if parte_fraccionaria_octal else '')
            return resultado_octal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: Ingrese números hexadecimales reales positivos"
    
    def hexadecimal_a_decimal_dos(numero_hexadecimal_decimal_dos):
        try:
        # Convierte el número hexadecimal a decimal
            partes_hexadecimal_decimal = numero_hexadecimal_decimal_dos.split('.')

            parte_entera_hexadecimal_decimal = int(partes_hexadecimal_decimal[0], 16)
            parte_fraccionaria_hexadecimal_decimal = 0
            if len(partes_hexadecimal_decimal) == 2:
                parte_fraccionaria_hexadecimal_decimal = sum(int(digit, 16) * 16**(-i-1) for i, digit in enumerate(partes_hexadecimal_decimal[1]))
            resultante_hexadecimal_decimal = parte_entera_hexadecimal_decimal + parte_fraccionaria_hexadecimal_decimal
            return resultante_hexadecimal_decimal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: Ingrese números hexadecimales reales positivos"

    def hexadecimal_a_octal(numero_hexadecimal_dos):
        try:
            resultado_decimal = hexadecimal_a_decimal_dos(numero_hexadecimal_dos)
            resultado_octal = decimal_a_octal_dos(resultado_decimal)
            return resultado_octal
        except ValueError as e:
            return f"Error: {str(e)}"
    
    def mostrar_resultado_conversion_hexadecimal_octal():
        try:
            valor_hexadecimal_octal = numero_hexadecimal_base.value if numero_hexadecimal_base.value is not None else ""
            resultado_hexadecimal_octal = hexadecimal_a_octal(valor_hexadecimal_octal)
            resultado_base_hexadecimal_octal.value = f"{resultado_hexadecimal_octal}"
        except ValueError:
            resultado_base_hexadecimal_octal.value = "Error de conversión"
        page.update()
    
    mostrar_resultado_base_hexadecimal_octal = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                                style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                    color="Black", bgcolor="#9cc4b2"), width=140,
                                on_click=lambda _: mostrar_resultado_conversion_hexadecimal_octal())
    
    poner_en_funcion_hexadecimal_octal = ft.Stack([
    ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
    ft.Container(digite_numero_base, top=120), ft.Container(numero_hexadecimal_base, top=140), 
    ft.Container(mostrar_resultado_base_hexadecimal_octal, top=350, left=1),
    ft.Container(resultado_base_hexadecimal_octal, top=390)])




    #DE HEXADECIMAL A HEXADECIMAL&&&&&&&&&&&&&&&&&&&&
    resultado_base_hexadecimal_hexadecimal=ft.TextField(bgcolor="#9cc4b2", width=605)
    def hexadecimal_a_hexadecimal(numero_hexadecimal_hexadecimal):
        try:
        # Agregar ".0" si no hay parte fraccionaria
            numero_hexadecimal_hexadecimal = numero_hexadecimal_hexadecimal + ".0" if '.' not in numero_hexadecimal_hexadecimal else numero_hexadecimal_hexadecimal

            partes_hexadecimal_hexadecimal = numero_hexadecimal_hexadecimal.split('.')
        
            parte_entera_hexadecimal = partes_hexadecimal_hexadecimal[0]
            parte_fraccionaria_hexadecimal = partes_hexadecimal_hexadecimal[1] if len(partes_hexadecimal_hexadecimal) == 2 else ''

        # Validar que los dígitos de la parte entera y fraccionaria estén en el rango del 0 al 9 y de A a F
            if any(not (digito.isdigit() or digito.upper() in {'A', 'B', 'C', 'D', 'E', 'F'}) for digito in parte_entera_hexadecimal) or \
            any(not (digito.isdigit() or digito.upper() in {'A', 'B', 'C', 'D', 'E', 'F'}) for digito in parte_fraccionaria_hexadecimal):
                raise ValueError("Ingrese números hexadecimales reales positivos")

        # En este ejemplo, simplemente devolveremos el mismo valor
            resultado_hexadecimal = parte_entera_hexadecimal + ('.' + parte_fraccionaria_hexadecimal if parte_fraccionaria_hexadecimal else '')
            return resultado_hexadecimal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: {str(e)}"


    def mostrar_resultado_conversion_hexadecimal_hexadecimal():
        try:
            valor_hexadecimal_hexadecimal = numero_hexadecimal_base.value if numero_hexadecimal_base.value is not None else ""
            resultado_hexadecimal_hexadecimal = hexadecimal_a_hexadecimal(valor_hexadecimal_hexadecimal)
            resultado_base_hexadecimal_hexadecimal.value = f"{resultado_hexadecimal_hexadecimal}"
        except ValueError:
            resultado_base_hexadecimal_hexadecimal.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_hexadecimal_hexadecimal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                            style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                color="Black", bgcolor="#9cc4b2"), width=140,
                            on_click=lambda _: mostrar_resultado_conversion_hexadecimal_hexadecimal())
    poner_en_funcion_hexadecimal_hexadecimal = ft.Stack([
ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
ft.Container(digite_numero_base, top=120), ft.Container(numero_hexadecimal_base, top=140), 
ft.Container(mostrar_resultado_base_hexadecimal_hexadecimal_, top=350, left=1),
ft.Container(resultado_base_hexadecimal_hexadecimal, top=390)])
    
    #DE DECIMAL A BINARIO&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_decimal_binario=ft.TextField(bgcolor="#9cc4b2", width=605)
    def decimal_a_binario(numero_decimal):
        try:
        # Dividir el número en parte entera y fraccionaria
            partes = str(numero_decimal).split('.')

        # Convertir la parte entera a binario
            parte_entera_binario = bin(int(partes[0]))[2:]

        # Convertir la parte fraccionaria a binario si existe
            parte_fraccionaria_binario = ''
            if len(partes) == 2:
                parte_fraccionaria_decimal = float('0.' + partes[1])
                parte_fraccionaria_binario = ''
                while parte_fraccionaria_decimal > 0:
                    parte_fraccionaria_decimal *= 2
                    parte_fraccionaria_binario += str(int(parte_fraccionaria_decimal))
                    parte_fraccionaria_decimal -= int(parte_fraccionaria_decimal)

        # Unir la parte entera y fraccionaria si es necesario
            resultado_binario = parte_entera_binario + ('.' + parte_fraccionaria_binario if parte_fraccionaria_binario else '')
            return resultado_binario
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: Ingrese números decimales reales positivos"
    
    def mostrar_resultado_conversion_decimal_binario():
        try:
            valor_decimal_binario = numero_decimal_base.value if numero_decimal_base.value is not None else ""
            resultado_decimal_binario = decimal_a_binario(valor_decimal_binario)
            resultado_base_decimal_binario.value = f"{resultado_decimal_binario}"
        except ValueError:
            resultado_base_decimal_binario.value = "Error de conversión"
        page.update()

    mostrar_resultado_base_decimal_binario_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                            style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                color="Black", bgcolor="#9cc4b2"), width=140,
                            on_click=lambda _: mostrar_resultado_conversion_decimal_binario())
    poner_en_funcion_decimal_binario = ft.Stack([
ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
ft.Container(digite_numero_base, top=120), ft.Container(numero_decimal_base, top=140), 
ft.Container(mostrar_resultado_base_decimal_binario_, top=350, left=1),
ft.Container(resultado_base_decimal_binario, top=390)])
    
    #DE DECIMAL A OCTAL&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    resultado_base_decimal_octal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def decimal_a_octal(numero_decimal_octal):
        try:
        # Dividir el número en parte entera y fraccionaria
            partes = str(numero_decimal_octal).split('.')

        # Convertir la parte entera a octal
            parte_entera_octal = oct(int(partes[0]))[2:]

        # Convertir la parte fraccionaria a octal si existe
            parte_fraccionaria_octal = ''
            if len(partes) == 2:
                parte_fraccionaria_decimal = float('0.' + partes[1])
                precision = 12  # Puedes ajustar la precisión según tus necesidades
                for _ in range(precision):
                    parte_fraccionaria_decimal *= 8
                    parte_fraccionaria_octal += str(int(parte_fraccionaria_decimal))
                    parte_fraccionaria_decimal -= int(parte_fraccionaria_decimal)

        # Unir la parte entera y fraccionaria si es necesario
            resultado_octal = parte_entera_octal + ('.' + parte_fraccionaria_octal if parte_fraccionaria_octal else '')
            return resultado_octal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: Ingrese números decimales reales positivos"

    def mostrar_resultado_conversion_decimal_octal():
        try:
            valor_decimal_octal = numero_decimal_base.value if numero_decimal_base.value is not None else ""
            resultado_decimal_octal = decimal_a_octal(valor_decimal_octal)
            resultado_base_decimal_octal.value = f"{resultado_decimal_octal}"
        except ValueError:
            resultado_base_decimal_octal.value = "Error de conversión"
        page.update()

    
    mostrar_resultado_base_decimal_octal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                        style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                            color="Black", bgcolor="#9cc4b2"), width=140,
                        on_click=lambda _: mostrar_resultado_conversion_decimal_octal())
    poner_en_funcion_decimal_octal = ft.Stack([
ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
ft.Container(digite_numero_base, top=120), ft.Container(numero_decimal_base, top=140), 
ft.Container(mostrar_resultado_base_decimal_octal_, top=350, left=1),
ft.Container(resultado_base_decimal_octal, top=390)])
    
    #DE DECIMAL A HEXADECIMAL&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    resultado_base_decimal_hexadecimal = ft.TextField(bgcolor="#9cc4b2", width=605)

    def decimal_a_hexadecimal(numero_decimal_hexadecimal):
        try:
        # Dividir el número en parte entera y fraccionaria
            partes = str(numero_decimal_hexadecimal).split('.')

        # Convertir la parte entera a hexadecimal
            parte_entera_hexadecimal = hex(int(partes[0]))[2:]

        # Convertir la parte fraccionaria a hexadecimal si existe
            parte_fraccionaria_hexadecimal = ''
            if len(partes) == 2:
                parte_fraccionaria_decimal = float('0.' + partes[1])
                precision = 12  # Puedes ajustar la precisión según tus necesidades
                for _ in range(precision):
                    parte_fraccionaria_decimal *= 16
                    parte_fraccionaria_hexadecimal += hex(int(parte_fraccionaria_decimal))[2:]
                    parte_fraccionaria_decimal -= int(parte_fraccionaria_decimal)

        # Unir la parte entera y fraccionaria si es necesario
            resultado_hexadecimal = parte_entera_hexadecimal + ('.' + parte_fraccionaria_hexadecimal if parte_fraccionaria_hexadecimal else '')
            return resultado_hexadecimal
        except ValueError as e:
        # Captura errores de conversión y devuelve un mensaje de error
            return f"Error: Ingrese números decimales reales positivos"

    def mostrar_resultado_conversion_decimal_hexadecimal():
        try:
            valor_decimal_hexadecimal = numero_decimal_base.value if numero_decimal_base.value is not None else ""
            resultado_decimal_hexadecimal = decimal_a_hexadecimal(valor_decimal_hexadecimal)
            resultado_base_decimal_hexadecimal.value = f"{resultado_decimal_hexadecimal}"
        except ValueError:
            resultado_base_decimal_hexadecimal.value = "Error de conversión"
        page.update()

    
    mostrar_resultado_base_decimal_hexadecimal_ = ft.OutlinedButton("♥ Convertir ♥", tooltip="Convertir",
                        style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                            color="Black", bgcolor="#9cc4b2"), width=140,
                        on_click=lambda _: mostrar_resultado_conversion_decimal_hexadecimal())
    poner_en_funcion_decimal_hexadecimal = ft.Stack([
ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
ft.Container(digite_numero_base, top=120), ft.Container(numero_decimal_base, top=140), 
ft.Container(mostrar_resultado_base_decimal_hexadecimal_, top=350, left=1),
ft.Container(resultado_base_decimal_hexadecimal, top=390)])

#Rows de cada sección
    #Sección ayuda
    ayuda_abajo = ft.Row([
        ft.OutlinedButton("Info", tooltip="Info", 
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=140, on_click=info),
        ft.OutlinedButton("ASCII", tooltip="ASCII",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), color="#3e8c69"),
                           width=140, on_click=ascii),
        ft.IconButton(icon=ft.icons.HOME, icon_color="white", bgcolor="#3e8c69",
                      tooltip="Home", on_click=home),
        ft.OutlinedButton("Calculadora", tooltip="Calculadora",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69",), on_click=calculadora, width=140),
        ft.OutlinedButton("Cambio Base", tooltip="Cambio Base",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), on_click=base, width=140)],
    spacing=2)
    #Sección info
    info_abajo = ft.Row([
        ft.OutlinedButton("Info", tooltip="Info",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"), width=140, on_click=info),
        ft.OutlinedButton("ASCII", tooltip="ASCII",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), color="#3e8c69"),
                           width=140, on_click=ascii),
        ft.IconButton(icon=ft.icons.HOME, icon_color="white", bgcolor="#3e8c69",
                      tooltip="Home", on_click=home),
        ft.OutlinedButton("Calculadora", tooltip="Calculadora",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), on_click=calculadora, width=140),
        ft.OutlinedButton("Cambio Base", tooltip="Cambio Base",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), on_click=base, width=140)],
    spacing=2)

    #sección ascii
        #Row abajo
    ascii_abajo = ft.Row([
        ft.OutlinedButton("Info", tooltip="Info",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=140, on_click=info),
        ft.OutlinedButton("ASCII", tooltip="ASCII",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"),width=140, on_click=ascii),
        ft.IconButton(icon=ft.icons.HOME, icon_color="white", bgcolor="#3e8c69",
                      tooltip="Home", on_click=home),
        ft.OutlinedButton("Calculadora", tooltip="Calculadora",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), on_click=calculadora, width=140),
        ft.OutlinedButton("Cambio Base", tooltip="Cambio Base",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), on_click=base, width=140)],
    spacing=2)
        #Row arriba
    
    #Sección calculadora
        #Row abajo
    calculadora_abajo = ft.Row([
        ft.OutlinedButton("Info", tooltip="Info",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=140, on_click=info),
        ft.OutlinedButton("ASCII", tooltip="ASCII",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69",),width=140, on_click=ascii),
        ft.IconButton(icon=ft.icons.HOME, icon_color="white", bgcolor="#3e8c69",
                      tooltip="Home", on_click=home),
        ft.OutlinedButton("Calculadora", tooltip="Calculadora",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"), on_click=calculadora, width=140),
        ft.OutlinedButton("Cambio Base", tooltip="Cambio Base",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), on_click=base, width=140)],
    spacing=2)
        #Row arriba
    calculadora_arriba = ft.Row([
        ft.OutlinedButton("Suma", tooltip="Suma",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=150, on_click=suma),
        ft.OutlinedButton("Resta", tooltip="Resta",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"),width=150, on_click=resta),
        ft.OutlinedButton("Multiplicación", tooltip="Multiplicación",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=150, on_click=multiplicacion),
        ft.OutlinedButton("División", tooltip="División",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), 
                           width=150, on_click=division)],
    spacing=2)

    #Sección cambio base

    base_abajo = ft.Row([
        ft.OutlinedButton("Info", tooltip="Info",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=140, on_click=info),
        ft.OutlinedButton("ASCII", tooltip="ASCII",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69",),width=140, on_click=ascii),
        ft.IconButton(icon=ft.icons.HOME, icon_color="white", bgcolor="#3e8c69",
                      tooltip="Home", on_click=home),
        ft.OutlinedButton("Calculadora", tooltip="Calculadora",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), on_click=calculadora, width=140),
        ft.OutlinedButton("Cambio Base", tooltip="Cambio Base",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"), on_click=base, width=140)],
    spacing=2)

    #Sección suma
    suma_arriba = ft.Row([
        ft.OutlinedButton("Suma", tooltip="Suma",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"), width=150, on_click=suma),
        ft.OutlinedButton("Resta", tooltip="Resta",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"),width=150, on_click=resta),
        ft.OutlinedButton("Multiplicación", tooltip="Multiplicación",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=150, on_click=multiplicacion),
        ft.OutlinedButton("División", tooltip="División",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), 
                           width=150, on_click=division)],
    spacing=2)
    #Sección resta
    resta_arriba = ft.Row([
        ft.OutlinedButton("Suma", tooltip="Suma",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=150, on_click=suma),
        ft.OutlinedButton("Resta", tooltip="Resta",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"),width=150, on_click=resta),
        ft.OutlinedButton("Multiplicación", tooltip="Multiplicación",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=150, on_click=multiplicacion),
        ft.OutlinedButton("División", tooltip="División",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), 
                           width=150, on_click=division)],
    spacing=2)
    #Sección Multiplicación
    multiplicacion_arriba = ft.Row([
        ft.OutlinedButton("Suma", tooltip="Suma",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=150, on_click=suma),
        ft.OutlinedButton("Resta", tooltip="Resta",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"),width=150, on_click=resta),
        ft.OutlinedButton("Multiplicación", tooltip="Multiplicación",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"), width=150, on_click=multiplicacion),
        ft.OutlinedButton("División", tooltip="División",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), 
                           width=150, on_click=division)],
    spacing=2)
    #Sección División
    division_arriba = ft.Row([
        ft.OutlinedButton("Suma", tooltip="Suma",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=150, on_click=suma),
        ft.OutlinedButton("Resta", tooltip="Resta",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"),width=150, on_click=resta),
        ft.OutlinedButton("Multiplicación", tooltip="Multiplicación",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=150, on_click=multiplicacion),
        ft.OutlinedButton("División", tooltip="División",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"),
                           width=150, on_click=division)],
    spacing=2)
    

#Botón de ayuda
    boton_ayuda = ft.IconButton(
        icon=ft.icons.HELP,
        icon_color="#9cc4b2",
        bgcolor="#3e8c69",
        icon_size=40,
        tooltip="Ayuda",
        on_click=ayuda)

#Row de home 
    
    home_abajo = ft.Row([
        ft.ElevatedButton("Info", color="#3e8c69", bgcolor="white", tooltip="Info",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6)), width=140,
                           on_click=info),
        ft.ElevatedButton("ASCII", color="#3e8c69", bgcolor="white", tooltip="ASCII",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6)), 
                           width=140, on_click=ascii),
        ft.IconButton(icon=ft.icons.HOME, icon_color="#9cc4b2", bgcolor="#3e8c69",
                      tooltip="Home",),
        ft.ElevatedButton("Calculadora", color="#3e8c69", bgcolor="white", tooltip="Calculadora",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6)), width=140,
                           on_click=calculadora),
        ft.ElevatedButton("Cambio Base", color="#3e8c69", bgcolor="white", tooltip="Cambio Base",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6)), 
                           on_click=base, width=140)],
        spacing=2, auto_scroll=False)

#FUNCIÓN PARA CODIFICADOR DE ASCII.....................................................................................

    def encode_extended_ascii_binary(text_50, caracteres_adicionales_1):
        try:
        # Convierte cada carácter a su representación binaria y concatena los resultados
            binary_string_50 = ''.join(format(caracteres_adicionales_1.get(caracter_50, ord(caracter_50)), '08b') for caracter_50 in text_50)
        
        # Inserta un espacio después de cada grupo de 8 bits
            binary_string_with_spaces_50 = ' '.join([binary_string_50[i:i+8] for i in range(0, len(binary_string_50), 8)])
        
        # Devuelve la cadena de bits con espacios
            return binary_string_with_spaces_50
        except UnicodeEncodeError as e:
            print(f"Error al codificar el texto: {e}")
            return None

    def codificar_ascii_extendido(text_50, caracteres_adicionales_1):
        try:
        # Verifica si todos los caracteres en el texto están en caracteres_adicionales o son dígitos
            if all(caracter_50 in caracteres_adicionales_1 or caracter_50.isdigit() for caracter_50 in text_50):
            # Obtiene el valor numérico de cada carácter y lo convierte a cadena
                valores_ascii_50 = [str(caracteres_adicionales_1.get(caracter_50, ord(caracter_50))) for caracter_50 in text_50]
                return ' '.join(valores_ascii_50)
            else:
                return "Error: Solo se permiten caracteres en la lista y dígitos"
        except TypeError:
            return "Error: Ingrese un texto válido"

    cuadro_texto_1 = ft.TextField()

    cuadro_resultado_binario_50 = ft.TextField(multiline=True, bgcolor="#9cc4b2", width=605)

    caracteres_adicionales_1 = {
    'Ç': 128, 'a': 97, 'ü': 129, 'é': 130, 'â': 131, 'ä': 132, 'à': 133, 'å': 134, 'ç': 135, 'ê': 136, 'ë': 137,
    'è': 138, 'ï': 139, 'î': 140, 'ì': 141, 'Ä': 142, 'Å': 143, 'É': 144, 'æ': 145, 'Æ': 146, 'ô': 147, 'ö': 148,
    'ò': 149, 'û': 150, 'ù': 151, 'ÿ': 152, 'Ö': 153, 'Ü': 154, 'ø': 155, '£': 156, 'Ø': 157, '×': 158, 'ƒ': 159,
    'á': 160, 'í': 161, 'ó': 162, 'ú': 163, 'ñ': 164, 'Ñ': 165, 'ª': 166, 'º': 167, '¿': 168, '®': 169, '¬': 170,
    '½': 171, '¼': 172, '¡': 173, '«': 174, '»': 175, '░': 176, '▒': 177, '▓': 178, '│': 179, '┤': 180, 'Á': 181,
    'Â': 182, 'À': 183, '©': 184, '╣': 185, '║': 186, '╗': 187, '╝': 188, '¢': 189, '¥': 190, '┐': 191, '└': 192,
    '┴': 193, '┬': 194, '├': 195, '─': 196, '┼': 197, 'ã': 198, 'Ã': 199, '╚': 200, '╔': 201, '╩': 202, '╦': 203,
    '╠': 204, '═': 205, '╬': 206, '¤': 207, 'ð': 208, 'Ð': 209, 'Ê': 210, 'Ë': 211, 'È': 212, 'ı': 213, 'Í': 214,
    'Î': 215, 'Ï': 216, '┘': 217, '┌': 218, '█': 219, '▄': 220, '¦': 221, 'Ì': 222, '▀': 223, 'Ó': 224, 'ß': 225,
    'Ô': 226, 'Ò': 227, 'õ': 228, 'Õ': 229, 'µ': 230, 'þ': 231, 'Þ': 232, 'Ú': 233, 'Û': 234, 'Ù': 235, 'ý': 236,
    'Ý': 237, '¯': 238, '´': 239, '≡': 240, '±': 241, '‗': 242, '¾': 243, '¶': 244, '§': 245, '÷': 246, '¸': 247,
    '°': 248, '¨': 249, '·': 250, '¹': 251, '³': 252, '²': 253, '■': 254, '!': 33, '"': 34, '#': 35, '$': 36,
    '%': 37, '&': 38, "'": 39, '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47, '0': 48,
    '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, ':': 58, ';': 59, '<': 60,
    '=': 61, '>': 62, '?': 63, '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72,
    'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84,
    'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96,
    'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107,
    'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118,
    'w': 119, 'x': 120, 'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126, ' ': 32,
}

    def deditos(e):
        texto_ingresado_50 = cuadro_texto_1.value.strip()

        resultado_binario_50 = encode_extended_ascii_binary(texto_ingresado_50, caracteres_adicionales_1)
        cuadro_resultado_binario_50.value = resultado_binario_50

        # Forzar una actualización de la interfaz gráfica
        page.update()

    boton_codificar_1 = ft.OutlinedButton("♖ Codificar ♖", on_click=deditos,
                                         style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                             color="Black", bgcolor="#9cc4b2"), width=150)


#Función Biblioteca ASCII}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

    desplegable_biblioteca_todo = ft.Dropdown(
    options=[
        ft.dropdown.Option("Encontrar representación decimal y tecla a través de carácter"),
        ft.dropdown.Option("Encontrar carácter y tecla a través de representación decimal"),
    ],
    width=480, focused_bgcolor="#9cc4b2",
    filled=True,
    autofocus=True,
    focused_color="black",
    text_size=16,
    border_color="#3e8c69",
    border_radius=20,
    hint_text="Seleccione Modo de Búsqueda"
)
    def mostrar_seccion_segun_opcion_biblioteca(opcion_seleccionada_biblioteca):
    # Eliminar todos los controles existentes
        for control_biblioteca in page._controls.copy():
            page.remove(control_biblioteca)

    # Mostrar la sección correspondiente a la opción seleccionada
        if opcion_seleccionada_biblioteca == "Encontrar representación decimal y tecla a través de carácter":
            contenedor_caracter = ft.Stack([ft.Container(ascii_abajo, top=550, left=0),
                                           ft.Container(biblioteca_arriba, top=4, left=1), 
                                           ft.Container(desplegable_biblioteca_todo, top=100),
                                           ft.Container(ft.Text("Ingrese un carácter", size=10), top=200),
                                           ft.Container(cuadro_texto, top=240),
                                           ft.Container(boton_encontrar, top=320),
                                           ft.Container(ft.Row([
                    ft.Container(ft.OutlinedButton("Representación Decimal", height=55, width=205,
                                                   style=ft.ButtonStyle(color="black",
                                                    shape=ft.RoundedRectangleBorder(radius=5)))),
                    ft.Container(cuadro_resultado_ascii)], spacing=2), top=380),
                                           ft.Container(ft.Row([
                    ft.Container(ft.OutlinedButton("Tecla", height=55, width=205, style=ft.ButtonStyle(color="black",
                                                    shape=ft.RoundedRectangleBorder(radius=5)))),
                    ft.Container(cuadro_resultado_tecla_alt)], spacing=2), top=440)])
            page.add(contenedor_caracter)
        
        elif opcion_seleccionada_biblioteca == "Encontrar carácter y tecla a través de representación decimal":
            contenedor_decimal = ft.Stack([ft.Container(ascii_abajo, top=550, left=0),
                                           ft.Container(biblioteca_arriba, top=4, left=1), 
                                           ft.Container(desplegable_biblioteca_todo, top=100),
                                           ft.Container(ft.Text("Ingrese un número decimal", size=10), top=200),
                                           ft.Container(cuadro_texto_2, top=240),
                                           ft.Container(boton_codificar, top=320),
                                           ft.Container(ft.Row([
                    ft.Container(ft.OutlinedButton("Carácter ASCII", height=55, width=205,
                                                   style=ft.ButtonStyle(color="black",
                                                    shape=ft.RoundedRectangleBorder(radius=5)))),
                    ft.Container(cuadro_resultado_ascii_2)], spacing=2), top=380),
                                           ft.Container(ft.Row([
                    ft.Container(ft.OutlinedButton("Tecla", height=55, width=205, style=ft.ButtonStyle(color="black",
                                                    shape=ft.RoundedRectangleBorder(radius=5)))),
                    ft.Container(cuadro_resultado_tecla_alt_2)], spacing=2), top=440)])
            page.add(contenedor_decimal)

    def oprimir_sistema_biblioteca(e):
        sistema_seleccionado_biblioteca = desplegable_biblioteca_todo.value
        if sistema_seleccionado_biblioteca in {"Encontrar representación decimal y tecla a través de carácter", 
                                               "Encontrar carácter y tecla a través de representación decimal"}:
            mostrar_seccion_segun_opcion_biblioteca(sistema_seleccionado_biblioteca)

    desplegable_biblioteca_todo.on_change = oprimir_sistema_biblioteca

    def biblioteca(e):
    # Eliminar todos los controles existentes
        for control_biblioteca_2 in page._controls.copy():
            page.remove(control_biblioteca_2)

    # Agregar contenido nuevo
        biblioteca_ = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["white"]), width=620, height=620),
        ft.Container(desplegable_biblioteca_todo, top=100),
        ft.Container(ascii_abajo, bottom=30, left=0),
        ft.Container(biblioteca_arriba, top=4, left=1)
    ])

    # Agregar la sección correspondiente según la opción seleccionada en el desplegable

        page.add(biblioteca_)

    ascii_arriba = ft.Row([
        ft.OutlinedButton("Biblioteca ASCII Extendido", tooltip="Biblioteca ASCII Extendido",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=303, on_click=biblioteca),
        ft.OutlinedButton("Codificador ASCII Extendido", tooltip="Codificador ASCII Extendido",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69",),width=303, on_click=codificador_ascii_extendido)], spacing=2)
    
    biblioteca_arriba = ft.Row([
        ft.OutlinedButton("Biblioteca ASCII Extendido", tooltip="Biblioteca ASCII Extendido",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"), width=303, on_click=biblioteca),
        ft.OutlinedButton("Codificador ASCII Extendido", tooltip="Codificador ASCII Extendido",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69",),width=303, on_click=codificador_ascii_extendido)], spacing=2)
    
    codificador_ascii_extendido_abajo = ft.Row([
        ft.OutlinedButton("Biblioteca ASCII Extendido", tooltip="Biblioteca ASCII Extendido",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69"), width=303,on_click=biblioteca ),
        ft.OutlinedButton("Codificador ASCII Extendido", tooltip="Codificador ASCII Extendido",
                           style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6), 
                            color="#3e8c69", bgcolor="#9cc4b2"),width=303, on_click=codificador_ascii_extendido)], spacing=2)
    
#DE CARÁCTER A DECIMAL
    def encode_extended_ascii_binary(text, caracteres_adicionales):
        try:
        # Convierte cada carácter a su representación binaria y concatena los resultados
            binary_string = ''.join(format(caracteres_adicionales.get(caracter, ord(caracter)), '08b') for caracter in text)
        
        # Inserta un espacio después de cada grupo de 8 bits
            binary_string_with_spaces = ' '.join([binary_string[i:i+8] for i in range(0, len(binary_string), 8)])
        
        # Devuelve la cadena de bits con espacios
            return binary_string_with_spaces
        except UnicodeEncodeError as e:
            print(f"Error al codificar el texto: {e}")
            return None

    def codificar_ascii_extendido(text, caracteres_adicionales):
        try:
        # Verifica si solo se ingresó un carácter
            if len(text) == 1:
            # Obtiene el valor numérico del carácter y lo convierte a cadena
                valor_ascii = str(caracteres_adicionales.get(text, ord(text)))
                return valor_ascii
            else:
                if text.lower() == 'espacio':
                    return str(caracteres_adicionales[' '])
                elif text.lower() == 'null':
                    return "00"
                elif text.lower() == 'soh':
                    return "01"
                elif text.lower() == 'stx':
                    return "02"
                elif text.lower() == 'etx':
                    return "03"
                elif text.lower() == 'eot':
                    return "04"
                elif text.lower() == 'enq':
                    return "05"
                elif text.lower() == 'ack':
                    return "06"
                elif text.lower() == 'bel':
                    return "07"
                elif text.lower() == 'bs':
                    return "08"
                elif text.lower() == 'ht':
                    return "09"
                elif text.lower() == 'lf':
                    return "10"
                elif text.lower() == 'vt':
                    return "11"
                elif text.lower() == 'ff':
                    return "12"
                elif text.lower() == 'cr':
                    return "13"
                elif text.lower() == 'so':
                    return "14"
                elif text.lower() == 'si':
                    return "15"
                elif text.lower() == 'dle':
                    return "16"
                elif text.lower() == 'dc1':
                    return "17"
                elif text.lower() == 'dc2':
                    return "18"
                elif text.lower() == 'dc3':
                    return "19"
                elif text.lower() == 'dc4':
                    return "20"
                elif text.lower() == 'nak':
                    return "21"
                elif text.lower() == 'syn':
                    return "22"
                elif text.lower() == 'etb':
                    return "23"
                elif text.lower() == 'can':
                    return "24"
                elif text.lower() == 'em':
                    return "25"
                elif text.lower() == 'sub':
                    return "26"
                elif text.lower() == 'esc':
                    return "27"
                elif text.lower() == 'fs':
                    return "28"
                elif text.lower() == 'gs':
                    return "29"
                elif text.lower() == 'rs':
                    return "30"
                elif text.lower() == 'us':
                    return "31"
                elif text.lower() == 'del':
                    return "127"
                elif text.lower() == 'nbsp':
                    return "255"
                else:
                    return "Error: Ingrese un carácter válido"
        except TypeError:
            return "Error: Ingrese un texto válido"

    def obtener_valor_decimal(caracter, caracteres_adicionales):
        if caracter.lower() == 'espacio':
            return caracteres_adicionales[' '], "Alt + 32"
    # Verifica si el carácter es 'null' o 'NULL'
        if caracter.lower() == 'null':
            return 0, "00"
        if caracter.lower() == 'soh':
            return "01"
        if caracter.lower() == 'stx':
            return "02"
        if caracter.lower() == 'etx':
            return "03"
        if caracter.lower() == 'eot':
            return "04"
        if caracter.lower() == 'enq':
            return "05"
        if caracter.lower() == 'ack':
            return "06"
        if caracter.lower() == 'bel':
            return "07"
        if caracter.lower() == 'bs':
            return "08"
        if caracter.lower() == 'ht':
            return "09"
        if caracter.lower() == 'lf':
            return "10"
        if caracter.lower() == 'vt':
            return "11"
        if caracter.lower() == 'ff':
            return "12"
        if caracter.lower() == 'cr':
            return "13"
        if caracter.lower() == 'so':
            return "14"
        if caracter.lower() == 'si':
            return "15"
        if caracter.lower() == 'dle':
            return "16"
        if caracter.lower() == 'dc1':
            return "17"
        if caracter.lower() == 'dc2':
            return "18"
        if caracter.lower() == 'dc3':
            return "19"
        if caracter.lower() == 'dc4':
            return "20"
        if caracter.lower() == 'nak':
            return "21"
        if caracter.lower() == 'syn':
            return "22"
        if caracter.lower() == 'etb':
            return "23"
        if caracter.lower() == 'can':
            return "24"
        if caracter.lower() == 'em':
            return "25"
        if caracter.lower() == 'sub':
            return "26"
        if caracter.lower() == 'esc':
            return "27"
        if caracter.lower() == 'fs':
            return "28"
        if caracter.lower() == 'gs':
            return "29"
        if caracter.lower() == 'rs':
            return "30"
        if caracter.lower() == 'us':
            return "31"
        if caracter.lower() == 'del':
            return "127"
        if caracter.lower() == 'nbsp':
            return "255"
    # Verifica si el carácter es válido
        if caracter not in caracteres_adicionales:
            return "Error: Ingrese un carácter válido"
    
    # Obtiene el valor decimal del carácter
        valor_decimal = caracteres_adicionales[caracter]
        return valor_decimal, f"Alt + {valor_decimal}"

    cuadro_texto = ft.TextField()

    cuadro_resultado_ascii = ft.TextField(bgcolor="#9cc4b2", width=350)
    cuadro_resultado_tecla_alt = ft.TextField(bgcolor="#9cc4b2", width=350)

    # Define caracteres adicionales (copiar y pegar)
    caracteres_adicionales = {'Ç': 128, 'a': 97, 'ü': 129, 'é': 130, 'â': 131, 'ä': 132, 'à': 133, 'å': 134, 'ç': 135, 'ê': 136, 'ë': 137,
    'è': 138, 'ï': 139, 'î': 140, 'ì': 141, 'Ä': 142, 'Å': 143, 'É': 144, 'æ': 145, 'Æ': 146, 'ô': 147, 'ö': 148,
    'ò': 149, 'û': 150, 'ù': 151, 'ÿ': 152, 'Ö': 153, 'Ü': 154, 'ø': 155, '£': 156, 'Ø': 157, '×': 158, 'ƒ': 159,
    'á': 160, 'í': 161, 'ó': 162, 'ú': 163, 'ñ': 164, 'Ñ': 165, 'ª': 166, 'º': 167, '¿': 168, '®': 169, '¬': 170,
    '½': 171, '¼': 172, '¡': 173, '«': 174, '»': 175, '░': 176, '▒': 177, '▓': 178, '│': 179, '┤': 180, 'Á': 181,
    'Â': 182, 'À': 183, '©': 184, '╣': 185, '║': 186, '╗': 187, '╝': 188, '¢': 189, '¥': 190, '┐': 191, '└': 192,
    '┴': 193, '┬': 194, '├': 195, '─': 196, '┼': 197, 'ã': 198, 'Ã': 199, '╚': 200, '╔': 201, '╩': 202, '╦': 203,
    '╠': 204, '═': 205, '╬': 206, '¤': 207, 'ð': 208, 'Ð': 209, 'Ê': 210, 'Ë': 211, 'È': 212, 'ı': 213, 'Í': 214,
    'Î': 215, 'Ï': 216, '┘': 217, '┌': 218, '█': 219, '▄': 220, '¦': 221, 'Ì': 222, '▀': 223, 'Ó': 224, 'ß': 225,
    'Ô': 226, 'Ò': 227, 'õ': 228, 'Õ': 229, 'µ': 230, 'þ': 231, 'Þ': 232, 'Ú': 233, 'Û': 234, 'Ù': 235, 'ý': 236,
    'Ý': 237, '¯': 238, '´': 239, '≡': 240, '±': 241, '‗': 242, '¾': 243, '¶': 244, '§': 245, '÷': 246, '¸': 247,
    '°': 248, '¨': 249, '·': 250, '¹': 251, '³': 252, '²': 253, '■': 254, '!': 33, '"': 34, '#': 35, '$': 36,
    '%': 37, '&': 38, "'": 39, '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47, '0': 48,
    '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, ':': 58, ';': 59, '<': 60,
    '=': 61, '>': 62, '?': 63, '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72,
    'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84,
    'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96,
    'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107,
    'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118,
    'w': 119, 'x': 120, 'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126, ' ': 32, 'soh':1, 'stx':2, 'etx':3,
    'eot':4, 'enq':5, 'ack':6, 'bel':7, 'bs':8, 'ht':9, 'lf':10, 'vt':11, 'ff':12, 'cr':13, 'so':14, 'si':15, 'dle':16,
    'dc1':17, 'dc2':18, 'dc3':19, 'dc4':20, 'nak':21, 'syn':22, 'etb':23, 'can':24, 'em':25, 'sub':26, 'esc':27, 'fs':28, 'gs':29,
    'rs':30, 'us':31, 'del':127, 'nbsp':255
    }

    def codificar(e):
        texto_ingresado = cuadro_texto.value.strip()

        # Verifica si solo se ingresó un carácter
        if len(texto_ingresado) == 1:
            resultado_ascii = codificar_ascii_extendido(texto_ingresado, caracteres_adicionales)
            cuadro_resultado_ascii.value = resultado_ascii

            # Obtiene el valor decimal y muestra la tecla Alt
            valor_decimal, tecla_alt = obtener_valor_decimal(texto_ingresado, caracteres_adicionales)
            cuadro_resultado_tecla_alt.value = tecla_alt
        else:
            # Verifica si hay más de un espacio en blanco
            if texto_ingresado.lower() == 'espacio':
                cuadro_resultado_ascii.value = str(caracteres_adicionales[' '])
                cuadro_resultado_tecla_alt.value = "Alt + 32"
            elif texto_ingresado.lower() == 'null':
                cuadro_resultado_ascii.value = "0"
                cuadro_resultado_tecla_alt.value = "Alt + 00"
            elif texto_ingresado.count(' ') > 1:
                cuadro_resultado_ascii.value = "Error: Solo se permite ingresar un solo carácter o una definición completa"
                cuadro_resultado_tecla_alt.value = ""
            else:
                # Divide el texto en partes y procesa cada parte
                partes = texto_ingresado.split()
                resultados_ascii = [codificar_ascii_extendido(part, caracteres_adicionales) for part in partes]
                cuadro_resultado_ascii.value = ' '.join(resultados_ascii)

                # Obtiene los valores decimales y muestra las teclas Alt
                valores_decimales = [obtener_valor_decimal(part, caracteres_adicionales) for part in partes]
                teclas_alt = [f"Alt + {valor}" for valor in valores_decimales]
                cuadro_resultado_tecla_alt.value = ' '.join(teclas_alt)

        # Forzar una actualización de la interfaz gráfica
        page.update()

    boton_encontrar = ft.OutlinedButton("♘ Encontrar ♘", on_click=codificar,
                                        style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                            color="Black", bgcolor="#9cc4b2"), width=150)
    
    #DE DECIMAL A CARÁCTER

    def codificar_ascii_extendido_2(text, caracteres_adicionales):
        try:
        # Verifica si solo se ingresó un carácter
            if len(text) == 1:
            # Obtiene el valor numérico del carácter y lo convierte a cadena
                valor_ascii = str(caracteres_adicionales.get(text, ord(text)))
                return valor_ascii
            else:
            # Verifica si hay más de un espacio en blanco
                if text.lower() == 'espacio':
                    return str(caracteres_adicionales['espacio'])
                elif text.lower() == 'null':
                    return str(caracteres_adicionales['null'])
                elif text.lower() == 'soh':
                    return "01"
                elif text.lower() == 'stx':
                    return "02"
                elif text.lower() == 'etx':
                    return "03"
                elif text.lower() == 'eot':
                    return "04"
                elif text.lower() == 'enq':
                    return "05"
                elif text.lower() == 'ack':
                    return "06"
                elif text.lower() == 'bel':
                    return "07"
                elif text.lower() == 'bs':
                    return "08"
                elif text.lower() == 'ht':
                    return "09"
                elif text.lower() == 'lf':
                    return "10"
                elif text.lower() == 'vt':
                    return "11"
                elif text.lower() == 'ff':
                    return "12"
                elif text.lower() == 'cr':
                    return "13"
                elif text.lower() == 'cr':
                    return "13"
                elif text.lower() == 'so':
                    return "14"
                elif text.lower() == 'si':
                    return "15"
                elif text.lower() == 'dle':
                    return "16"
                elif text.lower() == 'dc1':
                    return "17"
                elif text.lower() == 'dc2':
                    return "18"
                elif text.lower() == 'dc3':
                    return "19"
                elif text.lower() == 'dc4':
                    return "20"
                elif text.lower() == 'nak':
                    return "21"
                elif text.lower() == 'syn':
                    return "22"
                elif text.lower() == 'etb':
                    return "23"
                elif text.lower() == 'can':
                    return "24"
                elif text.lower() == 'em':
                    return "25"
                elif text.lower() == 'sub':
                    return "26"
                elif text.lower() == 'esc':
                    return "27"
                elif text.lower() == 'fs':
                    return "28"
                elif text.lower() == 'gs':
                    return "29"
                elif text.lower() == 'rs':
                    return "30"
                elif text.lower() == 'us':
                    return "31"
                elif text.lower() == 'del':
                    return "127"
                elif text.lower() == 'nbsp':
                    return "255"
                else:
                    return "Error: Ingrese un carácter válido"
        except TypeError:
            return "Error: Ingrese un texto válido"

    def obtener_caracter_y_tecla_por_decimal(valor_decimal, caracteres_adicionales):
        try:
        # Maneja específicamente el caso del espacio en blanco
            if valor_decimal == 32:
                return 'espacio', f"Alt + {valor_decimal:02d}"

        # Busca el carácter correspondiente al valor decimal, y maneja los caracteres especiales
            for key, value in caracteres_adicionales.items():
                if value == valor_decimal:
                    return key, f"Alt + {valor_decimal:02d}"
        
        # Si no se encuentra un carácter correspondiente, devuelve un mensaje de error
            return "Error: No se encontró un carácter para el valor decimal proporcionado"
        except Exception as e:
            return f"Error: {str(e)}"

    cuadro_texto_2 = ft.TextField()

    cuadro_resultado_ascii_2 = ft.TextField(bgcolor="#9cc4b2", width=400)
    cuadro_resultado_tecla_alt_2 = ft.TextField(bgcolor="#9cc4b2", width=400)

    # Define caracteres adicionales (copiar y pegar)
    caracteres_adicionales = {'Ç': 128, 'a': 97, 'ü': 129, 'é': 130, 'â': 131, 'ä': 132, 'à': 133, 'å': 134, 'ç': 135, 'ê': 136, 'ë': 137,
    'è': 138, 'ï': 139, 'î': 140, 'ì': 141, 'Ä': 142, 'Å': 143, 'É': 144, 'æ': 145, 'Æ': 146, 'ô': 147, 'ö': 148,
    'ò': 149, 'û': 150, 'ù': 151, 'ÿ': 152, 'Ö': 153, 'Ü': 154, 'ø': 155, '£': 156, 'Ø': 157, '×': 158, 'ƒ': 159,
    'á': 160, 'í': 161, 'ó': 162, 'ú': 163, 'ñ': 164, 'Ñ': 165, 'ª': 166, 'º': 167, '¿': 168, '®': 169, '¬': 170,
    '½': 171, '¼': 172, '¡': 173, '«': 174, '»': 175, '░': 176, '▒': 177, '▓': 178, '│': 179, '┤': 180, 'Á': 181,
    'Â': 182, 'À': 183, '©': 184, '╣': 185, '║': 186, '╗': 187, '╝': 188, '¢': 189, '¥': 190, '┐': 191, '└': 192,
    '┴': 193, '┬': 194, '├': 195, '─': 196, '┼': 197, 'ã': 198, 'Ã': 199, '╚': 200, '╔': 201, '╩': 202, '╦': 203,
    '╠': 204, '═': 205, '╬': 206, '¤': 207, 'ð': 208, 'Ð': 209, 'Ê': 210, 'Ë': 211, 'È': 212, 'ı': 213, 'Í': 214,
    'Î': 215, 'Ï': 216, '┘': 217, '┌': 218, '█': 219, '▄': 220, '¦': 221, 'Ì': 222, '▀': 223, 'Ó': 224, 'ß': 225,
    'Ô': 226, 'Ò': 227, 'õ': 228, 'Õ': 229, 'µ': 230, 'þ': 231, 'Þ': 232, 'Ú': 233, 'Û': 234, 'Ù': 235, 'ý': 236,
    'Ý': 237, '¯': 238, '´': 239, '≡': 240, '±': 241, '‗': 242, '¾': 243, '¶': 244, '§': 245, '÷': 246, '¸': 247,
    '°': 248, '¨': 249, '·': 250, '¹': 251, '³': 252, '²': 253, '■': 254, '!': 33, '"': 34, '#': 35, '$': 36,
    '%': 37, '&': 38, "'": 39, '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47, '0': 48,
    '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, ':': 58, ';': 59, '<': 60,
    '=': 61, '>': 62, '?': 63, '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72,
    'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84,
    'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96,
    'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107,
    'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118,
    'w': 119, 'x': 120, 'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126, 'Espacio': 32, 'NULL':0, 'SOH': 1, 'STX': 2, 
    'ETX': 3, 'EOT': 4, 'ENQ': 5, 'ACK': 6, 'BEL': 7, 'BS': 8, 'HT': 9, 'LF': 10, 'VT': 11, 'FF': 12, 'CR': 13, 'SO': 14, 
    'SI': 15, 'DLE': 16, 'DC1': 17, 'DC2': 18, 'DC3': 19, 'DC4': 20, 'NAK': 21, 'SYN': 22, 'ETB': 23, 'CAN': 24, 'EM': 25, 
    'SUB': 26, 'ESC': 27, 'FS': 28, 'GS': 29, 'RS': 30, 'US': 31, 'DEL': 127, 'nbsp':255
    }

    def codificar(e):
        texto_ingresado = cuadro_texto_2.value.strip()

        try:
            # Intenta convertir el texto a un número entero
            valor_decimal = int(texto_ingresado)

            # Obtiene el carácter y la tecla Alt correspondientes al valor decimal
            caracter, tecla_alt = obtener_caracter_y_tecla_por_decimal(valor_decimal, caracteres_adicionales)

            # Actualiza los cuadros de texto con el resultado
            cuadro_resultado_ascii_2.value = caracter
            cuadro_resultado_tecla_alt_2.value = tecla_alt

        except ValueError:
            # En caso de que la conversión a entero falle
            cuadro_resultado_ascii_2.value = "Error: Ingrese un número en el intervalo [0,255]"
            cuadro_resultado_tecla_alt_2.value = "Error: Ingrese un número en el intervalo [0,255]"

        # Forzar una actualización de la interfaz gráfica
        page.update()

    boton_codificar = ft.OutlinedButton("♕ Encontrar ♕", on_click=codificar,
                                        style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=6),
                                                            color="Black", bgcolor="#9cc4b2"), width=150,)

#Escudo de la distri
    img_distri = ft.Image(
        src="https://rita.udistrital.edu.co:23604/adminlab/storage/imagenes_index/logoud.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
#Lo que va a aparecer para el inicio de la App

    fondo = ft.Stack([
        ft.Container(gradient=ft.LinearGradient(colors=["#9cc4b2"]), width=620, height=620),
        ft.Container(ft.Text("Bienvenido a", size=60, color="#3e8c69",
                             weight=ft.FontWeight.BOLD, italic=True), top=120, left=120),
        ft.Container(boton_ayuda, top=10, right=10),
        ft.Container(img, top=220, left=150), ft.Container(img_distri, top=-45, left=10),
        ft.Container(home_abajo, bottom=30, left=1,)
    ])
#Configuración página
    page.window_max_width = 646
    page.window_width = 646
    page.window_max_height = 640
    page.window_height = 640


#Añadir fondo para el inicio
    page.add(fondo)

#Para iniciar la función principal de la aplicación
ft.app(target=main, assets_dir="assets")
#ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")