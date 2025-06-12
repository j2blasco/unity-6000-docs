* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysEmissionModule.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Particle System module component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
  * Emission module reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysMainModule.html)
Main module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysShapeModule.html)
Shape module reference
# Emission module reference
The properties in this module affect the rate and timing of [Particle System](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) emissions.
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html).
**Property** | **Function**  
---|---  
**Rate over Time** | The number of particles emitted per unit of time.  
**Rate over Distance** | The number of particles emitted per unit of distance moved.  
**Bursts** | A burst is an event which spawns particles. These settings allow particles to be emitted at specified times.  
 _Time_ | Set the time (in seconds, after the Particle System begins playing) at which to emit the burst.  
 _Count_ | Set a value for the number of particles that may be emitted.  
 _Cycles_ | Set a value for how many times to play the burst.  
 _Interval_ | Set a value for the time (in seconds) between when each cycle of the burst is triggered.  
 _Probability_ | Controls how likely it is that each burst event spawns particles. A higher value makes the system produce more particles, and a value of 1 guarantees that the system produces particles.  
## Additional resources
  * [Particle emissions and emitters](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-emissions-emitters.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysMainModule.html)
Main module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysShapeModule.html)
Shape module reference
