* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SamplePlayableGraph.html

#  [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html).SamplePlayableGraph(GameObject,PlayableGraph,int,float)
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
### Parameters
Parameter | Description  
---|---  
graph | The [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) to sample.  
index | The output index to sample in the Playable Graph.  
time | The time at which to sample.  
### Description
Samples the specified output index of a [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) and also records modified properties when in Animation mode.
To successfully use this method, [BeginSampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.BeginSampling.html) must be called before this method and [EndSampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.EndSampling.html) must be called after. If a property is no longer sampled (for example, through [SampleAnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SampleAnimationClip.html), [SamplePlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SamplePlayableGraph.html), or [AddPropertyModification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.AddPropertyModification.html)), the property reverts to its original value when [EndSampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.EndSampling.html) is called.
* * *
