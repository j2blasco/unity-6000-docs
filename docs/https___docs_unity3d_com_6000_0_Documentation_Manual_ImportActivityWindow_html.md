* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ImportActivityWindow.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Analyzing asset processes](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-optimizing.html)
  * [Analyze the import process](https://docs.unity3d.com/6000.0/Documentation/Manual/import-analyze.html)
  * Import Activity window introduction


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ImporterConsistency.html)
Check the consistency of the import process
[](https://docs.unity3d.com/6000.0/Documentation/Manual/import-activity-window-reference.html)
Import Activity window reference
# Import Activity window introduction
The Import Activity window provides you with information about what happens when Unity imports your assets. You can use this information to identify the assets in your project that Unity recently imported, how long each asset took to import, and why Unity imported it. This information can inform decisions about how to improve the time Unity takes to import your assets, or how to avoid unnecessary imports altogether.
## Open the Import Activity window
To open the Import Activity window:
  * Go to **Window** > **Analysis** > **Import Activity**.


You can also open the Import Activity window directly from an asset, which causes the window to immediately display the import details for the selected asset. To open the window from an asset choose from the following options:
  * Right-click an asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) and select **View in Import Activity Window**.
  * Select an asset, and right-click its **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)’s tab. From the context menu, select **Open in Import Activity Window**.

![The Import Activity window with an asset selected.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/import-activity-window.png) The Import Activity window with an asset selected.
## Analyze import data
The Import Activity window contains various options to investigate the import timings of the assets within your project. For more information about the options available, refer to [Import Activity window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/import-activity-window-reference.html).
## Overview of import data
Select the **Show Overview** option in the **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) to get an overview of the most impactful assets in your project. The Import Activity Overview panel displays a list of assets with the most dependencies and longest import duration. It’s useful to identify which assets might slow down the import process of your project. Assets with more dependencies are more likely to be regularly re-imported, because an asset is re-imported whenever any of its dependencies are modified.
![The Import Activity Overview panel displaying the most dependencies, longest import duration, and suggestions to improve import times.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/import-activity-window-overview.png) The Import Activity Overview panel displaying the most dependencies, longest import duration, and suggestions to improve import times.
You can select **Analyze Import Process** to get a list of issues with the importing process and ways to fix the warnings.
## Investigate previous import instances of an asset
To view the import history of an asset, enable the [Show previous imports](https://docs.unity3d.com/6000.0/Documentation/Manual/import-activity-window-reference.html#toolbar) option. In a separate panel, Unity then displays the number of revisions of the asset that are stored in the `Library` folder. The list is cleared when you restart the Unity Editor and artifact garbage collection runs.
If you want to keep import results from previous Editor sessions to aid with debugging or analysis, disable artifact garbage collection. To do this:
  1. Open the **Project Settings** window (**Edit** > **Project Settings**).
  2. Select **Editor** and under the **Asset Pipeline** settings, disable the **Remove unused Artifacts on Restart** setting.


You can also control this setting with `EditorUserSettings.artifactGarbageCollection`.
## Additional resources
  * [Import Activity window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/import-activity-window-reference.html)
  * [Introduction to importing assets](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingAssets.html)
  * [Asset metadata](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ImporterConsistency.html)
Check the consistency of the import process
[](https://docs.unity3d.com/6000.0/Documentation/Manual/import-activity-window-reference.html)
Import Activity window reference
