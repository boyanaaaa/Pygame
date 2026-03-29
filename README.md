# 🚀 Asteroids Game (Pygame)

A simple Asteroids-style game built with Python and Pygame as part of a learning project.

---

## 📌 Project Overview

This project walks through building a small 2D game step by step:
- Player movement
- Shooting mechanics
- Asteroid spawning
- Collision detection
- Object splitting

---

**Phase 1: Foundations & Environment**

1. Project Setup:
  Create your folder and virtual environment.
  pip install pygame.

2. main.py Initialization:
  import pygame and call pygame.init().
  Define constants like SCREEN_WIDTH and SCREEN_HEIGHT.
  Create the Screen and the Clock object.
3. The Base Component (CircleShape):
  Create circleshape.py.
  This class handles the math for position, velocity, and radius.
  Add the collision method (the distance formula).

---

**Phase 2: The Player & Movement**


4. The Player Component:
  Create player.py inheriting from CircleShape and pygame.sprite.Sprite.
  Define the triangle() method to draw the ship's shape.

5. Groups & The Game Loop:
  In main.py, create updatable and drawable groups.
  Add the Player to these groups using containers.
  Start the while True: loop.
  Step: Calculate dt (delta time) using clock.tick(60) / 1000.

6. Player Input:
  Add rotate() and move() methods to the Player class.
  Inside Player.update(), check for pygame.K_w, a, and d.

---

**Phase 3: The Enemies (Asteroids)**


7. The Asteroid Component:
  Create asteroid.py.
  Define its draw() (a circle) and update() (position + velocity * dt) methods.

8. The AsteroidField Manager:
  Create asteroidfield.py.
  This component doesn't draw anything; it just spawns Asteroid objects at the screen edges on a timer.

9. Collision Detection (Game Over):
  In the main loop, iterate through your asteroids group.
  Check if any asteroid collides_with(player). If so, print("Game over!") and sys.exit().

---

**Phase 4: Combat & Cleanup**


10. The Shot Component:
  Create a Shot class for bullets.
  Give it a constant speed and a small radius.

11. Shooting Logic:
  In the Player class, add a shoot() method that creates a new Shot at the player's position, moving in the direction     the player is facing.
  Map this to pygame.K_SPACE with a "cooldown" timer so the player can't spam infinite bullets.

12. Bullet Collisions:
  In the main loop, check if any Shot collides with any Asteroid.
  Use .kill() on both objects when they touch.

---
**Phase 5: Refinement (Splitting)**

13. The split() Method:
  Inside the Asteroid class, add logic to spawn two smaller asteroids when a large one is killed by a shot.
  Calculate new velocities using vector.rotate().

14. Final Polish:
  Ensure all objects are being drawn and updated correctly.
  Clear the screen with screen.fill("black") at the start of every loop.
  Call pygame.display.flip() at the end of every loop.

---
**Phase 6: Deployment**

15. Git & GitHub:
  Create a .gitignore to ignore the venv/ folder.
  Push your code to a repository to share your victory!
