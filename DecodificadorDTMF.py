import wave
import struct
import math
import random
from datetime import datetime, date, time, timedelta
class GoertzelDTMF:
    def __init__(self, frecuenciaMuestreo):
        self.frecuenciaMuestreo = frecuenciaMuestreo
        self.frecuenciasDTMF = [1209.0, 1336.0, 1477.0, 1633.0, 697.0, 770.0, 852.0, 941.0]
        self.secuenciaAnterior = {}
        self.secuenciaAnterior2 = {}
        self.potenciaTotal = {}
        self.indicesN = {}
        self.coeficientesVelocidadAngular = {}
        for frecuenciaDTMF in self.frecuenciasDTMF:
            self.secuenciaAnterior[frecuenciaDTMF] = 0.0
            self.secuenciaAnterior2[frecuenciaDTMF] = 0.0
            self.potenciaTotal[frecuenciaDTMF] = 0.0
            self.indicesN[frecuenciaDTMF] = 0.0
            frecuenciaNormalizada = frecuenciaDTMF / self.frecuenciaMuestreo
            self.coeficientesVelocidadAngular[frecuenciaDTMF] = 2.0 * math.cos(2.0 * math.pi * frecuenciaNormalizada)

    def identificarTecla(self, frecuencias):
        altasFrecuenciasDTMF = [1209.0, 1336.0, 1477.0, 1633.0]
        bajasFrecuenciasDTMF = [697.0, 770.0, 852.0, 941.0]
        altaFrecuencia = 0.0
        altaFrecuencia2 = 0.0
        for frecuenciaDTMF in altasFrecuenciasDTMF:
            if frecuencias[frecuenciaDTMF] > altaFrecuencia2:
                altaFrecuencia2 = frecuencias[frecuenciaDTMF]
                altaFrecuencia = frecuenciaDTMF
        bajaFrecuencia = 0.0
        bajaFrecuencia2 = 0.0
        for frecuenciaDTMF in bajasFrecuenciasDTMF:
            if frecuencias[frecuenciaDTMF] > bajaFrecuencia2:
                bajaFrecuencia2 = frecuencias[frecuenciaDTMF]
                bajaFrecuencia = frecuenciaDTMF
        if bajaFrecuencia == 697.0:
            if altaFrecuencia == 1209.0:
                return "1"
            elif altaFrecuencia == 1336.0:
                return "2"
            elif altaFrecuencia == 1477.0:
                return "3"
            elif altaFrecuencia == 1633.0:
                return "A"
        elif bajaFrecuencia == 770.0:
            if altaFrecuencia == 1209.0:
                return "4"
            elif altaFrecuencia == 1336.0:
                return "5"
            elif altaFrecuencia == 1477.0:
                return "6"
            elif altaFrecuencia == 1633.0:
                return "B"
        elif bajaFrecuencia == 852.0:
            if altaFrecuencia == 1209.0:
                return "7"
            elif altaFrecuencia == 1336.0:
                return "8"
            elif altaFrecuencia == 1477.0:
                return "9"
            elif altaFrecuencia == 1633.0:
                return "C"
        elif bajaFrecuencia == 941.0:
            if altaFrecuencia == 1209.0:
                return "*"
            elif altaFrecuencia == 1336.0:
                return "0"
            elif altaFrecuencia == 1477.0:
                return "#"
            elif altaFrecuencia == 1633.0:
                return "D"

    def run(self, valorMuestreado):
        frecuencias = {}
        for frecuenciaDTMF in self.frecuenciasDTMF:
            secuencia = valorMuestreado + self.coeficientesVelocidadAngular[frecuenciaDTMF] * self.secuenciaAnterior[frecuenciaDTMF] - self.secuenciaAnterior2[frecuenciaDTMF]
            self.secuenciaAnterior2[frecuenciaDTMF] = self.secuenciaAnterior[frecuenciaDTMF]
            self.secuenciaAnterior[frecuenciaDTMF] = secuencia
            self.indicesN[frecuenciaDTMF] += 1
            potencia = self.secuenciaAnterior2[frecuenciaDTMF] * self.secuenciaAnterior2[frecuenciaDTMF] + self.secuenciaAnterior[frecuenciaDTMF] * self.secuenciaAnterior[frecuenciaDTMF] - self.coeficientesVelocidadAngular[frecuenciaDTMF] * self.secuenciaAnterior[frecuenciaDTMF] * self.secuenciaAnterior2[frecuenciaDTMF]
            self.potenciaTotal[frecuenciaDTMF] += valorMuestreado * valorMuestreado
            if self.potenciaTotal[frecuenciaDTMF] == 0:
                self.potenciaTotal[frecuenciaDTMF] = 1
            frecuencias[frecuenciaDTMF] = potencia / (self.potenciaTotal[frecuenciaDTMF] * self.indicesN[frecuenciaDTMF])
        return self.identificarTecla(frecuencias)

def decode( grabacion ):
    archivoWAV = wave.open(grabacion, 'r')
    (numeroCanalesAudio, anchoMuestra, frecuenciaMuestreo, numeroMuestrasAudio, tipoCompresion, nombreCompresion) = archivoWAV.getparams()
    muestrasAudio = archivoWAV.readframes(numeroMuestrasAudio * numeroCanalesAudio)
    #Conversion del audio a un arreglo de numeros enteros
    muestrasAudio = struct.unpack_from("%dH" % numeroMuestrasAudio * numeroCanalesAudio, muestrasAudio)

    #Determinacion de la canalizacion del sonido (Si esta en Stereo o en Mono)
    canalIzquierda = []
    canalDerecha = []
    if numeroCanalesAudio == 2:
        for numero in range(0, len(muestrasAudio), 2):
            canalIzquierda.append(muestrasAudio[numero])
        for numero in range(1, len(muestrasAudio), 2):
            canalDerecha.append(muestrasAudio[numero])
    else:
        canalIzquierda = muestrasAudio
        canalDerecha = canalIzquierda

    binSize = 1600
    #Separar bin en cierto numero de partes para reducir errores debido al ruido
    binSizeSplit = 1
    cadenaTeclasOprimidas = ""
    valorTeclaAnterior = ""
    contador = 0
    valorTeclaAnteriorAuxiliar = ""
    for indice in range(0, len(canalIzquierda) - binSize, binSize / binSizeSplit):
        goertzelDTMF = GoertzelDTMF(frecuenciaMuestreo)
        for valorMuestreado in canalIzquierda[indice:indice + binSize]:
            value = goertzelDTMF.run(valorMuestreado)
        if value == valorTeclaAnterior:
            contador += 1
            if contador >= 10:
                cadenaTeclasOprimidas += value
                valorTeclaAnteriorAuxiliar = value
                contador = 0
        else:
            contador = 0
            valorTeclaAnterior = value
    return cadenaTeclasOprimidas


cedula = decode("./cedula.wav")
cita = int(decode("./cita.wav")[0])
dias = int(decode("./dias.wav"))
print cedula + "    " + str(cita) + ";   " + str(dias)
citas = ["Transferir a un asesor", "Medicina general", "Odontologia", "Higiene oral", "Ortopedia", "Nutricion", "Planificacion Familiar", "Neurologia", "Psicologia", "Control prenatal"]
print "Cedula paciente: " + cedula
if(cita == 0):
    print citas[cita]
else:
    print "Cita solicitada: " + citas[cita]
    print "Fecha: " + str( date.today() + timedelta(days=dias))
    print "Hora: " + str(random.randint(6,20)) + ":" + str(random.randrange(0,60,20))
    print "Consultorio: " + str(random.randint(201,215))
