* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.Direct.html

#  [RenderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.html).Direct
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
Use the Direct enum to directly render your application from the main thread.
In this rendering threading mode, the main thread processes your application's high-level code, and directly converts it into the target platform's low-level graphics API commands.   
  
On some platforms you can test this mode by passing the command line argument `-force-gfx-jobs legacy` to an application built with BuildSettings option [BuildOptions.Development](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html).
* * *
