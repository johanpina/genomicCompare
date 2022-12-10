
#!/usr/bin/pytgon3
### ojo modificarlo para que haga los dos extremos al tiempo

## Importamos la liberia
import sys
import re

def main():

    ## Abrimos el archivo de entrada, el sys.argv[1] toma el nombre de lo que le enviemos en la terminal
    ## cuando ejecutamos y es lo que ingresa a la función para abrir el archivo
    infile          = open(sys.argv[1],'r')
    outfile_name    = sys.argv[1].replace('.fq','_trunc.fq')
    outfile         = open(outfile_name, 'w')
    ## Vamos a recorrer las lineas del archivo
    while True:
        ## leemos la primera linea
        id1 = infile.readline()
        ## se debe validar que retorne una linea vacía. con esto sabemos cuando parar el ciclo while
        if not id1:
            break

        sec = str(infile.readline()) ## Leemos la siguiente línea que es la de la secuencia
        id2 = str(infile.readline()) ## leemos el id2 
        cal = str(infile.readline()) ## leemos la línea de calidad
        

        ## Se realizan las validaciones para saber si es el archivo R1 o R2 para cortar las secuencias a la longitud que nos indicaron
        if re.search('R1', sys.argv[1]): ## si el archivo de entrada tiene R1 es porque es el de la ccadena forward y se deben cortar hasta 260 nucl.
            sec,cal = truncar(sec,cal,261) ## les enviamos las secuencias a la función truncar y el valor de la longitud de la secuecia
        elif re.search('R2',sys.argv[1]): ## si el archivo de entrada tiene R2 es porquee es el de la candena reverse y de deben cortar gast 220 nucl.
            sec,cal = truncar(sec,cal,220) ## se hace el llamado a truncar pero con diferente longitud.
        else:
            sys.stderr.write("El nombre de su archivo debe indicar R1 o R2") ## dde no encontrar los patrones en el archivo, me saca un error.


        imprimir = f'{id1} {sec}{id2} {cal}' ## definimos la forma en la que queremos imprimir la información en el archivo de salida
        outfile.write(imprimir) ## escribirmos la linea en el archivo.
        #print(imprimir)


    ## cerramos los archivos 
    infile.close()
    outfile.close()



def truncar(sec,cal, trunc_length):
    """
        Esta función recibe la secuencia y la linea de calidad y las recorta el numero caracteres que
        se especifiquen en trunc_length

        return: la línea de la secuencia y la linea de calidad truncadas (cortadas hasta n caracteres)
        donde n = trunc_length
    """
    sec = sec[0:trunc_length] ## extraemos solo los caracteres desde la posición 0 hasta trunc_length -1
    cal = cal[0:trunc_length]
    if not "\n" in sec: ## Si la secuencia no tiene un salto de carro se lo vamos a agregar
        sec = f'{sec}\n' ## usando el format para strings se le agrega al final de la secuencia el salto de línea.
        cal = f'{cal}\n'
    return sec,cal ## retornamos los valores.


if __name__=='__main__': ## Definimos este archivo como nuestro archivo principal (main)
    main() ## llamamos la función main para que ejecute todo lo que tenemos dentro de ella

