* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-creating.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-scenes.html)
  * [Scene Templates](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates.html)
  * Creating scene templates


[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates.html)
Scene Templates
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html)
Editing scene templates
# Creating scene templates
You can create a new **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) template in one of the following ways:
  * Start an [empty template](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-creating.html#creating-an-empty-scene-template).
  * Create a template [from an existing scene asset](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-creating.html#creating-a-template-from-an-existing-scene-asset).
  * Create a template [from the current scene](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-creating.html#creating-a-template-from-the-current-scene).


After you create a template, you can [edit its properties](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html) or [create new scenes from it](https://docs.unity3d.com/6000.0/Documentation/Manual/scenes-working-with.html#creating-a-new-scene-from-the-new-scene-dialog).
**Tip:**  
---  
Before you create a template from a scene, create a folder with the same name as the scene, and put any assets you want to clone in it. When you create the template, Unity automatically enables the **Clone** property for those assets. For details, see [Editing scene templates](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html).  
## Creating an empty scene template
You can create empty scene templates and configure them later. An empty template does not appear in the New Scene dialog until you [edit its properties](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html) to associate a scene asset to it. 
To create an empty scene template in the current project folder:
  * From the menu, select **Assets > Create > Scene Template**.


To create an empty scene template in a specific project folder:
  1. Do one of the following:
  2. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), right-click the folder to open the context menu.
  3. Open the folder in the Project window, and right-click the asset pane to open the context menu.
  4. Select **Create > Scene Template**.


## Creating a template from an existing scene asset
You can turn any existing scene into a scene template. After you create a template from an existing scene, you might want to [edit its properties](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html) to specify which of its dependencies Unity clones when you create a new scene from it.
To create a template from an existing scene asset, open the Project window, and do one of the following:
  * Right-click a scene asset to open the context menu. Then select **Create > Scene Template From Scene**.
  * Select the scene asset, and from the main menu, select **Assets > Create > Scene Template From Scene**.


## Creating a template from the current scene
To create a scene template from the current scene, from the menu, select **File > Save As Scene Template**.
If you have unsaved changes, Unity prompts you to save the scene before it saves the template.
After you create a template from the current scene, you might want to [edit its properties](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html) to specify which of its dependencies Unity clones when you create a new scene from it.
## Creating templates from C# scripts
You can create scene templates from your C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
To create an empty scene template, use the [**CreateSceneTemplate** method](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.CreateSceneTemplate.html).
```
SceneTemplate.CreateSceneTemplate(string sceneTemplatePath)

```

To create a template from an existing scene, use the [**CreateTemplateFromScene** method](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.CreateTemplateFromScene.html). Unity automatically associates the scene with the template, and extracts the scene’s dependencies.
```
SceneTemplate.CreateTemplateFromScene(SceneAsset sourceSceneAsset, string sceneTemplatePath);

```

* * *
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates.html)
Scene Templates
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-templates-editing.html)
Editing scene templates
