"""
Chapitre 11.4

Classes pour représenter un magicien et ses pouvoirs magiques.
"""


import random

import utils
from character import *
from spellcaster import *
from weapon_user import *


class Magician(WeaponUser, Spellcaster):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.using_magic = True

	def compute_Damage(self, other):
		if self.will_use_spell():
			Spellcaster.compute_damage(self, other)
		else:
			WeaponUser.compute_damage(self, other)

	def will_use_spell(self):
		return self.using_magic and self.can_use_spell()
