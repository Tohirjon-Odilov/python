class Gun:
    def __init__(self, screen):
        """Inistalizatsiya pushki"""
        self.screen = screen
        self.rect = self.image.get_rect("images/tank.png")
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """Risovanie pushki"""
        self.screen.blit(self.image, self.rect)
