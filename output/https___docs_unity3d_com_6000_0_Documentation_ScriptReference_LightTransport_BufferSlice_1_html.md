* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.html

# BufferSlice<T0>
struct in UnityEngine.LightTransport
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
Unity uses the BufferSlice struct to split one large buffer allocation into one or more smaller buffers, each with explicit types.
### Properties
Property | Description  
---|---  
[Id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.Id.html) | Buffer ID.  
[Offset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.Offset.html) | The number of elements to offset, measured from the beginning of the buffer. The value must not exceed the end of the buffer allocation.  
### Constructors
Constructor | Description  
---|---  
[BufferSlice_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1-ctor.html) | Construct a new BufferSlice struct by defining an offset from the beginning of a buffer. The buffer is defined by the BufferID.  
### Public Methods
Method | Description  
---|---  
[SafeReinterpret](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.SafeReinterpret.html) | Reinterpret the slice as having a different data type (type punning), performing checks to ensure the reinterpret is valid.  
[UnsafeReinterpret](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.UnsafeReinterpret.html) | Reinterpret the slice as having a different data type (type punning), but does not check if the reinterpret is valid.  
* * *
