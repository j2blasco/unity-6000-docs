* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inParticleSystem.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * Create and view a Particle System


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ChoosingYourParticleSystem.html)
Choosing your particle system solution
[](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html)
Vary Particle System properties over time
# Create and view a Particle System
The Built-in Particle System uses a component, so placing a Particle System in a Scene is a matter of adding a pre-made GameObject (menu: **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) > **Effects** > **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem)) or adding the component to an existing GameObject (menu: **Component** A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#component) > **Effects** > **Particle System**). Because the component is quite complicated, the Inspector is divided into a number of collapsible sub-sections or **modules** that each contain a group of related properties. Additionally, you can edit one or more systems at the same time using a separate Editor window accessed via the **Open Editor** button in the Inspector. See documentation on the [Particle System component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html) and individual [Particle System modules](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html) to learn more.
When a GameObject with a Particle System is selected, the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view contains a small **Particle Effect** panel, with some simple controls that are useful for visualising changes you make to the system’s settings.
![The Particle Effect panel in the Scene view.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PartSysEffectPanel.png) The Particle Effect panel in the Scene view.
The **Playback Speed** allows you to speed up or slow down the particle simulation, so you can quickly see how it looks at an advanced state. The **Playback Time** indicates the time elapsed since the system was started; this may be faster or slower than real time depending on the playback speed. The **Particle Count** indicates how many particles are currently in the system. The playback time can be moved backwards and forwards by clicking on the **Playback Time** label and dragging the mouse left and right. The buttons at the top of the panel can be used to pause and resume the simulation, or to stop it and reset to the initial state.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ChoosingYourParticleSystem.html)
Choosing your particle system solution
[](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html)
Vary Particle System properties over time
