import time
import json
import random


def generate_synthetic_event():
    """Generates synthetic football event data matching hackathon requirements."""
    players = ["A. Brodalka", "M. Salah", "B. Fernandes", "K. De Bruyne", "E. Haaland"]
    event_types = ["Pass", "Shot", "Tackle", "Interception", "Pressure"]

    player = random.choice(players)
    event_type = random.choice(event_types)
    pass_dist = round(random.uniform(5.0, 45.0), 2)
    ball_speed = round(random.uniform(12.0, 34.0), 2)

    return {
        "timestamp": time.strftime("%H:%M:%S"),
        "player": player,
        "event_type": event_type,
        "pass_distance_m": pass_dist,
        "ball_speed_mps": ball_speed,
        "x_coord": round(random.uniform(0.0, 105.0), 1),
        "y_coord": round(random.uniform(0.0, 68.0), 1)
    }


def analyze_patterns(event):
    """BrodAIPerson Intelligence: Analyzes match context & personalizes narrative output."""
    context = ""
    # Tactical explanation logic
    if event["event_type"] == "Pass" and event["pass_distance_m"] > 30.0:
        context = "High-risk progressive line-breaking pass opening up defensive structure."
    elif event["event_type"] == "Shot" and event["ball_speed_mps"] > 25.0:
        context = "High-velocity strike on target; immediate threat creation."
    elif event["event_type"] == "Pressure":
        context = "Sustained high-press pattern forcing turnover probability build-up."
    else:
        context = "Standard possession retention and lateral spatial movement."

    # Personalized rendering output
    analyst_view = f"[ANALYST FEED] {event['player']} | {event['event_type']} | Distance: {event['pass_distance_m']}m | Speed: {event['ball_speed_mps']} m/s | Insight: {context}"
    fan_view = f"[FAN FEED] 🔥 {event['player']} with a dynamic {event['event_type'].lower()}! {context}"

    return analyst_view, fan_view


def run_engine():
    print("=" * 80)
    print(" BrodAIPerson Engine — Real-Time Match Intelligence & Personalization")
    print(" Powered by Azure & Synthetic Telemetry Stream")
    print(" Author: Aleksandra Brodalka")
    print("=" * 80)

    for i in range(5):
        event = generate_synthetic_event()
        analyst, fan = analyze_patterns(event)

        print(f"\n[EVENT {i + 1} INGESTED] Raw Telemetry: {json.dumps(event)}")
        print(analyst)
        print(fan)
        time.sleep(1)


if __name__ == "__main__":
    run_engine()