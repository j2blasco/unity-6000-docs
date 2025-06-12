* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer-line-renderer-properties.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lines and trails](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lines-trails-billboards.html)
  * [Rendering lines](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-lines.html)
  * [Line Renderer component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)
  * Line Renderer properties reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer-scene-tools-panel.html)
Line Renderer Scene Tools panel reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-trails.html)
Rendering trails
# Line Renderer properties reference
## Line settings
**Property** | **Function**  
---|---  
**Loop** | Enable this to connect the first and last positions of the line, and form a closed loop.  
**Positions** | The array of Vector3 points to connect.  
**Width** | Define a width value, and a curve value to control the width of your line along its length.  
  
The curve is sampled at each vertex, so its accuracy is limited by the number of vertices in your line. The overall width of the line is controlled by the width value.  
**Color** | Define a gradient to control the color of the line along its length.  
  
Unity samples colors from the Color gradient at each vertex. Between each vertex, Unity applies linear interpolation to colors. Adding more vertices to your line might give a closer approximation of a detailed gradient.  
**Corner Vertices** | This property dictates how many extra vertices are used when drawing corners in a line. Increase this value to make the line corners appear rounder.  
**End Cap Vertices** | This property dictates how many extra vertices are used to create end caps on the line. Increase this value to make the line caps appear rounder.  
**Alignment** | Set the direction that the line faces. The options are: 
  * **View** : The line faces the Camera.
  * **TransformZ** : The line faces the Z axis of its Transform component.

  
**Texture Mode** | Control how the Texture is applied to the line. The options are: 
  * **Stretch** : Map the texture once along the entire length of the line.
  * **Tile** : Repeat the texture along the line, based on its length in world units. To set the tiling rate, use [Material.SetTextureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTextureScale.html).
  * **DistributePerSegment** : Map the texture once along the entire length of the line, assuming all vertices are evenly spaced.
  * **RepeatPerSegment** : Repeat the texture along the line, repeating at a rate of once per line segment. To adjust the tiling rate, use [Material.SetTextureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTextureScale.html).

  
**Shadow Bias** | Set the amount to move shadows away from the Light to remove shadowing artifacts caused by approximating a volume with billboarded geometry.  
**Generate Lighting Data** | If enabled, Unity builds the line geometry with normals and tangents included. This allows it to use Materials that use the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) lighting.  
**Use World Space** | If enabled, the points are considered as world space coordinates. If disabled, they are local to the transform of the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to which this component is attached.  
## Materials
The **Materials** section lists all the [materials](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) that this component uses.
**Property** | **Description**  
---|---  
**Size** | The number of elements in the material list.  
  
If you decrease the number of elements, Unity deletes the elements at the end of the list. If you increase the number of elements, Unity adds new elements to the end of the list. Unity populates new elements with the same material that the element at the end of the list uses.  
**Element** | The materials in the list. You can assign a material asset to each element.  
  
By default, Unity orders the list alphabetically based on the name of the materials. This list is reorderable, and Unity updates the number of the elements automatically as you change their order.  
## Lighting
The **Lighting** section contains properties that relate to lighting.
**Property** | **Description**  
---|---  
**Cast Shadows** | Specify if and how this Renderer casts shadows when a suitable [Light](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html) shines on it.  
  
This property corresponds to the [Renderer.shadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-shadowCastingMode.html) API.  
  
The options are:
  * **On** : This Renderer casts a shadow when a shadow-casting Light shines on it.
  * **Off** : This Renderer does not cast shadows.
  * **Two-sided** : This Renderer casts two-sided shadows. This means that single-sided objects like a plane or a quad can cast shadows, even if the light source is behind the mesh. For [Baked Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#MixedLighting) or Enlighten [Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#RealtimeLighting) to support two-sided shadows, the material must support [Double Sided Global Illumination](https://docs.unity3d.com/Manual/class-Material.html).
  * **Shadows Only** : This Renderer casts shadows, but the Renderer itself isn’t visible.

  
**Receive Shadows** | Specify if Unity displays shadows cast onto this Renderer.  
  
This property only has an effect if you enable [Baked Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#MixedLighting) or Enlighten [Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#RealtimeLighting) for this scene.  
  
This property corresponds to the [Renderer.receiveShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-receiveShadows.html) API.  
**Contribute Global Illumination** | Include this Renderer in global illumination calculations, which take place at bake time.  
  
This property only has an effect if you enable [Baked Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#MixedLighting) or Enlighten [Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#RealtimeLighting) for this scene.  
  
Enabling this property enables the Contribute GI flag in the GameObject’s [Static Editor Flags](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html). It corresponds to the [StaticEditorFlags.ContributeGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.ContributeGI.html) API.  
**Receive Global Illumination** | Whether Unity provides global illumination data to this Renderer from baked lightmaps, or from runtime Light Probes.  
  
This property is only editable if you enable **Contribute Global Illumination**. It only has an effect if you enable [Baked Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#MixedLighting) or Enlighten [Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#RealtimeLighting) for this scene.  
  
This property corresponds to the [MeshRenderer.receiveGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer-receiveGI.html) API.  
  
The options are:
  * **Lightmaps** : Unity provides global illumination data to this Renderer from lightmaps.
  * **Light Probes** : Unity provides global illumination data to this Renderer from [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) in the scene.

  
**Prioritize Illumination** | Enable this property to always include this Renderer in Enlighten Realtime Global Illumination calculations. This ensures that the Renderer is affected by distant emissives, even those which are normally excluded from Global Illumination calculations for performance reasons.  
  
This property is visible only if **Contribute GI** is enabled in the GameObject’s [Static Editor Flags](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html), your project uses the Built-in Render Pipeline, and Enlighten [Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#RealtimeLighting) is enabled in your scene.  
## Probes
The **Probes** section contains properties relating to [Light Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html) and [Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe).
**Property** | **Description**  
---|---  
**Light Probes** | Set how this Renderer receives light from the [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html) system.  
  
This property corresponds to the [Renderer.lightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-lightProbeUsage.html) API.  
  
The options are:
  * **Off** : The Renderer doesn’t use any interpolated Light Probes.
  * **Blend Probes** : The Renderer uses one interpolated Light Probe. This is the default value.
  * **Use Proxy Volume** : The Renderer uses a 3D grid of interpolated Light Probes.
  * **Custom Provided** : The Renderer extracts Light Probe shader uniform values from the [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).

  
**Proxy Volume Override** | Set a reference to another GameObject that has a Light Probe Proxy Volume component.  
  
This property is only visible when **Light Probes** is set to **Use Proxy Volume**.  
**Reflection Probes** | Set how the Renderer receives reflections from the [Reflection Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html) system.  
  
This property corresponds to the [Renderer.probeAnchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-probeAnchor.html) API.  
  
The options are:
  * **Off** : Disables Reflection Probes. Unity uses a skybox for reflection.
  * **Blend Probes** : Enables Reflection Probes. Blending occurs only between Reflection Probes. This is useful in indoor environments where the character may transition between areas with different lighting settings.
  * **Blend Probes and Skybox** : Enables Reflection Probes. Blending occurs between Reflection Probes, or between Reflection Probes and the default reflection. This is useful for outdoor environments.
  * **Simple** : Enables Reflection Probes, but no blending occurs between Reflection Probes when there are two overlapping volumes.

  
**Anchor Override** | Set the Transform that Unity uses to determine the interpolation position when using the [Light Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html) or [Reflection Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html) systems. By default, this is the centre of the bounding box of the Renderer’s geometry.  
  
This property corresponds to the [Renderer.probeAnchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-probeAnchor.html) API.  
## Additional Settings
The **Additional Settings** section contains additional properties.
**Property** | **Description**  
---|---  
**Motion Vectors** | Set whether to use motion vectors to track this Renderer’s per-pixel, screen-space motion from one frame to the next. You can use this information to apply post-processing effects such as motion blur.  
  
**Note:** not all platforms support motion vectors. See [SystemInfo.supportsMotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMotionVectors.html) for more information.  
  
This property corresponds to the [Renderer.motionVectorGenerationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-motionVectorGenerationMode.html) API.  
  
The options are:
  * **Camera Motion Only** : Use only Camera movement to track motion.
  * **Per Object Motion** : Use a specific pass to track motion for this Renderer.
  * **Force No Motion** : Do not track motion.

  
**Dynamic Occlusion** | When **Dynamic Occlusion** is enabled, Unity’s [occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling) system culls this Renderer when it is blocked from a Camera’s view by a Static Occluder. Otherwise, the system does not cull this Renderer when it is blocked from a Camera’s view by a Static Occluder.  
  
Dynamic Occlusion is enabled by default. Disable it for effects such as drawing the outline of a character behind a wall.  
**Sorting Layer** | The name of this Renderer’s [Sorting Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html).  
**Order in Layer** | This Renderer’s order within a [Sorting Layer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html).  
LineRenderer
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer-scene-tools-panel.html)
Line Renderer Scene Tools panel reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-trails.html)
Rendering trails
