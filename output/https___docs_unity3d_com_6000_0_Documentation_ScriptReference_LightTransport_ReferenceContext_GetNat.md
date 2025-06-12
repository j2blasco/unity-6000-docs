* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.GetNativeArray.html

#  [ReferenceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.html).GetNativeArray
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
public NativeArray<byte> GetNativeArray([LightTransport.BufferID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.html) id); 
### Parameters
Parameter | Description  
---|---  
id | ID of the buffer to get the underlying NativeArray from.  
### Returns
**NativeArray <byte>** The NativeArray of bytes for a given [BufferID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.html). 
### Description
Get the NativeArray used for storing buffers in the context.
The reference context is using NativeArray for storing the contents of buffers. This method will return the array.
* * *
