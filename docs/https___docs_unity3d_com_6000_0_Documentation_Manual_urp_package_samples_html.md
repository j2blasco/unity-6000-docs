* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-samples.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Installing and upgrading URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
  * [Creating a URP project](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/creating-a-urp-project.html)
  * Import a package sample in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/scene-templates.html)
Scene templates in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html)
Package samples reference for URP
# Import a package sample in URP
The Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) comes with a set of samples to help you get started.
A sample is a set of assets that you can import into your Unity project and use as a base to build upon or learn how to use a feature. A package sample can contain anything from a single C# script to multiple **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
## Importing package samples
Before you import any package samples for URP, be aware that they require your project to be URP-compatible. A project is URP-compatible if you [created it from a template](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/creating-a-new-project-with-urp.html) or manually [installed and set up URP in it](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallURPIntoAProject.html). If the project is not URP-compatible, errors can occur when you import a package sample.
To import package samples, use the [Unity Package Manager window](https://docs.unity3d.com/Manual/upm-ui.html):
  1. Go to **Window** > **Package Manager** and, in the [packages list view](https://docs.unity3d.com/Manual/upm-ui-list.html), select **Universal RP**.
  2. In the package [details view](https://docs.unity3d.com/Manual/upm-ui-details.html), find the **Samples** section.
  3. Find the sample you want to import and click the **Import** button next to it.


Unity imports URP package samples into `Assets/Samples/Universal RP/<package version>/<sample name>`.
## Opening package samples
To open a package sample:
  1. Go to `Assets/Samples/Universal RP/<package version>/`. Here there is a folder for each URP package sample you have imported.
  2. Find the folder that contains the package sample you want and open it. The folder has the same name that the package sample has in the Unity Package Manager window.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/scene-templates.html)
Scene templates in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html)
Package samples reference for URP
