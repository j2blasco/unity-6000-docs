* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule.html

# MainModule
struct in UnityEngine
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
Script interface for the MainModule of a Particle System.
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-main.html).
### Properties
Property | Description  
---|---  
[cullingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-cullingMode.html) | Configure whether the Particle System will still be simulated each frame, when it is offscreen.  
[customSimulationSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-customSimulationSpace.html) | Simulate particles relative to a custom transform component.  
[duration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-duration.html) | The duration of the Particle System in seconds.  
[emitterVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-emitterVelocity.html) | The current Particle System velocity.  
[emitterVelocityMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-emitterVelocityMode.html) | Control how the Particle System calculates its velocity, when moving in the world.  
[flipRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-flipRotation.html) | Makes some particles spin in the opposite direction.  
[gravityModifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-gravityModifier.html) | A scale that this Particle System applies to gravity, defined either by Physics.gravity or [Physics2D.gravity]].  
[gravityModifierMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-gravityModifierMultiplier.html) | Change the gravity multiplier.  
[gravitySource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-gravitySource.html) | Specify whether to use the gravity strength from the 2D or 3D physics system.  
[loop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-loop.html) | Specifies whether the Particle System is looping.  
[maxParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-maxParticles.html) | The maximum number of particles to emit.  
[playOnAwake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-playOnAwake.html) | If set to true, the Particle System automatically begins to play on startup.  
[prewarm](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-prewarm.html) | If ParticleSystem.MainModule.loop is true, when you enable this property, the Particle System looks like it has already simulated for one loop when first becoming visible.  
[ringBufferLoopRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-ringBufferLoopRange.html) | When ParticleSystem.MainModule.ringBufferMode is set to loop, this value defines the proportion of the particle life that loops.  
[ringBufferMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-ringBufferMode.html) | Configure the Particle System to not kill its particles when their lifetimes are exceeded.  
[scalingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-scalingMode.html) | Control how the Particle System applies its Transform component to the particles it emits.  
[simulationSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-simulationSpace.html) | This selects the space in which to simulate particles. It can be either world or local space.  
[simulationSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-simulationSpeed.html) | Override the default playback speed of the Particle System.  
[startColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startColor.html) | The initial color of particles when the Particle System first spawns them.  
[startDelay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startDelay.html) | Start delay in seconds.  
[startDelayMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startDelayMultiplier.html) | A multiplier for ParticleSystem.MainModule.startDelay in seconds.  
[startLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startLifetime.html) | The total lifetime in seconds that each new particle has.  
[startLifetimeMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startLifetimeMultiplier.html) | A multiplier for ParticleSystem.MainModule.startLifetime.  
[startRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startRotation.html) | The initial rotation of particles when the Particle System first spawns them.  
[startRotation3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startRotation3D.html) | A flag to enable 3D particle rotation.  
[startRotationMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startRotationMultiplier.html) | A multiplier for ParticleSystem.MainModule.startRotation.  
[startRotationX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startRotationX.html) | The initial rotation of particles around the x-axis when emitted.  
[startRotationXMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startRotationXMultiplier.html) | The initial rotation multiplier of particles around the x-axis when the Particle System first spawns them.  
[startRotationY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startRotationY.html) | The initial rotation of particles around the y-axis when the Particle System first spawns them.  
[startRotationYMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startRotationYMultiplier.html) | The initial rotation multiplier of particles around the y-axis when the Particle System first spawns them..  
[startRotationZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startRotationZ.html) | The initial rotation of particles around the z-axis when the Particle System first spawns them  
[startRotationZMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startRotationZMultiplier.html) | The initial rotation multiplier of particles around the z-axis when the Particle System first spawns them.  
[startSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSize.html) | The initial size of particles when the Particle System first spawns them.  
[startSize3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSize3D.html) | A flag to enable specifying particle size individually for each axis.  
[startSizeMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSizeMultiplier.html) | A multiplier for the initial size of particles when the Particle System first spawns them.  
[startSizeX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSizeX.html) | The initial size of particles along the x-axis when the Particle System first spawns them.  
[startSizeXMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSizeXMultiplier.html) | A multiplier for ParticleSystem.MainModule.startSizeX.  
[startSizeY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSizeY.html) | The initial size of particles along the y-axis when the Particle System first spawns them.  
[startSizeYMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSizeYMultiplier.html) | A multiplier for ParticleSystem.MainModule.startSizeY.  
[startSizeZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSizeZ.html) | The initial size of particles along the z-axis when the Particle System first spawns them.  
[startSizeZMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSizeZMultiplier.html) | A multiplier for ParticleSystem.MainModule.startSizeZ.  
[startSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSpeed.html) | The initial speed of particles when the Particle System first spawns them.  
[startSpeedMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startSpeedMultiplier.html) | A multiplier for ParticleSystem.MainModule.startSpeed.  
[stopAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-stopAction.html) | Select whether to Disable or Destroy the GameObject, or to call the MonoBehaviour.OnParticleSystemStopped script Callback, when the Particle System stops and all particles have died.  
[useUnscaledTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-useUnscaledTime.html) | When true, use the unscaled delta time to simulate the Particle System. Otherwise, use the scaled delta time.  
* * *
