* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DepthState.html

# DepthState
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
Values for the depth state.
Use this with [RenderStateBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html) and ScriptableRenderContext.DrawRenderers to override the GPU's render state.  
  
Corresponds to the `ZTest` and `ZWrite` commands in [ShaderLab](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html).  
  
Additional resources: [RenderStateBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html), [[ScriptableRenderContext.DrawRenderers], [ShaderLab command: ZTest](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ZTest.html), [ShaderLab command: ZWrite](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ZWrite.html).
### Static Properties
Property | Description  
---|---  
[defaultValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DepthState-defaultValue.html) | Default values for the depth state.  
### Properties
Property | Description  
---|---  
[compareFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DepthState-compareFunction.html) | How should depth testing be performed.  
[writeEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DepthState-writeEnabled.html) | Controls whether pixels from this object are written to the depth buffer.  
### Constructors
Constructor | Description  
---|---  
[DepthState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DepthState-ctor.html) | Creates a new depth state with the given values.  
* * *
