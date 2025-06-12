* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ParticleSystemModule.html

# UnityEngine.ParticleSystemModule
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
The ParticleSystem module implements Unity's Particle System.
### Classes
Class | Description  
---|---  
[IJobParticleSystemExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.IJobParticleSystemExtensions.html) | Extension methods for Jobs using the IJobParticleSystem interface.  
[IJobParticleSystemParallelForBatchExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.IJobParticleSystemParallelForBatchExtensions.html) | Extension methods for Jobs using the IJobParticleSystemParallelForBatch interface.  
[IJobParticleSystemParallelForExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.IJobParticleSystemParallelForExtensions.html) | Extension methods for Jobs using the IJobParticleSystemParallelFor interface.  
[ParticlePhysicsExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticlePhysicsExtensions.html) | Method extension for Physics in Particle System.  
[ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) | Script interface for the Built-in Particle System. Unity's powerful and versatile particle system implementation.  
[ParticleSystemForceField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceField.html) | Script interface for Particle System Force Fields.  
[ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) | Use this class to render particles on to the screen.  
### Structs
Struct | Description  
---|---  
[ParticleCollisionEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleCollisionEvent.html) | Information about a particle collision.  
[ParticleSystemJobData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.ParticleSystemJobData.html) | This struct specifies all the per-particle data.  
[ParticleSystemNativeArray3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.ParticleSystemNativeArray3.html) | A container to hold x, y, and z-axis data for particles.  
[ParticleSystemNativeArray4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemJobs.ParticleSystemNativeArray4.html) | A container to hold 4 arrays of data for particles.  
### Enumerations
Enumeration | Description  
---|---  
[ParticleSystemAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationMode.html) | The animation mode.  
[ParticleSystemAnimationRowMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationRowMode.html) | The mode used for selecting rows of an animation in the Texture Sheet Animation Module.  
[ParticleSystemAnimationTimeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationTimeMode.html) | Control how animation frames are selected.  
[ParticleSystemAnimationType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationType.html) | The animation type.  
[ParticleSystemBakeMeshOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemBakeMeshOptions.html) | Configure how a Particle System is baked into a mesh.  
[ParticleSystemBakeTextureOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemBakeTextureOptions.html) | Configure how a Particle System is baked into a texture.  
[ParticleSystemColliderQueryMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemColliderQueryMode.html) | Whether collider information is available when using the [[ParticleSystem::GetTriggerParticles]] method.  
[ParticleSystemCollisionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCollisionMode.html) | Whether to use 2D or 3D colliders for particle collisions.  
[ParticleSystemCollisionQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCollisionQuality.html) | Quality of world collisions. Medium and low quality are approximate and may leak particles.  
[ParticleSystemCollisionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCollisionType.html) | The type of collisions to use for a given Particle System.  
[ParticleSystemCullingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCullingMode.html) | The action to perform when the Particle System is offscreen.  
[ParticleSystemCurveMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCurveMode.html) | The particle curve mode.  
[ParticleSystemCustomData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCustomData.html) | Which stream of custom particle data to set.  
[ParticleSystemCustomDataMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCustomDataMode.html) | Which mode CustomDataModule uses to generate its data.  
[ParticleSystemEmitterVelocityMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemEmitterVelocityMode.html) | Control how a Particle System calculates its velocity.  
[ParticleSystemForceFieldShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemForceFieldShape.html) | The type of shape used for influencing particles in the Force Field Component.  
[ParticleSystemGameObjectFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemGameObjectFilter.html) | The particle GameObject filtering mode that specifies which objects are used by specific Particle System modules.  
[ParticleSystemGradientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemGradientMode.html) | The particle gradient mode.  
[ParticleSystemGravitySource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemGravitySource.html) | Options for which physics system to use the gravity setting from.  
[ParticleSystemInheritVelocityMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemInheritVelocityMode.html) | How to apply emitter velocity to particles.  
[ParticleSystemMeshDistribution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemMeshDistribution.html) | Sets which method Unity uses to randomly assign Meshes to particles.  
[ParticleSystemMeshShapeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemMeshShapeType.html) | The mesh emission type.  
[ParticleSystemNoiseQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemNoiseQuality.html) | The quality of the generated noise.  
[ParticleSystemOverlapAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemOverlapAction.html) | What action to perform when the particle trigger module passes a test.  
[ParticleSystemRenderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.html) | The rendering mode for particle systems.  
[ParticleSystemRenderSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderSpace.html) | How particles are aligned when rendered.  
[ParticleSystemRingBufferMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRingBufferMode.html) | Control how particles are removed from the Particle System.  
[ParticleSystemScalingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemScalingMode.html) | Control how particle systems apply transform scale.  
[ParticleSystemShapeMultiModeValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemShapeMultiModeValue.html) | The mode used to generate new points in a shape.  
[ParticleSystemShapeTextureChannel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemShapeTextureChannel.html) | The texture channel.  
[ParticleSystemShapeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemShapeType.html) | The emission shape.  
[ParticleSystemSimulationSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSimulationSpace.html) | The space to simulate particles in.  
[ParticleSystemSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSortMode.html) | The sorting mode for particle systems.  
[ParticleSystemStopAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopAction.html) | The action to perform when the Particle System stops.  
[ParticleSystemStopBehavior](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopBehavior.html) | The behavior to apply when calling Stop.  
[ParticleSystemSubEmitterProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSubEmitterProperties.html) | The properties of sub-emitter particles.  
[ParticleSystemSubEmitterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemSubEmitterType.html) | The events that cause new particles to be spawned.  
[ParticleSystemTrailMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTrailMode.html) | Choose how Particle Trails are generated.  
[ParticleSystemTrailTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTrailTextureMode.html) | Choose how textures are applied to Particle Trails.  
[ParticleSystemTriggerEventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemTriggerEventType.html) | The different types of particle triggers.  
[ParticleSystemVertexStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.html) | All possible Particle System vertex shader inputs.  
[UVChannelFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.UVChannelFlags.html) | A flag representing each UV channel.  
* * *
