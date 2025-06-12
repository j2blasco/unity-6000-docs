* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html

# Playable
struct in UnityEngine.Playables
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
  

Implements interfaces:[IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html)
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
Playables are customizable runtime objects that can be connected together and are contained in a [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) to create complex behaviours.
Playables can be used to create complex and flexible data evaluation trees. Playables are nodes that can be connected together, after which each Playable can set the "weight" or "influence" of each of its children.  
  
The playables of the same graph are contained in a [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html). A PlayableGraph can have several outputs, also called "players", which implement [IPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayableOutput.html). The PlayableOutput takes the result of their source playable and apply it to an object in the Scene. For instance, the [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html) is linked to a playable node in the graph (the "source playable") and to an [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) in the Scene. When the graph is played, the animation pose resulting of the graph evaluation is applied by the Animator. There are as many PlayableOutputs as there are different playable types: [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html), [AudioPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioPlayableOutput.html), [TexturePlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.TexturePlayableOutput.html), [ScriptPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.html), etc...  
  
The ScriptPlayable<T> is a special kind of playable. It's main role is to be a "custom" playable. It is a templated struct where `T` must derived from [PlayableBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html). These custom PlayableBehaviours allow to write behaviours at specific moments in the graph evaluation (see [PlayableBehaviour.PrepareFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.PrepareFrame.html) and [PlayableBehaviour.ProcessFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.ProcessFrame.html)). A good example of a ScriptPlayable is the TimelinePlayable which is controlling the Timeline graph. It creates and links together the playables in charge of the tracks and the clips.  
  
When a [PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) is played, each PlayableOutput will be traversed. During this traversal, it will call the PrepareFrame method on each Playable. This allows the Playable to "prepare itself for the next evaluation". It is during the PrepareFrame stage that each Playable can modify its children (either by adding new inputs or by removing some of them). This enables Playable to "spawn" new children branches in the Playable tree at runtime. This means that Playable trees are not static structures. They can adapt and change over time.  
  
Once the preparation is done, the PlayableOutputs are in charge of processing the result, that's why they are also called "players". In the case of an [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html), the [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) is in charge of processing the graph. And in the case of a [ScriptPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.html), [PlayableBehaviour.ProcessFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.ProcessFrame.html) will be called on each ScriptPlayable.  
  
**Note:** You can use the [PlayableExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html) methods on any struct implementing [IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html).  
  
**Note:** The Manual has detailed documentation about the [Playables API](https://docs.unity3d.com/6000.0/Documentation/Manual/Playables.html). 
### Static Properties
Property | Description  
---|---  
[Null](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.Null.html) | Returns an invalid Playable.  
* * *
