import random
import string
f = open("data-iot.txt","w+")
header_statement = "# DDL\n\nCREATE DATABASE IOT-generator\n\n# DML\n\n# CONTEXT-DATABASE: IOT-generator\n\n"
f.write(header_statement)
time = 1483250400
states = ["California", "Texas", "New_York"]
temperature_ca = [random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401),]
temperature_tx = [random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401),]
temperature_ny = [random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401), random.randint(80,401),]
weight_ca = [50000, 50000, 50000, 50000, 50000]
weight_tx = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
weight_ny = [50000, 50000, 50000, 50000, 50000, 50000]
for j in range(1000000):
    for i in range(5):
        if temperature_ca[i] <80:
            temperature_ca[i] = temperature_ca[i] + random.randint(10,15)
        elif temperature_ca[i] >400:
            temperature_ca[i] = temperature_ca[i] - random.randint(10,15)
        else:
            random_num = random.randint(0,2)
            if random_num == 0:
                temperature_ca[i] = temperature_ca[i] + random.randint(5,10)
            else:
                temperature_ca[i] = temperature_ca[i] - random.randint(5,10)
        energy = temperature_ca[i] * 0.3
        weight_ca[i] = weight_ca[i] - temperature_ca[i]*0.0125
        if weight_ca[i] < 0:
            weight_ca[i] = 50000
        f.write("energy,location=California,generator=" + str(i +1) +" value=" + str(energy) + " " + str(time)+"\n")
        f.write("temperature,location=California,generator=" + str(i +1) +" value=" + str(temperature_ca[i]) + " " + str(time)+"\n")
        f.write("weight,location=California,generator=" + str(i +1) +" value=" + str(weight_ca[i]) + " " + str(time)+"\n")
    for i in range(9):
        if temperature_tx[i] <80:
            temperature_tx[i] = temperature_tx[i] + random.randint(10,15)
        elif temperature_tx[i] >400:
            temperature_tx[i] = temperature_tx[i] - random.randint(10,15)
        else:
            random_num = random.randint(0,2)
            if random_num == 0:
                temperature_tx[i] = temperature_tx[i] + random.randint(5,10)
            else:
                temperature_tx[i] = temperature_tx[i] - random.randint(5,10)
        energy = temperature_tx[i] * 0.3
        weight_tx[i] = weight_tx[i] - temperature_tx[i]*0.0125
        if weight_tx[i] < 0:
            weight_tx[i] = 50000
        f.write("energy,location=Texas,generator=" + str(i +1) +" value=" + str(energy) + " " + str(time)+"\n")
        f.write("temperature,location=Texas,generator=" + str(i +1) +" value=" + str(temperature_tx[i]) + " " + str(time)+"\n")
        f.write("weight,location=Texas,generator=" + str(i +1) +" value=" + str(weight_tx[i]) + " " + str(time)+"\n")
    for i in range(6):
        if temperature_ny[i] <80:
            temperature_ny[i] = temperature_ny[i] + random.randint(10,15)
        elif temperature_ny[i] >400:
            temperature_ny[i] = temperature_ny[i] - random.randint(10,15)
        else:
            random_num = random.randint(0,2)
            if random_num == 0:
                temperature_ny[i] = temperature_ny[i] + random.randint(5,10)
            else:
                temperature_ny[i] = temperature_ny[i] - random.randint(5,10)
        energy = temperature_ny[i] * 0.3
        weight_ny[i] = weight_ny[i] - temperature_ny[i]*0.0125
        if weight_ny[i] < 0:
            weight_ny[i] = 50000
        f.write("energy,location=NY,generator=" + str(i +1) +" value=" + str(energy) + " " + str(time)+"\n")
        f.write("temperature,location=NY,generator=" + str(i +1) +" value=" + str(temperature_ny[i]) + " " + str(time)+"\n")
        f.write("weight,location=NY,generator=" + str(i +1) +" value=" + str(weight_ny[i]) + " " + str(time)+"\n")
    time+=10

f.close()
