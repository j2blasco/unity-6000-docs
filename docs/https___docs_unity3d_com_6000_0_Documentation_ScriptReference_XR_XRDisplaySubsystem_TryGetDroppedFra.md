* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetDroppedFrameCount.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).TryGetDroppedFrameCount
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
public bool TryGetDroppedFrameCount(out int droppedFrameCount); 
### Parameters
Parameter | Description  
---|---  
droppedFrameCount | Outputs the number of frames dropped since the last update.  
### Returns
**bool** Returns true if the dropped frame count is available. Returns false otherwise. 
### Description
Retrieves the number of dropped frames reported by the XR Plugin.
Use this method for games and applications that you want to scale content or settings dynamically in order to maximise frame rates. XR applications and games must run at a consistent, high frame rate. If an application has too many draw calls or calculations, it may have to "drop" frames in order to keep a high frame rate. When the SDK reports that the application is dropping frames, the application can adjust settings, disable objects, or perform other actions to reduce overhead.  
  
Statistics are only available for SDKs that support this method, and they can vary based on hardware, the SDK, and the frame. You should always check the return value of this method before you use the statistic value from the out parameter.
* * *
