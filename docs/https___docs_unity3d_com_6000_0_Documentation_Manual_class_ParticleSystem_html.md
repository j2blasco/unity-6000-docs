* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * Particle System component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/access-particle-system-from-animation.html)
Access the Particle System from the Animation system
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
Particle System module component reference
# Particle System component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html "Go to ParticleSystem page in the Scripting Reference")
A **Particle System** component simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). For a full introduction to particle systems and their uses, see further documentation on [Particle Systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html).
**Property** | **Function**  
---|---  
**Simulate Layers** | Allows you to preview Particle Systems that are not selected. By default, only selected Particle Systems play in the **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView). However, when you set Simulate Layers to anything other than **Nothing** , effects that match the **Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask) play automatically, without you needing to select them. This is particularly useful for previewing environmental effects.  
**Resimulate** | When this property is enabled, the Particle System immediately applies property changes to particles it has already generated. When disabled, the Particle System leaves existing particles as they are, and only applies property changes to new particles.  
**Show Bounds** | When this property is enabled, Unity displays the **bounding volume** A closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Boundingvolume) around the selected Particle Systems. These bounds determine whether a Particle System is currently on screen or not.  
**Show Only Selected** | When this property is enabled, Unity hides all non-selected Particle Systems, allowing you to focus on producing a single effect.  
ParticleSystem
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/access-particle-system-from-animation.html)
Access the Particle System from the Animation system
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
Particle System module component reference
