* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint.html

# CharacterJoint
class in UnityEngine
/
Inherits from:[Joint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.html)
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterJoint.html "Go to CharacterJoint Component in the Manual")
### Description
Character Joints are mainly used for Ragdoll effects.
They are an extended ball-socket joint which allows you to limit the joint on each axis.
### Properties
Property | Description  
---|---  
[enableProjection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-enableProjection.html) | Brings violated constraints back into alignment even when the solver fails.  
[highTwistLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-highTwistLimit.html) | The upper limit around the primary axis of the character joint.  
[lowTwistLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-lowTwistLimit.html) | The lower limit around the primary axis of the character joint.  
[projectionAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-projectionAngle.html) | Set the angular tolerance threshold (in degrees) for projection.  
[projectionDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-projectionDistance.html) | Set the linear tolerance threshold for projection.  
[swing1Limit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-swing1Limit.html) | The angular limit of rotation (in degrees) around the primary axis of the character joint.  
[swing2Limit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-swing2Limit.html) | The angular limit of rotation (in degrees) around the primary axis of the character joint.  
[swingAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-swingAxis.html) | The secondary axis around which the joint can rotate.  
[swingLimitSpring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-swingLimitSpring.html) | The configuration of the spring attached to the swing limits of the joint.  
[twistLimitSpring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterJoint-twistLimitSpring.html) | The configuration of the spring attached to the twist limits of the joint.  
### Inherited Members
### Properties
Property | Description  
---|---  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[anchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-anchor.html) | The Position of the anchor around which the joints motion is constrained.  
[autoConfigureConnectedAnchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-autoConfigureConnectedAnchor.html) | Should the connectedAnchor be calculated automatically?  
[axis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-axis.html) | The Direction of the axis around which the body is constrained.  
[breakForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-breakForce.html) | The force that needs to be applied for this joint to break.  
[breakTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-breakTorque.html) | The torque that needs to be applied for this joint to break. To be able to break, a joint must be _Locked_ or _Limited_ on the axis of rotation where the torque is being applied. This means that some joints cannot break, such as an unconstrained Configurable Joint.  
[connectedAnchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-connectedAnchor.html) | Position of the anchor relative to the connected Rigidbody.  
[connectedArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-connectedArticulationBody.html) | A reference to an articulation body this joint connects to.  
[connectedBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-connectedBody.html) | A reference to another rigidbody this joint connects to.  
[connectedMassScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-connectedMassScale.html) | The scale to apply to the inverse mass and inertia tensor of the connected body prior to solving the constraints.  
[currentForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-currentForce.html) | The force applied by the solver to satisfy all constraints.  
[currentTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-currentTorque.html) | The torque applied by the solver to satisfy all constraints.  
[enableCollision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-enableCollision.html) | Enable collision between bodies connected with the joint.  
[enablePreprocessing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-enablePreprocessing.html) | Toggle preprocessing for this joint.  
[massScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-massScale.html) | The scale to apply to the inverse mass and inertia tensor of the body prior to solving the constraints.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
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
### Messages
Message | Description  
---|---  
[OnJointBreak](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.OnJointBreak.html) | Called when a joint attached to the same game object broke.  
* * *
