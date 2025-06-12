* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData.html

# ShadowSplitData
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
Describes the culling information for a given shadow split (e.g. directional cascade).
### Static Properties
Property | Description  
---|---  
[maximumCullingPlaneCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData-maximumCullingPlaneCount.html) | The maximum number of culling planes.  
### Properties
Property | Description  
---|---  
[cullingMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData-cullingMatrix.html) | The model view projection matrix Unity uses to cull objects it renders into this shadow map.  
[cullingNearPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData-cullingNearPlane.html) | The near plane distance that Unity uses to cull objects. Unity transforms the objects with ShadowSplitData.cullingMatrix, and then culls the ones that are farther than the near plane distance.  
[cullingPlaneCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData-cullingPlaneCount.html) | The number of culling planes.  
[cullingSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData-cullingSphere.html) | The culling sphere. The first three components of the vector describe the sphere center, and the last component specifies the radius.  
[shadowCascadeBlendCullingFactor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData-shadowCascadeBlendCullingFactor.html) |  A multiplier applied to the radius of the culling sphere.Values must be in the range 0 to 1. With higher values, Unity culls more objects. Lower makes the cascades share more rendered objects. Using lower values allows blending between different cascades as they then share objects.   
### Public Methods
Method | Description  
---|---  
[GetCullingPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData.GetCullingPlane.html) | Gets a culling plane.  
[SetCullingPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData.SetCullingPlane.html) | Sets a culling plane.  
* * *
