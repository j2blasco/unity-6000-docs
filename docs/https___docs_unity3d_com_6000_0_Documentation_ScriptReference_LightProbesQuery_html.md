* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbesQuery.html

# LightProbesQuery
struct in UnityEngine
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
Thread-safe struct for batch sampling Light Probes in a Scene.
This struct allows for sampling Light Probes from a job or a thread. If you load a scene additively, you must call LightProbes.Tetrahedralize to include its Light Probes in the batch sample.
### Properties
Property | Description  
---|---  
[IsCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbesQuery.IsCreated.html) | This property indicates whether target query data is valid.  
### Constructors
Constructor | Description  
---|---  
[LightProbesQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbesQuery-ctor.html) | "Constructor for creating Light Probe sample queries."  
### Public Methods
Method | Description  
---|---  
[CalculateInterpolatedLightAndOcclusionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbesQuery.CalculateInterpolatedLightAndOcclusionProbe.html) | Calculate light probe and occlusion probe at the given world space position.  
[CalculateInterpolatedLightAndOcclusionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbesQuery.CalculateInterpolatedLightAndOcclusionProbes.html) | Calculate light probes and occlusion probes at the given world space positions.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbesQuery.Dispose.html) | Use this method to clean up the memory this query references.  
* * *
