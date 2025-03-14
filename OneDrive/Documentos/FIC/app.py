from flask import Flask, Response
import matplotlib.pyplot as plt
import io
import random
import datetime

app = Flask(__name__)

@app.route('/plot.png')
def plot():
    # Simulated realistic data over 10 time intervals
    times = [(datetime.datetime.now() - datetime.timedelta(minutes=10-i)).strftime("%H:%M:%S") for i in range(10)]
    radiation = [random.uniform(5, 50) for _ in range(10)]  # Radiation (mSv/h)
    temperature = [random.uniform(-100, 120) for _ in range(10)]  # Temperature (°C)
    degradation = [100 - (i * random.uniform(0.1, 2)) for i in range(10)]  # Material Degradation %

    # Custom style inspired by RadShield Monitoring page
    plt.style.use("dark_background")
    
    fig, ax = plt.subplots(figsize=(10, 5), facecolor="#181818")  # Background to match UI
    
    # Custom plot lines with neon colors
    ax.plot(times, radiation, label="Radiation (mSv/h)", color='#FF4500', marker='o', linewidth=2.5, markersize=7)
    ax.plot(times, temperature, label="Temperature (°C)", color='#00FF7F', marker='s', linewidth=2.5, markersize=7)
    ax.plot(times, degradation, label="Material Degradation (%)", color='#1E90FF', marker='^', linewidth=2.5, markersize=7)

    # Customizing labels and title
    ax.set_xlabel("Time", fontsize=13, fontweight='bold', color="#FFFFFF")
    ax.set_ylabel("Values", fontsize=13, fontweight='bold', color="#FFFFFF")
    ax.set_title("RadShield Monitoring - Live Data", fontsize=15, fontweight='bold', color="#00FF7F")

    # Grid with soft transparency
    ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.5)

    # Improve axis labels visibility
    ax.tick_params(axis="x", rotation=45, labelsize=11, colors="#B0B0B0")
    ax.tick_params(axis="y", labelsize=11, colors="#B0B0B0")

    # Custom legend with futuristic effect
    ax.legend(fontsize=11, loc="upper right", frameon=True, facecolor="#222222", edgecolor="#00FF7F", fancybox=True)

    # Rounded borders for a modern look
    for spine in ax.spines.values():
        spine.set_edgecolor("#00FF7F")
        spine.set_linewidth(1.5)
        spine.set_capstyle("round")

    # Adjust layout for better spacing
    plt.tight_layout()

    # Save the image in memory
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=120, bbox_inches='tight', transparent=True)
    img.seek(0)

    return Response(img.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5000)


