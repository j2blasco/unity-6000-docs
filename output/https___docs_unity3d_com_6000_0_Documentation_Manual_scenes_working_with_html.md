* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * Creating, loading, and saving Scenes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)
Introduction to scenes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MultiSceneEditing.html)
Work with multiple scenes in Unity
# Creating, loading, and saving Scenes
This page explains how to [create](https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html#creating-a-new-scene), [load](https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html#loading-scenes), and [save](https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html#saving-scenes) **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
## Creating a new scene
There are several ways to create a new scene:
  * Use the [New Scene dialog](https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html#creating-a-new-scene-from-the-new-scene-dialog) to create a new scene from a specific scene template.
  * Use the [menu](https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html#creating-a-new-scene-from-the-menu) or the [Project window](https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html#creating-a-new-scene-from-the-project-window)A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) to create new scenes from your Project’s Basic scene template without opening the New Scene dialog.
  * Create a scene from a specific template directly [from a C# script](https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html#creating-a-new-scene-from-a-csharp-script).


Unity creates every new scene from a scene template. For information about creating and managing scene templates, see [Scene templates](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates.html).
### Creating a new scene from the New Scene dialog
Use the New Scene dialog to create new scenes from specific scene templates in your Project. You can also use the New Scene dialog to find and manage scene templates. For details see [The New Scene dialog](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html#new-scene-dialog).
By default, the New Scene dialog opens when you create a new scene from the menu (**File** > **New Scene**) or by using a shortcut (**Ctrl/Cmd + n**).
To create a new Scene:
  1. Select a template from the list.
  2. If you want Unity to load the new scene additively (see note below), enable **Load Additively**.
  3. Click **Create** to create a new scene from the template.

**Note:**  
---  
Additive loading means that Unity loads the scene in addition to any other scenes you have open. For more information, see [Multi-Scene editing](https://docs.unity3d.com/6000.0/Documentation/Manual/MultiSceneEditing.html).  
If the template does not have any [cloneable dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates.html#templates-and-scene-dependencies), Unity loads the new scene in memory, but does not save it.
If the template has [cloneable dependencies](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates.html#templates-and-scene-dependencies), Unity prompts you to choose a location in the Project to save it to. When you save the scene, Unity creates a folder in the same location, and with the same name as the new scene. It then clones the cloneable dependencies into the new folder, and updates the new scene to use the cloned assets instead of the original assets used by the template scene.
### Creating a new scene from the menu:
Use the menu (**Assets** > **Create** > **Scene**) to create a new scene without opening the New Scene dialog.
When you create a new scene from the menu, Unity automatically copies the project’s Basic template, and adds the new scene to whichever folder is currently open in the project window.
### Creating a new scene from the project window
Use the context menu in the Project window to create a new scene without opening the New Scene dialog.
  1. Navigate to the folder where you want to create the new scene.
  2. Right click the folder in the left-hand pane, or right-click an empty area in the right hand pane, and select **Create** > **Scene** from the context menu.


When you create a new scene from the menu, Unity automatically copies the project’s Basic template, and adds the new scene to the selected folder.
### Creating a new scene from a C# script
To create a new scene from a C# script using a specific scene template, use the [**Instantiate** method](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.Instantiate.html).
```
Tuple<Scene, SceneAsset> SceneTemplate.Instantiate(SceneTemplateAsset sceneTemplate, bool loadAdditively, string newSceneOutputPath = null);

```

The `Instantiate` method instantiates a new scene from a scene template. It returns the newly created `Scene` handle, and its matching `SceneAsset`. You can create this scene additively. If the scene contains [assets that need to be cloned](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates.html#templates-and-scene-dependencies), you must provide a path for Unity to save the scene to disk.
#### New scene events
When you create a new scene from a template, either from a script or using the New Scene dialog, Unity triggers an [event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService-newSceneTemplateInstantiated.html). Unity triggers this event after the template is instantiated, and also after it triggers the [`EditorSceneManager.newSceneCreated`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-newSceneCreated.html) or [`EditorSceneManager.sceneOpened`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneOpened.html) events.
```

public class SceneTemplate
{
    public delegate void NewTemplateInstantiated(SceneTemplateAsset sceneTemplateAsset, Scene scene, SceneAsset sceneAsset, bool additiveLoad);

    public static event NewTemplateInstantiated newSceneTemplateInstantiated;
}

```

## Loading scenes
To open a scene, do one of the following:
  * In the Project window, double-click the scene asset.
  * From the menu, select **File** > **Open Scene**.
  * From the menu, select **File** > **Recent Scenes** and select the name of the scene.


If your current scene contains unsaved changes, Unity prompts you to save the scene or discard the changes.
### Opening multiple scenes at once
You can open multiple scenes for editing at the same time. For details, see [Multi-Scene editing](https://docs.unity3d.com/6000.0/Documentation/Manual/MultiSceneEditing.html).
## Saving scenes
To save the scene you’re currently working on, choose **File** > **Save Scene** from the menu, or press Ctrl + S (Windows) or Cmd + S (macOS).
![Saved scene assets visible in the Project window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SceneAssetsInProjectView_01.png) Saved scene assets visible in the Project window
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)
Introduction to scenes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MultiSceneEditing.html)
Work with multiple scenes in Unity
