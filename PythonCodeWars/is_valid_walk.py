'''Vives en la ciudad de Cartesia, donde todos los caminos están dispuestos en una cuadrícula perfecta. Llegaste diez minutos antes a una cita, por lo que decidiste aprovechar para dar un pequeño paseo. La ciudad proporciona a sus ciudadanos una aplicación de generación de caminatas en sus teléfonos: cada vez que presiona el botón, le envía una serie de cadenas de una letra que representan las direcciones para caminar (por ejemplo, ['n', 's', 'w', 'mi']). Siempre camina solo una cuadra por cada letra (dirección) y sabe que le toma un minuto atravesar una cuadra de la ciudad, así que cree una función que se vuelva verdadera si la caminata que le da la aplicación le toma exactamente diez minutos (usted ¡No quiero llegar temprano ni tarde!) y, por supuesto, lo regresará a su punto de partida. Devuelve false en caso contrario.

Nota : siempre recibirá una matriz válida que contiene una variedad aleatoria de letras de dirección (solo 'n', 's', 'e' o 'w'). Nunca le dará una matriz vacía (¡eso no es caminar, eso es quedarse quieto!).'''

def is_valid_walk(walk):
    n = 0
    s = 0
    e = 0
    w = 0
    
    for i in walk:
        if i == 'n':
            n +=1
        elif i == 's':
            s +=1
        elif i == 'e':
            e +=1
        elif i == 'w':
            w +=1

    return (n == s) and (e == w) and (10 == n + s + e + w)


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))

'''def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
    return False'''