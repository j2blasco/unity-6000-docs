* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.GetClosestReflectionProbes.html

#  [Terrain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain.html).GetClosestReflectionProbes
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
public void GetClosestReflectionProbes(List<ReflectionProbeBlendInfo> result); 
### Parameters
Parameter | Description  
---|---  
result | [in / out] A list to hold the returned reflection probes and their weights. See [ReflectionProbeBlendInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeBlendInfo.html).  
### Description
Fills the list with reflection probes whose AABB intersects with terrain's AABB. Their weights are also provided. Weight shows how much influence the probe has on the terrain, and is used when the blending between multiple reflection probes occurs.
This function won't touch `result` if [Terrain.reflectionProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Terrain-reflectionProbeUsage.html) is [ReflectionProbeUsage.Off](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeUsage.Off.html), otherwise the original content of the list will be cleared.
* * *
