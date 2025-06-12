* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableAsset.CreatePlayable.html

#  [PlayableAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableAsset.html).CreatePlayable
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
public [Playables.Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) CreatePlayable([Playables.PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) graph, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) owner); 
### Parameters
Parameter | Description  
---|---  
graph | The graph to inject playables into.  
owner | The game object which initiated the build.  
### Returns
**Playable** The playable injected into the graph, or the root playable if multiple playables are injected. 
### Description
Implement this method to have your asset inject playables into the given graph.
* * *
