* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html

# Cloth
class in UnityEngine
/
Inherits from:[Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)
/
Implemented in:[UnityEngine.ClothModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ClothModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html "Go to Cloth Component in the Manual")
### Description
The Cloth class provides an interface to cloth simulation physics.
### Properties
Property | Description  
---|---  
[bendingStiffness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-bendingStiffness.html) | Bending stiffness of the cloth.  
[capsuleColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-capsuleColliders.html) | An array of CapsuleColliders which this Cloth instance should collide with.  
[clothSolverFrequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-clothSolverFrequency.html) | Number of cloth solver iterations per second.  
[coefficients](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-coefficients.html) | The cloth skinning coefficients used to set up how the cloth interacts with the skinned mesh.  
[collisionMassScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-collisionMassScale.html) | How much to increase mass of colliding particles.  
[damping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-damping.html) | Damp cloth motion.  
[enableContinuousCollision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-enableContinuousCollision.html) | Enable continuous collision to improve collision stability.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-enabled.html) | Is this cloth enabled?  
[externalAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-externalAcceleration.html) | A constant, external acceleration applied to the cloth.  
[friction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-friction.html) | The friction of the cloth when colliding with the character.  
[normals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-normals.html) | The current normals of the cloth object.  
[randomAcceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-randomAcceleration.html) | A random, external acceleration applied to the cloth.  
[selfCollisionDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-selfCollisionDistance.html) | Minimum distance at which two cloth particles repel each other (default: 0.0).  
[selfCollisionStiffness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-selfCollisionStiffness.html) | Self-collision stiffness defines how strong the separating impulse should be for colliding particles.  
[sleepThreshold](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-sleepThreshold.html) | Cloth's sleep threshold.  
[sphereColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-sphereColliders.html) | An array of ClothSphereColliderPairs which this Cloth instance should collide with.  
[stiffnessFrequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-stiffnessFrequency.html) | Sets the stiffness frequency parameter.  
[stretchingStiffness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-stretchingStiffness.html) | Stretching stiffness of the cloth.  
[useGravity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-useGravity.html) | Should gravity affect the cloth simulation?  
[useTethers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-useTethers.html) | Use Tether Anchors.  
[useVirtualParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-useVirtualParticles.html) | Add one virtual particle per triangle to improve collision stability.  
[vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-vertices.html) | The current vertex positions of the cloth object.  
[worldAccelerationScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-worldAccelerationScale.html) | How much world-space acceleration of the character will affect cloth vertices.  
[worldVelocityScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-worldVelocityScale.html) | How much world-space movement of the character will affect cloth vertices.  
### Public Methods
Method | Description  
---|---  
[ClearTransformMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.ClearTransformMotion.html) | Clear the pending transform changes from affecting the cloth simulation.  
[GetSelfAndInterCollisionIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.GetSelfAndInterCollisionIndices.html) | Get list of particles to be used for self and inter collision.  
[GetVirtualParticleIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.GetVirtualParticleIndices.html) | Get list of indices to be used when generating virtual particles.  
[GetVirtualParticleWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.GetVirtualParticleWeights.html) | Get weights to be used when generating virtual particles for cloth.  
[SetEnabledFading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.SetEnabledFading.html) | Fade the cloth simulation in or out.  
[SetSelfAndInterCollisionIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.SetSelfAndInterCollisionIndices.html) | This allows you to set the cloth indices used for self and inter collision.  
[SetVirtualParticleIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.SetVirtualParticleIndices.html) | Set indices to use when generating virtual particles.  
[SetVirtualParticleWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.SetVirtualParticleWeights.html) | Sets weights to be used when generating virtual particles for cloth.  
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
