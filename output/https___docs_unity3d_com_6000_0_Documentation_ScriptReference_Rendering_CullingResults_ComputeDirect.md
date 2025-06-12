* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.ComputeDirectionalShadowMatricesAndCullingPrimitives.html

#  [CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html).ComputeDirectionalShadowMatricesAndCullingPrimitives
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
public bool ComputeDirectionalShadowMatricesAndCullingPrimitives(int activeLightIndex, int splitIndex, int splitCount, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) splitRatio, int shadowResolution, float shadowNearPlaneOffset, out [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) viewMatrix, out [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) projMatrix, out [Rendering.ShadowSplitData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData.html) shadowSplitData); 
### Parameters
Parameter | Description  
---|---  
activeLightIndex | The index into the active light array.  
splitIndex | The cascade index.  
splitCount | The number of cascades.  
splitRatio | The cascade ratios.  
shadowResolution | The resolution of the shadowmap.  
shadowNearPlaneOffset | The near plane offset for the light.  
viewMatrix | The computed view matrix.  
projMatrix | The computed projection matrix.  
shadowSplitData | The computed cascade data.  
### Returns
**bool** If false, the shadow map for this cascade does not need to be rendered this frame. 
### Description
Calculates the view and projection matrices and shadow split data for a directional light.
Additional resources: [ShadowSplitData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData.html).
* * *
