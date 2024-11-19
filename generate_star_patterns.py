import matplotlib.pyplot as plt
import numpy as np
import random

# Function to generate random star field
def generate_star_pattern(name, num_stars=10, noise=20, save_path="patterns"):
    """
    Generate an image of a star pattern with optional noise.
    
    :param name: Name of the star pattern (e.g., Orion)
    :param num_stars: Number of stars in the pattern
    :param noise: Number of noise points (extra random stars)
    :param save_path: Directory to save the image
    """
    # Create figure
    fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
    
    # Star pattern coordinates (centered for simplicity)
    pattern_x = np.random.uniform(0.2, 0.8, num_stars)
    pattern_y = np.random.uniform(0.2, 0.8, num_stars)
    
    # Add noise (random stars in the background)
    noise_x = np.random.uniform(0, 1, noise)
    noise_y = np.random.uniform(0, 1, noise)
    
    # Plot the main star pattern
    ax.scatter(pattern_x, pattern_y, color='white', s=60, label=f'{name} Stars')
    
    # Add noise stars
    ax.scatter(noise_x, noise_y, color='gray', s=30, alpha=0.5, label='Noise Stars')
    
    # Annotate stars in the pattern
    for i, (x, y) in enumerate(zip(pattern_x, pattern_y)):
        ax.text(x, y, f"{i+1}", color="yellow", fontsize=10, ha='center', va='center')
    
    # Remove axes and set limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.legend(loc='upper left', fontsize=8, facecolor='black', edgecolor='white')
    
    # Save the figure
    plt.savefig(f"{save_path}/{name}.png", dpi=300, bbox_inches='tight', facecolor='black')
    plt.close()
    print(f"Star pattern '{name}' saved to {save_path}/{name}.png")

# Generate a few star patterns
patterns = ["Orion", "Cassiopeia", "BigDipper"]
for pattern in patterns:
    generate_star_pattern(name=pattern, num_stars=8, noise=30)
