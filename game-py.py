import random
from datetime import datetime

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

sky = Sky()

player = FirstPersonController()

texto_ayuda =Text(text=" W S D A para moverse y Espacio para saltar", color=color.black, scale= (1,1), origin=(0,-19))

cubo_inicio = Entity(position=Vec3(0, 0, 0),
                     model='cube',
                     scale=Vec3(1, 1, 1),
                     color=color.red,
                     collider='box')
cubo_final = Entity(position=Vec3(0, 0, -1),
                    model='cube',
                    scale=Vec3(1, 1, 1),
                    color=color.blue,
                    collider='box')


def crear_cubo(posicion):
    cubo = Entity(position=posicion,
                  model='cube',
                  scale=Vec3(1, 1, 1),
                  color=color.gray,
                  collider='box')


player.position = Vec3(0, 100, 0)

for i in range(10):
    x = random.randint(0, 4)
    crear_cubo(Vec3(x, 0, i))

tiempo_inicio = datetime.now()

def update():
    tiempo_ahora = datetime.now()
    if (tiempo_ahora - tiempo_inicio).total_seconds() > 3:
        texto_ayuda.disable()

    if player.position.y <= -10:
        player.position = Vec3(0, 100, 0)
    ray = raycast(player.position, player.down, distance=2, ignore=[player])

    if ray.entity == cubo_final:
        #print("Llegaste al cubo final")
        player.disable()
        texto = Text(text="Llegaste al cubo final", color=color.green, scale= (4,4), origin=(0,-1))
        boton = Button(text="Llegaste al cubo final", color=color.black, scale= (0.2,0.1), origin=(0,1))
        boton.on_click = quit



def input(key):
    if key == 'escape':
        quit()


app.run()
