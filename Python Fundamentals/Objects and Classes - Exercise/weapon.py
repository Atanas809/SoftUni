Class Weapon:
  def __init__(self, bullets: int):
        self.bullets = bullets
      
  def shoot(self):

        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"
