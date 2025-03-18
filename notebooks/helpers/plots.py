import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def plot_simple_shift_schedule(shifts, model, x):
    # Create Gantt chart
    fig, ax = plt.subplots(figsize=(10, 6))
    y_position = 0
    colors = plt.cm.Paired(np.linspace(0, 1, len(shifts)))
    shift_color_map = {} 
    nurse_assignments = {j: int(model.getVal(x[j])) for j in shifts if model.getVal(x[j]) > 0}
    shift_times = {
    "Shift 1": (0, 8),  # 8 AM - 4 PM
    "Shift 2": (2, 10),  # 10 PM - 6 PM
    "Shift 3": (3, 11), # 11 PM - 7 PM
    "Shift 4": (1, 7),  # 9 AM - 3 PM
    "Shift 5": (4, 10),  # 11 AM - 3 PM
    "Split Shift": (0, 4, 10, 11)  # 8 AM - 12 PM and 6 PM - 7 PM
}   
    for i, (shift, count) in enumerate(nurse_assignments.items()):
        start_end = shift_times[shift]
        shift_color_map[shift] = colors[i]  # Assign color for legend

        for nurse in range(count):
            if shift == "Split Shift":
                ax.barh(y_position, start_end[1] - start_end[0], left=start_end[0], color=colors[i], edgecolor='black')
                ax.barh(y_position, start_end[3] - start_end[2], left=start_end[2], color=colors[i], edgecolor='black')
            else:
                ax.barh(y_position, start_end[1] - start_end[0], left=start_end[0], color=colors[i], edgecolor='black')
            y_position += 1

    ax.set_xlabel("Time (Hours from 8 AM)")
    ax.set_ylabel("Scheduled Nurse Count")
    ax.set_xticks(np.arange(0, 12, 1))
    ax.set_xticklabels([f"{8 + i}:00" for i in range(12)])
    ax.set_title("Nurse Rostering Gantt Chart")

    # Create a legend
    legend_patches = [mpatches.Patch(color=color, label=shift) for shift, color in shift_color_map.items()]
    ax.legend(handles=legend_patches, title="Shift Assignments", loc="upper left", bbox_to_anchor=(1, 1))

    plt.show()