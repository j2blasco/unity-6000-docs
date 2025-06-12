* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbesQuery.CalculateInterpolatedLightAndOcclusionProbe.html

#  [LightProbesQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbesQuery.html).CalculateInterpolatedLightAndOcclusionProbe
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
public void CalculateInterpolatedLightAndOcclusionProbe([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, ref int tetrahedronIndex, out [Rendering.SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html) lightProbe, out [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) occlusionProbe); 
### Parameters
Parameter | Description  
---|---  
position | The world space position used to evaluate the probe.  
tetrahedronIndex | Tetrahedron index that guides interpolation. Start with a value of 0 and reuse results between frames for faster lookup.  
lightProbe | The light probe where the resulting lighting is written to.  
occlusionProbe | The occlusion probe where the resulting occlusion is written to.  
### Description
Calculate light probe and occlusion probe at the given world space position.
* * *
