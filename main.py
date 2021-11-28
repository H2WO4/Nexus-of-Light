from __future__ import annotations

import pygame
from pygame.event import Event
from pygame.surface import Surface

from typing import List, Tuple

Color = Tuple[int, int, int] | Tuple[int, int, int, int]


# Define a tile class, from which all tiles will inherit
class Tile:
	"""
	A tile represent an object on the map.
	"""

	__slots__ = 'baseColor', 'color'

	def __init__(self):
		self.baseColor: Color = (0, 0, 0)
		self.color: Color = self.baseColor
	
	def render(self, screen: Surface, x: int, y: int) -> None:
		"""
		Render the tile on the screen.
		"""
		pygame.draw.rect(screen, self.color, (x, y, 32, 32))

	def on_level_start(self):
		pass

	def on_powered(self):
		pass

	def on_unpowered(self):
		pass

class TileEmpty(Tile):
	"""
	A tile that does nothing.
	"""
	def __init__(self):
		self.baseColor: Color = (255, 255, 255)
		self.color: Color = self.baseColor


# Define a level class
class Level:
	"""
	A level is composed of a grid, with :
	 - A default arrangement
	 - A clear condition
	"""
	__slots__ = {'grid': List[List[Tile]]}

	currLevel: Level

	def __init__(self):
		self.grid: List[List[Tile]] = [[TileEmpty() for _ in range(10)] for _ in range(10)]

		self.grid[0][0] = Tile()

		Level.currLevel = self

	def render(self, screen: Surface) -> None:
		"""
		Render the level on the screen.
		"""
		for x in range(10):
			for y in range(10):
				self.grid[x][y].render(screen, x * 32, y * 32)




# Define the main game object
class Instance:
	def __init__(self) -> None:
		self._running = True
		self.size = self.weight, self.height = 900, 600
		self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		pygame.display.set_caption('Nexus of Light')

	def on_init(self) -> None:
		pygame.init()
		self._running = True

	def on_event(self, event: Event) -> None:
		match event.type:
			case pygame.QUIT:
				self._running = False

	def on_loop(self) -> None:
		pass

	def on_render(self) -> None:
		self._display_surf.fill((0, 0, 0))

		Level.currLevel.render(self._display_surf)

		pygame.display.update()

	def on_cleanup(self) -> None:
		pygame.quit()

	def on_execute(self) -> None:
		if self.on_init() == False:
			self._running = False

		while (self._running):
			for event in pygame.event.get():
				self.on_event(event)

			self.on_loop()
			self.on_render()

		self.on_cleanup()

# Main
if __name__ == "__main__":
	Level()

	NexusOfLight = Instance()



	NexusOfLight.on_execute()