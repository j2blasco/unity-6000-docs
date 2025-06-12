* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Baking lightmaps before runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html)
  * Set up your scene and lights for baking


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmappers.html)
Introduction to lightmaps and baking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-preview.html)
Preview baked lighting
# Set up your scene and lights for baking
Select **Window** > **Rendering** > **Lighting** from the Unity Editor menu to open the Lighting window. Make sure any Mesh you want to apply a lightmap to has proper UVs for lightmapping. The easiest way to do this is to open the [Mesh import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Model.html) and enable the **Generate Lightmap UVs** setting.
Next, to control the resolution of the **lightmaps** , go to the **Lightmapping Settings** section and adjust the **Lightmap Resolution** value. 
To be included in your lightmap, Renderers must meet the following criteria:
  * Have a **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) or **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) component
  * Be marked as [**Contribute GI**](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html)
  * Use a built-in Unity Material or **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that supports lightmaps, or a shader in the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) with a [Meta Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/MetaPass.html).


You can adjust settings for Lights in the [Light Explorer](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingExplorer.html). To open the Light Explorer, go to **Window** > **Rendering** > **Light Explorer**.
### Static versus Dynamic
No matter which **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) system you use, Unity will only consider objects that are marked as [“Contribute GI”](https://docs.unity3d.com/Manual/StaticObjects.html) during the baking/precomputing of the lighting. Dynamic (i.e. non-static) objects have to rely on the Light Probes you placed throughout the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) to receive indirect lighting.
Because the baking/precomputing of the lighting is a relatively slow process, only large and complex assets with distinct lighting variations, such as concavity and self-shadowing, should be tagged as “Contribute GI”. Smaller and convex meshes that receive homogeneous lighting should not be marked as such, and they should, therefore, receive indirect lighting from the [Light Probes](https://docs.unity3d.com/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) which store a simpler approximation of the lighting. Larger dynamic objects can rely on [LPPVs](https://docs.unity3d.com/Manual/class-LightProbeProxyVolume.html), in order to receive better localized indirect lighting. Limiting the number of objects tagged as “Contribute GI” in your scene is absolutely crucial to minimize baking times while maintaining an adequate lighting quality. You can learn more about this optimization process and the importance of Probe lighting in this [tutorial](https://unity3d.com/learn/tutorials/topics/graphics/introduction-precomputed-realtime-gi?playlist=17102).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmappers.html)
Introduction to lightmaps and baking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-preview.html)
Preview baked lighting
