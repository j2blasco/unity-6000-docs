* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.html

# XRMirrorViewBlitMode
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
Engine reserved blit modes. Blit mode capabilities should be queried from [XRDisplaySubsystemDescriptor.GetAvailableMirrorBlitModeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystemDescriptor.GetAvailableMirrorBlitModeCount.html) and [XRDisplaySubsystemDescriptor.GetMirrorBlitModeByIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystemDescriptor.GetMirrorBlitModeByIndex.html).
### Static Properties
Property | Description  
---|---  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.Default.html) | Mirror view pass should blit platform default image to the mirror target.  
[Distort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.Distort.html) | Mirror view pass should blit after distortion pass image to the mirror target.  
[LeftEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.LeftEye.html) | Mirror view pass should blit left eye image to the mirror target.  
[MotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.MotionVectors.html) | Mirror view pass should blit left eye image and right eye image in a side-by-side fashion to the mirror target, displaying motion vectors.  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.None.html) | Mirror view pass should not be performed.  
[RightEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.RightEye.html) | Mirror view pass should blit right eye image to the mirror target.  
[SideBySide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.SideBySide.html) | Mirror view pass should blit left eye image and right eye image in a side-by-side fashion to the mirror target.  
[SideBySideOcclusionMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.SideBySideOcclusionMesh.html) | Mirror view pass should blit similar to side-by-side mode, but also showing not rendered pixels saved by the occlusion mesh.  
* * *
