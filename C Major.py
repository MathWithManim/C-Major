from manim import *

class CMajor(Scene):
    def construct(self):
        # Loads the MusiXTex
        musixtex = TexTemplate()
        musixtex.add_to_preamble(r"\usepackage{musixtex}")
        
        # Creates the scale of a cmajor
        trebelcmajor = Tex(r"""
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

        # Writes the scale for trebel
        self.play(Write(trebelcmajor))
        self.wait(2)

        # Writes the scale name for trebel
        trebelscale = Text("Treble - C Major Scale", font="Zekton").shift(UP*3).scale(1.4)
        self.play(Write(trebelscale))
        self.wait()

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        
        basscmajor = Tex(r"""
        \begin{music}
        \instrumentnumber{1}
        \setstaffs1{1}
        \setclef1{\bass}
        \startextract
           \Notes
           \wh{J} \wh{K} \wh{L} \wh{M} \wh{N} \wh{a} \wh{b} \wh{c}
        \en
        \zendextract
        \end{music}
        """, tex_template=musixtex).scale(1.4)

        # Writes the scale for bass
        self.play(Write(basscmajor))
        self.wait(2)

        # Writes the scale name for bass
        bassscale = Text("Bass - C Major Scale", font="Zekton").shift(UP*3).scale(1.4)
        self.play(Write(bassscale))
        self.wait()

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        
        # Create a trebel and bass clef
        trebelclef = Tex(r"""
          \begin{music}
          \trebleclef
          \end{music}
        """, tex_template=musixtex).scale(1.4).to_edge(LEFT+UP, buff=0.2)
        self.play(Write(trebelclef))
        bassclef = Tex(r"""
          \begin{music}
          \bassclef
          \end{music}
        """, tex_template=musixtex).scale(1.4).to_edge(RIGHT+DOWN, buff=0.2)
        self.play(Write(bassclef))
        
        # Key signature
        keysignature = Text("C major has no sharps or flats in its key signature, making it the simplest major key in terms of notation. This is often why it's one of the first keys taught to beginners.", width=config["frame_width"]-2, font_size=128, font="Zekton")
        self.play(Write(keysignature))
        self.wait(4)
        
        # Fade out everything
        self.play(FadeOut(*self.mobjects))
        
        # Title for the diatonic chords
        titlediatonic = Text("Diatonic Chords of C Major", font="Zekton")
        self.play(Write(titlediatonic), titlediatonic.animate.shift(UP*3))
        self.wait()
        
        # Diatonic chords of the C major scale
        item1 = Text("• C Major")
        item2 = Text("• D Minor")
        item3 = Text("• E Minor")
        item4 = Text("• F Major")
        item5 = Text("• G Major")
        item6 = Text("• A Major")
        item7 = Text("• B Diminished")
        
        diatonics = VGroup(item1, item2, item3, item4, item5, item6, item7).scale(0.7)
        diatonics.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(diatonics))
        self.wait()
        
