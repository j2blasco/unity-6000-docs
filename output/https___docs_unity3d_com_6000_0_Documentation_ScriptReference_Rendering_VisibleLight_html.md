* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight.html

# VisibleLight
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
Holds data of a visible light.
After [ScriptableRenderContext.Cull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.Cull.html) is done, [CullingResults.visibleLights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleLights.html) will contain an array of lights that are visible. The visible light structure contains packed information for most commonly used [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) variables, and a [VisibleLight.light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-light.html) reference to the Light component itself.  
  
Additional resources: [CullingResults.visibleLights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults-visibleLights.html), [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).
### Properties
Property | Description  
---|---  
[finalColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-finalColor.html) | Light color multiplied by intensity.  
[forcedVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-forcedVisible.html) | Has the light been forced to be visibile.  
[intersectsFarPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-intersectsFarPlane.html) | Light intersects far clipping plane.  
[intersectsNearPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-intersectsNearPlane.html) | Light intersects near clipping plane.  
[light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-light.html) | Accessor to Light component.  
[lightType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-lightType.html) | Light type.  
[localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-localToWorldMatrix.html) | Light transformation matrix.  
[range](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-range.html) | Light range.  
[screenRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-screenRect.html) | Light's influence rectangle on screen.  
[spotAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight-spotAngle.html) | Spot light angle.  
* * *
