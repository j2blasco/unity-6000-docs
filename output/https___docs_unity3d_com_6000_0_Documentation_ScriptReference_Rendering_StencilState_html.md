* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState.html

# StencilState
struct in UnityEngine.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Values for the stencil state.
Use this with [RenderStateBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html) and ScriptableRenderContext.DrawRenderers to override the GPU's render state.  
  
Corresponds to the `Stencil` command in [ShaderLab](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html).  
  
Additional resources: [RenderStateBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html), [[ScriptableRenderContext.DrawRenderers], [ShaderLab command: Stencil](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Stencil.html).
### Static Properties
Property | Description  
---|---  
[defaultValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-defaultValue.html) | Default values for the stencil state.  
### Properties
Property | Description  
---|---  
[compareFunctionBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-compareFunctionBack.html) | The function used to compare the reference value to the current contents of the buffer for back-facing geometry.  
[compareFunctionFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-compareFunctionFront.html) | The function used to compare the reference value to the current contents of the buffer for front-facing geometry.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-enabled.html) | Controls whether the stencil buffer is enabled.  
[failOperationBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-failOperationBack.html) | What to do with the contents of the buffer if the stencil test fails for back-facing geometry.  
[failOperationFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-failOperationFront.html) | What to do with the contents of the buffer if the stencil test fails for front-facing geometry.  
[passOperationBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-passOperationBack.html) | What to do with the contents of the buffer if the stencil test (and the depth test) passes for back-facing geometry.  
[passOperationFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-passOperationFront.html) | What to do with the contents of the buffer if the stencil test (and the depth test) passes for front-facing geometry.  
[readMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-readMask.html) | An 8 bit mask as an 0–255 integer, used when comparing the reference value with the contents of the buffer.  
[writeMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-writeMask.html) | An 8 bit mask as an 0–255 integer, used when writing to the buffer.  
[zFailOperationBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-zFailOperationBack.html) | What to do with the contents of the buffer if the stencil test passes, but the depth test fails for back-facing geometry.  
[zFailOperationFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-zFailOperationFront.html) | What to do with the contents of the buffer if the stencil test passes, but the depth test fails for front-facing geometry.  
### Constructors
Constructor | Description  
---|---  
[StencilState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState-ctor.html) | Creates a new stencil state with the given values.  
### Public Methods
Method | Description  
---|---  
[SetCompareFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState.SetCompareFunction.html) | The function used to compare the reference value to the current contents of the buffer.  
[SetFailOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState.SetFailOperation.html) | What to do with the contents of the buffer if the stencil test fails.  
[SetPassOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState.SetPassOperation.html) | What to do with the contents of the buffer if the stencil test (and the depth test) passes.  
[SetZFailOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState.SetZFailOperation.html) | What to do with the contents of the buffer if the stencil test passes, but the depth test fails.  
* * *
