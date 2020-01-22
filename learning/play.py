clefrom manimlib.imports import *


class WritingStuff(Scene):
	def construct(self):
		text = TextMobject("hey...this is pretty cool")
		self.play(Write(text))
		self.wait(3)

class AddText(Scene):
	def construct(self):
		line  = TextMobject("adding text")
		self.add(line)
		self.wait(2)

class types_of_text(Scene):
	def construct(self):
		texttypes = TextMobject("""
			this is regular text,
			$\\displaystyle\\frac{x}{y}$,
			$$x^2 + y^2 = a^2$$""" )
		self.play(Write(texttypes))
		self.wait(3)

class textmoving(Scene):
	def construct(self):
		text = TextMobject("upppppppp")
		text.to_edge(UP+RIGHT)
		self.play(Write(text),runtime=2)
		self.wait(2)

class custompos(Scene):
	def construct(self):
		text1 = TextMobject("hello")
		text2 = TextMobject("there")
		text1.move_to(3*UP)
		self.play(Write(text1),Write(text2))
		self.wait(2)