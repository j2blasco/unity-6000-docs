* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetFramePresentCount.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).TryGetFramePresentCount
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
public bool TryGetFramePresentCount(out int framePresentCount); 
### Parameters
Parameter | Description  
---|---  
framePresentCount | Outputs the number of times the current frame has been presented.  
### Returns
**bool** Returns true if the current frame count is available. Returns false otherwise. 
### Description
Retrieves the number of times the current frame has been drawn to the device as reported by the XR Plugin.
If performance degrades, some SDKs draw the current frame multiple times. You can use the frame present count to see if the SDK has presented the same frame to the viewer multiple times.  
  
Statistics are only available for SDKs that support this method, and they can vary based on hardware, the SDK, and the frame. You should always check the return value of this method before you use the statistic value from the out parameter.
* * *
