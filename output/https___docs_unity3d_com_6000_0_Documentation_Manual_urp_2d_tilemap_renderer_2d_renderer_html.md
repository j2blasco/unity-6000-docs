* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d/tilemap-renderer-2d-renderer.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * Enable 2D lighting with the Tilemap Renderer in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/PrepShader.html)
Prepare and upgrade sprites for 2D lighting in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-blending.html)
Blend Modes in 2D lighting
# Enable 2D lighting with the Tilemap Renderer in URP
To enable 2D lighting in URP, set up the required settings to use the Tilemap Renderer component.
You can use the Tilemap Renderer with URP 2D to enable [2D lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Lights-2D-intro.html) on [tiles](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/tiles-landing.html)A simple class that allows a sprite to be rendered on a Tilemap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tile) and [tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tilemap), especially [isometric tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html) which simulate pseudo-depth. Doing so requires you to setup your project and adjust the Tilemap Renderer’s settings in the following ways.
When you select the [2D Renderer Data asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DRendererData-overview.html) for your project’s [Scriptable Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/scriptable-render-pipeline-introduction.html), the Renderer Data asset assumes control of the Tilemap Renderer’s **Transparency Sort Mode** property settings and requires you to adjust the settings under the 2D Renderer Data asset’s property settings instead of in the **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings).
To optimize the rendering of the Tilemap Renderer component with the 2D lighting system, Unity can batch the rendering of the [Tilemap Renderer component](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-renderer-reference.html) with the [Scriptable Render Pipeline Batcher](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher.html) to improve the rendering performance of the Tilemap Renderer with other **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) renderers with the same rendering characteristics.
## Adjusting the Transparency Sort Mode settings in the 2D Renderer Data asset
When you [create an isometric tilemap](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html), one of the steps requires you to set the **Transparency Sort Mode** (**Edit** > **Project Settings…** > **Graphics** > **Camera Settings**) to **Custom Axis** and to set it to the [required values](https://docs.unity3d.com/Manual/Tilemap-Isometric-CreateIso.html#customaxis) to have Unity render the Tiles with the pseudo-depth of an isometric perspective.
![The default location of the Transparency Sort Mode settings when no specific URP Pipeline is selected.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/non-renderer2d-project-settings.png) The default location of the **Transparency Sort Mode** settings when no specific URP Pipeline is selected.
If you want to use the 2D Renderer with the Tilemap Renderer in your Project, first create the URP Asset and its associated 2D Renderer Data asset by right-clicking the Asset window and go to **Create > Rendering > URP Asset (with 2D Renderer)**. Then go to your Project’s **Scriptable Render Pipeline Settings** (menu: **Edit > Project Settings… > Graphics**) and select the Universal Render Pipeline (URP) 2D asset.
When you do so, the ****Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) Settings** (including the **Transparency Sort Mode** property) become hidden.
![Camera Settings hidden after selecting a Universal Render Pipeline Asset.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/renderer-2d-selected.png) Camera Settings hidden after selecting a Universal Render Pipeline Asset.
The 2D Renderer Data asset now controls the **Transparency Sort Mode** property settings, and the values set in the active Renderer 2D Data asset supersedes the values set in the **Project Settings**. Select the 2D Renderer Data asset go to its **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. In the General section, set **Transparency Sort Mode** to **Custom Axis**.
![Select Custom Axis in the 2D Renderer Data asset.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/renderer-2d-custom-axis.png) Select **Custom Axis** in the 2D Renderer Data asset.
The **Transparency Sort Axis** property settings then become available. Use the same values for the **Transparency Sort Axis** as those used to for the [rendering of tiles on an isometric tilemap](https://docs.unity3d.com/Manual/Tilemap-Isometric-CreateIso.html#customaxis).
![The Transparency Sort Axis setting for isometric tilemaps in the Renderer 2D asset properties.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/renderer-data-asset-properties.png) The **Transparency Sort Axis** setting for isometric tilemaps in the Renderer 2D asset properties.
## Enabling the Scriptable Render Pipeline Batcher
To prepare the Tilemap Renderer for SRP batching:
  1. Fulfill the requirements and steps for enabling the [SRP Batcher](https://docs.unity3d.com/Manual/SRPBatcher.html#using-the-srp-batcher) in URP.
  2. Select the Tilemap Renderer component and go to its **Mode** property setting.
  3. Select either **Individual** or **SRP Batch** (only supported in the Universal Render Pipeline version 15 onwards). **Note** : **Chunk** mode is incompatible with the SRP batcher.


## Additional resources
  * [2D Sorting](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-renderer-sorting.html)
  * [Scriptable Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/scriptable-render-pipeline-introduction.html)
  * [Isometric Tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/PrepShader.html)
Prepare and upgrade sprites for 2D lighting in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-blending.html)
Blend Modes in 2D lighting
