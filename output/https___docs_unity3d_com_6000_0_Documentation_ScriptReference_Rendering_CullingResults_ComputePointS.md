* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.ComputePointShadowMatricesAndCullingPrimitives.html

#  [CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html).ComputePointShadowMatricesAndCullingPrimitives
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
public bool ComputePointShadowMatricesAndCullingPrimitives(int activeLightIndex, [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) cubemapFace, float fovBias, out [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) viewMatrix, out [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) projMatrix, out [Rendering.ShadowSplitData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData.html) shadowSplitData); 
### Parameters
Parameter | Description  
---|---  
activeLightIndex | The index into the active light array.  
cubemapFace | The cubemap face to be rendered.  
fovBias | The amount by which to increase the camera FOV above 90 degrees.  
viewMatrix | The computed view matrix.  
projMatrix | The computed projection matrix.  
shadowSplitData | The computed split data.  
### Returns
**bool** If false, the shadow map for this light and cubemap face does not need to be rendered this frame. 
### Description
Calculates the view and projection matrices and shadow split data for a point light.
* * *
