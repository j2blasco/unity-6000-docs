* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/setup-project-2d-game.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-game-development-landing.html)
  * Setup a project for 2D games


[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-game-development-landing.html)
2D game development
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-game-creation-wokflow.html)
2D game creation workflow
# Setup a project for 2D games
**Note** : For this guide, Unity recommends and assumes that you choose the [Universal Render Pipeline (URP)](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html) and not the [Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html).
  1. Install Unity version 2019 LTS or a later version; see [Installing Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/GettingStartedInstallingUnity.html).
  2. Create a new project with the [2D template](https://docs.unity3d.com/hub/manual/Templates.html).
  3. In the Package Manager, install the latest [URP package](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-introduction.html) version; see [Installing the Universal Render Pipeline into an existing Project](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html).
  4. Install any optional packages you need; see [Installing packages](https://docs.unity3d.com/6000.0/Documentation/Manual/setup-project-2d-game.html#InstallingPackages).


## Installing packages 
Most packages you need to make a 2D game in Unity are included in the Unity Editor. The following table lists the packages included by default when you choose the [2D template](https://docs.unity3d.com/hub/manual/Templates.html):
**Package** | **Description**  
---|---  
[2D Animation](https://docs.unity3d.com/Packages/com.unity.2d.animation@latest) | 2D Animation provides the necessary tooling and runtime components for applying skeletal animation to your **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite).  
[2D Pixel Perfect](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect.html) | The 2D **Pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) Perfect package contains the Pixel Perfect **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) component, which ensures your pixel art remains crisp and clear at different resolutions, and stable in motion. A standalone [2D Pixel Perfect package](https://docs.unity3d.com/Packages/com.unity.2d.pixel-perfect@latest) that doesn’t require the URP is available if you want to use this package in a project using the [Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html) instead.  
[2D PSD Importer](https://docs.unity3d.com/Packages/com.unity.2d.psdimporter@latest) | The 2D PSD Importer package allows you to import multilayered PSD files from Photoshop. You can use this for your Sprites, or to rig your characters.  
[2D Sprite](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html) | The Sprite Editor provides an in-Editor environment to create and edit Sprite assets. Sprite Editor lets you add custom behavior for editing Sprite-related data.  
[2D SpriteShape](https://docs.unity3d.com/Packages/com.unity.2d.spriteshape@latest) | 2D Sprite Shape allows you to create organic shapes and **terrains** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain), similar to a vector drawing tool. For example, you can choose the fill texture and border Sprites.  
[2D Tilemap Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html) | 2D **Tilemap** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tilemap) Editor allows you to create grid-based worlds with square, hexagonal or isometric tiles. Add your Tiles to the Tile Palette, and paint and fill Tile Grids using different settings and brushes. Extra tools let you add smart drawing, randomization or animation to the Tile assets.  
The following table lists some optional packages you can install that might be particularly useful for 2D game development:
**Package** | **Description**  
---|---  
[Shader Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest) |  **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Graph lets you build your shaders visually.  
[Cinemachine](https://docs.unity3d.com/Packages/com.unity.cinemachine@latest) | The Cinemachine package is a suite of modules that provide advanced functionality for operating the Unity Camera.  
[2D Tilemap Extras](https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@latest) | The 2D Tilemap Extras package contains reusable 2D and Tilemap Editor **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) that you can use for your own Projects.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-game-development-landing.html)
2D game development
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-game-creation-wokflow.html)
2D game creation workflow
