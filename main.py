from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint

Window.size = (360, 640)  # Dimensões de um smartphone padrão

class Player(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "player.png"  # imagem do jogador (adicione depois)
        self.size_hint = (None, None)
        self.size = (64, 64)
        self.pos = (Window.width // 2 - self.width // 2, 50)


class Enemy(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "enemy.png"  # imagem do inimigo (adicione depois)
        self.size_hint = (None, None)
        self.size = (48, 48)
        self.x = randint(0, Window.width - self.width)
        self.y = Window.height
        self.pos = (self.x, self.y)

    def move(self):
        self.y -= 3
        self.pos = (self.x, self.y)


class GameScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player = Player()
        self.add_widget(self.player)

        self.enemies = []

        # Agendando o loop do jogo
        Clock.schedule_interval(self.spawn_enemy, 2)
        Clock.schedule_interval(self.update, 1/60)

    def spawn_enemy(self, dt):
        enemy = Enemy()
        self.enemies.append(enemy)
        self.add_widget(enemy)

    def update(self, dt):
        for enemy in self.enemies:
            enemy.move()
            if enemy.y < -enemy.height:
                self.remove_widget(enemy)
                self.enemies.remove(enemy)


class ArcadeGameApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    ArcadeGameApp().run()
