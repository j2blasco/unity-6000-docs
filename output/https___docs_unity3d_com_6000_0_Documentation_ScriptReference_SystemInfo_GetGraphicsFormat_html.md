* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.GetGraphicsFormat.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).GetGraphicsFormat
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
public static [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) GetGraphicsFormat([Experimental.Rendering.DefaultFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.DefaultFormat.html) format); 
### Parameters
Parameter | Description  
---|---  
format | The [DefaultFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.DefaultFormat.html) format to look up.  
### Description
Returns the platform-specific GraphicsFormat that is associated with the DefaultFormat.
You can create a RenderTexture with [DefaultFormat.DepthStencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.DefaultFormat.DepthStencil.html) by setting the resulting [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) to [RenderTexture.depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthStencilFormat.html), [RenderTextureDescriptor.depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-depthStencilFormat.html) or by using one of the constructors.  
  
To create a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) that you can use as a shadow map, set the [ShadowSamplingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSamplingMode.html) using [RenderTextureDescriptor.shadowSamplingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-shadowSamplingMode.html). If you only set the depth or stencil format and not the [ShadowSamplingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSamplingMode.html) then you will not have a valid shadow map.  
  
Additional resources: [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) enum and [DefaultFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.DefaultFormat.html).
* * *
