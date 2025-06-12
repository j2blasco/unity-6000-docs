* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html

# StateMachineBehaviour
class in UnityEngine
/
Inherits from:[ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
StateMachineBehaviour is a component that can be added to a state machine state. It's the base class any script on a state must derive from.
State machines can have up to three different active states at the same time: the current state, the next state and the interrupted state.  
The state machine always has a current state. When the state machine transitions to a new state, a "next state" is added. Once the transition is complete, the current state is terminated and the next state becomes the new current state.  
If an ongoing transition is interrupted by a transition to a new state, then the next state becomes the interrupted state and the state targeted by the new transition is now the next state. The current state will remain the same until all interrupted transitions have completed. Once the last transition is complete and there are no more interruptions, the current and interrupted states are terminated, and the next state becomes the new current state.  
  
StateMachineBehaviour has some predefined state-related messages that you can implement:[OnStateEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateEnter.html), [OnStateExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateExit.html), [OnStateIK](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateIK.html), [OnStateMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMove.html), [OnStateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateUpdate.html).  
Whenever appropriate, these messages will be invoked for the active states mentioned above in the following order: current state, then interrupted state, then next state.  
See the description of each message for more information.  
  
StateMachineBehaviour also has some predefined messages related to transitions in and out of state machines:  
[OnStateMachineEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineEnter.html), [OnStateMachineExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineExit.html).  
These are invoked whenever a state machine transition is taken.  
  
**Layer considerations** :  
If an [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html) contains sychronized layers, the messages may be invoked multiple times for a single state. In that situation, the messages will be invoked once per synchronized layer that contains the state, in ascending order.  
  
**Additional considerations** :  
By default the Animator instantiates a new instance of each behaviour defined in the controller. If you wish to share behaviour instances, use the class attribute [SharedBetweenAnimatorsAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SharedBetweenAnimatorsAttribute.html) to control how behaviours are instantiated. 
```
using UnityEngine;  
  
public class AttackBehaviour : StateMachineBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) particle;
    public float radius;
    public float power;  
  
    protected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) clone;  
  
    override public void OnStateEnter(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        clone = Instantiate(particle, animator.rootPosition, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html)) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
        Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rb = clone.GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        rb.AddExplosionForce(power, animator.rootPosition, radius, 3.0f);
    }  
  
    override public void OnStateExit(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        Destroy(clone);
    }  
  
    override public void OnStateUpdate(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("On Attack Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) ");
    }  
  
    override public void OnStateMove(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("On Attack Move ");
    }  
  
    override public void OnStateIK(Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, AnimatorStateInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorStateInfo.html) stateInfo, int layerIndex)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("On Attack IK ");
    }
}

```

### Public Methods
Method | Description  
---|---  
[OnStateMachineEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineEnter.html) | Invoked on the first update frame when taking a transition into a state machine. Implement this message to influence the entry transition into the sub-state machine.  
[OnStateMachineExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMachineExit.html) | Invoked on the last update frame when taking a transition out of a StateMachine. Implement this message to influence the exit transition out of the sub-state machine  
### Messages
Message | Description  
---|---  
[OnStateEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateEnter.html) | Invoked on the first update frame when a state machine evaluates this state. Implement this message to react to a new state starting.  
[OnStateExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateExit.html) | Invoked on the last update frame when a state machine evaluates this state. Implement this message to react to a state ending.  
[OnStateIK](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateIK.html) | Invoked during the Animator IK pass. Implement this message to modify the result of the animation after the evaluation of the state machine on a state by state basis.  
[OnStateMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateMove.html) | Invoked during the Animator Root Motion pass. Implement this message to modify the result of the animation root motion on a state by state basis.  
[OnStateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StateMachineBehaviour.OnStateUpdate.html) | Invoked on each update frame except for the first and last frame. Implement this message to execute custom logic on a state by state basis.  
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
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
* * *
