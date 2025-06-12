* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upgrade-material.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)
  * Upgrade material assets to URP or HDRP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-material.html)
Create and assign a material
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MaterialsAccessingViaScript.html)
Access material properties in a script
# Upgrade material assets to URP or HDRP
When you upgrade your project from the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (BiRP) to either the Universal Render Pipeline (URP) or the High Definition Render Pipeline (HDRP), you need to upgrade your materials, otherwise, the materials appear bright pink in **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view.
![A bright pink cube in Scene view.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/shader-error.png) A bright pink cube in Scene view.
**Notes:**
  * Make sure there are no shader-related errors in the console, or in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window when you select a material.
  * If your assets use custom **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), refer to [Upgrade custom shaders for URP compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/birp-urp-custom-shader-upgrade-guide.html).


## Upgrade BiRP materials to URP
To upgrade all material assets from BiRP to URP:
  1. Back up your Built-in Render Pipeline material assets.
  2. In your URP project, go to **Window** > **Rendering** > **Render Pipeline Converter**.
  3. In the **Render Pipeline Converter** window, select **Built-in to URP** from the drop-down, enable **Material Upgrade** , then select **Initialize and Convert**.


To upgrade only some material assets from BiRP to URP:
  1. Back up your Built-in Render Pipeline material assets.
  2. In your URP project, select your Built-in Render Pipeline material assets.
  3. Go to **Edit** > **Rendering** > **Materials** > **Convert Selected Built-in Materials to URP**.


**Note:** If the console or the **Inspector** window displays [error messages](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-error.html) when you select a material, there’s an issue with a shader that an automatic converter can’t solve.
For more information, refer to [Convert assets using the Render Pipeline Converter](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rp-converter.html).
## Upgrade BiRP materials to HDRP
To upgrade all material assets from BiRP to HDRP:
  1. Back up your Built-in Render Pipeline material assets.
  2. In your HDRP project, go to **Edit** > **Rendering** > **Materials** > **Convert All Built-in Materials to HDRP**.


To upgrade only some material assets from BiRP to HDRP:
  1. Back up your Built-in Render Pipeline material assets.
  2. In your HDRP project, select your Built-in Render Pipeline material assets in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow).
  3. Go to **Edit** > **Rendering** > **Materials** > **Convert Selected Built-in Materials to HDRP**.


For more information, refer to [Convert materials and shaders (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/convert-from-built-in-convert-materials-and-shaders.html).
## Additional resources
  * [Upgrading from the Built-In Render Pipeline to URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrading-from-birp.html)
  * [Upgrading to HDRP from the built-in render pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/convert-project-from-built-in-render-pipeline.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-material.html)
Create and assign a material
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MaterialsAccessingViaScript.html)
Access material properties in a script
