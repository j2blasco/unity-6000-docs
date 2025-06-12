* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-ctor.html

# GraphicsBuffer Constructor
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
public GraphicsBuffer([GraphicsBuffer.Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html) target, [GraphicsBuffer.UsageFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UsageFlags.html) usageFlags, int count, int stride); 
### Parameters
Parameter | Description  
---|---  
target | Specify how this buffer can be used within the graphics pipeline.  
usageFlags | Select what kind of update mode the buffer will have.  
count | Number of elements in the buffer.  
stride | Size of one element in the buffer. For index buffers, this must be either 2 or 4 bytes.  
### Description
Create a Graphics Buffer.
Use [Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Release.html) to release the buffer when no longer needed.  
  
If the buffer size exceeds the value in [SystemInfo.maxGraphicsBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxGraphicsBufferSize.html), the constructor raises an exception.  
  
Additional resources: [Graphics.RenderPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitives.html).
* * *
## Declaration
public GraphicsBuffer([GraphicsBuffer.Target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html) target, int count, int stride); 
### Parameters
Parameter | Description  
---|---  
target | Specify how this buffer can be used within the graphics pipeline.  
count | Number of elements in the buffer.  
stride | Size of one element in the buffer. For index buffers, this must be either 2 or 4 bytes.  
### Description
Create a Graphics Buffer.
Use [Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Release.html) to release the buffer when no longer needed.  
  
If the buffer size exceeds the value in [SystemInfo.maxGraphicsBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxGraphicsBufferSize.html), the constructor raises an exception.  
  
Additional resources: [Graphics.RenderPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitives.html).
* * *
