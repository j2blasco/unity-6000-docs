* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html

# ParticleSystem
class in UnityEngine
/
Inherits from:[Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)
/
Implemented in:[UnityEngine.ParticleSystemModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ParticleSystemModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html "Go to ParticleSystem Component in the Manual")
### Description
Script interface for the Built-in Particle System. Unity's powerful and versatile particle system implementation.
**General parameters**   
  
The Particle System's general parameters are kept inside a special Main module. These parameters are visible in the Inspector above all the other modules.  
  
In script, these parameters are accessible through [ParticleSystem.main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-main.html).  
  
**Accessing module properties**  
  
Particle System properties are grouped by the module they belong to, such as [ParticleSystem.noise](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-noise.html) and [ParticleSystem.emission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-emission.html). These properties are structs, but do not behave like normal C# structs. They are simply interfaces directly into the native code, so it is important to know how to use them, compared to a normal C# struct.  
  
The key difference is that it is not necessary to assign the struct back to the Particle System component. When you set any property on a module struct, Unity immediately assigns that value to the Particle System.  
  
Also, because each module is a struct, you must cache it in a local variable before you can assign any new values to the module. For example, instead of:  
`ParticleSystem.emission.enabled = true;    // Doesn't compile`  
write:  
`var emission = ParticleSystem.emission;    // Stores the module in a local variable`  
`emission.enabled = true;    // Applies the new value directly to the Particle System`  
  
  
**Module effect multipliers**  
  
Every module has special multiplier properties that allow you to change the overall effect of a curve without having to edit the curve itself. These multiplier properties are all named after the curve they affect - for instance ParticleSystem.emission.rateMultiplier controls the overall effect of ParticleSystem.emission.rate in a given system.  
  
**Constant value shorthand**  
  
Parameters support a shorthand notation for simple constant values. To set a constant value for a parameter, all you need to do is assign a number to it. It is not necessary to create a [MinMaxCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html) or [MinMaxGradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.html) object in the [ParticleSystemCurveMode.Constant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCurveMode.Constant.html) mode.  
  
For example, instead of:  
`var emission = ParticleSystem.emission;`  
`emission.rate = new ParticleSystem.MinMaxCurve(5.0f);`  
write:  
`var emission = ParticleSystem.emission;`  
`emission.rate = 5.0f;`  
  
**Performance note** : When setting properties on particle modules, the settings are passed immediately into native code. This gives the best performance. This means that setting properties on a module struct doesn't set something in script that requires setting back to the Particle System; it all happens automatically.  
  
Additional resources: [Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html).
### Properties
Property | Description  
---|---  
[collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-collision.html) | Script interface for the CollisionModule of a Particle System.  
[colorBySpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-colorBySpeed.html) | Script interface for the ColorByLifetimeModule of a Particle System.  
[colorOverLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-colorOverLifetime.html) | Script interface for the ColorOverLifetimeModule of a Particle System.  
[customData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-customData.html) | Script interface for the CustomDataModule of a Particle System.  
[emission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-emission.html) | Script interface for the EmissionModule of a Particle System.  
[externalForces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-externalForces.html) | Script interface for the ExternalForcesModule of a Particle System.  
[forceOverLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-forceOverLifetime.html) | Script interface for the ForceOverLifetimeModule of a Particle System.  
[has3DParticleRotations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-has3DParticleRotations.html) | Determines whether the Particle System rotates its particles around only the Z axis, or whether the system specifies separate values for the X, Y and Z axes.  
[hasNonUniformParticleSizes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-hasNonUniformParticleSizes.html) | Determines whether the Particle System uses a single value for the width and height (and depth, when using meshes), or if the system specifies different values for each axis.  
[inheritVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-inheritVelocity.html) | Script interface for the InheritVelocityModule of a Particle System.  
[isEmitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-isEmitting.html) | Determines whether the Particle System is emitting particles. A Particle System may stop emitting when its emission module has finished, it has been paused or if the system has been stopped using Stop with the StopEmitting flag. Resume emitting by calling Play.  
[isPaused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-isPaused.html) | Determines whether the Particle System is paused.  
[isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-isPlaying.html) | Determines whether the Particle System is playing.  
[isStopped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-isStopped.html) | Determines whether the Particle System is in the stopped state.  
[lifetimeByEmitterSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-lifetimeByEmitterSpeed.html) | Script interface for the Particle System Lifetime By Emitter Speed module.  
[lights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-lights.html) | Script interface for the LightsModule of a Particle System.  
[limitVelocityOverLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-limitVelocityOverLifetime.html) | Script interface for the LimitVelocityOverLifetimeModule of a Particle System. .  
[main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-main.html) | Access the main Particle System settings.  
[noise](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-noise.html) | Script interface for the NoiseModule of a Particle System.  
[particleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-particleCount.html) | The current number of particles (Read Only). The number doesn't include particles of child Particle Systems  
[proceduralSimulationSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-proceduralSimulationSupported.html) | Determines whether this system supports Procedural Simulation.  
[randomSeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-randomSeed.html) | Override the random seed used for the Particle System emission.  
[rotationBySpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-rotationBySpeed.html) | Script interface for the RotationBySpeedModule of a Particle System.  
[rotationOverLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-rotationOverLifetime.html) | Script interface for the RotationOverLifetimeModule of a Particle System.  
[shape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-shape.html) | Script interface for the ShapeModule of a Particle System.   
[sizeBySpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-sizeBySpeed.html) | Script interface for the SizeBySpeedModule of a Particle System.  
[sizeOverLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-sizeOverLifetime.html) | Script interface for the SizeOverLifetimeModule of a Particle System.   
[subEmitters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-subEmitters.html) | Script interface for the SubEmittersModule of a Particle System.  
[textureSheetAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-textureSheetAnimation.html) | Script interface for the TextureSheetAnimationModule of a Particle System.  
[time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-time.html) | Playback position in seconds.  
[totalTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-totalTime.html) | Total playback time in seconds, including the Start Delay setting.  
[trails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-trails.html) | Script interface for the TrailsModule of a Particle System.  
[trigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-trigger.html) | Script interface for the TriggerModule of a Particle System.  
[useAutoRandomSeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-useAutoRandomSeed.html) | Controls whether the Particle System uses an automatically-generated random number to seed the random number generator.  
[velocityOverLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-velocityOverLifetime.html) | Script interface for the VelocityOverLifetimeModule of a Particle System.  
### Public Methods
Method | Description  
---|---  
[AllocateAxisOfRotationAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.AllocateAxisOfRotationAttribute.html) | Ensures that the axisOfRotations particle attribute array is allocated.  
[AllocateCustomDataAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.AllocateCustomDataAttribute.html) | Ensures that the customData1 and customData2 particle attribute arrays are allocated.  
[AllocateMeshIndexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.AllocateMeshIndexAttribute.html) | Ensures that the meshIndices particle attribute array is allocated.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Clear.html) | Remove all particles in the Particle System.  
[Emit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Emit.html) | Emit count particles immediately.  
[GetCustomParticleData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetCustomParticleData.html) | Get a stream of custom per-particle data.  
[GetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetParticles.html) | Gets the particles of this Particle System.  
[GetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetPlaybackState.html) | Returns all the data that relates to the current internal state of the Particle System.  
[GetTrails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetTrails.html) | Returns all the data relating to the current internal state of the Particle System Trails.  
[IsAlive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.IsAlive.html) | Does the Particle System contain any live particles, or will it produce more?  
[Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Pause.html) | Pauses the system so no new particles are emitted and the existing particles are not updated.  
[Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Play.html) | Starts the Particle System.  
[SetCustomParticleData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetCustomParticleData.html) | Set a stream of custom per-particle data.  
[SetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetParticles.html) | Sets the particles of this Particle System.  
[SetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetPlaybackState.html) | Use this method with the results of an earlier call to ParticleSystem.GetPlaybackState, in order to restore the Particle System to the state stored in the playbackState object.  
[SetTrails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetTrails.html) | Use this method with the results of an earlier call to ParticleSystem.GetTrails, in order to restore the Particle System to the state stored in the Trails object.  
[Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Simulate.html) | Fast-forwards the Particle System by simulating particles over the given period of time, then pauses it.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Stop.html) | Stops playing the Particle System using the supplied stop behaviour.  
[TriggerSubEmitter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerSubEmitter.html) | Triggers the specified sub emitter on all particles of the Particle System.  
### Static Methods
Method | Description  
---|---  
[ResetPreMappedBufferMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ResetPreMappedBufferMemory.html) | Reset the cache of reserved graphics memory used for efficient rendering of Particle Systems.  
[SetMaximumPreMappedBufferCounts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetMaximumPreMappedBufferCounts.html) | Limits the amount of graphics memory Unity reserves for efficient rendering of Particle Systems.  
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
