* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html

# PlayableGraph
struct in UnityEngine.Playables
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
Use the PlayableGraph to manage [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) creations and destructions.
The PlayableGraph is also the link to different systems, through structs that implement [IPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayableOutput.html). For example, [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html) or [AudioPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioPlayableOutput.html).
### Public Methods
Method | Description  
---|---  
[Connect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Connect.html) | Connects two Playable instances.  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Destroy.html) | Destroys the graph.  
[DestroyOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.DestroyOutput.html) | Destroys the PlayableOutput.  
[DestroyPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.DestroyPlayable.html) | Destroys the Playable.  
[DestroySubgraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.DestroySubgraph.html) | Destroys the Playable and all its inputs, recursively.  
[Disconnect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Disconnect.html) | Disconnects the Playable. The connections determine the topology of the PlayableGraph and how it is evaluated.  
[Evaluate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Evaluate.html) | Evaluates all the PlayableOutputs in the graph, and updates all the connected Playables in the graph.  
[GetEditorName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetEditorName.html) | Returns the name of the PlayableGraph.  
[GetOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetOutput.html) | Get PlayableOutput at the given index in the graph.  
[GetOutputByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetOutputByType.html) | Get PlayableOutput of the requested type at the given index in the graph.  
[GetOutputCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetOutputCount.html) | Returns the number of PlayableOutput in the graph.  
[GetOutputCountByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetOutputCountByType.html) | Get the number of PlayableOutput of the requested type in the graph.  
[GetPlayableCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetPlayableCount.html) | Returns the number of Playable owned by the Graph.  
[GetResolver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetResolver.html) | Returns the table used by the graph to resolve ExposedReferences.  
[GetRootPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetRootPlayable.html) | Returns the Playable with no output connections at the given index.  
[GetRootPlayableCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetRootPlayableCount.html) | Returns the number of Playable owned by the Graph that have no connected outputs.  
[GetTimeUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.GetTimeUpdateMode.html) | Returns how time is incremented when playing back.  
[IsDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.IsDone.html) | Indicates that a graph has completed its operations.  
[IsPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.IsPlaying.html) | Indicates that a graph is presently running.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.IsValid.html) | Returns true if the PlayableGraph has been properly constructed using PlayableGraph.CreateGraph and is not deleted.  
[Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Play.html) | Plays the graph.  
[SetResolver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.SetResolver.html) | Changes the table used by the graph to resolve ExposedReferences.  
[SetTimeUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.SetTimeUpdateMode.html) | Changes how time is incremented when playing back.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Stop.html) | Stops the graph, if it is playing.  
### Static Methods
Method | Description  
---|---  
[Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html) | Creates a PlayableGraph.  
* * *
