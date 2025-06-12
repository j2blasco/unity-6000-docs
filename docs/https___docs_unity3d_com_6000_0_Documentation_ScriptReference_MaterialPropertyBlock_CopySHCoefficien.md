* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopySHCoefficientArraysFrom.html

#  [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).CopySHCoefficientArraysFrom
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
public void CopySHCoefficientArraysFrom(List<SphericalHarmonicsL2> lightProbes); 
## Declaration
public void CopySHCoefficientArraysFrom(SphericalHarmonicsL2[] lightProbes); 
### Parameters
Parameter | Description  
---|---  
lightProbes | The array of SH values to copy from.  
### Description
This function converts and copies the entire source array into 7 Vector4 property arrays named `unity_SHAr`, `unity_SHAg`, `unity_SHAb`, `unity_SHBr`, `unity_SHBg`, `unity_SHBb` and `unity_SHC` for use with instanced [light probe](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html) rendering.
If the array properties don't exist on the MaterialPropertyBlock, they will be created with the length of the source array.  
Call [LightProbes.CalculateInterpolatedLightAndOcclusionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html) to calculate SH values at the given world space positions.  
ArgumentNullException is thrown if `lightProbes` is `null`.  
Note that all MaterialPropertyBlock arrays can only have a maximum of 1023 elements. Warnings are printed and the excess array elements are ignored if the source array exceeds the range.  
  
Additional resources: [CopyProbeOcclusionArrayFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopyProbeOcclusionArrayFrom.html), [Graphics.RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html), [CommandBuffer.DrawMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawMeshInstanced.html).
* * *
## Declaration
public void CopySHCoefficientArraysFrom(SphericalHarmonicsL2[] lightProbes, int sourceStart, int destStart, int count); 
## Declaration
public void CopySHCoefficientArraysFrom(List<SphericalHarmonicsL2> lightProbes, int sourceStart, int destStart, int count); 
### Parameters
Parameter | Description  
---|---  
lightProbes | The array of SH values to copy from.  
sourceStart | The index of the first element in the source array to copy from.  
destStart | The index of the first element in the destination MaterialPropertyBlock array to copy to.  
count | The number of elements to copy.  
### Description
This function converts and copies the source array into 7 Vector4 property arrays named `unity_SHAr`, `unity_SHAg`, `unity_SHAb`, `unity_SHBr`, `unity_SHBg`, `unity_SHBb` and `unity_SHC` with the specified source and destination range for use with instanced [light probe](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html) rendering.
If the array properties don't exist on the MaterialPropertyBlock, they will be created with the length of the spcified range.  
Call [LightProbes.CalculateInterpolatedLightAndOcclusionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html) to calculate SH values at the given world space positions.  
ArgumentNullException is thrown if `occlusionProbes` is `null`.  
ArgumentOutOfRangeException is thrown if the source or destination range is invalid.  
Note that all MaterialPropertyBlock arrays can only have a maximum of 1023 elements. Warnings are printed and the excess array elements are ignored if the source array exceeds the range.  
  
Additional resources: [CopyProbeOcclusionArrayFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopyProbeOcclusionArrayFrom.html), [Graphics.RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html), [CommandBuffer.DrawMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawMeshInstanced.html).
* * *
