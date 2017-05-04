import pyaudio
import wave

numeroMuestrasPorBuffer = 1024
nombreArchivoAudio = "output.wav"
archivoEncontrado = True

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