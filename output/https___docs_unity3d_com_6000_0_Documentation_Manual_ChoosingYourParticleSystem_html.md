* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ChoosingYourParticleSystem.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * Choosing your particle system solution


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
Particle systems
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysUsage.html)
Create and view a Particle System
## Choosing your particle system solution
To provide flexibility when you author a **particle system** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem), Unity offers two solutions to choose from. If your Project targets platforms that support [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html), Unity allows you to use both at the same time. The two particle system solutions are:
  * The [Built-in Particle System](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysUsage.html): A solution that gives you full read/write access to the system, and the particles it contains, from C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). You can use the [Particle System API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) to create custom behaviors for your particle system.
  * The [Visual Effect Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/VFXGraph.html): A solution that can run on the GPU to simulate millions of particles and create large-scale visual effects. The Visual Effect Graph also includes a visual graph editor to help you author highly customizable visual effects.


The following table shows a high-level comparison of the two particle system solutions. For more information about either solution, see [Built-in Particle System](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysUsage.html) or [Visual Effect Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/VFXGraph.html).
**Feature** | **Built-in Particle System** | **Visual Effect Graph**  
---|---|---  
****Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) compatibility** | Built-in Render Pipeline, Universal Render Pipeline, High Definition Render Pipeline | Universal Render Pipeline, High Definition Render Pipeline  
**Feasible number of particles** | Thousands | Millions  
**Particle system authoring** | Simple modular authoring process that uses the [Particle System component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html) in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector). Each module represents a predefined behavior for the particle. | Highly customizable authoring process that uses a graph view.  
**Physics** | Particles can interact with Unity’s underlying physics system. | Particles can interact with specific elements that you define in the Visual Effect Graph. For example, particles can interact with the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer).  
**Script interaction** | You can use C# scripts to fully customize the Particle System at runtime. You can read from and write to each particle in a system, and respond to **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) events. The [Particle System component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html) also provides playback control API. This means that you can use scripts to play and pause the effect, and simulate the effect with custom step sizes. | You can expose graph properties and access them through C# scripts to customize instances of the effect. You can also use the [Event Interface](https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@latest/index.html?subfolder=/manual/Events.html) to send custom events with attached data that the graph can process. The [Visual Effect component](https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@latest/index.html?subfolder=/manual/VisualEffectComponent.html) also provides playback control API. This means that you can use scripts to play and pause the effect, and simulate the effect with custom step sizes.  
**Frame buffers** | No | In the High Definition Render Pipeline, provides access to the color and depth buffer. For example, you can sample the color buffer and use the result to set particle color, or you can use the depth buffer to simulate collisions.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
Particle systems
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysUsage.html)
Create and view a Particle System
