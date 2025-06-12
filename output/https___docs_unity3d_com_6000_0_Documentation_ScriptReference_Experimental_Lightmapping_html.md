* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# Lightmapping
class in UnityEditor.Experimental
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
Experimental lightmapping features.
Additional resources: [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).
### Static Properties
Property | Description  
---|---  
[probesIgnoreDirectEnvironment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping-probesIgnoreDirectEnvironment.html) | If enabled ignores the direct contribution from the environment lighting in baked probes.  
[probesIgnoreIndirectEnvironment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping-probesIgnoreIndirectEnvironment.html) | If enabled ignores the indirect contribution from the environment lighting in baked probes.  
### Static Methods
Method | Description  
---|---  
[Bake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.Bake.html) | Starts a synchronous lighting bake job for the target Scene.  
[BakeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.BakeAsync.html) | Starts an asynchronous lighting bake job for the target Scene.  
[GetAdditionalBakedProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.GetAdditionalBakedProbes.html) | Retrieve the bake result of additional probes.  
[GetCustomBakeResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.GetCustomBakeResults.html) | Retrieve the custom bake results.  
[GetCustomBakeResultsNoCopy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.GetCustomBakeResultsNoCopy.html) | Retrieve the custom bake results.  
[SetAdditionalBakedProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.SetAdditionalBakedProbes.html) | Submit additional probe positions to be baked using an identifier.  
[SetCustomBakeInputs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.SetCustomBakeInputs.html) | Set the custom bake inputs.  
[SetLightDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.SetLightDirty.html) | Manually sets a light as dirty.  
### Events
Event | Description  
---|---  
[additionalBakedProbesCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping-additionalBakedProbesCompleted.html) | Event which is called when additional probe bakes have completed and results are ready to be fetched.  
* * *
