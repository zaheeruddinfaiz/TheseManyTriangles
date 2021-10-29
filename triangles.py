from typing import List
from manim import *


class MovingVertices(Scene):

    def construct(self):
        self.dots: List[Dot] = []
        self.lines: List[Line] = []
        self.render_base_image()
        self.detect_triangles()

    def detect_triangles(self):
        print(len(self.dots))
        print(len(self.lines))

    def render_base_image(self):
        start_x = 0
        start_y = 3
        x = start_x
        y = start_y
        start_dot = Dot(point=[start_x, start_y, 0])
        self.dots.append(start_dot)
        all_dots = [start_dot]
        all_lines = []

        for i in range(5):
            dot_right = Dot(point=[x, y, 0])
            dot_left = Dot(point=[-1 * x, y, 0])
            if i > 0:
                ver_line_right = Line(start_dot, dot_right)
                ver_line_left = Line(start_dot, dot_left)
                all_lines.extend([ver_line_left, ver_line_right])
                self.add(ver_line_left, ver_line_right)
                self.play(Indicate(ver_line_right))
                self.play(Indicate(ver_line_left))
                all_dots.append(dot_right)
                all_dots.append(dot_left)
                all_dots.append(one_third_dot)
                all_dots.append(two_third_dot)
            prev_dot_right = dot_right
            prev_dot_left = dot_left
            x += 1
            y -= 1
            hor_line = Line(dot_left, dot_right, )
            all_lines.append(hor_line)
            self.play(Indicate(hor_line))
            one_third_dot = self.get_one_third(dot_left, dot_right)
            two_third_dot = self.get_two_third(dot_left, dot_right)
            mid_hor_left = Line(start_dot, one_third_dot)
            mid_hor_right = Line(start_dot, two_third_dot)
            all_lines.append(mid_hor_left)
            all_lines.append(mid_hor_right)
            self.play(Indicate(mid_hor_right))
            self.play(Indicate(mid_hor_left))
            self.add(dot_left, dot_right, hor_line,
                     one_third_dot, two_third_dot, mid_hor_left, mid_hor_right)
        self.dots = all_dots
        self.lines = all_lines
        print(len(self.lines))
        self.play(Indicate(self.lines[-1]), Indicate(self.lines[-2]))

        self.wait(duration=3)

    def get_two_third(self, start: Dot, end: Dot) -> Dot:
        x = (2 * end.get_x()) / 3 + start.get_x()/3
        y = (2 * start.get_y()) / 3 + end.get_y()/3
        return Dot(point=[x, y, 0])

    def get_one_third(self, start: Dot, end: Dot) -> Dot:
        x = (2 * start.get_x()) / 3 + end.get_x()/3
        y = (2 * start.get_y()) / 3 + end.get_y()/3
        return Dot(point=[x, y, 0])

        # self.add(NumberPlane())

        # dot = Dot(point=[0, 1, 0])
        # arrow = Arrow(ORIGIN, [1, 1, 0], buff=0)
        # numberplane = NumberPlane(
        #     x_range=[-10, 10, 1],
        #     y_range=[-10, 10, 1],
        # )
        # # origin_text = Text('(0, 0)').next_to(dot, DOWN)
        # # tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        # self.play(Indicate(arrow))
        # self.wait()
