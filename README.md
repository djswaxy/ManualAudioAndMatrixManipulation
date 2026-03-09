# ManualAudioAndMatrixManipulation
Manipulating audio manually with matrices in python using numpy and displaying in matplotlib.

```
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
```
we will use these libraries to import, proccess and display the audio and manipulated audio.
**THE FILE MUST BE IN WAV FORMAT**
In addition, make a path="/path/to/wav/file/"

``` 
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
```
We want to play with stereo audio since many of the fun applications of matrices is swapping Left and Right audio channels or scaling them differently at the same time. In line 23 signal we reshape the Audio Array to have 2 columns, so we can use 2x2 matrices to manipulate it.

```
 swapLRmatrix = np.array([[0,1],
                          [1,0]])
    MuteRight = np.array([[1,0],
                          [0,0]])
    MuteLeft = np.array([ [0,0],
                          [0,1]])
 ScalarMatrix = np.array([[2,0  ],
                          [0,0.5]])

```
Here are some example matrices, *swapLRmatrix* will swap Left and Right audio channels when you matrix multiply it with your audio array, *MuteRight* will mute the Right audio channel, *MuteLeft* will mute the left one and *ScalarMatrix* will scale the left with 2 and the right with 0.5
