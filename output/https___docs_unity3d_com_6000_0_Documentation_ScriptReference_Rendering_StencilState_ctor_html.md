* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-ctor.html

# StencilState Constructor
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
public StencilState(bool enabled, byte readMask, byte writeMask, [Rendering.CompareFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.html) compareFunction, [Rendering.StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) passOperation, [Rendering.StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) failOperation, [Rendering.StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) zFailOperation); 
## Declaration
public StencilState(bool enabled, byte readMask, byte writeMask, [Rendering.CompareFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.html) compareFunctionFront, [Rendering.StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) passOperationFront, [Rendering.StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) failOperationFront, [Rendering.StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) zFailOperationFront, [Rendering.CompareFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.html) compareFunctionBack, [Rendering.StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) passOperationBack, [Rendering.StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) failOperationBack, [Rendering.StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) zFailOperationBack); 
### Parameters
Parameter | Description  
---|---  
readMask | An 8 bit mask as an 0–255 integer, used when comparing the reference value with the contents of the buffer.  
writeMask | An 8 bit mask as an 0–255 integer, used when writing to the buffer.  
enabled | Controls whether the stencil buffer is enabled.  
compareFunctionFront | The function used to compare the reference value to the current contents of the buffer for front-facing geometry.  
passOperationFront | What to do with the contents of the buffer if the stencil test (and the depth test) passes for front-facing geometry.  
failOperationFront | What to do with the contents of the buffer if the stencil test fails for front-facing geometry.  
zFailOperationFront | What to do with the contents of the buffer if the stencil test passes, but the depth test fails for front-facing geometry.  
compareFunctionBack | The function used to compare the reference value to the current contents of the buffer for back-facing geometry.  
passOperationBack | What to do with the contents of the buffer if the stencil test (and the depth test) passes for back-facing geometry.  
failOperationBack | What to do with the contents of the buffer if the stencil test fails for back-facing geometry.  
zFailOperationBack | What to do with the contents of the buffer if the stencil test passes, but the depth test fails for back-facing geometry.  
compareFunction | The function used to compare the reference value to the current contents of the buffer.  
passOperation | What to do with the contents of the buffer if the stencil test (and the depth test) passes.  
failOperation | What to do with the contents of the buffer if the stencil test fails.  
zFailOperation | What to do with the contents of the buffer if the stencil test passes, but the depth test.  
### Description
Creates a new stencil state with the given values.
* * *
