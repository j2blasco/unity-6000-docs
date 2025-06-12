* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * Particle System module component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)
Particle System component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/activate-access-particle-system-modules.html)
Activate and access Particle System modules
# Particle System module component reference
The [Particle System](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) component has a powerful set of properties that are organized into modules for ease of use. This section of the manual covers each of the modules in detail. 
**Topic** | **Description**  
---|---  
[Activate and access component modules](https://docs.unity3d.com/6000.0/Documentation/Manual/activate-access-particle-system-modules.html) | Activate component modules on a Particle System to access and change the properties of particles and emitters.  
[Main module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysMainModule.html) | Explore properties on the Main module, to configure the initial state of new particles.  
[Emission module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysEmissionModule.html) | Explore properties on the Emission module, to configure the rate and timing of particle emissions.  
[Shape module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysShapeModule.html) | Explore properties on the Shape module, to configure the volume or surface that the Particle System uses to emit particles, and the direction of the start velocity.  
[Velocity over Lifetime module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysVelOverLifeModule.html) | Explore properties on the Velocity over Lifetime module, to configure particles that change velocity over time.  
[Noise module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysNoiseModule.html) | Explore properties on the Noise module, to configure the turbulence of particles as they move.  
[Limit Velocity over Lifetime module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLimitVelOverLifeModule.html) | Explore properties on the Limit Velocity over Lifetime module, to configure particles that reduce in velocity over time.  
[Inherit Velocity module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysInheritVelocity.html) | Explore properties on the Inherit Velocity module, to configure the velocity of particles from sub-emitters to match the velocity of the parent particle.  
[Lifetime by Emitter Speed module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLifetimeByEmitterSpeedModule.html) | Explore properties on the Lifetime by Emitter Speed module, to configure the initial lifetime of each particle based on the speed of the emitter when the particle spawns.  
[Force over Lifetime module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysForceOverLifeModule.html) | Explore properties on the Force over Lifetime module, to configure simulated physics forces that affect the movement of particles over time.  
[Color over Lifetime module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysColorOverLifeModule.html) | Explore properties on the Color over Lifetime module, to configure particles that change color over time.  
[Color by Speed module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysColorBySpeedModule.html) | Explore properties on the Color by Speed module, to configure particles that change color based on their speed.  
[Size over Lifetime module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysSizeOverLifeModule.html) | Explore properties on the Size over Lifetime module, to configure particles that change size over time.  
[Size by Speed module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysSizeBySpeedModule.html) | Explore properties on the Size by Speed module, to configure particles that change size based on their speed.  
[Rotation over Lifetime module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRotOverLifeModule.html) | Explore properties on the Rotation over Lifetime module, to configure particles that change rotation over time.  
[Rotation by Speed module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRotBySpeedModule.html) | Explore properties on the Rotation by Speed module, to configure particles that change rotation based on their speed.  
[External Forces module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysExtForceModule.html) | Explore properties on the External Forces module, to configure the effect of external physics forces such as **wind zones** A GameObject that adds the effect of wind to your terrain. For instance, Trees within a wind zone will bend in a realistic animated fashion and the wind itself will move in pulses to create natural patterns of movement among the tree. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#windzone) and force fields on particles emitted by the system.  
[Collision module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysCollisionModule.html) | Explore properties on the **Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) module, to configure particle collisions.  
[Triggers module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysTriggersModule.html) | Explore properties on the Triggers module, to configure particles that act as triggers.  
[Sub Emitters module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysSubEmitModule.html) | Explore properties on the Sub Emitters module, to configure particles that emit other particles.  
[Texture Sheet Animation module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysTexSheetAnimModule.html) | Explore properties on the Texture Sheet Animation module, to configure particles that use a texture grid to create animation frames.  
[Lights module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLightsModule.html) | Explore properties on the Lights module, to configure real-time lights on particles.  
[Trails module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysTrailsModule.html) | Explore properties on the Trails module, to configure trails on particles.  
[Custom Data module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysCustomDataModule.html) | Explore properties in the Custom Data module, to configure custom data formats in the Editor to attach to particles.  
[Renderer module reference](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRendererModule.html) | Explore properties on the Renderer module, to configure how a particle’s image or **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) is transformed, shaded and overdrawn by other particles.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)
Particle System component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/activate-access-particle-system-modules.html)
Activate and access Particle System modules
