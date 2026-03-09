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

** The real fun begins when we CHAIN these operations together ** 
Lets say we want to do maaany operations, we want to scale one, then swap, then mute we can chain all of these together. The signal all the way to the right is given by:
``` ScaleAndSwap = ScalarMatrix @ swapLRmatrix ```
Here we chain two matrices so that when we later do
```manipulated_signal2 = signal @ ScaleAndSwap`` 
BOTH the Scale operation and the Swap Left and Right Operation is executed, when we only did one matrix manipulation. This is one of the coolest uses of matrices.
<img width="1757" height="767" alt="image" src="https://github.com/user-attachments/assets/5dee3b62-1fcb-4761-93cc-c46ed0edacb2" />

The one on the left is the original signal, the one in the middle the left audio stream is scaled by two, and the right audio stream is scaled by 0.5. In the rightmost signal both the scale operation and swap of left and right is done to the original signal!

The full code is in the github repository!
