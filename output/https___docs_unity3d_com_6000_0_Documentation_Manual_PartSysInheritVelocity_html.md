* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysInheritVelocity.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Particle System module component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
  * Inherit Velocity module reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLimitVelOverLifeModule.html)
Limit Velocity over Lifetime module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLifetimeByEmitterSpeedModule.html)
Lifetime by Emitter Speed module reference
# Inherit Velocity module reference
Use this module on subemitters. Each particle in the parent system can spawn particles in the subemitter. This module reads the velocity from the parent particle and controls how the speed of the subemitter particles reacts to that velocity over time.
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html).
**Property** | **Function**  
---|---  
**Mode** | Specifies how the emitter velocity is applied to particles  
Current | The emitter’s current velocity will be applied to all particles on every frame. For example, if the emitter slows down, all particles will also slow down.  
Initial | The emitter’s velocity will be applied once, when each particle is born. Any changes to the emitter’s velocity made after a particle is born will not affect that particle.  
**Multiplier** | The proportion of the emitter’s velocity that the particle should inherit.  
## Additional resources
  * [Particle velocity](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-velocity.html)
  * [Create particles that change velocity over time](https://docs.unity3d.com/6000.0/Documentation/Manual/create-particles-that-change-velocity-over-time.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLimitVelOverLifeModule.html)
Limit Velocity over Lifetime module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLifetimeByEmitterSpeedModule.html)
Lifetime by Emitter Speed module reference
