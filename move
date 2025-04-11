from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
import random

Window.size = (480, 800)

class Projectile(Widget):
    velocity_y = NumericProperty(5)

    def move(self):
        self.y += self.velocity_y

class Enemy(Widget):
    velocity_y = NumericProperty(-2)

    def move(self):
        self.y += self.velocity_y

class Player(Widget):
    pass

class GameScreen(Widget):
    player = None
    projectiles = []
    enemies = []

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        with self.canvas:
            Color(0.1, 0.1, 0.1)
            Rectangle(pos=self.pos, size=Window.size)
        self.player = Player(pos=(Window.width / 2 - 25, 50), size=(50, 50))
        self.add_widget(self.player)
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        Clock.schedule_interval(self.spawn_enemy, 2)

    def on_touch_down(self, touch):
        self.fire_projectile()

    def fire_projectile(self):
        projectile = Projectile(pos=(self.player.center_x - 5, self.player.top), size=(10, 20))
        with projectile.canvas:
            Color(0.2, 0.8, 1)
            Rectangle(pos=projectile.pos, size=projectile.size)
        self.add_widget(projectile)
        self.projectiles.append(projectile)

    def spawn_enemy(self, dt):
        x = random.randint(0, Window.width - 50)
        enemy = Enemy(pos=(x, Window.height), size=(50, 50))
        with enemy.canvas:
            Color(1, 0.2, 0.2)
            Rectangle(pos=enemy.pos, size=enemy.size)
        self.add_widget(enemy)
        self.enemies.append(enemy)

    def update(self, dt):
        for projectile in self.projectiles[:]:
            projectile.move()
            if projectile.top > Window.height:
                self.remove_widget(projectile)
                self.projectiles.remove(projectile)

        for enemy in self.enemies[:]:
            enemy.move()
            if enemy.y < 0:
                self.remove_widget(enemy)
                self.enemies.remove(enemy)

        for projectile in self.projectiles[:]:
            for enemy in self.enemies[:]:
                if projectile.collide_widget(enemy):
                    self.remove_widget(projectile)
                    self.remove_widget(enemy)
                    self.projectiles.remove(projectile)
                    self.enemies.remove(enemy)
                    break

class ArcadeShooterApp(App):
    def build(self):
        return GameScreen()

if __name__ == "__main__":
    ArcadeShooterApp().run()
