* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * [Scene Templates](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates.html)
  * Editing scene templates


[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-creating.html)
Creating scene templates
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-customizing-scene-instantiation.html)
Customizing new scene creation
# Editing scene templates
To edit a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) template, select it in the [Project window](https://docs.unity3d.com/Manual/ProjectView.html)A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), then open it in an [Inspector window](https://docs.unity3d.com/Manual/UsingTheInspector.html).
**Note** : When you first create an [empty scene template](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-creating.html#creating-an-empty-scene-template), you must edit its properties to associate it with a scene before you can use it. Templates that you create from the active scene, or an existing scene asset, have some properties set by default.
![The Inspector window displays the properties of a scene template asset.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/scene-template-inspector.png)  

The scene template **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) has the following sections:
  1. **[Details](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html#details)** : Specifies which scene the template uses, and contains the template description that appears in the New Scene dialog.
  2. **[Thumbnail](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html#thumbnail)** : Provides options for creating a preview image for the template.
  3. **[Scene Template Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html#scene-template-pipeline)** : Specifies an optional custom script to run when Unity creates a new scene from the template.
  4. **[Dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html#dependencies)** : Lists the template scene’s dependencies, and specifies whether Unity clones them when it creates a new scene from the template.


### Details
Use the Details section to specify which scene to use for a template, and control how the template appears in the [New Scene dialog](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html#new-scene-dialog).
![The Details section of the scene template Inspector window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/scene-template-inspector-details.png)  

**Property:** | **Description:**  
---|---  
**Template Scene** | Specifies the scene to use as a template. This can be any scene in the Project.  
**Title** | The template name. The name you enter here appears in the [New Scene dialog](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html#new-scene-dialog).  
**Description** | The template description. The description you enter here appears in the [New Scene dialog](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html#new-scene-dialog).  
**Pin in New Scene Dialog** | Controls whether this template is pinned in the [New Scene dialog](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html#new-scene-dialog).  
  
Pinned templates always appear at the top of the **Scene Templates in Project** list.  
### Thumbnail
The Thumbnail section contains options for creating a preview image for the template.
![The Thumbnail section of the scene template Inspector window.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/scene-template-inspector-thumbnail.png)  

**Property:** | **Description:**  
---|---  
**Badge** | Specifies a Texture asset to use as a badge thumbnail for this template. You can use any Texture asset in the project. Badge thumbnails are commonly used as a quick way to identify what type of scene this template relates to, for example: 2D or 3D.  
**Preview** | Specifies a texture to use as a preview thumbnail for this template. You can use any Texture asset in the project. The preview image appears in the New Scene dialog when selecting a scene template.  
**Snapshot** | Provides options for capturing a thumbnail image for this template. Select a **View** to take the snapshot from. The following options are available: 
  * **Main Camera**
  * **Game View**

Click the **Take Snapshot** button to capture the selected **View**.  
### Scene Template Pipeline
Use these properties to add a **Scene Template Pipeline** script to this template.
![The Inspector window displays the Scene Template Pipeline section of the properties for a scene template asset.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/scene-template-inspector-pipeline.png)  

A Scene Template Pipeline script lets you execute custom code when you create a new scene from the template. See [Customizing new scene creation](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-customizing-scene-instantiation.html).
### Dependencies
This section lists all of the template scene’s **Dependencies**. You can specify whether or not to **Clone** each dependency when you [create a new scene from the template](https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html).
To search for a dependency by name, enter text in the search bar.
To sort the **Dependencies** list:
  * Click the **Dependencies** heading to sort by the name of the dependency in alphabetical order.
  * Click the **Type** heading to sort by the dependency Type.
  * Click the **Clone** heading to sort by dependencies that are cloned and not cloned.


![The Inspector window displays the Dependencies section of the properties for a scene template asset.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Scene-template-inspector-dependencies.png)  

For each dependency in the list, toggle the **Clone** option on to clone the dependency, or off to reference the dependency. When you clone a dependency, you create a copy. When you reference a dependency, all changes made to the original will affect the dependency.
When you create a new scene from the template, Unity checks whether the template scene has cloneable dependencies. If it does, Unity creates a folder with the same name as the new scene, and puts any cloned dependencies in that folder.
For more information about cloned and referenced dependencies, see [Templates and scene dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates.html#templates-and-scene-dependencies).
To specify which types of asset Unity clones by default, edit the [scene template Project settings](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-settings.html).
* * *
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-creating.html)
Creating scene templates
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-customizing-scene-instantiation.html)
Customizing new scene creation
