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
    
    def render_base_figure(self):
        start_x = 0
        start_y = 3
        x = start_x
        y = start_y
        start_dot = Dot(point=[start_x, start_y, 0])
        self.dots.append(start_dot)
        all_dots = [start_dot]
        all_lines = []
        self.add(start_dot)

        x += 1
        y -= 1
        figure_height = 5

        for i in range(figure_height - 1):
            dot_right = Dot(point=[x, y, 0])
            dot_left = Dot(point=[-1 * x, y, 0])
            ver_line_right = Line(start_dot, dot_right)
            self.line_dots_correspondence.append([start_dot, dot_right])
            ver_line_left = Line(start_dot, dot_left)
            self.line_dots_correspondence.append([start_dot, dot_left])
            all_lines.extend([ver_line_left, ver_line_right])
            self.add(ver_line_left, ver_line_right)
            self.play(Indicate(ver_line_right))
            self.play(Indicate(ver_line_left))
            all_dots.append(dot_right)
            all_dots.append(dot_left)
            prev_dot_right = dot_right
            prev_dot_left = dot_left
            x += 1
            y -= 1
            one_third_dot = self.get_one_third(dot_left, dot_right)
            two_third_dot = self.get_two_third(dot_left, dot_right)
            all_dots.append(one_third_dot)
            all_dots.append(two_third_dot)
            hor_lines = [Line(dot_left, one_third_dot), Line(
                one_third_dot, two_third_dot), Line(two_third_dot, dot_right),

                Line(dot_left, two_third_dot),
                Line(one_third_dot, dot_right),
                Line(dot_left, dot_right)
            ]
            self.line_dots_correspondence.append([dot_left, one_third_dot])
            self.line_dots_correspondence.append(
                [one_third_dot, two_third_dot])
            self.line_dots_correspondence.append([two_third_dot, dot_right])
            self.line_dots_correspondence.append([dot_left, dot_right])
            self.line_dots_correspondence.append([dot_left, two_third_dot])
            self.line_dots_correspondence.append([one_third_dot, dot_right])

            all_lines.extend(hor_lines)
            for hor_line in hor_lines:
                self.play(Indicate(hor_line))
            mid_ver_left = Line(start_dot, one_third_dot)
            self.line_dots_correspondence.append([start_dot, one_third_dot])

            mid_ver_right = Line(start_dot, two_third_dot)
            self.line_dots_correspondence.append([start_dot, two_third_dot])
            all_lines.append(mid_ver_left)
            all_lines.append(mid_ver_right)
            self.play(Indicate(mid_ver_right))
            self.play(Indicate(mid_ver_left))

            for hor_line in hor_lines:
                self.add(hor_line)
            self.add(dot_left, dot_right,
                     one_third_dot, two_third_dot, mid_ver_left, mid_ver_right)
        self.dots = all_dots
        self.lines = all_lines
        print(len(self.lines))

    def get_two_third(self, start: Dot, end: Dot) -> Dot:
        x = (2 * end.get_x()) / 3 + start.get_x()/3
        y = (2 * start.get_y()) / 3 + end.get_y()/3
        return Dot(point=[x, y, 0])

    def get_one_third(self, start: Dot, end: Dot) -> Dot:
        x = (2 * start.get_x()) / 3 + end.get_x()/3
        y = (2 * start.get_y()) / 3 + end.get_y()/3
        return Dot(point=[x, y, 0])