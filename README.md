# BrodAIPerson

**BrodAIPerson: AI Engine that Matches you real time taking into consideration your patterns**

Developed by **Aleksandra Brodalka** for the *Inside the Game: Developer Hackathon* (Microsoft & Premier League).

## Overview
BrodAIPerson is a real-time match intelligence engine running on Azure. It ingests synthetic football event streams (passes, shots, pressure, spatial vectors), analyzes tactical patterns in real time, and renders dynamic personalized narratives for live broadcast studio feeds, tactical analysts, and end fans.

## Key Features & Pipeline Stages
1. **Event Ingestion:** High-throughput ingestion of synthetic match telemetry (2D pitch coordinates, velocities, pass lengths).
2. **Tactical Pattern Engine:** Evaluates pass difficulty, ball speed, and team press intensity in real time.
3. **Contextual Narrative Generation:** Explains tactical reasoning rather than simply printing static statistics.
4. **Broadcast Overlay Formatting:** Outputs structured JSON and stream feeds for live graphics integration.
5. **Dual-Audience Personalization:** Simultaneously feeds detailed metrics to analysts and engaging storylines to fans.

## Technical Architecture
- **Language:** Python 3.12
- **Data Pipeline:** Synthetic telemetry stream simulation, rule-based pattern analytics, real-time string/JSON rendering engine.
- **Target Cloud Infrastructure:** Azure Container Apps, Azure Event Hubs, Microsoft Agent Framework, GitHub Actions CI/CD.

## Quick Start
To execute the pipeline locally:
```bash
python app.py