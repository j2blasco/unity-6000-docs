* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetCompositorGPUTimeLastFrame.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).TryGetCompositorGPUTimeLastFrame
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
## Declaration
public bool TryGetCompositorGPUTimeLastFrame(out float gpuTimeLastFrameCompositor); 
### Parameters
Parameter | Description  
---|---  
gpuTimeLastFrameCompositor | Outputs the time spent by the GPU for the compositor during the last frame.  
### Returns
**bool** Returns true if the GPU time spent on the last frame is available. Returns false if that time is unavailable. 
### Description
Retrieves the amount of time that the GPU spent executing the compositor renderer during the last frame, as reported by the XR Plugin. Measured in seconds.
You can use this method to get more accurate timing information from the SDK, including information about GPU time spent in SDK-specific layers.  
  
Statistics are only available for SDKs that support this method, and they can vary based on hardware, the SDK, and the frame. You should always check the return value of this method before you use the statistic value from the out parameter.
* * *
