* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-maxQueuedFrames.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).maxQueuedFrames
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
maxQueuedFrames; 
### Description
Maximum number of frames queued up by graphics driver.
Graphics drivers queue up frames that are yet to be rendered, especially when the CPU has lesser processes to execute than the graphics card, this queue can grow large. In such scenarios, the user's input might lag behind the content displayed on the screen.  
  
Use [QualitySettings.maxQueuedFrames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-maxQueuedFrames.html) to limit maximum number of frames that are queued. On PC, the default value is 2, which strikes a good balance between frame latency and framerate.  
  
**Note:** You can reduce input latency by using smaller `maxQueuedFrames`, such that the CPU waits until the graphics card completes rendering previous frames. However, doing this might result in a lower framerate.  
  
Currently, `maxQueuedFrames` is implemented in Direct3D 11, Direct3D 12, and Vulkan graphics APIs only and ignored by other graphics APIs. For information about other graphics APIs and where `maxQueuedFrames` is implemented, refer to platform-specific documentation.
* * *
