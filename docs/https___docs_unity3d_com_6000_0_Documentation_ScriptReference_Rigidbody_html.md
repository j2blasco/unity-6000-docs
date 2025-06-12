* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html

# Rigidbody
class in UnityEngine
/
Inherits from:[Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
### Description
Control of an object's position through physics simulation.
Adding a Rigidbody component to an object will put its motion under the control of Unity's physics engine. Even without adding any code, a Rigidbody object will be pulled downward by gravity and will react to collisions with incoming objects if the right [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component is also present.  
  
The Rigidbody also has a scripting API that lets you apply forces to the object and control it in a physically realistic way. For example, a car's behaviour can be specified in terms of the forces applied by the wheels. Given this information, the physics engine can handle most other aspects of the car's motion, so it will accelerate realistically and respond correctly to collisions.  
  
In a script, the [FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) function is recommended as the place to apply forces and change Rigidbody settings (as opposed to [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html), which is used for most other frame update tasks). The reason for this is that physics updates are carried out in measured time steps that don't coincide with the frame update. FixedUpdate is called immediately before each physics update and so any changes made there will be processed directly.  
  
A common problem when starting out with Rigidbodies is that the game physics appears to run in "slow motion". This is actually due to the scale used for your models. The default gravity settings assume that one world unit corresponds to one metre of distance. With non-physical games, it doesn't make much difference if your models are all 100 units long but when using physics, they will be treated as very large objects. If a large scale is used for objects that are supposed to be small, they will appear to fall very slowly - the physics engine thinks they are very large objects falling over very large distances. With this in mind, be sure to keep your objects more or less at their scale in real life (so a car should be about 4 units = 4 metres, for example).
### Properties
Property | Description  
---|---  
[angularDamping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-angularDamping.html) | The angular damping of the object.  
[angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-angularVelocity.html) | The angular velocity vector of the rigidbody measured in radians per second.  
[automaticCenterOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-automaticCenterOfMass.html) | Whether or not to calculate the center of mass automatically.  
[automaticInertiaTensor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-automaticInertiaTensor.html) | Whether or not to calculate the inertia tensor automatically.  
[centerOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-centerOfMass.html) | The center of mass relative to the transform's origin.  
[collisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-collisionDetectionMode.html) | The Rigidbody's collision detection mode.  
[constraints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-constraints.html) | Controls which degrees of freedom are allowed for the simulation of this Rigidbody.  
[detectCollisions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-detectCollisions.html) | Should collision detection be enabled? (By default always enabled).  
[excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-excludeLayers.html) | The additional layers that all Colliders attached to this Rigidbody should exclude when deciding if the Collider can come into contact with another Collider.  
[freezeRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-freezeRotation.html) | Controls whether physics will change the rotation of the object.  
[includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-includeLayers.html) | The additional layers that all Colliders attached to this Rigidbody should include when deciding if the Collider can come into contact with another Collider.  
[inertiaTensor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-inertiaTensor.html) | The inertia tensor of this body, defined as a diagonal matrix in a reference frame positioned at this body's center of mass and rotated by Rigidbody.inertiaTensorRotation.  
[inertiaTensorRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-inertiaTensorRotation.html) | The rotation of the inertia tensor.  
[interpolation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-interpolation.html) | Interpolation provides a way to manage the appearance of jitter in the movement of your Rigidbody GameObjects at run time.  
[isKinematic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-isKinematic.html) | Controls whether physics affects the rigidbody.  
[linearDamping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-linearDamping.html) | The linear damping of the Rigidbody linear velocity.  
[linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-linearVelocity.html) | The linear velocity vector of the rigidbody. It represents the rate of change of Rigidbody position.  
[mass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-mass.html) | The mass of the rigidbody.  
[maxAngularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-maxAngularVelocity.html) | The maximum angular velocity of the rigidbody measured in radians per second. (Default 7) range { 0, infinity }.  
[maxDepenetrationVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-maxDepenetrationVelocity.html) | Maximum velocity of a rigidbody when moving out of penetrating state.  
[maxLinearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-maxLinearVelocity.html) | The maximum linear velocity of the rigidbody measured in meters per second.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-position.html) | The position of the rigidbody.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-rotation.html) | The rotation of the Rigidbody.  
[sleepThreshold](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-sleepThreshold.html) | The mass-normalized energy threshold, below which objects start going to sleep.  
[solverIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-solverIterations.html) | The solverIterations determines how accurately Rigidbody joints and collision contacts are resolved. Overrides Physics.defaultSolverIterations. Must be positive.  
[solverVelocityIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-solverVelocityIterations.html) | The solverVelocityIterations affects how how accurately Rigidbody joints and collision contacts are resolved. Overrides Physics.defaultSolverVelocityIterations. Must be positive.  
[useGravity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-useGravity.html) | Controls whether gravity affects this rigidbody.  
[worldCenterOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-worldCenterOfMass.html) | The center of mass of the rigidbody in world space (Read Only).  
### Public Methods
Method | Description  
---|---  
[AddExplosionForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddExplosionForce.html) | Applies a force to a rigidbody that simulates explosion effects.  
[AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddForce.html) | Adds a force to the Rigidbody.  
[AddForceAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddForceAtPosition.html) | Applies force at position. As a result this will apply a torque and force on the object.  
[AddRelativeForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddRelativeForce.html) | Adds a force to the rigidbody relative to its coordinate system.  
[AddRelativeTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddRelativeTorque.html) | Adds a torque to the rigidbody relative to its coordinate system.  
[AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddTorque.html) | Adds a torque to the rigidbody.  
[ClosestPointOnBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.ClosestPointOnBounds.html) | The closest point to the bounding box of the attached colliders.  
[GetAccumulatedForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.GetAccumulatedForce.html) | Returns the force that the Rigidbody has accumulated before the simulation step.  
[GetAccumulatedTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.GetAccumulatedTorque.html) | Returns the torque that the Rigidbody has accumulated before the simulation step.  
[GetPointVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.GetPointVelocity.html) | The velocity of the rigidbody at the point worldPoint in global space.  
[GetRelativePointVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.GetRelativePointVelocity.html) | The velocity relative to the rigidbody at the point relativePoint.  
[IsSleeping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.IsSleeping.html) | Is the rigidbody sleeping?  
[Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.Move.html) | Moves the Rigidbody to position and rotates the Rigidbody to rotation.  
[MovePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.MovePosition.html) | Moves the kinematic Rigidbody towards position.  
[MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.MoveRotation.html) | Rotates the rigidbody to rotation.  
[PublishTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.PublishTransform.html) | Applies the position and rotation of the Rigidbody to the corresponding Transform component.  
[ResetCenterOfMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.ResetCenterOfMass.html) | Reset the center of mass of the rigidbody.  
[ResetInertiaTensor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.ResetInertiaTensor.html) | Reset the inertia tensor value and rotation.  
[SetDensity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.SetDensity.html) | Sets the mass based on the attached colliders assuming a constant density.  
[Sleep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.Sleep.html) | Forces a rigidbody to sleep until woken up.  
[SweepTest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.SweepTest.html) | Tests if a rigidbody would collide with anything, if it was moved through the Scene.  
[SweepTestAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.SweepTestAll.html) | Like Rigidbody.SweepTest, but returns all hits.  
[WakeUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.WakeUp.html) | Forces a rigidbody to wake up.  
### Messages
Message | Description  
---|---  
[OnCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.OnCollisionEnter.html) | OnCollisionEnter is called when this collider/rigidbody has begun touching another rigidbody/collider.  
[OnCollisionExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.OnCollisionExit.html) | OnCollisionExit is called when this collider/rigidbody has stopped touching another rigidbody/collider.  
[OnCollisionStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.OnCollisionStay.html) | OnCollisionStay is called once per frame for every Collider or Rigidbody that touches another Collider or Rigidbody.  
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
