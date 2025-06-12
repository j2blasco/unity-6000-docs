* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2DAnd3DModeSettings.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * 2D and 3D mode settings


[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
Editor Features
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html)
Preferences
# 2D and 3D mode settings
When creating a new Project, you can specify whether to start the Unity Editor in 2D mode or 3D mode. However, you also have the option of switching the Editor between 2D mode and 3D mode at any time. You can read more about [the difference between 2D and 3D Projects here](https://docs.unity3d.com/6000.0/Documentation/Manual/2Dor3D.html). This page provides information about how to switch modes, and what exactly changes within the editor when you do.
## Switching between 3D and 2D modes
To change modes between 2D or 3D mode:
  1. Open the [Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html) settings (top menu: **Edit > Project Settings**, then select the **Editor** category).
  2. Then set **Default Behavior Mode** to either **2D** or **3D**.

![Use the Default Behavior Mode setting in the Editor settings to set the Project to 2D or 3D](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/BehaviorMode.png) Use the Default Behavior Mode setting in the Editor settings to set the Project to 2D or 3D
## 2D vs 3D mode settings
2D or 3D mode determines some settings for the Unity Editor. These are listed below.
### In 2D Project mode:
  * Any images you import are assumed to be 2D images (**Sprites**) and set to **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) mode.
  * The **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) is set to 2D.
  * The default game objects do not have real time, directional light.
  * The **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s default position is at 0,0,–10. (It is 0,1,–10 in 3D Mode.)
  * The camera is set to be **Orthographic**. (In 3D Mode it is **Perspective**.)
  * In the Lighting Window: 
    * **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) is disabled for new **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
    * **Ambient Source** is set to **Color**. (With the color set as a dark grey: RGB: 54, 58, 66.)
    * **Realtime Global Illumination** (Enlighten) is set to off.
    * **Baked Global Illumination** is set to off.
    * **Auto-Building** set to off.


### In 3D Project mode:
  * Any images you import are NOT assumed to be 2D images (**Sprites**).
  * The **Scene View** is set to 3D.
  * The default game objects have real time, directional light.
  * The camera’s default position is at 0,1,–10. (It is 0,0,–10. in 2D Mode.)
  * The camera is set to be **Perspective**. (In 2D Mode it is **Orthographic**.)
  * In the Lighting Window: 
    * **Skybox** is the built-in default **Skybox Material**.
    * **Ambient Source** is set to **Skybox**.
    * **Realtime Global Illumination** (Enlighten) is set to on.
    * **Baked Global Illumination** is set to on.
    * **Auto-Building** is set to on.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
Editor Features
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html)
Preferences
