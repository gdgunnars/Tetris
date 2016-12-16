from pygame.mixer import Sound

class Sounds():
    """A class to store all sounds in Tetris."""

    def __init__(self):
        """Initialize Sounds."""
        self.title_music = Sound('sounds/music/title_music.mp3')
        self.a_type_music = Sound('sounds/music/a_type_music.mp3')
        self.b_type_music = Sound('sounds/music/b_type_music.mp3')
        self.c_type_music = Sound('sounds/music/c_type_music.mp3')
        self.high_score_music = Sound('sounds/music/high_score_music.mp3')