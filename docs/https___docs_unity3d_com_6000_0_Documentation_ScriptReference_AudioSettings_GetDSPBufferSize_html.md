* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetDSPBufferSize.html

#  [AudioSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.html).GetDSPBufferSize
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSettings.html "Go to AudioSettings Component in the Manual")
## Declaration
public static void GetDSPBufferSize(out int bufferLength, out int numBuffers); 
### Parameters
Parameter | Description  
---|---  
bufferLength | Is the length of each buffer in the ring buffer.  
numBuffers | Is number of buffers.  
### Description
Get the mixer's buffer size in samples.
The buffer size can be set from 'Project Settings -> Audio -> DSP Buffer size'.  
  
The software mixer mixes to a ring buffer and the size of this ring buffer is determined here. It mixes a block of sound data every 'bufferLength' number of samples, and there are 'numBuffers' number of these blocks that make up the entire ring buffer. Adjusting these values can lead to extremely low latency performance (smaller values), or greater stability in sound output (larger values). The 'buffersize' is generally best left alone. Making the granularity smaller will just increase CPU usage (cache misses and DSP network overhead). Making it larger affects how often you hear commands update such as volume/pitch/pan changes. Anything above 20 ms will be noticeable and sound parameter changes will be obvious instead of smooth. Unity chooses the most optimal size by default for best stability, considering the output type and the drivers being used. It is not recommended changing this value unless you really need to. You may get worse performance than the default settings chosen by Unity.  
  
Additional resources: [Audio Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSettings.html).
* * *
