import turtle

# Функція для малювання одного відрізка на фракталі
def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)
        t.right(120)
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)

# Функція для малювання сніжинки Коха
def draw_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

# Основна частина програми
def main():
    window = turtle.Screen()
    window.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    
    # Встановлюємо довжину сторони та рівень рекурсії
    length = 300  # Довжина сторони трикутника
    level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    
    # Переміщаємо черепаху в початкову точку
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()
    
    draw_snowflake(t, length, level)
    
    window.exitonclick()

if __name__ == '__main__':
    main()
