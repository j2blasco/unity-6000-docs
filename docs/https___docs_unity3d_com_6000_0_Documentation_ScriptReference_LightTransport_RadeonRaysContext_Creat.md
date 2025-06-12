* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.CreateBuffer.html

#  [RadeonRaysContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html).CreateBuffer
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
public [LightTransport.BufferID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.html) CreateBuffer(ulong count, ulong stride); 
### Parameters
Parameter | Description  
---|---  
count | Number of elements in the buffer.  
stride | Stride of the buffer in bytes.  
### Returns
**BufferID** ID of the newly created buffer. 
### Description
Create a new buffer for a number of elements with a given stride.
```
          IDeviceContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html) ctx = new RadeonRaysContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html)();
ctx.Initialize();
const int numberOfElements = 4;
const int strideInBytes = 4;
var bufferID = ctx.CreateBuffer(numberOfElements, strideInBytes);
ctx.DestroyBuffer(bufferID);
ctx.Dispose();
```

How to create a buffer.
* * *
