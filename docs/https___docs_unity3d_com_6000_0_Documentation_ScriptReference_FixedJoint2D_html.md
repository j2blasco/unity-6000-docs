* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FixedJoint2D.html

# FixedJoint2D
class in UnityEngine
/
Inherits from:[AnchoredJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnchoredJoint2D.html)
/
Implemented in:[UnityEngine.Physics2DModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Physics2DModule.html)
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
Connects two [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) together at their anchor points using a configurable spring.
### Properties
Property | Description  
---|---  
[dampingRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FixedJoint2D-dampingRatio.html) | The amount by which the spring force is reduced in proportion to the movement speed.  
[frequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FixedJoint2D-frequency.html) | The frequency at which the spring oscillates around the distance between the objects.  
[referenceAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FixedJoint2D-referenceAngle.html) | The angle referenced between the two bodies used as the constraint for the joint.  
### Inherited Members
### Properties
Property | Description  
---|---  
[anchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnchoredJoint2D-anchor.html) | The joint's anchor point on the object that has the joint component.  
[autoConfigureConnectedAnchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnchoredJoint2D-autoConfigureConnectedAnchor.html) | Should the connectedAnchor be calculated automatically?  
[connectedAnchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnchoredJoint2D-connectedAnchor.html) | The joint's anchor point on the second object (ie, the one which doesn't have the joint component).  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[attachedRigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-attachedRigidbody.html) | The Rigidbody2D attached to the Joint2D.  
[breakAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakAction.html) | The action to take when the joint breaks the breakForce or breakTorque.  
[breakForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakForce.html) | The force that needs to be applied for this joint to break.  
[breakTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakTorque.html) | The torque that needs to be applied for this joint to break.  
[connectedBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-connectedBody.html) | The Rigidbody2D object to which the other end of the joint is attached (ie, the object without the joint component).  
[enableCollision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-enableCollision.html) | Should the two Rigidbody2D connected with this joint collide with each other?  
[reactionForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-reactionForce.html) | Gets the reaction force of the joint.  
[reactionTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-reactionTorque.html) | Gets the reaction torque of the joint.  
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
[GetReactionForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.GetReactionForce.html) | Gets the reaction force of the joint given the specified timeStep.  
[GetReactionTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.GetReactionTorque.html) | Gets the reaction torque of the joint given the specified timeStep.  
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
[OnJointBreak2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.OnJointBreak2D.html) | Called when a Joint2D attached to the same game object breaks.  
* * *
