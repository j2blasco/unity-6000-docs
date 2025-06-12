* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-configuration.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html)
  * Enable or disable shadows


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html)
Shadows
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-realtime.html)
Real-time shadows
# Enable or disable shadows
You can configure the real-time and baked shadow settings for each [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html) using the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
Each [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) also has a **Cast Shadows** and a **Receive Shadows** property, which must be enabled as required.
Enable **Cast Shadows** by selecting **On** from the drop-down menu to enable or disable shadow casting for the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh). Alternatively, select **Two Sided** to allow shadows to be cast by either side of the surface (so backface culling is ignored for shadow casting purposes), or **Shadows Only** to allow shadows to be cast by an invisible **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html)
Shadows
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-realtime.html)
Real-time shadows
