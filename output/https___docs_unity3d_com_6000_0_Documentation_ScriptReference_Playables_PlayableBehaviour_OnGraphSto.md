* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.OnGraphStop.html

#  [PlayableBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html).OnGraphStop
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
public void OnGraphStop([Playables.Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) playable); 
### Parameters
Parameter | Description  
---|---  
playable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) that owns the current PlayableBehaviour.  
### Description
This function is called when the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) that owns this PlayableBehaviour stops.
OnGraphStop is called when Unity stops playing the owning graph, and is guaranteed to always and only be called if OnGraphStart has been called. If the graph has been only been manually evaluated, OnGraphStop will be called prior to destroy. 
* * *
