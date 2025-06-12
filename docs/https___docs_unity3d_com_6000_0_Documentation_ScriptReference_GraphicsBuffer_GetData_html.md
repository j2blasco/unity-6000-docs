* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.GetData.html

#  [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).GetData
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
public void GetData(Array data); 
## Declaration
public void GetData(Array data, int managedBufferStartIndex, int computeBufferStartIndex, int count); 
### Parameters
Parameter | Description  
---|---  
data | An array to receive the data.  
managedBufferStartIndex | The first element index in data where retrieved elements are copied.  
computeBufferStartIndex | The first element index of the buffer from which elements are read.  
count | The number of elements to retrieve.  
### Description
Read data values from the buffer into an array. The array can only use [blittable](https://docs.microsoft.com/en-us/dotnet/framework/interop/blittable-and-non-blittable-types) types.
The retrieved data will follow the data layout rules of the graphics API in use. See [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html) for cross-platform compatibility information.  
  
Note that this function reads the data back from the GPU, which can be slow. If any GPU work has been submitted that writes to this buffer, Unity waits for the tasks to complete before it retrieves the requested data, guaranteeing this function returns the most up to date results. For this reason, you should use [AsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.html) instead because it performs the request in the background, and allows you to check when the result is available, without blocking the main thread.  
  
Note: Only [blittable](https://docs.microsoft.com/en-us/dotnet/framework/interop/blittable-and-non-blittable-types) data types can be copied from the buffer to the array, the array's type must be a blittable type. If you attempt to use non-blittable types, an exception will be raised.  
  
Additional resources: [SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetData.html), [count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-count.html), [stride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-stride.html).
* * *
