* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/PrepShader.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * Prepare and upgrade sprites for 2D lighting in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Setup.html)
Set up the 2D Renderer asset in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d/tilemap-renderer-2d-renderer.html)
Enable 2D lighting with the Tilemap Renderer in URP
# Prepare and upgrade sprites for 2D lighting in URP
Prepare your **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) and existing materials to be lit by 2D lighting.
To light a sprite with [2D lights](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DLightProperties.html), first go to the [Sprite Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteRenderer) component of the sprite and assign a material with a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that reacts to 2D lights. When you drag sprites onto the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), Unity automatically assigns the `Sprite-Lit-Default` material to them which enables them to interact and appear lit by 2D lights.
You can also [create a custom Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/ShaderGraph.html) that reacts to lights with the [Shader Graph package](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest).
## Upgrading existing materials
If you are installing the URP package into an existing project with preexisting **prefabs** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab), materials or scenes, you will need to upgrade any materials used to a lighting compatible Shader if you want to use the package’s 2D lighting features. 
**Warning:** The following task automatically upgrades a scene or project in a one way process. Unity can’t revert upgraded scenes or projects to their previous state. Before you start this task, back up any files you don’t want to lose or converted.
To upgrade your project, go to **Window > Rendering > Render Pipeline Converter**. Enable **Material Upgrade** and then select **Convert Assets** to begin the upgrade.
For information on converting assets made for a Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) project to assets compatible with 2D URP, refer to [Render Pipeline Converter](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rp-converter.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Setup.html)
Set up the 2D Renderer asset in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d/tilemap-renderer-2d-renderer.html)
Enable 2D lighting with the Tilemap Renderer in URP
