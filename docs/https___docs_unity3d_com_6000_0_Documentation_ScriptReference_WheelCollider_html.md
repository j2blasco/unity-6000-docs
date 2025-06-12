* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html

# WheelCollider
class in UnityEngine
/
Inherits from:[Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)
/
Implemented in:[UnityEngine.VehiclesModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.VehiclesModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html "Go to WheelCollider Component in the Manual")
### Description
A special collider for vehicle wheels.
Wheel collider is used to model vehicle wheels. It simulates a spring and damper suspension setup, and uses a slip based tire friction model to calculate wheel contact forces.  
  
Wheel's collision detection is performed by casting a ray from [center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-center.html) downwards the local y-axis. The wheel has a [radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-radius.html) and can extend downwards by [suspensionDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-suspensionDistance.html) amount.  
  
The wheel is controlled with [motorTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-motorTorque.html), [brakeTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-brakeTorque.html) and [steerAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-steerAngle.html) properties.  
  
Wheel collider computes friction separately from the rest of physics engine, using a slip based friction model. This allows for more realistic behaviour, but makes wheel colliders ignore standard [PhysicsMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial.html) settings. Simulation of different road materials is done by changing the [forwardFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-forwardFriction.html) and [sidewaysFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-sidewaysFriction.html) based on what material the wheel is hitting. Additional resources: [GetGroundHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.GetGroundHit.html) and [WheelFrictionCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelFrictionCurve.html).
### Properties
Property | Description  
---|---  
[brakeTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-brakeTorque.html) | Brake torque expressed in Newton metres.  
[center](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-center.html) | The center of the wheel, measured in the object's local space.  
[forceAppPointDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-forceAppPointDistance.html) | Application point of the suspension and tire forces measured from the base of the resting wheel.  
[forwardFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-forwardFriction.html) | Properties of tire friction in the direction the wheel is pointing in.  
[isGrounded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-isGrounded.html) | Indicates whether the wheel currently collides with something (Read Only).  
[mass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-mass.html) | The mass of the wheel, expressed in kilograms. Must be larger than zero. Typical values would be in range (20,80).  
[motorTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-motorTorque.html) | Motor torque on the wheel axle expressed in Newton metres. Positive or negative depending on direction.  
[radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-radius.html) | The radius of the wheel, measured in local space.  
[rotationSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-rotationSpeed.html) | Rotation speed of the wheel, measured in degrees per second.  
[rpm](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-rpm.html) | Current wheel axle rotation speed, in rotations per minute (Read Only).  
[sidewaysFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-sidewaysFriction.html) | Properties of tire friction in the sideways direction.  
[sprungMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-sprungMass.html) | The mass supported by this WheelCollider.  
[steerAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-steerAngle.html) | Steering angle in degrees, always around the local y-axis.  
[suspensionDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-suspensionDistance.html) | Maximum extension distance of wheel suspension, measured in local space.  
[suspensionExpansionLimited](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-suspensionExpansionLimited.html) | Limits the expansion velocity of the Wheel Collider's suspension. If you set this property on a Rigidbody that has several Wheel Colliders, such as a vehicle, then it affects all other Wheel Colliders on the Rigidbody.  
[suspensionSpring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-suspensionSpring.html) | The parameters of wheel's suspension. The suspension attempts to reach a target position by applying a linear force and a damping force.  
[wheelDampingRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-wheelDampingRate.html) | The damping rate of the wheel. Must be larger than zero.  
### Public Methods
Method | Description  
---|---  
[ConfigureVehicleSubsteps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.ConfigureVehicleSubsteps.html) | Configure vehicle sub-stepping parameters.  
[GetGroundHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.GetGroundHit.html) | Gets ground collision data for the wheel.  
[GetWorldPose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.GetWorldPose.html) | Gets the world space pose of the wheel accounting for ground contact, suspension limits, steer angle, and rotation angle (angles in degrees).  
[ResetSprungMasses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.ResetSprungMasses.html) | Reset the sprung masses of the vehicle.  
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
