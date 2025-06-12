* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.html

# PassType
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
Shader pass type for Unity's lighting pipeline.
This corresponds to "LightMode" tag in the shader pass, see [Pass tags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html).
### Properties
Property | Description  
---|---  
[Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.Normal.html) | Regular shader pass that does not interact with lighting.  
[Vertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.Vertex.html) | Legacy vertex-lit shader pass.  
[VertexLM](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.VertexLM.html) | Legacy vertex-lit shader pass, with mobile lightmaps.  
[ForwardBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.ForwardBase.html) | Forward rendering base pass.  
[ForwardAdd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.ForwardAdd.html) | Forward rendering additive pixel light pass.  
[ShadowCaster](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.ShadowCaster.html) | Shadow caster & depth texure shader pass.  
[Deferred](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.Deferred.html) | Deferred Shading shader pass.  
[Meta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.Meta.html) | Shader pass used to generate the albedo and emissive values used as input to lightmapping.  
[MotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.MotionVectors.html) | Motion vector render pass.  
[ScriptableRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.ScriptableRenderPipeline.html) | Custom scriptable pipeline.  
[ScriptableRenderPipelineDefaultUnlit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.ScriptableRenderPipelineDefaultUnlit.html) | Custom scriptable pipeline when lightmode is set to default unlit or no light mode is set.  
[GrabPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.GrabPass.html) | Grab Pass. Use this when you want to detect the type of the Grab Pass compared to other passes using the Normal type. Otherwise use Normal.  
* * *
