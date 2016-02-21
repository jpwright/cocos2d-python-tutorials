# Python Cocos2d Game Development
# Part 2: Scrollable Map

# Tutorial: http://jpwright.net/writing/python-cocos2d-game-2/
# Github: http://github.com/jpwright/cocos2d-python-tutorials

# Jason Wright (jpwright0@gmail.com)


# Imports

import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene, tiles
from cocos.director import director

# Player class

class Me(actions.Move):
  
  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
  def step(self, dt):
    
    super(Me, self).step(dt) # Run step function on the parent class.
    
    # Determine velocity based on keyboard inputs.
    velocity_x = 100 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
    velocity_y = 100 * (keyboard[key.UP] - keyboard[key.DOWN])
    
    # Set the object's velocity.
    self.target.velocity = (velocity_x, velocity_y)
    
    scroller.set_focus(self.target.x, self.target.y)
    
# Main class

def main():
    
  # Declare these as global so they can be accessed within class methods.
  global keyboard
  global scroller
  
  # Initialize the window.
  director.init(width=800, height=600, do_not_scale=True, resizable=True)
  
  # Create a layer and add a sprite to it.
  player_layer = layer.ScrollableLayer()
  me = sprite.Sprite('human-female.png')
  player_layer.add(me)
  
  # Set initial position and velocity.
  me.position = (100, 100)
  me.velocity = (0, 0)
  
  # Set the sprite's movement class.
  me.do(Me())
  
  # Create scroller object and load tiles.
  scroller = layer.ScrollingManager()
  map_layer = tiles.load('tiles/map.xml')['map0']
  
  # Add map and player layers.
  scroller.add(map_layer)
  scroller.add(player_layer)

  # Create a scene and set its initial layer.
  main_scene = scene.Scene(scroller)

  # Attach a KeyStateHandler to the keyboard object.
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)

  # Play the scene in the window.
  director.run(main_scene)

if __name__ == '__main__':
    main()
