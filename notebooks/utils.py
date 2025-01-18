import matplotlib.pyplot as plt


def plot_corrmat(corr):
    """
    :param corr : matriz de correlaciones
    """
    # Plotting the correlation matrix
    plt.figure(figsize=(8, 6))
    plt.imshow(corr, cmap='Blues', aspect='auto')

    # Adding colorbar
    plt.colorbar()

    # Adding labels to the matrix
    variables = corr.columns
    plt.xticks(range(len(corr)), variables, rotation=45, ha='right')
    plt.yticks(range(len(corr)), variables)

    # Adding the correlation values inside the cells
    for i in range(len(corr)):
        for j in range(len(corr)):
            plt.text(
                j, i, f"{corr.iloc[i, j]:.2f}",
                ha='center', va='center',
                color="black" if abs(corr.iloc[i, j]) < 0.5 else "white",  # Adjust text color for better readability
                fontsize=10
            )

    # Display the plot
    plt.tight_layout()
    plt.show()
    return