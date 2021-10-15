from big_ol_pile_of_manim_imports import *

class TikzMobject(TextMobject):
    CONFIG = {
        "stroke_width": 3,
        "fill_opacity": 0,
        "stroke_opacity": 1,
        # "stroke_color":RED,
        # "camera_config":{"background_color":WHITE},
    }

class ExampleTikz(Scene):
    def construct(self):
        # fichier = open("/home/huxod/recherche/opahc/presentation/figures/figures/arbres_pw/arbre1.tex","r")
        # lines = fichier.readlines()
        # arbre1 = TikzMobject(''.join(lines))
        # fichier.close()
        # self.play(Write(arbre1))
        # self.wait()
        # fichier = open("/home/huxod/recherche/opahc/presentation/figures/figures/arbres_pw/arbre12.tex","r")
        # lines = fichier.readlines()
        # arbre12 = TikzMobject(''.join(lines))
        # arbre12[-1:].set_fill(None,0) \
        #              .set_stroke(None,2) \
        #              .set_color(RED)
        # fichier.close()
        # self.play(ReplacementTransform(arbre1,arbre12))
        # self.wait()
        # self.remove(arbre12)
        fichier = open("/home/huxod/recherche/opahc/presentation/figures/figures/arbres_pw/arbre8767595394312ske.tex","r")
        lines = fichier.readlines()
        arbre8767595394312ske = TextMobject(''.join(lines))
        fichier.close()
        fichier = open("/home/huxod/recherche/opahc/presentation/figures/figures/arbres_pw/arbre_construct2_red_forest.tex","r")
        lines = fichier.readlines()
        arbre_construct2_red_forest = TextMobject(''.join(lines))
        fichier.close()
        fichier = open("/home/huxod/recherche/opahc/presentation/figures/figures/arbres_pw/arbre_construct3_red_forest.tex","r")
        lines = fichier.readlines()
        arbre_construct3_red_forest = TextMobject(''.join(lines))
        fichier.close()
        fichier = open("/home/huxod/recherche/opahc/presentation/figures/figures/arbres_pw/arbre8767595394312_1.tex","r")
        lines = fichier.readlines()
        arbre8767595394312 = TextMobject(''.join(lines))
        fichier.close()
        arbre8767595394312ske.set_fill(None,0) \
                             .set_stroke(None,2)
        arbre_construct2_red_forest.set_fill(None,0) \
                                   .set_stroke(None,2)
        arbre_construct3_red_forest.set_fill(None,0) \
                                   .set_stroke(None,2)
        arbre8767595394312.set_fill(None,0) \
                          .set_stroke(None,2)
        
        arbre8767595394312ske[-7:-5].set_color(RED)
        arbre8767595394312ske[-1].set_color(RED)
        arbre_construct2_red_forest[-9:-5].set_color(RED)
        arbre_construct2_red_forest[-1].set_color(RED)
        arbre_construct3_red_forest[-10:-5].set_color(RED)
        arbre_construct3_red_forest[-1].set_color(RED)
        arbre8767595394312[-11:-5].set_color(RED)
        arbre8767595394312[-1].set_color(RED)
        self.play(Write(arbre8767595394312ske))
        # self.play(Write(arbre8767595394312ske[0]))
        # self.play(Write(arbre8767595394312ske[1]))
        # self.play(Write(arbre8767595394312ske[2]))
        # self.play(Write(arbre8767595394312ske[3]))
        # self.play(Write(arbre8767595394312ske[4]))
        # self.play(Write(arbre8767595394312ske[5]))
        # self.play(Write(arbre8767595394312ske[6]))
        # self.play(Write(arbre8767595394312ske[7]))
        # self.play(Write(arbre8767595394312ske[8]))
        # self.play(Write(arbre8767595394312ske[9]))
        # self.play(Write(arbre8767595394312ske[10]))
        # self.play(Write(arbre8767595394312ske[11]))
        # self.play(Write(arbre8767595394312ske[12]))
        # self.play(Write(arbre8767595394312ske[13]))
        # self.play(Write(arbre8767595394312ske[14]))
        # self.play(Write(arbre8767595394312ske[15]))
        # self.play(Write(arbre8767595394312ske[16]))
        # self.play(Write(arbre8767595394312ske[17]))
        # self.play(Write(arbre8767595394312ske[18]))
        # self.play(Write(arbre8767595394312ske[19]))
        # self.play(Write(arbre8767595394312ske[20]))
        self.wait(3)
        # self.clear()
        
        # self.play(Write(arbre_construct2_red_forest[0]))
        # self.play(Write(arbre_construct2_red_forest[1]))
        # self.play(Write(arbre_construct2_red_forest[2]))
        # self.play(Write(arbre_construct2_red_forest[3]))
        # self.play(Write(arbre_construct2_red_forest[4]))
        # self.play(Write(arbre_construct2_red_forest[5]))
        # self.play(Write(arbre_construct2_red_forest[6]))
        # self.play(Write(arbre_construct2_red_forest[7]))
        # self.play(Write(arbre_construct2_red_forest[8]))
        # self.play(Write(arbre_construct2_red_forest[9]))
        # self.play(Write(arbre_construct2_red_forest[10]))
        # self.play(Write(arbre_construct2_red_forest[11]))
        # self.play(Write(arbre_construct2_red_forest[12]))
        # self.play(Write(arbre_construct2_red_forest[13]))
        # self.play(Write(arbre_construct2_red_forest[14]))
        # self.play(Write(arbre_construct2_red_forest[15]))
        # self.play(Write(arbre_construct2_red_forest[16]))
        # self.play(Write(arbre_construct2_red_forest[17]))
        # self.play(Write(arbre_construct2_red_forest[18]))
        # self.play(Write(arbre_construct2_red_forest[19]))
        # self.play(Write(arbre_construct2_red_forest[20]))
        # self.play(Write(arbre_construct2_red_forest[21]))
        # self.play(Write(arbre_construct2_red_forest[22]))
        # self.play(Write(arbre_construct2_red_forest[23]))
        # self.play(Write(arbre_construct2_red_forest[24]))
        # self.play(Write(arbre_construct2_red_forest[25]))
        # self.play(Write(arbre_construct2_red_forest[26]))
        # self.play(Write(arbre_construct2_red_forest[27]))
        # self.play(Write(arbre_construct2_red_forest[28]))
        # self.play(Write(arbre_construct2_red_forest[29]))
        # self.play(Write(arbre_construct2_red_forest[30]))
        self.play( # déplacement du petit arbre à droite 1-1
            ReplacementTransform(arbre8767595394312ske[16],arbre_construct2_red_forest[26]),
            ReplacementTransform(arbre8767595394312ske[17],arbre_construct2_red_forest[27]),
            ReplacementTransform(arbre8767595394312ske[18],arbre_construct2_red_forest[28]),
            ReplacementTransform(arbre8767595394312ske[19],arbre_construct2_red_forest[29]),
            ReplacementTransform(arbre8767595394312ske[20],arbre_construct2_red_forest[30]),
        )
        self.wait() # avant ça je peux écrire en haut à gauche par ex que max(3431421) = 4 
        self.play( # déplacement des lettres qui ne sont pas max dans la racine 33121
            ReplacementTransform(arbre8767595394312ske[1],arbre_construct2_red_forest[12]),
            ReplacementTransform(arbre8767595394312ske[3],arbre_construct2_red_forest[13]),
            ReplacementTransform(arbre8767595394312ske[4],arbre_construct2_red_forest[14]),
            ReplacementTransform(arbre8767595394312ske[6],arbre_construct2_red_forest[15]),
            ReplacementTransform(arbre8767595394312ske[7],arbre_construct2_red_forest[16]),
        )
        self.wait() # avant ça, ce serait bien d'avoir un 1234567 et voir que 44 sont en 25
        self.play( # transformation des deux max en leurs positions 44 -> 25
            ReplacementTransform(arbre8767595394312ske[2],arbre_construct2_red_forest[1]),
            ReplacementTransform(arbre8767595394312ske[5],arbre_construct2_red_forest[3]),
            # en même temps déplacement de la structure (sauf le noeud 212)
            ReplacementTransform(arbre8767595394312ske[0],arbre_construct2_red_forest[0]),
            ReplacementTransform(arbre8767595394312ske[8],arbre_construct2_red_forest[4]),
            ReplacementTransform(arbre8767595394312ske[9],arbre_construct2_red_forest[5]),
            ReplacementTransform(arbre8767595394312ske[14],arbre_construct2_red_forest[22]),
            ReplacementTransform(arbre8767595394312ske[15],arbre_construct2_red_forest[23]),
        )
        self.wait()
        self.play( # écriture de virgule, de F( ) et de l'arrête
            Write(arbre_construct2_red_forest[2]),
            Write(arbre_construct2_red_forest[10]),
            Write(arbre_construct2_red_forest[11]),
            Write(arbre_construct2_red_forest[17]),
            Write(arbre_construct2_red_forest[24]),
        )
        self.wait(3)
        self.play( # déplacement de la lettres qui n'est pas max dans 212
            ReplacementTransform(arbre8767595394312ske[12],arbre_construct2_red_forest[20]),
            # en même temp transformation des deux max en leurs positions 22 -> 13
            ReplacementTransform(arbre8767595394312ske[11],arbre_construct2_red_forest[7]),
            ReplacementTransform(arbre8767595394312ske[13],arbre_construct2_red_forest[9]),
            # en même temps déplacement du noeud
            ReplacementTransform(arbre8767595394312ske[10],arbre_construct2_red_forest[6]),
        )
        self.wait()
        self.play( # écriture de virgule, de F( ) et de l'arrête
            Write(arbre_construct2_red_forest[8]),
            Write(arbre_construct2_red_forest[18]),
            Write(arbre_construct2_red_forest[19]),
            Write(arbre_construct2_red_forest[21]),
            Write(arbre_construct2_red_forest[25]),
        )
        self.wait(3)
        # self.play(ReplacementTransform(arbre_construct2_red_forest,arbre_construct3_red_forest))
        # self.wait(3)
        # self.play(ReplacementTransform(arbre_construct3_red_forest,arbre8767595394312))
        # self.wait(3)


class TikZ3(Scene):
    def construct(self):
        tikzcode = TextMobject(r"""hello,
            \begin{tikzpicture}
            "\draw (0,0) -- (1,2) -- (2,1);
            \end{tikzpicture},
            world""")
        tikzcode[6:-6].set_fill(None,0) \
                      .set_stroke(None,2) \
                      .set_color(RED)
        self.play(Write(tikzcode))

class TikZ2(Scene):
    CONFIG = {
        "stroke_width" : 0.5,
        "stroke_color" : BLUE
        }
    def construct(self):
        tikzcode = TexMobject("\\text{hello}",
            "\\tikz\\draw[red] (0,0) -- (1,2) -- (2,1);",
            "\\text{world}")
        tikzcode[1].set_fill(opacity=0)
        tikzcode[1].set_stroke(None,2)
        tikzcode[1].set_color(RED)
        self.play(Write(tikzcode))

class PW(Scene):
    def construct(self):
        boite = TextMobject(r"""
              \begin{tabular}{c}
                \begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}
                  \hline
                  & & & & & $\bullet$ & & & $\bullet$ & & & &\\
                  \hline
                  $\bullet$ & & & & & & & & & & & & \\
                  \hline
                  & $\bullet$ & & $\bullet$ & & & & & & & & & \\
                  \hline
                  & & $\bullet$ & & & & & & & & & & \\
                  \hline
                  & & & & $\bullet$ & & $\bullet$ & & & & & & \\
                  \hline
                  & & & & & & & & & $\bullet$ & & & \\
                  \hline
                  & & & & & & & $\bullet$ & & & $\bullet$ & & \\
                  \hline
                  & & & & & & & & & & & & $\bullet$ \\
                  \hline
                  & & & & & & & & & & & $\bullet$ & \\
                  \hline
                \end{tabular}\\
                \begin{tabular}{*{13}{c}}
                  8&7&6&7&5&9&5&3&9&4&3&1&2
                \end{tabular}
              \end{tabular}
        """)
        self.play(Write(boite))
        self.wait()
