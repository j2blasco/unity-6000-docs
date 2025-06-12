* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Components.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Components](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-components.html)
  * Introduction to components


[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-components.html)
Components
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)
Use components
# Introduction to components
**Components** are the functional pieces of every **GameObject**. Components contain properties which you can edit to define the behavior of a GameObject. For more information on the relationship between components and GameObjects, see [GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).
To view a list of the components attached to a GameObject in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, select a GameObject in either the Hierarchy window or the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view.
You can attach many components to a GameObject, but every GameObject must have one and only one Transform component. This is because the Transform component dictates the GameObject’s location, rotation, and scale. To create an empty GameObject, select **GameObject** > **Create Empty**. When you select the new GameObject, the Inspector displays the Transform component with default values.
![Empty GameObjects have a Transform component](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/EmptyGO1.png) Empty GameObjects have a Transform component
A component must be in the same project as the GameObject you want to attach it to. A component can be specific to a package or created by a script. The Unity Editor can’t search for components from:
  * Other projects.
  * **Scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) that are not attached to the project.
  * [Packages](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)Packages are collections of assets to be shared and re-used in Unity. The [Unity Package Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui.html) (UPM) can display, add, and remove packages from your project. These packages are native to the Unity Package Manager and provide a fundamental method of delivering Unity functionality. However, the Unity Package Manager can also display [Asset Store packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePackages.html) that you downloaded from the Asset Store. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Packages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Packages) that haven’t been added to the project.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-components.html)
Components
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)
Use components
