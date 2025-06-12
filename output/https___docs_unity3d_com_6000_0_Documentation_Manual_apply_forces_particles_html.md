* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/apply-forces-particles.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Configuring particles](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-particles.html)
  * [Particle physics](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics.html)
  * Apply forces to particles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics-forces.html)
Particle physics forces
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-collisions.html)
Particle collisions
# Apply forces to particles
The **Particle System Force Field** component applies forces to particles in [Particle Systems](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem). 
To attach this component to a Particle System, enable the [External Forces Module](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysExtForceModule.html) in the Particle System, and assign either a **Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask), or the specific Force Field component. 
Use the [Particle System Force Field](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html) component to apply various types of forces to particles.
All forces are applied in the local space of the Force Field. For example, rotating Transform affects the direction and rotation properties.
For a full introduction to particle systems and their uses, see documentation on [Particle Systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics-forces.html)
Particle physics forces
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-collisions.html)
Particle collisions
