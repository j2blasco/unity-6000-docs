* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.MultiThreaded.html

#  [RenderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.html).MultiThreaded
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
Generates intermediate graphics commands via the main thread. The render thread converts them into low-level platform API graphics commands.
In this mode, the main thread processes the application's high-level code through an internal class **GfxDeviceClient** that issues an intermediate representation of all the required graphics commands, and stores them in a buffer shared with the render thread.  
At the same time, the render thread keeps reading from that shared buffer through an internal class **GfxDeviceWorker** . When the render thread reads a new intermediate graphics command, it forwards it to a separate internal class **GfxDevice[Platform]** that converts them into the platform's low-level graphics API commands.   
  
On some platforms you can test this mode by passing the command line argument `-force-gfx-mt` to an application built with BuildSettings option [BuildOptions.Development](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html).
* * *
