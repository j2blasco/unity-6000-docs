* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Evaluate.html

#  [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).Evaluate
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
public void Evaluate(float deltaTime = 0); 
## Declaration
public void Evaluate(); 
### Parameters
Parameter | Description  
---|---  
deltaTime | The time in seconds by which to advance each [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) in the graph.  
### Description
Evaluates all the [PlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutput.html)s in the graph, and updates all the connected [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html)s in the graph.
* * *
