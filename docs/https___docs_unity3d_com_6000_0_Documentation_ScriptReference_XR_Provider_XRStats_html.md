* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Provider.XRStats.html

# XRStats
class in UnityEngine.XR.Provider
/
Implemented in:[UnityEngine.XRModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.XRModule.html)
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
### Description
Provides timing and other statistics from XR subsystems.
The XRStats class allows XR SDK providers to expose timing and other statistics related to their XR subsystems. Such statistics can be used by XR application developers for profiling and making dynamic performance adjustments. For example, an application could dynamically adjust properties like [XRSettings.eyeTextureResolutionScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-eyeTextureResolutionScale.html) or [XRSettings.renderViewportScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-renderViewportScale.html) at run time to improve performance based on statistics provided by an XR subsystem.  
  
`Note:` XR SDK providers can use this class to provide their own, device-specific class for reporting statistics. XR application developers should not need to use the XRStats class directly.
### Static Methods
Method | Description  
---|---  
[TryGetStat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Provider.XRStats.TryGetStat.html) | Retrieve a statistic for an XR subsystem.  
* * *
