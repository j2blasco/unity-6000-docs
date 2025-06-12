* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html

# AnimatorState
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
States are the basic building blocks of a state machine. Each state contains a Motion ( AnimationClip or BlendTree) which will play while the character is in that state. When an event in the game triggers a state transition, the character will be left in a new state whose animation sequence will then take over.
### Properties
Property | Description  
---|---  
[behaviours](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-behaviours.html) | The Behaviour list assigned to this state.  
[cycleOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-cycleOffset.html) | Offset at which the animation loop starts. Useful for synchronizing looped animations. Units is normalized time.  
[cycleOffsetParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-cycleOffsetParameter.html) | The animator controller parameter that drives the cycle offset value.  
[cycleOffsetParameterActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-cycleOffsetParameterActive.html) | Define if the cycle offset value is driven by an Animator controller parameter or by the value set in the editor.  
[iKOnFeet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-iKOnFeet.html) | Should Foot IK be respected for this state.  
[mirror](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-mirror.html) | Whether the animation state is mirrored.  
[mirrorParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-mirrorParameter.html) | The animator controller parameter that drives the mirror value.  
[mirrorParameterActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-mirrorParameterActive.html) | Define if the mirror value is driven by an Animator controller parameter or by the value set in the editor.  
[motion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-motion.html) | The motion assigned to this state.  
[nameHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-nameHash.html) | The hashed name of the state.  
[speed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-speed.html) | The default speed of the motion.  
[speedParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-speedParameter.html) | The animator controller parameter that drives the speed value.  
[speedParameterActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-speedParameterActive.html) | Define if the speed value is driven by an Animator controller parameter or by the value set in the editor.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-tag.html) | A tag can be used to identify a state.  
[timeParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-timeParameter.html) | If timeParameterActive is true, the value of this Parameter will be used instead of normalized time.  
[timeParameterActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-timeParameterActive.html) | If true, use value of given Parameter as normalized time.  
[transitions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-transitions.html) | The transitions that are going out of the state.  
[writeDefaultValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState-writeDefaultValues.html) | Whether or not the AnimatorStates writes back the default values for properties that are not animated by its Motion.  
### Public Methods
Method | Description  
---|---  
[AddExitTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.AddExitTransition.html) | Utility function to add an outgoing transition to the exit of the state's parent state machine.  
[AddStateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.AddStateMachineBehaviour.html) | Adds a state machine behaviour class of type T to the AnimatorState. Note that there is no corresponding "Remove" method. To remove a state machine behaviour, use Object.Destroy.  
[AddTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.AddTransition.html) | Utility function to add an outgoing transition to the destination state.  
[RemoveTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.RemoveTransition.html) | Utility function to remove a transition from the state.  
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
