import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

# def parse_tripinfo(file):
#     tree = ET.parse(file)
#     root = tree.getroot()
#     travel_times, wait_times, speeds = [], [], []
#     for trip in root.findall('tripinfo'):
#         travel_times.append(float(trip.attrib['duration']))
#         wait_times.append(float(trip.attrib['waitingTime']))
#         speeds.append(float(trip.attrib['speed']))
#     return travel_times, wait_times, speeds

import xml.etree.ElementTree as ET

def parse_tripinfo(file):
    tree = ET.parse(file)
    root = tree.getroot()
    
    durations = []
    route_lengths = []
    speeds = []
    time_losses = []

    for trip in root.findall('tripinfo'):
        duration = float(trip.attrib['duration'])
        routeLength = float(trip.attrib['routeLength'])
        timeLoss = float(trip.attrib.get('timeLoss', 0))  # sometimes present

        durations.append(duration)
        route_lengths.append(routeLength)
        time_losses.append(timeLoss)
        
        if duration > 0:
            speeds.append(routeLength / duration)

    return {
        "avg_duration": sum(durations) / len(durations),
        "avg_length": sum(route_lengths) / len(route_lengths),
        "avg_speed": sum(speeds) / len(speeds),
        "avg_time_loss": sum(time_losses) / len(time_losses) if time_losses else None
    }

def parse_summary(file):
    tree = ET.parse(file)
    root = tree.getroot()
    mean_speeds, emissions = [], []
    for step in root.findall('step'):
        mean_speeds.append(float(step.attrib['meanSpeed']))
        emissions.append(float(step.attrib['CO2_abs']))
    return mean_speeds, emissions

def parse_queue(file):
    tree = ET.parse(file)
    root = tree.getroot()
    queue_lengths = []
    for interval in root.findall('interval'):
        queue_lengths.append(float(interval.attrib['queueing_length']))
    return queue_lengths

def parse_emission(file):
    tree = ET.parse(file)
    root = tree.getroot()
    co2, fuel = [], []
    for v in root.findall('vehicle'):
        co2.append(float(v.attrib['CO2']))
        fuel.append(float(v.attrib['fuel']))
    return co2, fuel

def compute_stats(label, tripinfo, summary, queue, emission):
    travel_times, wait_times, speeds = tripinfo
    mean_speeds, emissions_summary = summary
    queue_lengths = queue
    co2, fuel = emission

    print(f"\n==== {label} ====")
    print(f"Avg Travel Time: {np.mean(travel_times):.2f} s")
    print(f"Avg Waiting Time: {np.mean(wait_times):.2f} s")
    print(f"Avg Speed: {np.mean(speeds):.2f} m/s")
    print(f"Throughput (vehicles completed): {len(travel_times)}")
    print(f"Avg Queue Length: {np.mean(queue_lengths):.2f}")
    print(f"Max Queue Length: {np.max(queue_lengths):.2f}")
    print(f"Total CO2: {np.sum(co2):.2f} mg")
    print(f"Total Fuel: {np.sum(fuel):.2f} ml")
    print(f"Fairness (Trip Time StdDev): {np.std(travel_times):.2f}")

    # Plot comparison curves
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(mean_speeds, label="Mean Speed")
    plt.xlabel("Time Steps")
    plt.ylabel("Mean Speed (m/s)")
    plt.title(f"Speed over Time ({label})")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(emissions_summary, label="CO2 Emissions")
    plt.xlabel("Time Steps")
    plt.ylabel("CO2 (mg)")
    plt.title(f"CO2 over Time ({label})")
    plt.legend()

    plt.tight_layout()
    plt.show()

# === Run for both scenarios ===
tripinfo_base = parse_tripinfo('tripinfo_baseline.xml')
summary_base = parse_summary("summary_baseline.xml")
queue_base = parse_queue("queue_baseline.xml")
emission_base = parse_emission("emission_baseline.xml")

tripinfo_rl = parse_tripinfo("tripinfo_rl.xml")
summary_rl = parse_summary("summary_rl.xml")
queue_rl = parse_queue("queue_rl.xml")
emission_rl = parse_emission("emission_rl.xml")

compute_stats("Baseline (Fixed Lights)", tripinfo_base, summary_base, queue_base, emission_base)
compute_stats("RL-Controlled Lights", tripinfo_rl, summary_rl, queue_rl, emission_rl)
