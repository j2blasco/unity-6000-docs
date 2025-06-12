* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRMirrorViewBlitDesc.html

# XRMirrorViewBlitDesc
struct in UnityEngine.XR
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
All information in this struct describes the desired mirror view blit operation.
And XRMirrorViewBlitDesc can contain more than one [XRBlitParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRBlitParams.html) (describes exactly one blit operation). The render pipeline can query each child [XRBlitParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRBlitParams.html) via GetBlitParameter. [XRMirrorViewBlitDesc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRMirrorViewBlitDesc.html) is typically consumed by a scriptable rendering pipeline.
### Properties
Property | Description  
---|---  
[blitParamsCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRMirrorViewBlitDesc-blitParamsCount.html) | The number of XRBlitParams entries for this XRMirrorViewBlitDesc.  
[nativeBlitAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRMirrorViewBlitDesc-nativeBlitAvailable.html) | When this is true, the current display subsystem supports native blit and AddGraphicsThreadMirrorViewBlit must be called to perform native blit.  
[nativeBlitInvalidStates](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRMirrorViewBlitDesc-nativeBlitInvalidStates.html) | When this is true, display subsystem will modifiy the graphics state.  
### Public Methods
Method | Description  
---|---  
[GetBlitParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.XRMirrorViewBlitDesc.GetBlitParameter.html) | Gets an XRBlitParams for a specific XRMirrorViewBlitDesc.  
* * *
