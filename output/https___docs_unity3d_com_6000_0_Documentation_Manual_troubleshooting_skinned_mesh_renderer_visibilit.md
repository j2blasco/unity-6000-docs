* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/troubleshooting-skinned-mesh-renderer-visibility.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * Troubleshooting Skinned Mesh Renderer visibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html)
Mesh asset Inspector window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
Prefabs
# Troubleshooting Skinned Mesh Renderer visibility
Unity uses the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh)’s bounds to determine whether to render it. If the entire **bounding volume** A closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Boundingvolume) is outside the view of any active **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), Unity does not render the mesh.
In the case of a Skinned **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer), its mesh bounds change as it deforms. Unity accounts for all animations present at import time when it calculates the maximum bounding volume, and uses this value to determine visibility; however, the following situations that occur after import might push vertices or bones outside of the maximum known bounds:
  * Additive animations
  * Changing the positions of bones from a script at runtime
  * Using vertex **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that change vertex positions
  * Using ragdolls


If this happens, Unity might not correctly determine the visibility of the mesh, and might fail to show it when expected.
In these cases, you can try either of the following solutions to fix the problem:
  * Modify the bounds to match the maximum potential bounding volume of your mesh. Use this option if possible, because it is better for performance.
  * Enable **Update When Offscreen** , so that Unity continues to calculate the mesh bounds at all times, even when the mesh is not visible. Use this option if performance is not a major concern, or if you can’t predict the size of your bounding volume (for example, if you use ragdolls).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html)
Mesh asset Inspector window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)
Prefabs
