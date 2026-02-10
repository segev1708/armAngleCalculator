# 🦾 Robotic Arm Angle Calculator

A Python-based tool developed to calculate the necessary servo angles for a 3D robotic arm to reach specific coordinate.

## 🚀 Features
- Uses math to determine angles for servos.
- Built-in **custom error handling** for unreachable target coordinates.
- Designed for integration into 3D robotic systems.
- Visualizer (2D): use PS5 controller to controll an arm!
- 
## 🛠️ How it Works
The script takes the lengths of the upper and lower arm segments and the $(x, y)$ target tip. It then outputs the degrees required for the servos.
The visualizer uses pygame for both controller and the graphics. 

## 📈 Hack Club Progress
- **Goal:** Bambu Lab A1 Mini (4/105 Hours)
- **Status:** Currently in very early development, this is a mini project which is a part of a bigger one. For the bigger one i need the A1 mini and other stuff so it will take time.
  
## ⚙️ Installation & Usage
1. **Clone the Repo:** `git clone https://github.com/your-username/robotic-arm-calculator`
2. **Install Dependencies:** `pip install pygame`
3. **Connect Controller:** Plug in a DualSense (PS5) controller(see note 1).
4. **Run Visualizer(see note 2):** `python visualizer.py`

   Notes:
   *It is possible to use a different controller(like XBOX) but you must make your own map of keys and change the map used to your own.
   **If you want you can also use *two_dimentional_calculator* function from main.py(import). See the function itself for further explanation.
