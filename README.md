# 🚦 Smart Traffic Management Using Reinforcement Learning

This project presents an **intelligent traffic signal control system** that dynamically optimizes traffic light durations using **Reinforcement Learning (RL)**.  
The system is designed to overcome the limitations of **traditional fixed-time traffic signals** by adapting in real time to traffic conditions.

Two RL approaches — **Q-Learning** and **Deep Q-Learning (DQN)** — are implemented and evaluated against a **fixed-time baseline** using the **SUMO (Simulation of Urban Mobility)** simulator on a **custom-built road network**.

---

## 🧠 Motivation

Conventional traffic signals operate on predefined time intervals, which:
- Do not adapt to real-time traffic density
- Cause unnecessary congestion and waiting time
- Perform poorly under non-uniform or dynamic traffic patterns

Reinforcement Learning enables traffic signals to **learn optimal signal timings through interaction with the environment**, improving overall traffic flow efficiency.

---

## 🏗️ System Overview

- **Environment:** SUMO traffic simulator
- **Agent:** Traffic signal controller
- **State:** Traffic density / queue length / vehicle count per lane
- **Actions:** Adjust green signal duration for each direction
- **Reward:** Reduced waiting time, queue length, and congestion

---

## 🧪 Implemented Approaches

### 1️⃣ Fixed-Time Traffic Signal (Baseline)
- Predefined signal intervals
- No adaptation to traffic conditions

### 2️⃣ Q-Learning
- Tabular Reinforcement Learning
- Learns optimal signal timings through state–action rewards
- Suitable for smaller state spaces

### 3️⃣ Deep Q-Learning (DQN)
- Neural network–based Q-function approximation
- Handles larger and continuous state spaces
- More scalable and adaptive than tabular Q-learning

---

## 📊 Performance Comparison

The RL-based controllers were evaluated against fixed-time control under identical traffic conditions.

| Method        | Adaptivity | Traffic Efficiency | Scalability |
|---------------|------------|--------------------|-------------|
| Fixed-Time    | ❌ No       | Low                | High        |
| Q-Learning    | ✅ Yes      | Medium             | Limited     |
| **DQN**       | ✅ Yes      | **High**           | **High**    |

📌 **Key Observation:**  
Reinforcement Learning–based controllers significantly reduce congestion and improve traffic flow compared to fixed-time signaling, with **DQN achieving the best performance**.

---

## 🎥 Simulation Results

Simulation videos demonstrating performance differences:

- `fixed_time.mp4` → Traditional fixed-time signal behavior  
- `QL_improvement.mp4` → Improved traffic flow using Q-Learning  

---

## 📂 Repository Structure

```bash
├── Screenshots/                  # Simulation snapshots
├── configuration_files/          # SUMO and traffic signal configs
├── scripts/                      # RL training and control scripts
├── traffic_network_creation_files/ # Custom road network files
├── QL_improvement.mp4            # Q-Learning results video
├── fixed_time.mp4                # Fixed-time baseline video
└── README.md
```
🛠️ Tech Stack

Python
SUMO (Simulation of Urban Mobility)
Reinforcement Learning
NumPy
Matplotlib

🚀 Key Contributions

Designed a custom traffic network in SUMO from scratch
Implemented Q-Learning and Deep Q-Learning for traffic signal control
Benchmarked RL approaches against fixed-time traffic signaling
Demonstrated measurable improvement in traffic flow efficiency
Built an end-to-end simulation pipeline for intelligent traffic control

🔮 Future Enhancements

Multi-intersection coordination using multi-agent RL
Integration of real-world traffic data
Reward shaping for emergency vehicle prioritization
Deployment on real-time traffic control systems

📌 Acknowledgements
SUMO Traffic Simulator
Reinforcement Learning research community

