* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.ConnectInput.html

#  [PlayableExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html).ConnectInput
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
public static void ConnectInput(U playable, int inputIndex, V sourcePlayable, int sourceOutputIndex); 
## Declaration
public static void ConnectInput(U playable, int inputIndex, V sourcePlayable, int sourceOutputIndex, float weight); 
### Parameters
Parameter | Description  
---|---  
playable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) used by this operation.  
inputIndex | The input port index.  
sourcePlayable | The [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) to connect to.  
sourceOutputIndex | The output port of the [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html).  
weight | The weight of the input port.  
### Description
Connect the output port of a [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) to one of the input ports.
This method is a simple helper on top of [PlayableGraph.Connect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Connect.html).  
  
Use this templated extension method on any type that inherits from [IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html).
* * *
