from itertools import combinations
from typing import List

from manim import *


class TheseManyTriangles(Scene):

    def construct(self):
        self.dots: List[Dot] = []
        self.lines: List[Line] = []
        self.line_dots_correspondence: List[Dot] = []
        self.total_triangles = 0
        self.add_sound(sound_file="Vincent Rubinetti - Grant's Etude.mp3")
        self.render_welcom()
        self.render_base_figure()
        self.detect_triangles()
        self.remove_base_figure()
        self.final_triangle_count()
        self.wait(3)
        
    def render_welcom(self):
        self.welcom = Text('These many TRIANGLES', gradient=(BLUE, GREEN))
        self.play(Write(self.welcom))

        self.transform_num = Text('0 Triangles', gradient=(BLUE, GREEN))
        self.transform_num.to_corner(UP + LEFT)
        self.play(Transform(self.welcom, self.transform_num))