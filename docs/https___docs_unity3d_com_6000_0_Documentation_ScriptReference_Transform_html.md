* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html

# Transform
class in UnityEngine
/
Inherits from:[Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
### Description
Position, rotation and scale of an object.
Every object in a Scene has a Transform. It's used to store and manipulate the position, rotation and scale of the object. Every Transform can have a parent, which allows you to apply position, rotation and scale hierarchically. This is the hierarchy seen in the Hierarchy pane. They also support enumerators so you can loop through children using:
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Moves all transform children 10 units upwards!
    void Start()
    {
        foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) child in transform)
        {
            child.position += Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 10.0f;
        }
    }
}

```

Additional resources: [The component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html), [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html) class.
### Properties
Property | Description  
---|---  
[childCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-childCount.html) | The number of children the parent Transform has.  
[eulerAngles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-eulerAngles.html) | The rotation as Euler angles in degrees.  
[forward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-forward.html) | Returns a normalized vector representing the blue axis of the transform in world space.  
[hasChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-hasChanged.html) | Has the transform changed since the last time the flag was set to 'false'?  
[hierarchyCapacity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-hierarchyCapacity.html) | The transform capacity of the transform's hierarchy data structure.  
[hierarchyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-hierarchyCount.html) | The number of transforms in the transform's hierarchy data structure.  
[localEulerAngles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localEulerAngles.html) | The rotation as Euler angles in degrees relative to the parent transform's rotation.  
[localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html) | Position of the transform relative to the parent transform.  
[localRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localRotation.html) | The rotation of the transform relative to the transform rotation of the parent.  
[localScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localScale.html) | The scale of the transform relative to the GameObjects parent.  
[localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localToWorldMatrix.html) | Matrix that transforms a point from local space into world space (Read Only).  
[lossyScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-lossyScale.html) | The global scale of the object (Read Only).  
[parent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-parent.html) | The parent of the transform.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) | The world space position of the Transform.  
[right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-right.html) | The red axis of the transform in world space.  
[root](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-root.html) | Returns the topmost transform in the hierarchy.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html) | A Quaternion that stores the rotation of the Transform in world space.  
[up](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-up.html) | The green axis of the transform in world space.  
[worldToLocalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-worldToLocalMatrix.html) | Matrix that transforms a point from world space into local space (Read Only).  
### Public Methods
Method | Description  
---|---  
[DetachChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.DetachChildren.html) | Unparents all children.  
[Find](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Find.html) | Finds a child by name n and returns it.  
[GetChild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.GetChild.html) | Returns a transform child by index.  
[GetLocalPositionAndRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.GetLocalPositionAndRotation.html) | Gets the position and rotation of the Transform component in local space (that is, relative to its parent transform).  
[GetPositionAndRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.GetPositionAndRotation.html) | Gets the position and rotation of the Transform component in world space.  
[GetSiblingIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.GetSiblingIndex.html) | Gets the sibling index.  
[InverseTransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirection.html) | Transforms a direction from world space to local space. The opposite of Transform.TransformDirection.  
[InverseTransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformDirections.html) | Transforms multiple directions from world space to local space overwriting each original position with the transformed version. The opposite of Transform.TransformDirections.  
[InverseTransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoint.html) | Transforms position from world space to local space.  
[InverseTransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformPoints.html) | Transforms multiple positions from world space to local space overwriting each original position with the transformed version.  
[InverseTransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVector.html) | Transforms a vector from world space to local space. The opposite of Transform.TransformVector.  
[InverseTransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.InverseTransformVectors.html) | Transforms multiple vectors from world space to local space overwriting each original position with the transformed version. The opposite of Transform.TransformVectors.  
[IsChildOf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.IsChildOf.html) | Is this transform a child of parent?  
[LookAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.LookAt.html) | Rotates the transform so the forward vector points at /target/'s current position.  
[Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Rotate.html) | Use Transform.Rotate to rotate GameObjects in a variety of ways. The rotation is often provided as an Euler angle and not a Quaternion.  
[RotateAround](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.RotateAround.html) | Rotates the transform about axis passing through point in world coordinates by angle degrees.  
[SetAsFirstSibling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetAsFirstSibling.html) | Move the transform to the start of the local transform list.  
[SetAsLastSibling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetAsLastSibling.html) | Move the transform to the end of the local transform list.  
[SetLocalPositionAndRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetLocalPositionAndRotation.html) | Sets the position and rotation of the Transform component in local space (i.e. relative to its parent transform).  
[SetParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetParent.html) | Set the parent of the transform.  
[SetPositionAndRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetPositionAndRotation.html) | Sets the world space position and rotation of the Transform component.  
[SetSiblingIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetSiblingIndex.html) | Sets the sibling index.  
[TransformDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirection.html) | Transforms direction from local space to world space.  
[TransformDirections](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformDirections.html) | Transforms multiple directions from local space to world space overwriting each original direction with the transformed version.  
[TransformPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoint.html) | Transforms position from local space to world space.  
[TransformPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformPoints.html) | Transforms multiple points from local space to world space overwriting each original point with the transformed version.  
[TransformVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVector.html) | Transforms vector from local space to world space.  
[TransformVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.TransformVectors.html) | Transforms multiple vectors from local space to world space overwriting each original vector with the transformed version.  
[Translate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Translate.html) | Moves the transform in the direction and distance of translation.  
### Inherited Members
### Properties
Property | Description  
---|---  
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
