* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html

# PlayableExtensions
class in UnityEngine.Playables
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
Extensions for all the types that implements [IPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.IPlayable.html).
Extension methods are static methods that can be called as if they were instance methods on the extended type.
```
using UnityEngine;
using UnityEngine.Animations;
using UnityEngine.Playables;  
  
public class ExamplePlayableBehaviour : PlayableBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html)
{
    void Start()
    {
        PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) graph = PlayableGraph.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.Create.html)();
        AnimationMixerPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html) mixer = AnimationMixerPlayable.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.Create.html)(graph, 1);  
  
        // Calling method PlayableExtensions.SetDuration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetDuration.html) on AnimationMixerPlayable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationMixerPlayable.html) as if it was an instance method.
        mixer.SetDuration(10);  
  
        // The line above is the same as calling directly PlayableExtensions.SetDuration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetDuration.html), but it is more compact and readable.
        PlayableExtensions.SetDuration[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetDuration.html)(mixer, 10);
    }
}

```

### Static Methods
Method | Description  
---|---  
[AddInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.AddInput.html) | Create a new input port and connect it to the output port of the given Playable.  
[ConnectInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.ConnectInput.html) | Connect the output port of a Playable to one of the input ports.  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.Destroy.html) | Destroys the current Playable.  
[DisconnectInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.DisconnectInput.html) | Disconnect the input port of a Playable.  
[GetDuration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetDuration.html) | Returns the duration of the Playable.  
[GetGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetGraph.html) | Returns the PlayableGraph that owns this Playable. A Playable can only be used in the graph that was used to create it.  
[GetInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetInput.html) | Returns the Playable connected at the given input port index.  
[GetInputCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetInputCount.html) | Returns the number of inputs supported by the Playable.  
[GetInputWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetInputWeight.html) | Returns the weight of the Playable connected at the given input port index.  
[GetLeadTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetLeadTime.html) | Returns the Playable lead time in seconds.  
[GetOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetOutput.html) | Returns the Playable connected at the given output port index.  
[GetOutputCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetOutputCount.html) | Returns the number of outputs supported by the Playable.  
[GetPlayState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetPlayState.html) | Returns the current PlayState of the Playable.  
[GetPreviousTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetPreviousTime.html) | Returns the previous local time of the Playable.  
[GetPropagateSetTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetPropagateSetTime.html) | Returns the time propagation behavior of this Playable.  
[GetSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetSpeed.html) | Returns the speed multiplier that is applied to the the current Playable.  
[GetTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetTime.html) | Returns the current local time of the Playable.  
[GetTraversalMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.GetTraversalMode.html) | Returns the propagation mode for the multi-output playable.  
[IsDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.IsDone.html) | Returns a flag indicating that a playable has completed its operation.  
[IsNull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.IsNull.html) | Returns true if the Playable is null, false otherwise.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.IsValid.html) | Returns the vality of the current Playable.  
[Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.Pause.html) | Tells to pause the Playable.  
[Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.Play.html) | Starts to play the Playable.  
[SetDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetDone.html) | Changes a flag indicating that a playable has completed its operation.  
[SetDuration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetDuration.html) | Changes the duration of the Playable.  
[SetInputCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetInputCount.html) | Changes the number of inputs supported by the Playable.  
[SetInputWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetInputWeight.html) | Changes the weight of the Playable connected to the current Playable.  
[SetLeadTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetLeadTime.html) | Sets the Playable lead time in seconds.  
[SetOutputCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetOutputCount.html) | Changes the number of outputs supported by the Playable.  
[SetPropagateSetTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetPropagateSetTime.html) | Changes the time propagation behavior of this Playable.  
[SetSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetSpeed.html) | Changes the speed multiplier that is applied to the the current Playable.  
[SetTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetTime.html) | Changes the current local time of the Playable.  
[SetTraversalMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.SetTraversalMode.html) | Sets the propagation mode of PrepareFrame and ProcessFrame for the multi-output playable.  
* * *
