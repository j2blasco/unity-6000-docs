* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ModelingOptimizedCharacters.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Creating models outside of Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingDCCAssets.html)
  * Creating models for optimal performance


[](https://docs.unity3d.com/6000.0/Documentation/Manual/models-preparing.html)
Preparing your model files for export
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingHumanoidChars.html)
Creating models for animation
# Creating models for optimal performance
Here are a few tips for creating models for optimal performance. Some of these tips apply to all models, and some apply only to animated models:
  * [Minimize the polygon count](https://docs.unity3d.com/6000.0/Documentation/Manual/ModelingOptimizedCharacters.html#polygons)
  * [Use as few Materials as possible](https://docs.unity3d.com/6000.0/Documentation/Manual/ModelingOptimizedCharacters.html#mats)
  * [Use a single skinned Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/ModelingOptimizedCharacters.html#single)
  * [Use as few bones as possible](https://docs.unity3d.com/6000.0/Documentation/Manual/ModelingOptimizedCharacters.html#bones)
  * [Keep forward and inverse kinematics separate](https://docs.unity3d.com/6000.0/Documentation/Manual/ModelingOptimizedCharacters.html#ikfk)


Using these techniques might help increase the animation and rendering speed of your models, but be aware that they might also reduce the visual fidelity and realistic effects you are trying to achieve. There is no single answer for every situation that can produce a perfect balance between better performance and visual realism. You have to find the perfect balance according to the complexity of your characters and your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), vs. the overall appearance and realism that you require. 
## Minimize the polygon count
The number of polygons you should use depends on the visual quality you require and the platform you are targeting. These two competing facts are equally true:
  * The fewer the polygons you use in your meshes, the faster your application runs. This is because every vertex, edge, or face requires computing resources.
  * The more polygons you use in your Meshes, the more detailed and organic your **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) look, because smaller polygons give you more control over the shape.


Also consider what else is competing for rendering resources. If you have a lot of GameObjects or **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) objects on screen at the same time, consider reducing the polygon count per meshes.
Note that the actual number of vertices that graphics hardware has to process is usually not the same as the number reported by a modelling application. Modeling applications usually display the number of distinct corner points that make up a model (known as the geometric vertex count). For a graphics card, however, some geometric vertices need to be split into two or more logical vertices for rendering purposes: for example, a vertex must be split if it has multiple normals, UV coordinates or vertex colors. Consequently, the vertex count in Unity is usually higher than the count given by the 3D application.
## Use as few materials as possible
Keep the number of [materials](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) on each model as low as possible. Only use more than one material on a character when you need to use different **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) for different parts; for example, you might use a special shaders for the eyes on a character model.
## Use a single skinned mesh
For animated character models that use a [Skinned Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html), you should use only one of these components per character. Unity’s animation system optimizes animation using visibility culling and **bounding volume** A closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Boundingvolume) updates. It only activates these optimizations if you use one [Animation component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animation.html) and one Skinned **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer on a model.
Using two skinned meshes in place of a single one could roughly double the rendering time for a model, and there is seldom any practical advantage in using multiple meshes.
## Use as few bones as possible
In general, the fewer bones you use, the better the performance is. However, sometimes you need to create character models with a large number of bones: for example, when you want a lot of customizable attachments. These extra bones increase the size of the build, and may have a relative processing cost for each additional bone. For example, 15 additional bones on a rig that already has 30 bones takes Unity 50% more operations to solve in **Generic** mode, which might impact the time it takes to solve. 
Note that you can have additional bones for [Generic](https://docs.unity3d.com/6000.0/Documentation/Manual/GenericAnimations.html) and [Humanoid](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html) types. When you have no animations playing using the additional bones, the processing cost should be negligible. This cost is even lower if their attachments are non-existent or hidden.
For performance reasons, use linear blend ****skinning** The process of binding bone joints to the vertices of a character’s mesh or ‘skin’. Performed with an external tool, such as Blender or Autodesk Maya. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingHumanoidChars.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skinning)** with a maximum of four influences per vertex. However, some 3D modeling applications allow more than four bones to influence vertices, so you have to weigh the performance cost against greater control. 
## Keep forward and inverse kinematics separate
When Unity imports animations, it bakes a Model’s inverse kinematic (IK) nodes into forward **kinematics** The geometry that describes the position and orientation of a character’s joints and bodies. Used by inverse kinematics to control character movement.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#kinematics) (FK), and so Unity doesn’t need the IK nodes at all. However, if they are left in the model, then Unity still includes them in calculations, even though they don’t affect the animation. You can either delete the redundant IK nodes in Unity or in your 3D modeling application. To facilitate removing the IK nodes, keep separate IK and FK hierarchies while modeling.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/models-preparing.html)
Preparing your model files for export
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingHumanoidChars.html)
Creating models for animation
