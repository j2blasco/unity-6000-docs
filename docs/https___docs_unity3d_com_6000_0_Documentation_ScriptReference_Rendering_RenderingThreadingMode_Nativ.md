* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.NativeGraphicsJobsWithoutRenderThread.html

#  [RenderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.html).NativeGraphicsJobsWithoutRenderThread
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
Generates intermediate graphics commands via several worker threads and converts them into low-level platform API graphics commands.
In this mode, the main thread processes the application's high-level code and issues an intermediate representation of the required graphics commands for some of it.  
The main thread can also dispatch Graphics Jobs commands that describe bigger chunks of the high-level code, to several other worker threads.  
  
  
The worker threads also convert the Graphics Jobs into the platform's low-level graphics API commands.   
On some platforms you can test this mode by passing the command line argument `-gfx-enable-gfx-jobs -gfx-disable-mt-rendering` to an application built with BuildSettings option [BuildOptions.Development](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html).
* * *
