* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.UnsafeReinterpret.html

#  [BufferSlice<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.html).UnsafeReinterpret
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
public BufferSlice<U> UnsafeReinterpret(); 
### Returns
**BufferSlice <U>** An alias of the same slice, but reinterpreted as the target type. 
### Description
Reinterpret the slice as having a different data type (type punning), but does not check if the reinterpret is valid.
The size of the target type must be a multiple of the size of the current type.  
  
Additional resources: [BufferSlice<T0>.SafeReinterpret](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.SafeReinterpret.html).
* * *
