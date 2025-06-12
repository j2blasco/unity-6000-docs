* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.AddInput.html

#  [PlayableExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html).AddInput
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
public static int AddInput(U playable, V sourcePlayable, int sourceOutputIndex, float weight); 
### Parameters
Parameter | Description  
---|---  
playable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) used by this operation.  
sourcePlayable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) to connect to.  
sourceOutputIndex | The output port of the [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html).  
weight | The weight of the created input port.  
### Returns
**int** The index of the newly created input port. 
### Description
Create a new input port and connect it to the output port of the given [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html).
If several inputs are needed, it is better to use [SetInputCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetInputCount.html) and [ConnectInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.ConnectInput.html).  
This method is a mere helper on top of [PlayableGraph.Connect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Connect.html).  
  
Use this templated extension method on any type that inherits from [IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html).
* * *
