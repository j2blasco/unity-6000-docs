* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.GetSpectrumData.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).GetSpectrumData
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
## Declaration
public void GetSpectrumData(float[] samples, int channel, [FFTWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.html) window); 
### Parameters
Parameter | Description  
---|---  
samples | The array to populate with frequency domain representations of audio samples. The array length must be a power of 2 (such as 128, 256, 512). Also, the length must not be less than 64 or greater than 8192.  
channel | The channel to sample from.  
window | The FFTWindow type to use when sampling.  
### Description
Provides the block of audio frequencies (spectrum data) of the AudioSource that is currently playing.
This method fills the array you pass as the `samples` parameter with the spectrum data of the AudioSource.  
  
The frequency domain represents the frequencies and amplitude of an audio signal. Spectrum data provides the raw frequency domain data of the audio, which you can use to create a spectrogram to visualize the data.  
  
Audio frequency bands are ranges of sound frequencies that describe different parts of the audio spectrum (like sub-bass, bass, brilliance). The audio frequency bands are evenly spaced between 0 to half of the sampling rate. GetSpectrumData uses the sampling rate from [AudioSettings.outputSampleRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-outputSampleRate.html), not the sampling rate in the audio clip.  
  
Use [window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.html) to reduce leakage or scalloping loss between audio frequency bins/bands.  
  
**Note:** A more complex window type might be less efficient and worsen resolution (lobe width).  
  
**Note** : `GetSpectrumData` provides access to audio data from a short history window (for example, the last few milliseconds) for analysis purposes. Unity doesn't automatically allocate the buffers required to store this history because doing so would be expensive and memory-intensive. Instead, Unity only allocates buffers and starts to record when you first call this function, on a per-object basis. As a result, the output data will initially be empty until the engine processes sufficient audio to populate the buffer. Please note this function isn't suited for critical or chronological, real-time data analysis or processing, or scenarios where you require low latency.  
  
For related information, refer to [AudioSource.GetOutputData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.GetOutputData.html), [AudioListener.GetSpectrumData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.GetSpectrumData.html), [AudioListener.GetOutputData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.GetOutputData.html).
```
using UnityEngine;  
  

[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)))]
public class AudioSourceGetSpectrumDataExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) m_MyAudioSource;  
  
    void Start()
    {
        m_MyAudioSource = GetComponent<AudioSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)>();
    }
    
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float[] spectrum = new float[256];  
  
        m_MyAudioSource.GetSpectrumData(spectrum, 0, FFTWindow.Rectangular[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.Rectangular.html));  
  
        // Loop through the populated array
        // Start the loop from 1 and to 1 less than the length, so the loop can draw lines between adjacent bins.   
  
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
public float[] GetSpectrumData(int numSamples, int channel, [FFTWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.html) window); 
### Parameters
Parameter | Description  
---|---  
numSamples | The number of samples to retrieve. Must be a power of 2.  
channel | The channel to sample from.  
window | The FFTWindow type to use when sampling.  
### Returns
**float[]** Returns a block of the currently playing source's spectrum data. 
### Description
This version of GetSpectrumData is obsolete.
This version of GetSpectrumData is obsolete. Use the other version of GetSpectrumData instead.   
  
This variation of the function allocates a new array each time it is called. Use the other version instead for better performance.  
  
Number of values (numSamples) must be a power of 2. (ie 128/256/512 etc). Min = 64. Max = 8192. Use [window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FFTWindow.html) to reduce leakage between frequency bins/bands. Note, the more complex window type, the better the quality, but reduced speed.
* * *
