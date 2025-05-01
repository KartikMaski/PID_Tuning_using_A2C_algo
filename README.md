# Self Tuning PID using Deep Reinforcement Learning using Actor-Critic Model

# 🚁 Adaptive PID Tuning for Quadcopters Using Advantage Actor-Critic (A2C)

This repository is a refined and research-driven implementation of adaptive PID tuning using the **Advantage Actor-Critic (A2C)** reinforcement learning algorithm, designed for **quadcopter control in dynamic environments**.

> 🔗 Reference Implementation:  
> [KartikMaski/PID_Tuning_using_A2C_algo](https://github.com/KartikMaski/PID_Tuning_using_A2C_algo)

---

## 📄 Abstract

Quadcopters operate in dynamic and uncertain environments where stable control is challenging. This project presents an **A2C-based adaptive PID tuning** method that optimizes the gains in real-time based on environmental feedback, eliminating the need for static or manually-tuned PID controllers.

Our hybrid architecture combines **deep reinforcement learning (DRL)** and traditional PID mechanisms to enable robust flight control, validated through diverse simulations with disturbances and noise.

---

## 🧠 Key Highlights

- 🔁 Real-time PID tuning using Advantage Actor-Critic (A2C)
- ⚖️ Handles variable payloads and environmental disturbances
- 🧠 Combines traditional control theory with modern DRL techniques
- 🎯 Supports complex trajectories: Stationary, Circular, and Square

---

## 🛠️ Tech Stack

- `Python` | `NumPy` | `Matplotlib`
- `TensorFlow` or `PyTorch` (for A2C)
- `OpenAI Gym` (or custom simulation environment)
- `PID Controller` logic implemented with adaptive layers

---

## 📐 Architecture

The architecture features:
- **Actor-Critic Neural Network** for gain prediction and policy/value estimation
- **PID controller layer** tuned dynamically by RL agent
- **Reward shaping** based on tracking error and control effort

