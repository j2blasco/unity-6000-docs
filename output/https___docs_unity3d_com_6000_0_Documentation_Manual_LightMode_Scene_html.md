* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightMode-Scene.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Light sources](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-sources.html)
  * [Light components](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-components.html)
  * [Configuring Light components](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-components-configuring.html)
  * [Configuring Mixed lights with Lighting Modes](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-landing.html)
  * Set the Lighting Mode of a scene


[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html)
Lighting Mode
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-runtime.html)
Adjust Mixed lights at runtime
# Set the Lighting Mode of a scene
  1. Select the [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html) for the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), navigate to **Mixed Lighting**.
  3. Use the drop-down menu to set the **Lighting Mode**.


If your project uses the High-Definition **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (HDRP), follow the instructions in the [HDRP Shadowmask Lighting Mode](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Shadows-in-HDRP.html%23shadowmasks) documentation instead.
## Match shadow colors in Subtractive mode
When you set a Scene’s Lighting Mode to Subtractive, Unity displays the **Realtime Shadow Color** property in the Lighting window. Unity uses this color when it combines real-time shadows with baked shadows. Change this value to approximate the color of the indirect lighting in your Scene, to better match the real-time shadows with the baked shadows.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html)
Lighting Mode
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-runtime.html)
Adjust Mixed lights at runtime
