# Gravity Simulation

A minimal interactive gravity simulator that visualizes two point masses orbiting each other in real time.

![Gravity Simulation](docs/gravity.png)

---

## Features

* Real‑time numerical integration (Euler, easily switchable to Velocity‑Verlet or RK4)
* Scalable units – tweak mass, distance and `SCALE` to zoom in/out
* Pause/resume with one click
* Clean, dependency‑light code (only **pygame**)

## Requirements

| Package | Version (tested) |
|---------|------------------|
| Python  | 3.8 + |
| pygame  | ≥ 2.5 |

Install the requirement:

```bash
pip install pygame
```

## Running

```bash
python gravity.py
```

### Controls

| Action | Key / Mouse |
|--------|-------------|
| Pause / resume | **Left mouse button** |
| Quit | **Esc** or window close |

## Customising

* **Add more bodies**  
  Duplicate or create new `Body(...)` instances and append to the `bodies` list.

* **Better integrator**  
  Replace the Euler block with Velocity‑Verlet for energy conservation:

  ```python
  # example skeleton
  a_old = a_total
  b.pos += b.vel * dt + 0.5 * a_old * dt**2
  a_new = compute_accel(...)
  b.vel += 0.5 * (a_old + a_new) * dt
  ```

* **Trails**  
  Store previous positions in a list and draw a polyline.

* **Zoom / Pan**  
  Adjust `SCALE` dynamically; offset the origin with arrow keys or mouse drag.

## Folder structure (suggestion)

```
gravity/
├── gravity.py      # main code
├── resources/      # icons, future sprites
└── docs/
    └── gravity.png
```

## License

MIT — feel free to use this code for any purpose. Pull requests welcome!
