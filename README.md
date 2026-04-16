# autonomous-mobile-robot-pi5
<img width="390" height="520" alt="1000013635" src="https://github.com/user-attachments/assets/fe9cf399-271b-423e-93a8-4c5fcc951135" />

A smart autonomous wheeled robot powered by **Raspberry Pi 5**, designed for navigation, perception, and remote operation in both indoor and rough outdoor environments.  
The robot supports **line following, obstacle avoidance, remote control, live streaming**, and includes a **robotic arm for basic interaction tasks such as digging or object manipulation**.

---

## 🚀 Features

- 🛤️ Line following using IR sensors  
- 🚧 Obstacle avoidance using ultrasonic sensors  
- 🎮 Remote control (manual override mode)  
- 📡 Live video streaming from onboard camera  
- 🧠 Raspberry Pi 5-based processing unit  
- 🌄 Designed for rough and mountainous terrain  
- 🦾 Robotic arm for basic digging and interaction tasks  
- 📊 Multi-sensor fusion (IR + ultrasonic + others)

---

## 🧰 Hardware Components

- Raspberry Pi 5  
- Ultrasonic sensor (HC-SR04 or similar)  
- IR sensors for line tracking  
- Motor driver (L298N / similar)  
- DC motors with wheels  
- Camera module for live streaming  
- Robotic arm (servo-based)  
- Chassis (all-terrain / wheel platform)  
- Power supply (battery pack)

---

## 🧠 System Overview

The robot integrates multiple subsystems:

- **Perception Layer** → IR + Ultrasonic + Camera  
- **Control Layer** → Raspberry Pi 5 processing logic  
- **Actuation Layer** → Motor driver + wheels + robotic arm  
- **Communication Layer** → Remote control + live streaming interface  

---

## ⚙️ Features in Detail

### 🛤️ Line Following
Uses IR sensors to detect and follow predefined paths.

### 🚧 Obstacle Avoidance
Ultrasonic sensor detects obstacles and dynamically changes path.

### 🎮 Remote Control
Manual override mode for controlling movement remotely.

### 📡 Live Streaming
Real-time video streaming from the onboard camera for monitoring and navigation.

### 🦾 Robotic Arm
Basic servo-controlled arm used for:
- Picking small objects  
- Light digging tasks  
- Environmental interaction  

---

## 🌄 Target Use Cases

- Rough terrain exploration  
- Educational robotics projects  
- AI + embedded systems experimentation  
- Remote surveillance platforms  
- Prototype for rescue or field robotics  

---

## 🧩 Future Improvements

- SLAM-based autonomous navigation  
- AI-based object detection  
- GPS integration for outdoor mapping  
- Improved robotic arm precision  
- Fully autonomous mission mode  
