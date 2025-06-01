import turtle

# Seadistus
aken = turtle.Screen()
aken.bgcolor("white")
joonistaja = turtle.Turtle()
joonistaja.speed(0)  # kiirus

# kolmnurk
def kolmnurk(pikkus):
    for _ in range(3):
        joonistaja.forward(pikkus)
        joonistaja.left(120)

# 11 kolmnurka
for i in range(11):
    kolmnurk(100)
    joonistaja.left(360 / 11)

# aken kinni
aken.exitonclick()

