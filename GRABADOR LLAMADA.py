import pyaudio
import wave

numeroMuestrasPorBuffer = 1024
nombreArchivoAudio = "p1.wav"
archivoEncontrado = True
#REPRODUCCION INICIAL DE LA LLAMADA
try:
    archivoAudio = wave.open(nombreArchivoAudio, 'rb')
except:
    archivoEncontrado = False

if archivoEncontrado == True:
    grabadorAudio = pyaudio.PyAudio()
    audioLeido = grabadorAudio.open(format = grabadorAudio.get_format_from_width(archivoAudio.getsampwidth()), channels = archivoAudio.getnchannels(), rate = archivoAudio.getframerate(), output = True)
    datos = archivoAudio.readframes(numeroMuestrasPorBuffer)

    print "Empieza la reproduccion del archivo " + nombreArchivoAudio
    while datos != '':
        audioLeido.write(datos)
        datos = archivoAudio.readframes(numeroMuestrasPorBuffer)
    print "Finaliza la reproduccion del archivo " + nombreArchivoAudio

    audioLeido.stop_stream()
    audioLeido.close()
    grabadorAudio.terminate()
else:
    print "El archivo " + nombreArchivoAudio + " no existe"

    
#GRABACION DE LA CEDULA DEL USUARIO
formatoAudio = pyaudio.paInt16
numeroCanalesAudio = 2
frecuenciaSonido = 44100
tiempoGrabacion = 10
nombreArchivoAudio = "cedula.wav"

grabadorAudio = pyaudio.PyAudio()
audioGrabado = grabadorAudio.open(format = formatoAudio, channels = numeroCanalesAudio, rate = frecuenciaSonido, input = True, frames_per_buffer = numeroMuestrasPorBuffer)

muestrasAudio = []
print "Inicia la grabacion de " + str(tiempoGrabacion) + " segundos"
for iteracion in range(0, int(frecuenciaSonido / numeroMuestrasPorBuffer * tiempoGrabacion)):
    datos = audioGrabado.read(numeroMuestrasPorBuffer)
    muestrasAudio.append(datos)
print "Ha terminado la grabacion de " + str(tiempoGrabacion) + " segundos"

audioGrabado.stop_stream()
audioGrabado.close()
grabadorAudio.terminate()

archivoAudio = wave.open(nombreArchivoAudio, 'wb')
archivoAudio.setnchannels(numeroCanalesAudio)
archivoAudio.setsampwidth(grabadorAudio.get_sample_size(formatoAudio))
archivoAudio.setframerate(frecuenciaSonido)
archivoAudio.writeframes(b''.join(muestrasAudio))
archivoAudio.close()

nombreArchivoAudio = "p2.wav"
archivoEncontrado = True
#REPRODUCCION LISTA DE CITAS POSIBLES
try:
    archivoAudio = wave.open(nombreArchivoAudio, 'rb')
except:
    archivoEncontrado = False

if archivoEncontrado == True:
    grabadorAudio = pyaudio.PyAudio()
    audioLeido = grabadorAudio.open(format = grabadorAudio.get_format_from_width(archivoAudio.getsampwidth()), channels = archivoAudio.getnchannels(), rate = archivoAudio.getframerate(), output = True)
    datos = archivoAudio.readframes(numeroMuestrasPorBuffer)

    print "Empieza la reproduccion del archivo " + nombreArchivoAudio
    while datos != '':
        audioLeido.write(datos)
        datos = archivoAudio.readframes(numeroMuestrasPorBuffer)
    print "Finaliza la reproduccion del archivo " + nombreArchivoAudio

    audioLeido.stop_stream()
    audioLeido.close()
    grabadorAudio.terminate()
else:
    print "El archivo " + nombreArchivoAudio + " no existe"

#CAPTURA DEL TIPO DE CITA
formatoAudio = pyaudio.paInt16
numeroCanalesAudio = 2
frecuenciaSonido = 44100
tiempoGrabacion = 2
nombreArchivoAudio = "cita.wav"

grabadorAudio = pyaudio.PyAudio()
audioGrabado = grabadorAudio.open(format = formatoAudio, channels = numeroCanalesAudio, rate = frecuenciaSonido, input = True, frames_per_buffer = numeroMuestrasPorBuffer)

muestrasAudio = []
print "Inicia la grabacion de " + str(tiempoGrabacion) + " segundos"
for iteracion in range(0, int(frecuenciaSonido / numeroMuestrasPorBuffer * tiempoGrabacion)):
    datos = audioGrabado.read(numeroMuestrasPorBuffer)
    muestrasAudio.append(datos)
print "Ha terminado la grabacion de " + str(tiempoGrabacion) + " segundos"

audioGrabado.stop_stream()
audioGrabado.close()
grabadorAudio.terminate()

archivoAudio = wave.open(nombreArchivoAudio, 'wb')
archivoAudio.setnchannels(numeroCanalesAudio)
archivoAudio.setsampwidth(grabadorAudio.get_sample_size(formatoAudio))
archivoAudio.setframerate(frecuenciaSonido)
archivoAudio.writeframes(b''.join(muestrasAudio))
archivoAudio.close()

nombreArchivoAudio = "p3.wav"
archivoEncontrado = True
#REPRODUCCION SELECCION DIAS
try:
    archivoAudio = wave.open(nombreArchivoAudio, 'rb')
except:
    archivoEncontrado = False

if archivoEncontrado == True:
    grabadorAudio = pyaudio.PyAudio()
    audioLeido = grabadorAudio.open(format = grabadorAudio.get_format_from_width(archivoAudio.getsampwidth()), channels = archivoAudio.getnchannels(), rate = archivoAudio.getframerate(), output = True)
    datos = archivoAudio.readframes(numeroMuestrasPorBuffer)

    print "Empieza la reproduccion del archivo " + nombreArchivoAudio
    while datos != '':
        audioLeido.write(datos)
        datos = archivoAudio.readframes(numeroMuestrasPorBuffer)
    print "Finaliza la reproduccion del archivo " + nombreArchivoAudio

    audioLeido.stop_stream()
    audioLeido.close()
    grabadorAudio.terminate()
else:
    print "El archivo " + nombreArchivoAudio + " no existe"

#CAPTURA DE SELECCION DE DIAS
formatoAudio = pyaudio.paInt16
numeroCanalesAudio = 2
frecuenciaSonido = 44100
tiempoGrabacion = 3
nombreArchivoAudio = "dias.wav"

grabadorAudio = pyaudio.PyAudio()
audioGrabado = grabadorAudio.open(format = formatoAudio, channels = numeroCanalesAudio, rate = frecuenciaSonido, input = True, frames_per_buffer = numeroMuestrasPorBuffer)

muestrasAudio = []
print "Inicia la grabacion de " + str(tiempoGrabacion) + " segundos"
for iteracion in range(0, int(frecuenciaSonido / numeroMuestrasPorBuffer * tiempoGrabacion)):
    datos = audioGrabado.read(numeroMuestrasPorBuffer)
    muestrasAudio.append(datos)
print "Ha terminado la grabacion de " + str(tiempoGrabacion) + " segundos"

audioGrabado.stop_stream()
audioGrabado.close()
grabadorAudio.terminate()

archivoAudio = wave.open(nombreArchivoAudio, 'wb')
archivoAudio.setnchannels(numeroCanalesAudio)
archivoAudio.setsampwidth(grabadorAudio.get_sample_size(formatoAudio))
archivoAudio.setframerate(frecuenciaSonido)
archivoAudio.writeframes(b''.join(muestrasAudio))
archivoAudio.close()

nombreArchivoAudio = "p4.wav"
archivoEncontrado = True
#REPRODUCCION INICIAL DE LA LLAMADA
try:
    archivoAudio = wave.open(nombreArchivoAudio, 'rb')
except:
    archivoEncontrado = False

if archivoEncontrado == True:
    grabadorAudio = pyaudio.PyAudio()
    audioLeido = grabadorAudio.open(format = grabadorAudio.get_format_from_width(archivoAudio.getsampwidth()), channels = archivoAudio.getnchannels(), rate = archivoAudio.getframerate(), output = True)
    datos = archivoAudio.readframes(numeroMuestrasPorBuffer)

    print "Empieza la reproduccion del archivo " + nombreArchivoAudio
    while datos != '':
        audioLeido.write(datos)
        datos = archivoAudio.readframes(numeroMuestrasPorBuffer)
    print "Finaliza la reproduccion del archivo " + nombreArchivoAudio

    audioLeido.stop_stream()
    audioLeido.close()
    grabadorAudio.terminate()
else:
    print "El archivo " + nombreArchivoAudio + " no existe"

