* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters-backFaceTolerance.html

#  [LightmapParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html).backFaceTolerance
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html "Go to LightmapParameters Component in the Manual")
backFaceTolerance; 
### Description
The percentage of rays shot from a ray origin that must hit front faces to be considered usable.
The precompute calculates visibility from ray origins to clusters, but attempts to reject ray origins that are inside geometry. If the percentage of rays that hit front faces is less than backFaceTolerance, the ray origin is marked invalid and will not affect the radiosity computation.  
  
  
  
For example, if backFaceTolerance is 0.0, the ray origin is rejected only if it sees nothing but backfaces. If 1.0, the ray origin is rejected if it has even one ray that hits a backface.  
  
  
  
This setting can help control light leaking, but should be considered in the context of the mesh authoring workflow. Preventing ray origin rejection by setting a value of 0.0 will ensure Enlighten Realtime Global Illumination does not reject ray origins due to single-sided geometry. However, if the majority of the meshes are closed, so visible backfaces are rare, a positive value can reduce light leaking or darkening that intersecting geometry would otherwise cause.
* * *
