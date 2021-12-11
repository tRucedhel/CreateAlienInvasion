class Settings:
    """A Class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (115, 208, 207)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 1.8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 58, 58)
        self.bullets_allowed = 4

        #Alien settings
        self.alien_speed = 0.8
        self.fleet_drop_speed = 9
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5

        #fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and aliens point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)