* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UsageFlags.html

# UsageFlags
enumeration
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
The intended usage of a GraphicsBuffer.
Provide the intended usage (mode) when creating a GraphicsBuffer.  
  
[GraphicsBuffer.UsageFlags.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UsageFlags.None.html) lets you update the data using [GraphicsBuffer.SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetData.html).  
  
[GraphicsBuffer.UsageFlags.LockBufferForWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UsageFlags.LockBufferForWrite.html) lets you write to the buffer using [GraphicsBuffer.LockBufferForWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.LockBufferForWrite.html). See [GraphicsBuffer.UsageFlags.LockBufferForWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UsageFlags.LockBufferForWrite.html) for information on limitations and considerations to take when using this mode.  
  
Additional resources: [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) class, [GraphicsBuffer constructor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-ctor.html)
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UsageFlags.None.html) | Sets the update mode flags to None. This is the default update mode.  
[LockBufferForWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UsageFlags.LockBufferForWrite.html) | Enable the LockBufferForWrite and UnlockBufferAfterWrite methods on the GraphicsBuffer. CAUTION: when using this flag, ensure that you do not introduce memory read/write hazards.  
* * *
