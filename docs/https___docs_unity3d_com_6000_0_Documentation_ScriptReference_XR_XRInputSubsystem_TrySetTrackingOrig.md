* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.TrySetTrackingOriginMode.html

#  [XRInputSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.html).TrySetTrackingOriginMode
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
public bool TrySetTrackingOriginMode([XR.TrackingOriginModeFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.html) origin); 
### Parameters
Parameter | Description  
---|---  
origin | The new [TrackingOriginModeFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.html) that you'd like to change to.  
### Returns
**bool** True if the method changes the origin. Returns false otherwise. 
### Description
Attempts to set the [TrackingOriginModeFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.html) of the subsystem.
See [XRInputSubsystem.GetSupportedTrackingOriginModes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.GetSupportedTrackingOriginModes.html) in order to see what modes this individual XRInputSubsystem supports, and [XRInputSubsystem.GetTrackingOriginMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.GetTrackingOriginMode.html) to see the current mode.
* * *
