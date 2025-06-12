* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysTexSheetAnimModule.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Particle System module component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
  * Texture Sheet Animation module reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysSubEmitModule.html)
Sub Emitters module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLightsModule.html)
Lights module reference
# Texture Sheet Animation module reference
A particle’s graphic need not be a still image. This module lets you treat the Texture as a grid of separate sub-images that can be played back as frames of animation.
## Grid mode properties
**Property** | **Function**  
---|---  
**Mode popup** | Select **Grid** mode.  
**Tiles** A simple class that allows a sprite to be rendered on a Tilemap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tile) | The number of tiles the Texture is divided into in the X (horizontal) and Y (vertical) directions.  
**Animation** | The Animation mode can be set to **Whole Sheet** or **Single Row** (that is, each row of the sheet represents a separate Animation sequence).  
**Time Mode** | Choose how the **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) samples frames in the animation.  
Lifetime | Sample frames using an Animation Curve over the lifetime of the particle.  
Speed | Sample frames based on the speed of the particle. A speed range specifies the minimum and maximum speed range for the frame selection.  
**FPS** See first person shooter, frames per second.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FPS) | Sample frames based on the specified frames-per-second value.  
**Row Mode** | Make the Particle System choose a row from the Texture sheet to produce the animation. This property is only available when the **Animation** mode is set to **Single Row**.  
Custom | Use a specific row of the Texture sheet for the animation.  
Random | Randomly select a row for each particle when producing the animation.  
**Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Index | Select a row based on the Mesh index assigned to a particle. This is useful when you want to ensure that a particle using a particular Mesh also uses the same Texture.  
**Random Row** | Chooses a row from the sheet at random to produce the animation. This option is only available when **Single Row** is selected as the **Animation** mode.  
**Row** | Selects a particular row from the sheet to produce the animation This option is only available when **Single Row** mode is selected and **Random Row** is disabled.  
**Frame over Time** | A curve that specifies how the frame of animation increases as time progresses.  
**Start Frame** | Allows you to specify which frame the particle animation should start on (useful for randomly phasing the animation on each particle).  
**Cycles** | The number of times the animation sequence repeats over the particle’s lifetime.  
**Affected UV Channels** | Allows you to specify exactly which UV streams are affected by the Particle System.  
## Sprite mode properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html).
**Property** | **Function**  
---|---  
**Mode popup** | Select **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) mode.  
**Frame over Time** | A curve that specifies how the frame of animation increases as time progresses.  
**Start Frame** | Allows you to specify which frame the particle animation should start on (useful for randomly phasing the animation on each particle).  
**Cycles** | The number of times the animation sequence repeats over the particle’s lifetime.  
**Enabled UV Channels** | Allows you to specify exactly which UV streams are affected by the Particle System.  
## Additional resources
  * [Particle animation](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-animation.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysSubEmitModule.html)
Sub Emitters module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLightsModule.html)
Lights module reference
