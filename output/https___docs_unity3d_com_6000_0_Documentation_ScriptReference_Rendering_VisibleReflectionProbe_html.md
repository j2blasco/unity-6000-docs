* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe.html

# VisibleReflectionProbe
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
Holds data of a visible reflection reflectionProbe.
After [ScriptableRenderContext.Cull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Cull.html) is done, [CullingResults.visibleReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleReflectionProbes.html) will contain an array of reflection reflectionProbes that are visible. The visible reflection reflectionProbe structure contains packed information for most commonly used [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) variables, and a VisibleReflectionProbe.probe reference to the component itself.  
  
Additional resources: [CullingResults.visibleReflectionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleReflectionProbes.html), [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html).
### Properties
Property | Description  
---|---  
[blendDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe-blendDistance.html) | Probe blending distance.  
[bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe-bounds.html) | The probe's world space axis-aligned bounding box in which the probe can contribute to reflections.  
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe-center.html) | The center of the probe's bounding box in which the probe can contribute to reflections. The center is relative to the position of the probe.  
[hdrData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe-hdrData.html) | Shader data for probe HDR texture decoding.  
[importance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe-importance.html) | Probe importance.  
[isBoxProjection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe-isBoxProjection.html) | Should probe use box projection.  
[localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe-localToWorldMatrix.html) | Probe transformation matrix.  
[reflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe-reflectionProbe.html) | Accessor to ReflectionProbe component.  
[texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe-texture.html) | Probe texture.  
* * *
