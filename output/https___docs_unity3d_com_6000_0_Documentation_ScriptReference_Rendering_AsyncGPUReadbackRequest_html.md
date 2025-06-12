* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html

# AsyncGPUReadbackRequest
struct in UnityEngine.Rendering
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
Represents an asynchronous request for a GPU resource.
Use [AsyncGPUReadback.Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.Request.html) to retrieve an asynchronous request for a GPU resource. Pending requests are automatically updated each frame. The result is accessible only for a single frame once is successfully fulfilled and this request is then disposed of in the following frame. Common uses for this are to query [AsyncGPUReadbackRequest.done](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-done.html) each frame (or within a coroutine) and then call [AsyncGPUReadbackRequest.GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.GetData.html) if the [AsyncGPUReadbackRequest.hasError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-hasError.html) is false. You don't have to manage the request lifetime as this is managed internally. A request that has been disposed of will result in the [AsyncGPUReadbackRequest.hasError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-hasError.html) property being true. Additional resources:[AsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.html).
### Properties
Property | Description  
---|---  
[depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-depth.html) | When reading data from a ComputeBuffer, depth is 1, otherwise, the property takes the value of the requested depth from the texture.  
[done](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-done.html) | Checks whether the request has been processed.  
[forcePlayerLoopUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-forcePlayerLoopUpdate.html) | In the Editor, defines whether the Player loop is updated while the GPU request is in flight.  
[hasError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-hasError.html) | This property is true if the request has encountered an error.  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-height.html) | When reading data from a ComputeBuffer, height is 1, otherwise, the property takes the value of the requested height from the texture.  
[layerCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-layerCount.html) | Number of layers in the current request.  
[layerDataSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-layerDataSize.html) | The size in bytes of one layer of the readback data.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-width.html) | The width of the requested GPU data.  
### Public Methods
Method | Description  
---|---  
[GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.GetData.html) | Fetches the data of a successful request.  
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.Update.html) | Triggers an update of the request.  
[WaitForCompletion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.WaitForCompletion.html) | Waits for completion of the request.  
* * *
