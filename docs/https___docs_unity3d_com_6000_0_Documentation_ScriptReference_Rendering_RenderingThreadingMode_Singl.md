* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.SingleThreaded.html

#  [RenderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.html).SingleThreaded
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
Use SingleThreaded for internal debugging. It uses only a single thread to simulate [RenderingThreadingMode.MultiThreaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.MultiThreaded.html).
In this mode, the main thread processes the application's high-level code through an internal class **GfxDeviceClient** that issues an intermediate representation of all the required graphics commands.  
Those intermediate graphics commands are forwarded to a separate internal class **GfxDevice[Platform]** that converts them into the platform's low-level graphics API commands.   
  
On some platforms you can test this mode by passing the command line argument `-force-gfx-st` to an application built with BuildSettings option [BuildOptions.Development](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html).
* * *
