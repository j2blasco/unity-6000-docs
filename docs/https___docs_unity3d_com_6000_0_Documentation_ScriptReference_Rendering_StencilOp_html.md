* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html

# StencilOp
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
Specifies the operation that's performed on the stencil buffer when rendering.
### Properties
Property | Description  
---|---  
[Keep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.Keep.html) | Keeps the current stencil value.  
[Zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.Zero.html) | Sets the stencil buffer value to zero.  
[Replace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.Replace.html) | Replace the stencil buffer value with reference value (specified in the shader).  
[IncrementSaturate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.IncrementSaturate.html) | Increments the current stencil buffer value. Clamps to the maximum representable unsigned value.  
[DecrementSaturate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.DecrementSaturate.html) | Decrements the current stencil buffer value. Clamps to 0.  
[Invert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.Invert.html) | Bitwise inverts the current stencil buffer value.  
[IncrementWrap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.IncrementWrap.html) | Increments the current stencil buffer value. Wraps stencil buffer value to zero when incrementing the maximum representable unsigned value.  
[DecrementWrap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.DecrementWrap.html) | Decrements the current stencil buffer value. Wraps stencil buffer value to the maximum representable unsigned value when decrementing a stencil buffer value of zero.  
* * *
