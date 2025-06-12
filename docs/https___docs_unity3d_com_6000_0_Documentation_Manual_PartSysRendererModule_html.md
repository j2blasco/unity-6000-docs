* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRendererModule.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Particle System module component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
  * Renderer module reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysCustomDataModule.html)
Custom Data module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html)
Particle System Force Field component reference
# Renderer module reference
The Renderer module’s settings determine how a particle’s image or [Mesh](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html) is transformed, shaded and overdrawn by other particles.
![The Renderer module view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/renderer-module-view.png) The Renderer module view
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html).
**Property:** | **Function:**  
---|---  
**Render Mode** | How Unity produces the rendered image from the graphic image (or Mesh). For more information, refer to [Particle rendering and shading](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-rendering-shading.html).  
| **Billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) | Unity renders the particles as billboards and they face the direction you specify in **Render Alignment**.  
| **Stretched Billboard** | The particles face the ****Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)** with various possible scaling options applied.  
|  | Camera Scale | This setting is only available when you use the **Stretched Billboard** Render mode.  
  
Stretches particles according to Camera movement. Set this to zero to disable Camera movement stretching.  
|  | Velocity Scale | This setting is only available when you use the Stretched Billboard Render mode.  
  
Stretches particles proportionally to their speed. Set this to zero to disable stretching based on speed.  
|  | Length Scale | This setting is only available when you use the Stretched Billboard Render mode.  
  
Stretches particles proportionally to their current size along the direction of their velocity. Setting this to zero makes the particles disappear, having effectively zero length.  
|  | Freeform Stretching | This setting is only available when you use the Stretched Billboard Render mode.  
  
Indicates whether particles should use freeform stretching. With this stretching behavior, particles don’t become thin when you view them head-on.  
|  | Rotate With Stretch | This setting is only available when you use the Stretched Billboard Render mode.  
  
Indicates whether to rotate particles based on the direction they stretch in. This is added on top of other particle rotation. This property only has an effect when you enable **Freeform Stretching**. If you disable **Freeform Stretching** , particles always rotate based on the direction they stretch in, even if **Rotate With Stretch** is disabled.  
| **Horizontal Billboard** | The particle plane is parallel to the XZ “floor” plane.  
| **Vertical Billboard** | The particle is upright on the world Y-axis, but turns to face the Camera.  
| **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) | Unity renders the particle from a 3D Mesh instead of a Billboard. For more information on the specific settings for the Mesh Render mode, refer to [Particle rendering and shading](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-rendering-shading.html).  
|  | Mesh Distribution | Specifies the method that Unity uses to randomly assign meshes to particles.  
  
This setting is only available when you use the **Mesh** Render mode.  
|  |  | Uniform Random | Unity randomly assigns meshes to particles with an even weighting. The Particle System as a whole should contain a roughly equal number of each possible mesh at any given moment.  
  
This setting is only available when you use the **Mesh** Render mode.  
|  |  | Non-uniform Random | Unity randomly assigns meshes to particles with user-defined weights for each mesh.  
  
When this setting is enabled, the Renderer module Inspector window displays a Meshes list and a Mesh Weightings field for each mesh in the list. You can use the Mesh Weightings field to control how often Unity assigns each mesh to a particle.  
  
This setting is only available when you use the **Mesh** Render mode.  
|  | Mesh Weightings | Controls how likely Unity is to assign this mesh to a particle. The weights work relative to each other; Unity is twice as likely to assign a mesh with double the weight of another mesh, regardless of their absolute value. For more information, refer to [Particle rendering and shading](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-rendering-shading.html).  
  
This setting is only available when you use the **Mesh** Render mode and the **Mesh Distribution** property is set to “Non-uniform Random”.  
| **None** | Unity doesn’t render any particles. This can be useful alongside the [Trails](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysTrailsModule.html) module, if you want to only render the trails and hide any default particle rendering.  
**Normal Direction** | Specifies how to calculate lighting for the billboard. A value of 0 means Unity calculates lighting as though the billboard was a sphere. This results in the billboard looking more like a sphere. A value of 1 means Unity calculates lighting for the billboard as a flat quad.  
  
This property is only available when using one of the Billboard rendering modes: **Billboard** , **Stretched Billboard** , **Horizontal Billboard** or **Vertical Billboard**.  
**Material** An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) | The material Unity uses to render the particles.  
**Trail Material** | The material Unity uses to render particle trails.  
  
This option is only available when the **Trails** module is enabled.  
**Sort Mode** | The order in which Unity draws and overlays particles with a **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem).  
| None | When this setting is enabled, Unity doesn’t sort particles.  
| By Distance | Sorts particles in the system based on distance to the active Camera. Unity renders particles closer to the Camera on top of those that are further away. The order of particles doesn’t change when you rotate the camera with the setting.  
| Oldest in Front | Unity renders particles that have existed the longest at the front of the Particle System.  
| Youngest in Front | Unity renders particles that have existed for the shortest time at the front of the Particle System.  
| By Depth | Unity renders particles based on their distance from the camera’s near plane. The order of particles can change when you rotate the camera with this setting.  
**Sorting Fudge** | The bias of the Particle System sort ordering. Lower values increase the relative chance that Unity draws Particle Systems over other transparent **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), including other Particle Systems. This setting only affects Particle Systems as a whole that appear in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) - it does not perform sorting on individual particles within a system.  
**Min Particle Size** | The smallest particle size (regardless of other settings), expressed as a fraction of viewport size.  
  
This property is only available when using one of the Billboard rendering modes: **Billboard** , **Stretched Billboard** , **Horizontal Billboard** or **Vertical Billboard**.  
**Max Particle Size** | The largest particle size (regardless of other settings), expressed as a fraction of viewport size.   
  
This property is only available when using one of the Billboard rendering modes: **Billboard** , **Stretched Billboard** , **Horizontal Billboard** or **Vertical Billboard**.  
**Render Alignment** | This property determines the direction that particle billboards face.  
| View | Particles face the Camera plane.  
| World | Particles align with the world axes.  
| Local | Particles align to the ****Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TransformComponent)** of their GameObject.  
| Facing | Particles face the direct position defined by the Transform component in the GameObject of the active Camera.  
| Velocity | Particles face in the same direction as their velocity vector.  
**Enable Mesh GPU Instancing** | This property is only available when using the Mesh render mode.  
  
This property controls whether Unity renders the Particle System using GPU Instancing. This requires the use of a compatible shader. For more information, see [Particle Mesh GPU Instancing](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysInstancing.html).  
**Flip** | Mirror a proportion of the particles across the specified axes. A higher value flips more particles.  
**Allow Roll** | Controls whether camera-facing particles can rotate around the Z-axis of the camera. Disabling this can be particularly useful for **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR) applications, where HMD (Head-Mounted Display) roll can cause undesirable particle rotation for Particle Systems.  
**Pivot** | Modify the central pivot point for rotating particles. The value is a multiplier of the particle size.  
**Visualize Pivot** | Preview the particle pivot points in the **Scene** View.  
**Masking** | Set how the particles rendered by the Particle System behave when they interact with a ****Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) Mask**.  
| No Masking | The Particle System does not interact with any **Sprite Masks** A texture which defines which areas of an underlying image to reveal or hide. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/mask/mask-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteMask) in the Scene. This is the default option.  
| Visible Inside Mask | The particles are visible where the Sprite Mask overlays them, but not outside of it.  
| Visible Outside Mask | The particles are visible outside of the Sprite Mask, but not inside it. The Sprite Mask hides the sections of the particles it overlays.  
**Apply Active Color Space** | When rendering in Linear Color Space, the system converts particle colors from Gamma Space before it uploads them to the GPU.  
**Custom Vertex Streams** | Configure which particle properties are available in the Vertex **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) of your Material. For more information, see [Particle System vertex streams and Standard Shader support](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysVertexStreams.html).  
**Cast Shadows** | If this property is enabled, the Particle System creates shadows when a shadow-casting Light shines on it.  
| On | Enables shadows for this Particle System.  
| Off | Disables shadows for this Particle System.  
| Two-Sided | Select **Two Sided** to allow shadows to be cast from either side of the Mesh. Backface culling is not taken into account when this property is enabled.  
| Shadows Only | Select **Shadows Only** to make it so that the shadows are visible, but the Mesh itself is not.  
**Shadow Bias** | Move the shadows along the direction of the light. This removes shadowing artifacts caused by approximating volumes with billboards.  
**Motion Vectors** | Set whether to use motion vectors to track the per-pixel, screen-space motion of this Particle System’s Transform component from one frame to the next.  
  
**Note:** Not all platforms support motion vectors. See [SystemInfo.supportsMotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMotionVectors.html) for more information.  
| Camera Motion Only | Use only Camera movement to track motion.  
| Per Object Motion | Use a specific pass to track motion for this Renderer.  
| Force No Motion | Do not track motion.  
**Receive Shadows** | Dictates whether particles in this system can receive shadows from other sources. Only opaque materials can receive shadows.  
**Sorting Layer ID** | The name of the Renderer’s sorting layer.  
**Order in Layer** | This Renderer’s order within a sorting layer.  
**Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) | Probe-based lighting interpolation mode.  
**Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) | If enabled, and if reflection probes are present in the Scene, Unity assigns a reflection texture from the nearest reflection probe to this GameObject and sets the texture as a built-in Shader uniform variable.  
**Anchor Override** | A Transform that determines the interpolation position when you use the [Light Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html) or [Reflection Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html) systems.  
## Additional resources
  * [Particle rendering and shading](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-rendering-shading.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysCustomDataModule.html)
Custom Data module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html)
Particle System Force Field component reference
