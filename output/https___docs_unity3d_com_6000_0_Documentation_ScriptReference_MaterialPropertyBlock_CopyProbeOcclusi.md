* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopyProbeOcclusionArrayFrom.html

#  [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).CopyProbeOcclusionArrayFrom
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
public void CopyProbeOcclusionArrayFrom(Vector4[] occlusionProbes); 
## Declaration
public void CopyProbeOcclusionArrayFrom(List<Vector4> occlusionProbes); 
### Parameters
Parameter | Description  
---|---  
occlusionProbes | The array of probe occlusion values to copy from.  
### Description
This function copies the entire source array into a Vector4 property array named `unity_ProbesOcclusion` for use with instanced [Shadowmask](https://docs.unity3d.com/6000.0/Documentation/Manual/LightMode-Mixed-Shadowmask.html) rendering.
If the array property doesn't exist on the MaterialPropertyBlock, it will be created with the length of the source array.  
Call [LightProbes.CalculateInterpolatedLightAndOcclusionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html) to calculate probe occlusion values at the given world space positions.  
ArgumentNullException is thrown if `occlusionProbes` is `null`.  
Note that all MaterialPropertyBlock arrays can only have a maximum of 1023 elements. Warnings are printed and the excess array elements are ignored if the source array exceeds the range.  
  
Additional resources: [CopySHCoefficientArraysFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopySHCoefficientArraysFrom.html), [Graphics.RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html), [CommandBuffer.DrawMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawMeshInstanced.html).
* * *
## Declaration
public void CopyProbeOcclusionArrayFrom(Vector4[] occlusionProbes, int sourceStart, int destStart, int count); 
## Declaration
public void CopyProbeOcclusionArrayFrom(List<Vector4> occlusionProbes, int sourceStart, int destStart, int count); 
### Parameters
Parameter | Description  
---|---  
occlusionProbes | The array of probe occlusion values to copy from.  
sourceStart | The index of the first element in the source array to copy from.  
destStart | The index of the first element in the destination MaterialPropertyBlock array to copy to.  
count | The number of elements to copy.  
### Description
This function copies the source array into a Vector4 property array named `unity_ProbesOcclusion` with the specified source and destination range for use with instanced [Shadowmask](https://docs.unity3d.com/6000.0/Documentation/Manual/LightMode-Mixed-Shadowmask.html) rendering.
If the array property doesn't exist on the MaterialPropertyBlock, it will be created with the length of the spcified range.  
Call [LightProbes.CalculateInterpolatedLightAndOcclusionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html) to calculate probe occlusion values at the given world space positions.  
ArgumentNullException is thrown if `occlusionProbes` is `null`.  
ArgumentOutOfRangeException is thrown if the source or destination range is invalid.  
Note that all MaterialPropertyBlock arrays can only have a maximum of 1023 elements. Warnings are printed and the excess array elements are ignored if the source array exceeds the range.  
  
Additional resources: [CopySHCoefficientArraysFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopySHCoefficientArraysFrom.html), [Graphics.RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html), [CommandBuffer.DrawMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawMeshInstanced.html).
* * *
