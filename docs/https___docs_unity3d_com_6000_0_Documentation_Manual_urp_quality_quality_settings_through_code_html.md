* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/quality/quality-settings-through-code.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Graphics quality settings in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-quality-settings-landing.html)
  * Change the active URP Asset at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-asset-additional-settings.html)
Display advanced properties in a URP Asset
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/quality/change-urp-asset-settings.html)
Change URP Asset settings at runtime
# Change the active URP Asset at runtime
Unity has several preset levels of [Quality settings](https://docs.unity3d.com/Manual/class-QualitySettings.html) and you might add more to your project. To accommodate different hardware specifications, you can switch between these levels and the associated URP Asset from C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). The following examples show how to use API to change Quality setting levels and the active URP Asset, and how to change specific settings in the URP Asset at runtime.
**Note** : You should only change Quality settings and URP Asset settings at runtime at points where performance is not essential, such as during loading screens or on static menus. This is because these changes cause a temporary but significant performance impact.
## Change the active URP Asset
Each quality level uses a URP Asset to control many of the specific graphics settings. You can assigning different URP Assets to each quality level and switch between them at runtime.
### Configure Project Quality settings
To use Quality settings to switch between URP Assets, ensure that the quality levels of your project are configured to use different URP Assets. The URP 3D Sample **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) has this configuration by default.
  1. Create a URP Asset for each quality level. To do this, right-click in the Project window and select **Create** > **Rendering** > **URP Asset (with Universal Renderer)**.
> **Note** : These instructions are also valid for URP Assets that use the 2D Renderer.
  2. Configure and name the new URP Assets as necessary.
  3. Open the Quality section in the Project Settings (**Edit** > **Project Settings** > **Quality**).
  4. Assign each URP Asset to a quality level. To do this, select a quality level from the Levels list, then go to **Rendering** > **Render Pipeline Asset** and choose the URP Asset you created for this quality level. Do this for each quality level.


The quality levels of your project are now ready to be used to change between URP Assets at runtime.
### Change Quality Level
You can change the quality level Unity uses at runtime through the [QualitySettings API](https://docs.unity3d.com/ScriptReference/QualitySettings.html). With the quality levels setup as shown previously, this enables you to switch between URP Assets as well as Quality settings presets.
In the following simple example, the C# script uses the system’s total Graphics Memory to determine the appropriate quality level without any input from the user when they open the built project.
  1. Create a new C# script with the name QualityControls.
  2. Open the QualityControls script and add the `SwitchQualityLevel` method to the `QualityControls` class.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QualityControls : MonoBehaviour
{
    void Start()
    {
            
    }
        
    private void SwitchQualityLevel()
    {
            
    }
}

```

  3. Add a `switch` statement in the `SwitchQualityLevel` method to select the quality level with the `QualitySettings.SetQualityLevel()` method as shown below.
> **Note** : Each Quality level has an index that matches the level’s position in the list in the Quality section of the Project Settings window. The quality level at the top of the list has an index of 0. This index only counts quality levels which you specified as enabled for the target platform of any built version of your project.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QualityControls : MonoBehaviour
{
    void Start()
    {
            
    }
        
    private void SwitchQualityLevel()
    {
        // Select Quality settings level (URP Asset) based on the size of the device's graphics memory
        switch (SystemInfo.graphicsMemorySize)
        {
            case <= 2048:
                QualitySettings.SetQualityLevel(1);
                break;
            case <= 4096:
                QualitySettings.SetQualityLevel(2);
                break;
            default:
                QualitySettings.SetQualityLevel(0);
                break;
        }
    }
}

```

  4. Add a call to the `SwitchQualityLevel` method in the `Start` method. This ensures that the quality level only changes when the scene first loads.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QualityControls : MonoBehaviour
{
    void Start()
    {
        SwitchQualityLevel();
    }
        
    private void SwitchQualityLevel()
    {
        // Select Quality settings level (URP Asset) based on the size of the device's graphics memory
        switch (SystemInfo.graphicsMemorySize)
        {
            case <= 2048:
                QualitySettings.SetQualityLevel(1);
                break;
            case <= 4096:
                QualitySettings.SetQualityLevel(2);
                break;
            default:
                QualitySettings.SetQualityLevel(0);
                break;
        }
    }
}

```

  5. Open the first scene that your built project loads on startup.
  6. Create an empty **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) and call it QualityController. To do this, right-click in the Hierarchy Window and select **Create Empty**.
  7. Open the QualityController object in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
  8. Add the QualityControls script to the QualityController as a component.


Now when this scene loads, Unity runs the `SwitchQualityLevel` method in the QualityControls script which detects the system’s total graphics memory and sets the quality level. The quality level sets the URP Asset as the active **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) Asset.
You can create more complex systems and sequences of checks to determine which quality level to use, but the fundamental process remains the same. When the project starts, run a script which uses [`QualitySettings.SetQualityLevel`](https://docs.unity3d.com/ScriptReference/QualitySettings.SetQualityLevel.html) to select a quality level and through that select the URP Asset for the project to use at runtime.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-asset-additional-settings.html)
Display advanced properties in a URP Asset
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/quality/change-urp-asset-settings.html)
Change URP Asset settings at runtime
