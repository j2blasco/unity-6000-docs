* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.GetOutputData.html

#  [AudioListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.html).GetOutputData
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
public static void GetOutputData(float[] samples, int channel); 
### Parameters
Parameter | Description  
---|---  
samples | The array to populate with audio samples. Its length must be a power of 2.  
channel | The channel to sample from.  
### Description
Provides a block of the listener (master)'s output data.
The array given in the samples parameter will be filled with the requested data.  
  
`GetOutputData` provides access to audio data from a short history window (for example, the last few milliseconds) for analysis purposes. Unity doesn't automatically allocate the buffers required to store this history because doing so would be expensive and memory-intensive. Instead, Unity only allocates buffers and starts to record when you first call this function, on a per-object basis. As a result, the output data will initially be empty until the engine processes sufficient audio to populate the buffer. Please note this function isn't suited for critical or chronological, real-time data analysis or processing, or scenarios where you require low latency.  
  
Additional resources: [AudioListener.GetSpectrumData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.GetSpectrumData.html), [AudioSource.GetSpectrumData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.GetSpectrumData.html), [AudioSource.GetOutputData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.GetOutputData.html).
* * *
**Obsolete** GetOutputData returning a float[] is deprecated, use GetOutputData and pass a pre allocated array instead.
## Declaration
public static float[] GetOutputData(int numSamples, int channel); 
### Description
_Deprecated Version_. Returns a block of the listener (master)'s output data.
This variation of the function allocates a new array each time it is called. Use the Non-alloc version instead for better performance.
* * *
