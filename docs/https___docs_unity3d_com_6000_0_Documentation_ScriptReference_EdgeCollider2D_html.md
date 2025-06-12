* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html

# EdgeCollider2D
class in UnityEngine
/
Inherits from:[Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html)
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
Collider for 2D physics representing an arbitrary set of connected edges (lines) defined by its vertices.
Additional resources: [BoxCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html), [CircleCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CircleCollider2D.html), [PolygonCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.html).
### Properties
Property | Description  
---|---  
[adjacentEndPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-adjacentEndPoint.html) | Defines the position of a virtual point adjacent to the end point of the EdgeCollider2D.  
[adjacentStartPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-adjacentStartPoint.html) | Defines the position of a virtual point adjacent to the start point of the EdgeCollider2D.  
[edgeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-edgeCount.html) | Gets the number of edges.  
[edgeRadius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-edgeRadius.html) | Controls the radius of all edges created by the collider.  
[pointCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-pointCount.html) | Gets the number of points.  
[points](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-points.html) | Get or set the points defining multiple continuous edges.  
[useAdjacentEndPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-useAdjacentEndPoint.html) | Set this to true to use the adjacentEndPoint to form the collision normal that is used to calculate the collision response when a collision occurs at the Edge Collider's end point. Set this to false to not use the adjacentEndPoint, and the collision normal becomes the direction of motion of the collision.  
[useAdjacentStartPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-useAdjacentStartPoint.html) | Set this to true to use the adjacentStartPoint to form the collision normal that is used to calculate the collision response when a collision occurs at the Edge Collider's start point. Set this to false to not use the adjacentStartPoint, and the collision normal becomes the direction of motion of the collision.  
### Public Methods
Method | Description  
---|---  
[GetPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.GetPoints.html) | Gets all the points that define a set of continuous edges.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.Reset.html) | Reset to a single edge consisting of two points.  
[SetPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.SetPoints.html) | Sets all the points that define a set of continuous edges.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[attachedRigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-attachedRigidbody.html) | The Rigidbody2D attached to the Collider2D.  
[bounceCombine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-bounceCombine.html) | The bounciness combine mode used by the Collider2D.  
[bounciness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-bounciness.html) | The bounciness used by the Collider2D.  
[bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-bounds.html) | The world space bounding area of the collider.  
[callbackLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-callbackLayers.html) | The Layers that this Collider2D will report collision or trigger callbacks for during a contact with another Collider2D.  
[composite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-composite.html) | Get the CompositeCollider2D that is available to be attached to the collider.  
[compositeCapable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeCapable.html) | Indicates if this Collider2D is capable of being composited by the CompositeCollider2D.  
[compositeOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeOperation.html) | The composite operation to be used by a CompositeCollider2D.  
[compositeOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-compositeOrder.html) | The composite operation order to be used when a CompositeCollider2D is used.  
[contactCaptureLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-contactCaptureLayers.html) | The layers of other Collider2D involved in contacts with this Collider2D that will be captured.  
[density](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-density.html) | The density of the collider used to calculate its mass (when auto mass is enabled).  
[errorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-errorState.html) | The error state that indicates the state of the physics shapes the 2D Collider tried to create. (Read Only)  
[excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-excludeLayers.html) | The additional Layers that this Collider2D should exclude when deciding if a contact with another Collider2D should happen or not.  
[forceReceiveLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceReceiveLayers.html) | The Layers that this Collider2D can receive forces from during a Collision contact with another Collider2D.  
[forceSendLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceSendLayers.html) | The Layers that this Collider2D is allowed to send forces to during a Collision contact with another Collider2D.  
[friction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-friction.html) | The friction used by the Collider2D.  
[frictionCombine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-frictionCombine.html) | The friction combine mode used by the Collider2D.  
[includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-includeLayers.html) | The additional Layers that this Collider2D should include when deciding if a contact with another Collider2D should happen or not.  
[isTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-isTrigger.html) | Is this collider configured as a trigger?  
[layerOverridePriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-layerOverridePriority.html) | A decision priority assigned to this Collider2D used when there is a conflicting decision on whether a contact between itself and another Collision2D should happen or not.  
[localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-localToWorldMatrix.html) | The transformation matrix used to transform the Collider physics shapes to world space.  
[offset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-offset.html) | The local offset of the collider geometry.  
[shapeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-shapeCount.html) | The number of active PhysicsShape2D the Collider2D is currently using.  
[sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-sharedMaterial.html) | The PhysicsMaterial2D that is applied to this collider.  
[usedByEffector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-usedByEffector.html) | Whether the collider is used by an attached effector or not.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[Cast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Cast.html) | Casts the Collider shape into the Scene starting at the Collider position ignoring the Collider itself.  
[ClosestPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.ClosestPoint.html) | Returns a point on the perimeter of this Collider that is closest to the specified position.  
[CreateMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.CreateMesh.html) | Creates a planar Mesh that is identical to the area defined by the Collider2D geometry.  
[Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Distance.html) | Calculates the minimum separation of this collider against another collider.  
[GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) | Retrieves all contact points for this Collider.  
[GetShapeBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapeBounds.html) | Retrieves a list of Bounds for all PhysicsShape2D created by this Collider2D, and returns the combined Bounds of the retrieved list.  
[GetShapeHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapeHash.html) | Generates a simple hash value based upon the geometry of the Collider2D.  
[GetShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapes.html) | Gets all the PhysicsShape2D used by the Collider2D.  
[IsTouching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.IsTouching.html) | Check whether this collider is touching the collider or not.  
[IsTouchingLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.IsTouchingLayers.html) | Checks whether this collider is touching any colliders on the specified layerMask or not.  
[Overlap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Overlap.html) | Get a list of all Colliders that overlap this Collider.  
[OverlapPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OverlapPoint.html) | Check if a collider overlaps a point in space.  
[Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Raycast.html) | Casts a ray into the Scene that starts at the Collider position and ignores the Collider itself.  
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
[OnCollisionEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionEnter2D.html) | Sent when an incoming collider makes contact with this object's collider (2D physics only).  
[OnCollisionExit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionExit2D.html) | Sent when a collider on another object stops touching this object's collider (2D physics only).  
[OnCollisionStay2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnCollisionStay2D.html) | Sent each frame where a collider on another object is touching this object's collider (2D physics only).  
[OnTriggerEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerEnter2D.html) | Sent when another object enters a trigger collider attached to this object (2D physics only).  
[OnTriggerExit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerExit2D.html) | Sent when another object leaves a trigger collider attached to this object (2D physics only).  
[OnTriggerStay2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OnTriggerStay2D.html) | Sent each frame where another object is within a trigger collider attached to this object (2D physics only).  
* * *
