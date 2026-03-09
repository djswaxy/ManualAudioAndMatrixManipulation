#audio
# Code by Emil Østberg / djswaxy
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
path = ('C:/Users/emilo/Downloads/sample-6s.wav')

def visualize(path: str):
    with wave.open(path, 'rb') as raw:
        f_rate = raw.getframerate()
        n_channels = raw.getnchannels()

        signal_bytes = raw.readframes(-1)
        signal = np.frombuffer(signal_bytes, dtype="int16")

    # 1. RESHAPE the array into an N x 2 matrix (Frames x Channels)
    if n_channels == 2:
        signal = signal.reshape(-1, 2)
    else:
        print("non stereo!")
        return
    # to Plot the x-axis in seconds
    # you need get the frame rate
    # and divide by size of your signal
    # to create a Time Vector
    # spaced linearly with the size
    # of the audio file
    swapLRmatrix = np.array([[0,1],
                          [1,0]])
    MuteRight = np.array([[1,0],
                          [0,0]])
    MuteLeft = np.array([[0,0],
                          [0,1]])

    ScalarMatrix = np.array([[2,0], #Here we scale the left channel by *2 and the right by *0.5
                              [0,0.5]])



    time = np.linspace(
        0, # start
        len(signal) / f_rate,
        num = len(signal)
    )
    # using matplotlib to plot
    # creates a new figure
    ScaleAndSwap = ScalarMatrix @ swapLRmatrix #chained matrices here!

    manipulated_signal = signal @ ScalarMatrix
    manipulated_signal2 = signal @ ScaleAndSwap


    fig, axs = plt.subplots(2, 3, figsize=(18, 8), sharex=True, sharey=True)

    #Here we plot the left and right channels seperatly, to better see the swap and manipulation.
    axs[0, 0].set_title("Original - Left Channel")
    axs[0, 0].plot(time, signal[:, 0], color='blue')

    axs[1, 0].set_title("Original - Right Channel")
    axs[1, 0].set_xlabel("Time (s)")
    axs[1, 0].plot(time, signal[:, 1], color='orange')


    axs[0, 1].set_title("Scaled - Left Channel")
    axs[0, 1].plot(time, manipulated_signal[:, 0], color='blue')

    axs[1, 1].set_title("Scaled - Right Channel")
    axs[1, 1].set_xlabel("Time (s)")
    axs[1, 1].plot(time, manipulated_signal[:, 1], color='orange')


    axs[0, 2].set_title("Swapped - Left Channel")
    axs[0, 2].plot(time, manipulated_signal2[:, 0], color='blue')

    axs[1, 2].set_title("Swapped - Right (Channel")
    axs[1, 2].set_xlabel("Time (s)")
    axs[1, 2].plot(time, manipulated_signal2[:, 1], color='orange')

    plt.tight_layout()
    plt.show()
visualize(path)
