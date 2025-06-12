* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.GetData.html

#  [AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html).GetData
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
## Declaration
public NativeArray<T> GetData(int layer); 
### Parameters
Parameter | Description  
---|---  
layer | The index of the layer to retrieve.  
### Description
Fetches the data of a successful request.
This method throws an InvalidOperationException if called when the request has not been fulfilled or has been disposed of. If the request is still pending then calling [AsyncGPUReadbackRequest.done](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-done.html) on this request will return false. In the case of a request not completing successfully, or if it has been disposed of then calling [AsyncGPUReadbackRequest.hasError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-hasError.html) on this request will return true. Layer index allows you to access the different request slices of a [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html),TextureCube,[Texture2DArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.html) and TextureCubeArray.
* * *
