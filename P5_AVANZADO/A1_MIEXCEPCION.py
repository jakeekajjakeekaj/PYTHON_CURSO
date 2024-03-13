class MiExcepcion(Exception):   #De esta manera se declara una excepción propia, se crea una clase, la cuál llevará como atributos a Exception, es decir que tendrá todo lo de la clase Exception par amanejar excepciones
    def __init__(self, err):
        print(f"Cometiste el siguinete error: {err}");  #Este sería el mensaje que ocurriría con nuestra excepción

try:
    raise MiExcepcion("Simulando excepcion");   #Con raise se simula una excepción; así mismo nosotros al llamar a nuestra excepción la estamos ejecutando y mandando como parámero el 'error'
except:
    print("Pueh lo hiciste");   #De igual manera se ejcuta esta línea ya que se detectó una excepción