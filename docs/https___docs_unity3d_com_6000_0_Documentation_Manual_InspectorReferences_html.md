* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorReferences.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)
  * [Manage components and their values](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorManageComponents.html)
  * Manage references


[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorManageComponents.html)
Manage components and their values
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-advanced-object-picker.html)
Use the Advanced Object Picker
# Manage references
References are properties that use a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), a component, or an asset as an input. 
For example, on a 3D GameObject:
  * The [Mesh Filter](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)A mesh component that takes a mesh from your assets and passes it to the Mesh Renderer for rendering on the screen. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshFilter) component, which gives the mesh its shape, refers to a [mesh](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html)The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) asset.
  * The **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) component refers to a material.


Components can have default references, or you might need to add a reference manually. For example:
  * If you create a new 3D Cube GameObject, its Mesh Filter and Mesh Renderer components have default references to the Cube mesh and your project’s default material. You can replace these, but you don’t have to.
  * If you create an empty GameObject and add the Mesh Filter and Mesh Renderer components, they don’t refer to the default mesh or material. You must add those references manually.


## Assigning references
To assign a reference to a property, in the property field in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window, do one of the following:
  * From the **Hierarchy** or **Project** windows, drag a compatible item into the field.
  * To open a search window for the property field, select **Object Picker** (⊙). The search window filters for references that match the property type.
There are two types of reference search windows: classic and advanced. The advanced search shows the built-in filter, so you can override it. The classic view doesn’t allow this override. For more information about the advanced search and how to toggle it on or off, refer to [Search Object Picker](https://docs.unity3d.com/6000.0/Documentation/Manual/search-advanced-object-picker.html).


## Component-dependent references
You can assign a GameObject to a property field that expects a component reference. When you assign this GameObject, Unity uses the first component of the required type from that GameObject. In the **Inspector** window, the first component is the one at the top of the list.
If the GameObject doesn’t have the right component type, you can’t assign the GameObject as the reference. For example, if the reference field requires a Sphere **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider), and you try to assign a GameObject that only has a **Box Collider** A cube-shaped collider component that handles collisions for GameObjects like dice and ice cubes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#boxcollider), the Unity Editor doesn’t accept that assignment. 
## Additional references
  * [Search Object Picker](https://docs.unity3d.com/6000.0/Documentation/Manual/search-advanced-object-picker.html)
  * [The Hierarchy window](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorManageComponents.html)
Manage components and their values
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-advanced-object-picker.html)
Use the Advanced Object Picker
