* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint.html

# AimConstraint
class in UnityEngine.Animations
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
Leave feedback
  

Implements interfaces:[IConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IConstraint.html)
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
Constrains the orientation of an object relative to the position of one or more source objects, such that the object is facing the average position of the sources.
### Properties
Property | Description  
---|---  
[aimVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-aimVector.html) | The axis towards which the constrained object orients.  
[constraintActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-constraintActive.html) | Activates or deactivates the constraint.  
[locked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-locked.html) | Locks the offset and rotation at rest.  
[rotationAtRest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-rotationAtRest.html) | The rotation used when the sources have a total weight of 0.  
[rotationAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-rotationAxis.html) | The axes affected by the AimConstraint.  
[rotationOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-rotationOffset.html) | Represents an offset from the constrained orientation.  
[sourceCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-sourceCount.html) | The number of sources set on the component (read-only).  
[upVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-upVector.html) | The up vector.  
[weight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-weight.html) | The weight of the constraint component.  
[worldUpObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-worldUpObject.html) | The world up object, used to calculate the world up vector when the world up Type is AimConstraint.WorldUpType.ObjectUp or AimConstraint.WorldUpType.ObjectRotationUp.  
[worldUpType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-worldUpType.html) | The type of the world up vector.  
[worldUpVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint-worldUpVector.html) | The world up Vector used when the world up type is AimConstraint.WorldUpType.Vector or AimConstraint.WorldUpType.ObjectRotationUp.  
### Public Methods
Method | Description  
---|---  
[AddSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint.AddSource.html) | Adds a constraint source.  
[GetSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint.GetSource.html) | Gets a constraint source by index.  
[GetSources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint.GetSources.html) | Gets the list of sources.  
[RemoveSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint.RemoveSource.html) | Removes a source from the component.  
[SetSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint.SetSource.html) | Sets a source at a specified index.  
[SetSources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AimConstraint.SetSources.html) | Sets the list of sources on the component.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
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
* * *
