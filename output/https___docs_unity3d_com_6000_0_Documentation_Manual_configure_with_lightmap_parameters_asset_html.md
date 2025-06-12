* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configure-with-lightmap-parameters-asset.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * Save and load lighting settings with Lightmap Parameters Assets


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Reference.html)
Light Probes reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html)
Shadows
# Save and load lighting settings with Lightmap Parameters Assets
A **Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) Parameters Asset contains a set of values for the parameters that control Unity’s lighting features. These Assets allow you to define and save different sets of values for lighting, for use in different situations.
Lightmap Parameters Assets allow you to quickly create presets optimized for different types of **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), or for different platforms and different Scene types (for example, indoor or outdoor Scenes).
## Creating a Lightmap Parameters Asset
To create a new Lightmap Parameters Asset, right-click in the Project window and go to **Create** > **Lightmap Parameters**. Unity stores this in your Project folder.
## Assigning Lightmap Parameters Assets
### Scenes
To assign a Lightmap Parameters Asset to the whole Scene:
  1. Open the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html) (**Window** > **Rendering** > **Lighting**)
  2. Click the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) tab
  3. Navigate to the **Lightingmapping Settings**.
  4. Use the **Lightmap Parameters** drop-down to assign a default Lightmap Parameters Asset. This drop-down lists all available Lightmap Parameters Assets.


### GameObjects
To assign a Lightmap Parameters Asset to a single GameObject, ensure the GameObject has a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer or **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) component attached.
To assign a Lightmap Parameters Asset to a **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) component:
  1. In the Inspector, go to **Mesh Renderer** > **Lighting**
  2. Enable **Contribute Global Illumination**
  3. In the mesh Renderer component, go to **Lightmapping** > **Lightmap Parameters**.
  4. Select an option from the menu. Select **Scene Default Parameter** to use the same Lightmap Parameters Asset that’s assigned to the whole Scene.


To assign a Lightmap Parameters Asset to a Terrain component:
  1. In the Inspector, go to **Terrain** > **Terrain Settings** > **Lighting**
  2. Enable **Contribute Global Illumination**
  3. In **Terrain Settings** , go to **Lightmapping** > **Lightmap Parameters**.
  4. Select an option from the menu. Select **Scene Default Parameter** to use the same Lightmap Parameters Asset that’s assigned to the whole Scene.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Reference.html)
Light Probes reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html)
Shadows
