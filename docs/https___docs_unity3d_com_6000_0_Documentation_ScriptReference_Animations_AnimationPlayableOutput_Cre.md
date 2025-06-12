* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.Create.html

#  [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html).Create
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
public static [Animations.AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html) Create([Playables.PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) graph, string name, [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) target); 
### Parameters
Parameter | Description  
---|---  
graph | The [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) that will contain the [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html).  
name | The name of the output.  
target | The [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) that will process the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).  
### Returns
**AnimationPlayableOutput** A new [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html) attached to the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html). 
### Description
Creates an [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html) in the [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html).
The [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) plays the source [Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) of the [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html). This source Playable can be set with SetSourcePlayable.
* * *
