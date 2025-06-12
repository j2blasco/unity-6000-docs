* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.html

# RenderingThreadingMode
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
Options for the application's actual rendering threading mode.
The combination of Player Settings [PlayerSettings.MTRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.MTRendering.html), [PlayerSettings.graphicsJobs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-graphicsJobs.html) and [PlayerSettings.graphicsJobMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-graphicsJobMode.html), as well as the target platform capabilities decides the rendering threading mode during the start of the Unity Editor or Standalone. After startup, you can use the property [SystemInfo.renderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-renderingThreadingMode.html) to query the rendering threading mode.  
Refer to the [Multithreaded Rendering & Graphics Jobs ](https://unity3d.com/learn/tutorials/topics/best-practices/multithreaded-rendering-graphics-jobs) tutorial for a comparison of different rendering threading modes.   
To specify whether graphics jobs threading mode is allowed in the Editor, use the **Allow Graphics Jobs in Editor** checkbox in the Jobs panel of the [Preferences Window](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html). Enabling this option lets Unity use the graphics jobs threading mode in the Editor when graphics jobs is enabled in Player Settings. 
### Properties
Property | Description  
---|---  
[Direct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.Direct.html) | Use the Direct enum to directly render your application from the main thread.  
[SingleThreaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.SingleThreaded.html) | Use SingleThreaded for internal debugging. It uses only a single thread to simulate RenderingThreadingMode.MultiThreaded.  
[MultiThreaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.MultiThreaded.html) | Generates intermediate graphics commands via the main thread. The render thread converts them into low-level platform API graphics commands.  
[LegacyJobified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.LegacyJobified.html) | Generates intermediate graphics commands via several worker threads. A single render thread then converts them into low-level platform API graphics commands.  
[NativeGraphicsJobs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobs.html) | Main thread generates intermediate graphics commands. Render thread converts them into low-level platform API graphics commands. Render thread can also dispatch graphics jobs to several worker threads.  
[NativeGraphicsJobsWithoutRenderThread](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobsWithoutRenderThread.html) | Generates intermediate graphics commands via several worker threads and converts them into low-level platform API graphics commands.  
[NativeGraphicsJobsSplitThreading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobsSplitThreading.html) | Generates intermediate graphics commands via several worker threads and render thread dispatches several worker threads to convert them into low-level platform API graphics commands.  
* * *
