* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TreeMotionVectorModeOverride.html

# TreeMotionVectorModeOverride
enumeration
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
Options for motion vector rendering on the terrain.
### Properties
Property | Description  
---|---  
[CameraMotionOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TreeMotionVectorModeOverride.CameraMotionOnly.html) | Use only camera movement to track motion for all SpeedTree models painted on the terrain.  
[PerObjectMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TreeMotionVectorModeOverride.PerObjectMotion.html) | Use a specific pass to track motion for all SpeedTree models painted on the terrain.  
[ForceNoMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TreeMotionVectorModeOverride.ForceNoMotion.html) | Don't track motion for SpeedTree models painted on the terrain. Note that models are still rendered in the object motion vector pass, so the CPU performance is similar to `Per Object Motion`.  
[InheritFromPrototype](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TreeMotionVectorModeOverride.InheritFromPrototype.html) | For each SpeedTree model painted on the terrain, inherit the motion vector rendering mode from the import settings, instead of a terrain-global value.  
* * *
