* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming.html

# FrameTiming
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Struct containing basic FrameTimings and accompanying relevant data.
### Properties
Property | Description  
---|---  
[cpuFrameTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-cpuFrameTime.html) | This is the total CPU frame time calculated as the time between ends of two frames, which includes all waiting time and overheads, in ms.  
[cpuMainThreadFrameTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-cpuMainThreadFrameTime.html) | Total time between start of the frame and when the main thread finished the job, in ms.  
[cpuMainThreadPresentWaitTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-cpuMainThreadPresentWaitTime.html) | The CPU time the last frame spent in waiting for Present on the main thread, in ms.  
[cpuRenderThreadFrameTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-cpuRenderThreadFrameTime.html) | The frame time between start of the work on the render thread and when Present was called, in ms.  
[cpuTimeFrameComplete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-cpuTimeFrameComplete.html) | This is the CPU clock time at the point GPU finished rendering the frame and interrupted the CPU.  
[cpuTimePresentCalled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-cpuTimePresentCalled.html) | This is the CPU clock time at the point Present was called for the current frame.  
[firstSubmitTimestamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-firstSubmitTimestamp.html) | This is the CPU clock time of the time when the first job was submitted to GPU.  
[frameStartTimestamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-frameStartTimestamp.html) | This is the CPU clock time of the time when the frame was started.  
[gpuFrameTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-gpuFrameTime.html) | The GPU time for a given frame, in ms.  
[heightScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-heightScale.html) | This was the height scale factor of the Dynamic Resolution system(if used) for the given frame and the linked frame timings.  
[syncInterval](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-syncInterval.html) | This was the vsync mode for the given frame and the linked frame timings.  
[widthScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming-widthScale.html) | This was the width scale factor of the Dynamic Resolution system(if used) for the given frame and the linked frame timings.  
* * *
