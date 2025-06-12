* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.html

# AsyncGPUReadback
class in UnityEngine.Rendering
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
Allows the asynchronous read back of GPU resources.
This class is used to copy resource data from the GPU to the CPU without any stall (GPU or CPU), but adds a few frames of latency. Additional resources: [AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html).  
  
Additional resources: [SystemInfo.supportsAsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAsyncGPUReadback.html), [SystemInfo.supportsAsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsAsyncGPUReadback.html).
### Static Methods
Method | Description  
---|---  
[Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.Request.html) | Retrieves data asynchronously from a GPU resource.  
[RequestAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.RequestAsync.html) | Retrieves data asynchronously from a GPU resource.  
[RequestIntoNativeArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.RequestIntoNativeArray.html) | Retrieves data asynchronously from a GPU Texture resource.  
[RequestIntoNativeArrayAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.RequestIntoNativeArrayAsync.html) | Retrieves data asynchronously from a GPU Texture resource.  
[RequestIntoNativeSlice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.RequestIntoNativeSlice.html) | Retrieves data asynchronously from a GPU Texture resource.  
[RequestIntoNativeSliceAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.RequestIntoNativeSliceAsync.html) | Retrieves data asynchronously from a GPU Texture resource.  
[WaitAllRequests](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.WaitAllRequests.html) | Waits until the completion of every request.  
* * *
