* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Avatar.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Models](https://docs.unity3d.com/6000.0/Documentation/Manual/models.html)
  * [Importing models into Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/models-importing.html)
  * [Model Import Settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html)
  * [Rig tab](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html)
  * Avatar Mapping tab


[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html)
Rig tab
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MuscleDefinitions.html)
Avatar Muscle & Settings tab
# Avatar Mapping tab
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Avatar.html "Go to Avatar page in the Scripting Reference")
The Avatar Mapping tab is available when the Unity Editor is in Avatar Configuration mode.
To enter Avatar Configuration mode, either:
  * select the Avatar Asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), and click “Configure Avatar” in the Inspector, or
  * select the Model Asset in the Project window, go to the “Rig” tab in the Inspector, and click “Configure…” under the Avatar Definition menu.


When you are in Avatar Configuration mode, the **Avatar Mapping** tab appears in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) displaying Unity’s bone mapping:
![The Avatar window displays the bone mapping](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/classAvatar-Inspector.png) The Avatar window displays the bone mapping
**(A)** Buttons to toggle between the **Mapping** and **Muscles & Settings** tabs. You must **Apply** or **Revert** any changes made before switching between tabs.
**(B)** Buttons to switch between the sections of the Avatar: **Body** , **Head** , **Left Hand** , and **Right Hand**.
**(C)** Menus which provide various **Mapping** and **Pose** tools to help you map the bone structure to the Avatar.
**(D)** Buttons to accept any changes made (**Accept**), discard any changes (**Revert**), and leave the Avatar window (**Done**). You must **Apply** or **Revert** any changes made before leaving the **Avatar** An interface for retargeting animation from one rig to another. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ConfiguringtheAvatar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Avatar) window.
The Avatar Mapping indicates which of the bones are required (solid circles) and which are optional (dotted circles). Unity can interpolate optional bone movements automatically. 
## Saving and reusing Avatar data (Human Template files)
You can save the mapping of bones in your skeleton to the Avatar on disk as a [Human Template file](https://docs.unity3d.com/6000.0/Documentation/Manual/class-HumanTemplate.html) (extention `*.ht`). You can reuse this mapping for any character. For example, you want to put the Avatar mapping under source control and you prefer to commit text-based files; or perhaps you want to parse the file with your own custom tool.
To save the Avatar data in a **Human Template** A pre-defined bone-mapping. Used for matching bones from FBX files to the Avatar. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-HumanTemplate.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Humantemplate) file, choose **Save** from the **Mapping** drop-down menu at the bottom of the **Avatar** window. 
![The Mapping drop-down menu at the bottom of the Avatar window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/MecanimMappingMenus.png) The **Mapping** drop-down menu at the bottom of the **Avatar** window
Unity displays a dialog for you to choose the name and location of the file to save.
To load a Human Template file previously created, choose **Mapping** > **Load** and select the file you want to load.
## Using Avatar Masks
Sometimes it is useful to restrict an animation to specific body parts. For example, an walking animation might involve the character swaying their arms, but if they pick up a torch, they should hold it up to cast light. You can use an **Avatar Body Mask** to specify which parts of a character an animation should be restricted to. See documentation on [Avatar Masks](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AvatarMask.html)A specification for which body parts to include or exclude for an animation rig. Used in Animation Layers and in the importer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AvatarMask.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AvatarMask) for further details.
Avatar
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FBXImporter-Rig.html)
Rig tab
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MuscleDefinitions.html)
Avatar Muscle & Settings tab
