import pyaudio
import wave

numeroMuestrasPorBuffer = 1024
formatoAudio = pyaudio.paInt16
numeroCanalesAudio = 2
frecuenciaSonido = 44100
tiempoGrabacion = 15
nombreArchivoAudio = "output.wav"

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