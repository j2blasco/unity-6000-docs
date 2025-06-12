* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics-forces.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Configuring particles](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-particles.html)
  * [Particle physics](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics.html)
  * Particle physics forces


[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics.html)
Particle physics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/apply-forces-particles.html)
Apply forces to particles
# Particle physics forces
Understand how the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) can simulate physics forces that act on a particle.
## Force over lifetime
The [Force over Lifetime](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysForceOverLifeModule.html) module can change the strength of simulated physics forces on a particle based on how long the particle has existed.
Fluids are often affected by forces as they move. For example, smoke will accelerate slightly as it rises from a fire, carried up by the hot air around it. Subtle effects can be achieved by using curves to control the force over the particles’ lifetimes. Using the previous example, smoke will initially accelerate upward but as the rising air gradually cools, the force will diminish. Thick smoke from a fire might initially accelerate, then slow down as it spreads and perhaps even start to fall to earth if it persists for a long time.
## External forces
The [External Forces](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysExtForceModule.html) module modifies the effect of **wind zones** A GameObject that adds the effect of wind to your terrain. For instance, Trees within a wind zone will bend in a realistic animated fashion and the wind itself will move in pulses to create natural patterns of movement among the tree. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#windzone) and [Particle System Force Fields](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html) on particles emitted by the system.
To get the best results out of this feature, create separate **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with [ParticleSystemForceFields](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html) components.
A **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) can incorporate _wind zones_ which affect the movement of trees on the landscape. Enabling this section allows the wind zones to blow particles from the system. The _Multiplier_ value lets you scale the effect of the wind on the particles, since they will often be blown more strongly than tree branches.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics.html)
Particle physics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/apply-forces-particles.html)
Apply forces to particles
