* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html

# AnimatorController
class in UnityEditor.Animations
/
Inherits from:[RuntimeAnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeAnimatorController.html)
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
The Animator Controller controls animation through layers with state machines, controlled by parameters.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Animations;
using System.Collections;  
  
// Create a menu item that causes a new controller and statemachine to be created.  
  
public class SM : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Create Controller")]
    static void CreateController()
    {
        // Creates the controller
        var controller = UnityEditor.Animations.AnimatorController.CreateAnimatorControllerAtPath("Assets/Mecanim/StateMachineTransitions.controller");  
  
        // Add parameters
        controller.AddParameter("TransitionNow", AnimatorControllerParameterType.Trigger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorControllerParameterType.Trigger.html));
        controller.AddParameter("Reset", AnimatorControllerParameterType.Trigger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorControllerParameterType.Trigger.html));
        controller.AddParameter("GotoB1", AnimatorControllerParameterType.Trigger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorControllerParameterType.Trigger.html));
        controller.AddParameter("GotoC", AnimatorControllerParameterType.Trigger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorControllerParameterType.Trigger.html));  
  
        // Add StateMachines
        var rootStateMachine = controller.layers[0].stateMachine;
        var stateMachineA = rootStateMachine.AddStateMachine("smA");
        var stateMachineB = rootStateMachine.AddStateMachine("smB");
        var stateMachineC = stateMachineB.AddStateMachine("smC");  
  
        // Add States[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.States.html)
        var stateA1 = stateMachineA.AddState("stateA1");
        var stateB1 = stateMachineB.AddState("stateB1");
        var stateB2 = stateMachineB.AddState("stateB2");
        stateMachineC.AddState("stateC1");
        var stateC2 = stateMachineC.AddState("stateC2"); // don’t add an entry transition, should entry to state by default  
  
        // Add Transitions
        var exitTransition = stateA1.AddExitTransition();
        exitTransition.AddCondition(UnityEditor.Animations.AnimatorConditionMode.If, 0, "TransitionNow");
        exitTransition.duration = 0;  
  
        var resetTransition = rootStateMachine.AddAnyStateTransition(stateA1);
        resetTransition.AddCondition(UnityEditor.Animations.AnimatorConditionMode.If, 0, "Reset");
        resetTransition.duration = 0;  
  
        var transitionB1 = stateMachineB.AddEntryTransition(stateB1);
        transitionB1.AddCondition(UnityEditor.Animations.AnimatorConditionMode.If, 0, "GotoB1");
        stateMachineB.AddEntryTransition(stateB2);
        stateMachineC.defaultState = stateC2;
        var exitTransitionC2 = stateC2.AddExitTransition();
        exitTransitionC2.AddCondition(UnityEditor.Animations.AnimatorConditionMode.If, 0, "TransitionNow");
        exitTransitionC2.duration = 0;  
  
        var stateMachineTransition = rootStateMachine.AddStateMachineTransition(stateMachineA, stateMachineC);
        stateMachineTransition.AddCondition(UnityEditor.Animations.AnimatorConditionMode.If, 0, "GotoC");
        rootStateMachine.AddStateMachineTransition(stateMachineA, stateMachineB);
    }
}

```

### Properties
Property | Description  
---|---  
[layers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController-layers.html) | The layers in the controller.  
[parameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController-parameters.html) | Parameters are used to communicate between scripting and the controller. They are used to drive transitions and blendtrees for example.  
### Constructors
Constructor | Description  
---|---  
[AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController-ctor.html) | Constructor.  
### Public Methods
Method | Description  
---|---  
[AddEffectiveStateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.AddEffectiveStateMachineBehaviour.html) | Adds a state machine behaviour class of a specific type to the AnimatorState for layer layerIndex. This method should be used when you are dealing with synchronized layer and would like to add a state machine behaviour on a synchronized layer. Note that there is no corresponding "Remove" method. To remove a state machine behaviour, use Object.Destroy.  
[AddLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.AddLayer.html) | Utility function to add a layer to the controller.  
[AddMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.AddMotion.html) | Utility function that creates a new state with the motion in it.  
[AddParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.AddParameter.html) | Utility function to add a parameter to the controller.  
[CreateBlendTreeInController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.CreateBlendTreeInController.html) | Creates a BlendTree in a new AnimatorState.  
[GetBehaviours](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.GetBehaviours.html) | Returns all StateMachineBehaviour that match type T or are derived from T.  
[GetStateEffectiveBehaviours](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.GetStateEffectiveBehaviours.html) | Gets the effective state machine behaviour list for the AnimatorState. Behaviours are either stored in the AnimatorStateMachine or in the AnimatorLayer's ovverrides. Use this function to get Behaviour list that is effectively used.  
[GetStateEffectiveMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.GetStateEffectiveMotion.html) | Gets the effective Motion for the AnimatorState. The Motion is either stored in the AnimatorStateMachine or in the AnimatorLayer's ovverrides. Use this function to get the Motion that is effectively used.  
[MakeUniqueLayerName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.MakeUniqueLayerName.html) | Creates a unique name for the layers.  
[MakeUniqueParameterName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.MakeUniqueParameterName.html) | Creates a unique name for the parameter.  
[RemoveLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.RemoveLayer.html) | Utility function to remove a layer from the controller.  
[RemoveParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.RemoveParameter.html) | Utility function to remove a parameter from the controller.  
[SetStateEffectiveBehaviours](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.SetStateEffectiveBehaviours.html) | Sets the effective state machine Behaviour list for the AnimatorState. The Behaviour list is either stored in the AnimatorStateMachine or in the AnimatorLayer's ovverrides. Use this function to set the Behaviour list that is effectively used.  
[SetStateEffectiveMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.SetStateEffectiveMotion.html) | Sets the effective Motion for the AnimatorState. The Motion is either stored in the AnimatorStateMachine or in the AnimatorLayer's ovverrides. Use this function to set the Motion that is effectively used.  
### Static Methods
Method | Description  
---|---  
[CreateAnimatorControllerAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.CreateAnimatorControllerAtPath.html) | Creates an AnimatorController at the given path.  
[CreateAnimatorControllerAtPathWithClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.CreateAnimatorControllerAtPathWithClip.html) | Creates an AnimatorController at the given path, and automatically create an AnimatorLayer with an AnimatorStateMachine that will add a State with the AnimationClip in it.  
[CreateStateMachineBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.CreateStateMachineBehaviour.html) | This function will create a StateMachineBehaviour instance based on the class define in this script.  
[FindStateMachineBehaviourContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.FindStateMachineBehaviourContext.html) | Use this function to retrieve the owner of this behaviour.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
[animationClips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeAnimatorController-animationClips.html) | Retrieves all AnimationClip used by the controller.  
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
