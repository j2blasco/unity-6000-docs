* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html

# RenderParams
struct in UnityEngine
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
Rendering parameters used by various rendering functions.
This struct defines common parameters shared across various rendering functions.  
  
Additional resources: [Graphics.RenderMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html), [Graphics.RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html), [Graphics.RenderMeshIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshIndirect.html), [Graphics.RenderMeshPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshPrimitives.html), [Graphics.RenderPrimitives](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitives.html), [Graphics.RenderPrimitivesIndexed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndexed.html), [Graphics.RenderPrimitivesIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndirect.html), [Graphics.RenderPrimitivesIndexedIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderPrimitivesIndexedIndirect.html).
### Properties
Property | Description  
---|---  
[camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-camera.html) | The camera used for rendering. If set to null (default) renders for all cameras.  
[instanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-instanceID.html) | The instance ID of the GameObject that issues the draw. Provide an instanceID to make a rendered GameObject pickable in the scene view when you click on it. The default value is 0, which means that you can't pick or outline the procedural GameObject in the scene view.  
[layer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-layer.html) | Layer used for rendering. Layer to use.  
[lightProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-lightProbeProxyVolume.html) | Light Probe Proxy Volume (LPPV) used for rendering.  
[lightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-lightProbeUsage.html) | The type of light probe usage.  
[material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-material.html) | Material used for rendering.  
[matProps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-matProps.html) | Material properties used for rendering.  
[motionVectorMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-motionVectorMode.html) | Motion vector mode used for rendering.  
[overrideSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-overrideSceneCullingMask.html) | Uses the RenderParams.sceneCullingMask property to specify a custom SceneCullingMasks. This property is only available in the Editor, you can still access it in a Player but it'll be ignored.  
[receiveShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-receiveShadows.html) | Descripes if the rendered geometry should receive shadows.  
[reflectionProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-reflectionProbeUsage.html) | The type of reflection probe used for rendering.  
[rendererPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-rendererPriority.html) | Renderer priority.  
[renderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-renderingLayerMask.html) | Renderer layer mask used for rendering.  
[sceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-sceneCullingMask.html) | Overrides the scene culling mask for the rendered object. This can help you control prefab stage visibility or entities sub-scene visibiliy. This property is only available in the Editor, you can still access it in a Player but it'll be ignored..  
[shadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-shadowCastingMode.html) | Describes if geometry should cast shadows.  
[worldBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-worldBounds.html) | Defines world space bounds for the geometry. Used to cull and sort the rendered geometry.  
### Constructors
Constructor | Description  
---|---  
[RenderParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams-ctor.html) | Constructor.  
* * *
