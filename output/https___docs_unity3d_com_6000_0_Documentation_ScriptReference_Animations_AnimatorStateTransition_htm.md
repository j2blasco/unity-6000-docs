* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html

# AnimatorStateTransition
class in UnityEditor.Animations
/
Inherits from:[Animations.AnimatorTransitionBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase.html)
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
Transitions define when and how the state machine switch from one state to another. [AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) always originate from an Animator State (or AnyState) and have timing parameters.
A transition happens when all its conditions are met. [AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) derives from [AnimatorTransitionBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase.html).
### Properties
Property | Description  
---|---  
[canTransitionToSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-canTransitionToSelf.html) | Set to true to allow or disallow transition to self during AnyState transition.  
[duration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-duration.html) | The duration of the transition.  
[exitTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-exitTime.html) | If AnimatorStateTransition.hasExitTime is true, exitTime represents the exact time at which the transition can take effect. This is represented in normalized time, so for example an exit time of 0.75 means that on the first frame where 75% of the animation has played, the Exit Time condition will be true. On the next frame, the condition will be false. For looped animations, transitions with exit times smaller than 1 will be evaluated every loop, so you can use this to time your transition with the proper timing in the animation, every loop. Transitions with exit times greater than one will be evaluated only once, so they can be used to exit at a specific time, after a fixed number of loops. For example, a transition with an exit time of 3.5 will be evaluated once, after three and a half loops.  
[hasExitTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-hasExitTime.html) | When active the transition will have an exit time condition.  
[hasFixedDuration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-hasFixedDuration.html) | Determines whether the duration of the transition is reported in a fixed duration in seconds or as a normalized time.  
[interruptionSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-interruptionSource.html) | Which AnimatorState transitions can interrupt the Transition.  
[offset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-offset.html) | The time at which the destination state will start.  
[orderedInterruption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-orderedInterruption.html) | The Transition can be interrupted by a transition that has a higher priority.  
### Constructors
Constructor | Description  
---|---  
[AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition-ctor.html) | Creates a new animator state transition.  
### Inherited Members
### Properties
Property | Description  
---|---  
[conditions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase-conditions.html) |  AnimatorCondition conditions that need to be met for a transition to happen.  
[destinationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase-destinationState.html) | The destination state of the transition.  
[destinationStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase-destinationStateMachine.html) | The destination state machine of the transition.  
[isExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase-isExit.html) | Is the transition destination the exit of the current state machine.  
[mute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase-mute.html) | Mutes the transition. The transition will never occur.  
[solo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase-solo.html) | Mutes all other transitions in the source state.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[AddCondition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase.AddCondition.html) | Utility function to add a condition to a transition.  
[RemoveCondition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase.RemoveCondition.html) | Utility function to remove a condition from the transition.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
