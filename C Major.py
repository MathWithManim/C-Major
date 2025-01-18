from manim import *

class CMajor(Scene):
    def construct(self):
        # Loads the MusiXTex
        musixtex = TexTemplate()
        musixtex.add_to_preamble(r"\usepackage{musixtex}")

        # Creates the scale of a cmajor
        cmajor = Tex(r"""
        \begin{music}
        \instrumentnumber{1}
        \setstaffs1{1}
        \startextract
           \Notes
           \wh{c} \wh{d} \wh{e} \wh{f} \wh{g} \wh{h} \wh{i} \wh{j}
        \en
        \zendextract
        \end{music}
        """, tex_template=musixtex).scale(1.4)

        # Writes the scale
        self.play(Write(cmajor))
        self.wait(4)

        # Writes the scale name
        scale = Text("C Major Scale", font="Zekton").shift(UP*3).scale(1.4)
        self.play(Write(scale))
        self.wait()

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()