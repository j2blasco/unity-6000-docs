* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AreaEffector2D.html

# AreaEffector2D
class in UnityEngine
/
Inherits from:[Effector2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Effector2D.html)
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
Applies forces within an area.
When the source [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is a trigger, the effector will apply forces whenever the target [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) overlaps the source. When the source [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) isn't a trigger, the effector will apply forces whenever the target [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is in contact with the source only.  
  
This effector is designed primarily to work with source [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are set as triggers so that target [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) can overlap the defined area.
### Properties
Property | Description  
---|---  
[angularDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AreaEffector2D-angularDrag.html) | The angular drag to apply to rigid-bodies.  
[drag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AreaEffector2D-drag.html) | The linear drag to apply to rigid-bodies.  
[forceAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AreaEffector2D-forceAngle.html) | The angle of the force to be applied.  
[forceMagnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AreaEffector2D-forceMagnitude.html) | The magnitude of the force to be applied.  
[forceTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AreaEffector2D-forceTarget.html) | The target for where the effector applies any force.  
[forceVariation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AreaEffector2D-forceVariation.html) | The variation of the magnitude of the force to be applied.  
[useGlobalAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AreaEffector2D-useGlobalAngle.html) | Should the forceAngle use global space?  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[colliderMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Effector2D-colliderMask.html) | The mask used to select specific layers allowed to interact with the effector.  
[useColliderMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Effector2D-useColliderMask.html) | Should the collider-mask be used or the global collision matrix?  
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
