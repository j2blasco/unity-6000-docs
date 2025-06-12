* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.GetSpectrumData.html

#  [AudioListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.html).GetSpectrumData
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html "Go to AudioListener Component in the Manual")
## Declaration
public static void GetSpectrumData(float[] samples, int channel, [FFTWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.html) window); 
### Parameters
Parameter | Description  
---|---  
samples | The array to populate with audio samples. Its length must be a power of 2.  
channel | The channel to sample from.  
window | The FFTWindow type to use when sampling.  
### Description
Provides a block of the listener (master)'s spectrum data.
The array given in the samples parameter will be filled with the requested data.  
  
Number of values (the length of the samples array) must be a power of 2. (ie 128/256/512 etc). Min = 64. Max = 8192. Use [window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.html) to reduce leakage between frequency bins/bands. Note, the more complex window type, the better the quality, but reduced speed.  
  
This function will use the sampling rate specified in [AudioSettings.outputSampleRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-outputSampleRate.html), and NOT the sampling rate specified for the audio clip.  
  
**Note** : `GetSpectrumData` provides access to audio data from a short history window (for example, the last few milliseconds) for analysis purposes. Unity doesn't automatically allocate the buffers required to store this history because doing so would be expensive and memory-intensive. Instead, Unity only allocates buffers and starts to record when you first call this function, on a per-object basis. As a result, the output data will initially be empty until the engine processes sufficient audio to populate the buffer. Please note this function isn't suited for critical or chronological, real-time data analysis or processing, or scenarios where you require low latency.  
  
Additional resources: [AudioListener.GetOutputData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.GetOutputData.html), [AudioSource.GetSpectrumData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.GetSpectrumData.html), [AudioSource.GetOutputData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.GetOutputData.html).
```
using UnityEngine;  
  

[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioListener[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.html)))]
public class GetSpectrumDataExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float[] spectrum = new float[256];  
  
        AudioListener.GetSpectrumData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.GetSpectrumData.html)(spectrum, 0, FFTWindow.Rectangular[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.Rectangular.html));  
  
        for (int i = 1; i < spectrum.Length - 1; i++)
        {
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(i - 1, spectrum[i] + 10, 0), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(i, spectrum[i + 1] + 10, 0), Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(i - 1, Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(spectrum[i - 1]) + 10, 2), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(i, Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(spectrum[i]) + 10, 2), Color.cyan[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-cyan.html));
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(i - 1), spectrum[i - 1] - 10, 1), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(i), spectrum[i] - 10, 1), Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html));
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(i - 1), Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(spectrum[i - 1]), 3), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(i), Mathf.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Log.html)(spectrum[i]), 3), Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html));
        }
    }
}

```

* * *
**Obsolete** GetSpectrumData returning a float[] is deprecated, use GetSpectrumData and pass a pre allocated array instead.
## Declaration
public static float[] GetSpectrumData(int numSamples, int channel, [FFTWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.html) window); 
### Parameters
Parameter | Description  
---|---  
numSamples | Number of values (the length of the samples array). Must be a power of 2. Min = 64. Max = 8192.  
channel | The channel to sample from.  
window | The FFTWindow type to use when sampling.  
### Description
_Deprecated Version_. Returns a block of the listener (master)'s spectrum data.
This variation of the function allocates a new array each time it is called. Use the Non-alloc version instead for better performance.
* * *
