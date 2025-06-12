* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-renderingThreadingMode.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).renderingThreadingMode
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
[Rendering.RenderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.html) renderingThreadingMode; 
### Description
Application's actual rendering threading mode (Read Only).
Rendering threading mode is decided during the Unity application startup, according to the combination of Player Settings [PlayerSettings.MTRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.MTRendering.html), [PlayerSettings.graphicsJobs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-graphicsJobs.html) and [PlayerSettings.graphicsJobMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-graphicsJobMode.html), as well as according to the target platform capabilities.  
A comparison of different rendering threading modes can be found in tutorial page [Multithreaded Rendering & Graphics Jobs ](https://unity3d.com/learn/tutorials/topics/best-practices/multithreaded-rendering-graphics-jobs) .
* * *
