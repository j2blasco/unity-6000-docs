* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.LegacyJobified.html

#  [RenderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.html).LegacyJobified
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
Generates intermediate graphics commands via several worker threads. A single render thread then converts them into low-level platform API graphics commands.
In this mode, several job worker threads process the application's high-level code and issue an intermediate representation of all the required graphics commands.  
A separate single render thread reads those intermediate graphics commands, and forwards them to an internal class **GfxDevice[Platform]** that converts them into the platform's low-level graphics API commands.   
  
On some platforms this mode can be tested by passing command line argument `-force-gfx-jobs legacy` to an application built with BuildSettings option [BuildOptions.Development](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html) .
* * *
