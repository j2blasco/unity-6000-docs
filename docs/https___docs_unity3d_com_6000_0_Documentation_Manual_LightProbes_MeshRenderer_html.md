* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-MeshRenderer.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating indirect light with Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-landing.html)
  * Set a GameObject to use light from Light Probes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Placing-Scripting.html)
Place Light Probes with a script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-and-scene-loading.html)
Load Light Probes in multiple scenes
# Set a GameObject to use light from Light Probes
To use **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) on your moving GameObjects, the **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) component on the moving **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) must be set correctly. The **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer component has a **Light Probes** setting which is set to **Blend Probes** by default. This means that by default, all GameObjects will use light probes and will blend between the nearest probes as it changes position in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
You can change this setting to either “off” or “use proxy volume”. Switching the light probes setting to off will disable the light probe’s effect on this GameObject.
Light Probe Proxy Volumes are a special setting which you can use for situations where a **large moving object** might be too big to be sensibly lit by the results of a single tetrahedron from the **light probe group** A component that enables you to add Light Probes to GameObjects in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeGroup), and instead needs to be lit by multiple groups of light probes across the length of the model. See **Light Probe Proxy Volumes** A component that allows you to use more lighting information for large dynamic GameObjects that cannot use baked lightmaps (for example, large Particle Systems or skinned Meshes). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeProxyVolume) for more information.
The other setting in the Mesh Renderer **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) which relates to light probes is the **Anchor Override** setting. As described previously, when a GameObject moves through your scene, Unity calculates which tetrahedron the GameObject falls within from the volume defined by the light probe groups. By default this is calculated from the centre point of the Mesh’s bounding box, however you can override the point that is used by assigning a different GameObject to the **Anchor Override** field.
If you assign a different GameObject to this field, it is up to you to move that GameObject in a way that suits the lighting you want on your mesh.
The anchor override may be useful when a GameObject contains two separate adjoining meshes; if both meshes are lit individually according to their bounding box positions then the lighting will be discontinuous at the place where they join. This can be prevented by using the same Transform (for example the parent or a child object) as the interpolation point for both Mesh Renderers or by using a Light Probe Proxy Volume.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Placing-Scripting.html)
Place Light Probes with a script
[](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-and-scene-loading.html)
Load Light Probes in multiple scenes
