# TC3041-P4-Primavera-2019

Medidor de Temperatura y Energia:
Se genero un sistema de Peso de combustible, temperatura a la que se quema y la energia generada.
Por simplicidad la energia generada es solo un tercio de la temperatura en Jules.
El peso decrementa en una cantidad figa basada en la temperatura.
La temperatura puede incrementar o decrementar en intervalos de entre 5 y 10 grados cada 10 segundos.
En caso de que baje la temperatura bajo los 80 grados se comienza a incrementar en 15 grados.
En caso de que suba la temperatura sobre los 400 grados, la temperatura comienza a decrementar en 15 grados.

Existen 20 generadores en diferentes regiones:
California:
5 Generadores
Texas:
9 Generadores
New York:
6 Generadores

Para ejecutar el programa se siguen los siguientes commandos:
```
docker run --name grafana -d -p 3000:3000 grafana/grafana
docker run --name influxdb -d -p 8086:8086 -v $PWD:/var/lib/influxdb influxdb
python iot-db-creator.py
docker cp data-iot_100k.txt influxdb:/
docker exec -it influxdb bash
```
Dentro de la terminal de bash en el contenedor se ejecutarn los commandos:
```
influx -import -path=data-iot_100k.txt -precison=s
```
Despues en el navegador acceder a localhost:3000
Agregar un nuevo source
Agregar la base de datos IOT100k de localhost:8086


