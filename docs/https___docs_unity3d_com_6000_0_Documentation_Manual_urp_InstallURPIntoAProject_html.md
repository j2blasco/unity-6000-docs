* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Installing and upgrading URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
  * [Creating a URP project](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/creating-a-urp-project.html)
  * Install URP into an existing project


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html)
Package samples reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrading-from-birp.html)
Upgrading from the Built-In Render Pipeline to URP
# Install URP into an existing project
If you have started a Project using the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), you can install URP and configure your Project to use URP. When you do this, you must configure URP yourself. You will need to manually convert or recreate parts of your Project (such as lit shaders or post-processing effects) to be compatible with URP.
You can download and install the latest version of the Universal Render Pipeline (URP) to your existing Project via the [Package Manager system](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest/index.html), and then install it into your Project. If you don’t have an existing Project, refer to documentation on [how to start a new URP Project from a Template](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/creating-a-new-project-with-urp.html).
## Before you begin
URP uses its own [integrated post-processing solution](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html). If you have the Post Processing Version 2 package installed in your Project, you need to delete the Post Processing Version 2 package before you install URP into your Project. When you have installed URP, you can then recreate your **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects.
Projects made using URP are not compatible with the High Definition Render Pipeline (HDRP) or the Built-in Render Pipeline. Before you start development, you must decide which render pipeline to use in your Project. For information on choosing a render pipeline, refer to [the Render Pipelines section of the Unity Manual](https://docs.unity3d.com/2019.3/Documentation/Manual/render-pipelines.html).
## Installing URP
  1. In Unity, open your Project.
  2. In the top navigation bar, select **Window** > **Package Manager** to open the **Package Manager** window.
  3. In the **Packages** menu, select **Unity Registry**. This shows the list of available packages for the version of Unity that you are currently running.
  4. Select **Universal RP** from the list of packages.
  5. In the bottom right corner of the Package Manager window, select **Install**. Unity installs URP directly into your Project.


## Configuring URP
Before you can start using URP, you need to configure it. To do this, you need to create a Scriptable Render Pipeline Asset and adjust your Graphics settings.
### Creating the Universal Render Pipeline Asset
The [Universal Render Pipeline Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html) (URP Asset) contains the global rendering and quality settings of your project, and creates the rendering pipeline instance. The rendering pipeline instance contains intermediate resources and the render pipeline implementation.
To create a Universal Render Pipeline Asset:
  1. In the Editor, go to the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow).
  2. Right-click in the Project window, and select **Create** > **Rendering** > **URP Asset (with Universal Renderer)**. Alternatively, navigate to the menu bar at the top, and select **Assets** > **Create** > **Rendering** > **URP Asset (with Universal Renderer)**.


You can either leave the default name for the new Universal Render Pipeline Asset, or type a new one.
###  Set URP as the active render pipeline
To set URP as the active render pipeline:
  1. In your project, locate the Render Pipeline Asset that you want to use.  
**Tip** : to find all URP Assets in a project, use the following query in the search field: `t:universalrenderpipelineasset`.
  2. Select **Edit** > **Project Settings** > **Graphics**.
  3. In the **Scriptable Render Pipeline Settings** field, select the URP Asset. When you select the URP Asset, the available Graphics settings change immediately.


**Optional** :
Set an override URP Assets for different quality levels:
  1. Select **Edit** > **Project Settings** > **Quality**.
  2. Select a quality level. In the **Render Pipeline Asset** field, select the Render Pipeline Asset.


## Upgrading your shaders
If your project uses the prebuilt [Standard Shader](https://docs.unity3d.com/Manual/shader-StandardShader.html), or custom Unity **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) made for the Built-in Render Pipeline, you must convert them to URP-compatible Unity shaders. For more information on this topic, refer to [Upgrading your Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrading-your-shaders.html).
## Upgrade from the Built-in Render Pipeline
When you upgrade a project from the Built-in Render Pipeline (BiRP) to the Universal Render Pipeline (URP), there are many changes which occur. These changes are wide reaching and require some work beyond the initial installation process for URP shown here. The following pages explain more about these changes and provide guidance on any additional steps required:
  * [Converting your shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrading-your-shaders.html)
  * [Render Pipeline Converter](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rp-converter.html)
  * [Upgrade custom shaders for URP compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/birp-urp-custom-shader-upgrade-guide.html)
  * [Find graphics quality settings in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/birp-onboarding/quality-settings-location.html)
  * [Update graphics quality levels for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/birp-onboarding/quality-presets.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html)
Package samples reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrading-from-birp.html)
Upgrading from the Built-In Render Pipeline to URP
