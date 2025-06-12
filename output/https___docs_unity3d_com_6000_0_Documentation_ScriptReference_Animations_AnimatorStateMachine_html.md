* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html

# AnimatorStateMachine
class in UnityEditor.Animations
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
A graph controlling the interaction of states. Each state references a motion.
### Properties
Property | Description  
---|---  
[anyStatePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-anyStatePosition.html) | The position of the AnyState node.  
[anyStateTransitions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-anyStateTransitions.html) | The list of AnyState transitions.  
[behaviours](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-behaviours.html) | The Behaviour list assigned to this state machine.  
[defaultState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-defaultState.html) | The state that the state machine will be in when it starts.  
[entryPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-entryPosition.html) | The position of the entry node.  
[entryTransitions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-entryTransitions.html) | The list of entry transitions in the state machine.  
[exitPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-exitPosition.html) | The position of the exit node.  
[parentStateMachinePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-parentStateMachinePosition.html) | The position of the parent state machine node. Only valid when in a hierachic state machine.  
[stateMachines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-stateMachines.html) | The list of sub state machines.  
[states](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine-states.html) | The list of states.  
### Public Methods
Method | Description  
---|---  
[AddAnyStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.AddAnyStateTransition.html) | Utility function to add an AnyState transition to the specified state or statemachine.  
[AddEntryTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.AddEntryTransition.html) | Utility function to add an incoming transition to the exit of it's parent state machine.  
[AddState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.AddState.html) | Utility function to add a state to the state machine.  
[AddStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.AddStateMachine.html) | Utility function to add a state machine to the state machine.  
[AddStateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.AddStateMachineBehaviour.html) | Adds a state machine behaviour class of type T to the AnimatorStateMachine. Note that there is no corresponding "Remove" method. To remove a state machine behaviour, use Object.Destroy.  
[AddStateMachineExitTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.AddStateMachineExitTransition.html) | Utility function to add an outgoing transition from the source state machine to the exit of it's parent state machine.  
[AddStateMachineTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.AddStateMachineTransition.html) | Utility function to add an outgoing transition from the source state machine to the destination.  
[GetStateMachineTransitions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.GetStateMachineTransitions.html) | Gets the list of all outgoing state machine transitions from given state machine.  
[MakeUniqueStateMachineName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.MakeUniqueStateMachineName.html) | Makes a unique state machine name in the context of the parent state machine.  
[MakeUniqueStateName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.MakeUniqueStateName.html) | Makes a unique state name in the context of the parent state machine.  
[RemoveAnyStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.RemoveAnyStateTransition.html) | Utility function to remove an AnyState transition from the state machine.  
[RemoveEntryTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.RemoveEntryTransition.html) | Utility function to remove an entry transition from the state machine.  
[RemoveState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.RemoveState.html) | Utility function to remove a state from the state machine.  
[RemoveStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.RemoveStateMachine.html) | Utility function to remove a state machine from its parent state machine.  
[RemoveStateMachineTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.RemoveStateMachineTransition.html) | Utility function to remove an outgoing transition from source state machine.  
[SetStateMachineTransitions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.SetStateMachineTransitions.html) | Sets the list of all outgoing state machine transitions from given state machine.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
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
