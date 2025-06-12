* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-lwrp-to-urp.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Installing and upgrading URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
  * [Upgrade URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guides.html)
  * Upgrade from the Lightweight Render Pipeline to the Universal Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-7-2-0.html)
Upgrade to version 7.2.0 of the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/known-issues.html)
Known issues in URP
# Upgrade from the Lightweight Render Pipeline to the Universal Render Pipeline
The Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) replaces the Lightweight Render Pipeline (LWRP) in Unity 2019.3. If your Project uses LWRP, you must upgrade it to use URP to use Unity 2019.3.
Unity upgrades some things automatically, and you must make some manual changes. Follow the steps in this guide to transition from using LWRP to using URP.
## Before upgrading
### Update Assembly Definition Assets
URP uses GUIDs instead of Assembly Definition string names. If you are using Assembly Definition Assets (ASMDefs) in your Project, you should ensure that **Use GUIDs** is enabled on each of them.
Unity upgrades any existing string references to LWRP automatically as part of the upgrade process, but it is best practice to use GUIDs on your Assembly Definition Assets for future proofing.
For each Assembly Definition Asset in your Project:
  * Select the Assembly Defintion Asset
  * In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), enable **Use GUIDs**


For information on using Assembly Definition files, refer to the [documentation on Assembly Definitions](https://docs.unity3d.com/Manual/ScriptCompilationAssemblyDefinitionFiles.html).
## Upgrade process
### Upgrading your version of LWRP
To start the upgrade process:
  * Open the Project you want to upgrade in Unity 2019.3


Unity automatically updates LWRP to a 7.x.x version, and pulls in the URP package as a dependency of the updated LWRP package. The Unity script updater automatically upgrades your script files. When the script updater has finished, all of your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) should compile properly.
### Upgrading the Shader search path
If your LWRP Project uses `Shader.Find` to search for LWRP **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), you need to change the search path.
To do this:
  * Change all instances of `Shader.Find` that search for `Lightweight` to search for `Universal`.


### Upgrading custom shaders
#### Upgrading tags
URP uses its own scripting tags. If your Shaders use the LWRP `LightMode` tags, they will work in your URP Project, because Unity uses an internal alias for this. However, you should change the tags manually to future-proof your Project.
To do this:
  * Change all instances of `Lightweight2D` tag to `Universal2D`.
  * Change all instances of `LightweightForward` tag to `UniversalForward`.


In addition to this, URP also uses a different RenderPipeline tag to LWRP. If your own Shaders include this tag, you need to change it manually for the Shaders to work:
  * Change all instances of `LightweightPipeline` tag to `UniversalPipeline`.


#### Upgrading Shader names
The following Shader names have been changed for URP, so you need to manually update your Shader files:
  * Change all instances of `UsePass 'Lightweight Render Pipeline/...'` to `UsePass 'Universal Render Pipeline/...'`


#### Upgrading include paths
URP uses different include paths to LWRP. LWRP 7.x.x contains forwarding includes, so your custom Shaders will upgrade from LWRP to URP. However, URP 7.x.x does not contain forwarding includes, so you must then manually update the include paths.
  * Change all instances of `#include 'Packages/com.unity.render-pipelines.lightweight/xxx'` to `#include 'Packages/com.unity.render-pipelines.universal/xxx'`


### Upgrading namespaces
In the .cs files in your Project, find and replace references to the LWRP namespace with the new Universal namespace.
  * Change all instances of `UnityEditor.Rendering.LWRP.xxx` to now `UnityEditor.Rendering.Universal.xxx`


## Upgrading post-processing effects
URP version 7.x supports both [Post Processing Stack v2 (PPv2) and its own integrated post-processing solution](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html). If you have the Post Processing Version 2 package installed in your Project and you want to use URP’s integrated **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) solution, you need to delete the Post Processing Stack v2 package before you install URP into your Project. When you have installed URP, you can then recreate your post-processing effects.
Upgrading post-processing effects from LWRP to URP is a manual process. You must manually recreate each Post-Processing Profile in your Project, using URP’s post-processing implementation.
URP’s integrated post-processing solution does not currently support custom post-processing effects. If your Project uses custom post-processing effects, these cannot currently be recreated in URP’s integrated post-processing solution. Custom post-processing effects will be supported in a forthcoming release of URP.
## Installing URP and removing LWRP
As part of the automatic upgrade process, Unity installed URP as a dependency of LWRP. You must now install URP as a dependency of the Project itself, so that when you remove LWRP, Unity does not automatically remove URP.
To install URP as a dependency of the Project:
  * Go to menu: **Window** > **Package Manager**.
  * Locate the **Universal RP** package, and note the version number to the right of its name. This is the version of URP that has been added to your Project.
  * Close Unity.
  * In your file explorer, open the root folder of your Unity Project.
  * Open the Packages folder, and locate _manifest.json_. This is your Project’s **Project Manifest** Each Unity project has a _project manifest_ , which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPrj.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectmanifest) file.
  * Open the Project Manifest file using a text editor.
  * At the top of the dependencies section, add the following entry:

```
"com.unity.render-pipelines.universal": "[Version number you noted earlier]"

```

So, for example, if the version of URP was 7.1.1, your dependencies section would look like this:
```
"dependencies": {
    "com.unity.render-pipelines.universal": "7.1.1",
    ...
}

```

This marks the version of URP that you have installed as a dependency of the Project. You can now safely remove LWRP.
  * Open your Project in Unity.
  * Open the Package Manager Window.
  * Locate **Lightweight RP** and select it.
  * In the bottom right of the Package Manager window, click Remove. Unity completely removes the LWRP package from the Project.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrade-guide-7-2-0.html)
Upgrade to version 7.2.0 of the Universal Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/known-issues.html)
Known issues in URP
