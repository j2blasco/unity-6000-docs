* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainCollider.html

# TerrainCollider
class in UnityEngine
/
Inherits from:[Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)
/
Implemented in:[UnityEngine.TerrainPhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.TerrainPhysicsModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainCollider.html "Go to TerrainCollider Component in the Manual")
### Description
A heightmap based collider.
Additional resources: [SphereCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html), [CapsuleCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsuleCollider.html), [PhysicsMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial.html), [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).
### Properties
Property | Description  
---|---  
[terrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainCollider-terrainData.html) | The terrain that stores the heightmap.  
### Inherited Members
### Properties
Property | Description  
---|---  
[attachedArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-attachedArticulationBody.html) | The articulation body the collider is attached to.  
[attachedRigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-attachedRigidbody.html) | The rigidbody the collider is attached to.  
[bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-bounds.html) | The world space bounding volume of the collider (Read Only).  
[contactOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-contactOffset.html) | Contact offset value of this collider.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-enabled.html) | Enabled Colliders will collide with other Colliders, disabled Colliders won't.  
[excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-excludeLayers.html) | The additional layers that this Collider should exclude when deciding if the Collider can contact another Collider.  
[GeometryHolder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.GeometryHolder.html) | The structure holding the geometric shape of the collider and its type. (Read Only)  
[hasModifiableContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-hasModifiableContacts.html) | Specify whether this Collider's contacts are modifiable or not.  
[includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-includeLayers.html) | The additional layers that this Collider should include when deciding if the Collider can contact another Collider.  
[isTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-isTrigger.html) | Specify if this collider is configured as a trigger.  
[layerOverridePriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-layerOverridePriority.html) | A decision priority assigned to this Collider used when there is a conflicting decision on whether a Collider can contact another Collider.  
[material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-material.html) | The material used by the collider.  
[providesContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-providesContacts.html) | Whether or not this Collider generates contacts for Physics.ContactEvent.  
[sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-sharedMaterial.html) | The shared physics material of this collider.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[ClosestPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.ClosestPoint.html) | The closest point on the collider given a specified location.  
[ClosestPointOnBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.ClosestPointOnBounds.html) | The closest point to the bounding box of the attached collider.  
[GetGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.GetGeometry.html) | Returns the geometric shape of the collider of the requested type.  
[Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.Raycast.html) | Casts a Ray that ignores all Colliders except this one.  
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
[OnCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionEnter.html) | OnCollisionEnter is called when this collider/rigidbody has begun touching another rigidbody/collider.  
[OnCollisionExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionExit.html) | OnCollisionExit is called when this collider/rigidbody has stopped touching another rigidbody/collider.  
[OnCollisionStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnCollisionStay.html) | OnCollisionStay is called once per frame for every Collider or Rigidbody that touches another Collider or Rigidbody.  
[OnTriggerEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerEnter.html) | Called when a Collider with the Collider.isTrigger property overlaps another Collider.  
[OnTriggerExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerExit.html) | OnTriggerExit is called when the Collider other has stopped touching the trigger.  
[OnTriggerStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.OnTriggerStay.html) | OnTriggerStay is called almost all the frames for every Collider other that is touching the trigger. The function is on the physics timer so it won't necessarily run every frame.  
* * *
