* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightExplorerExtension.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Light sources](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-sources.html)
  * [Light components](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-components.html)
  * [Configuring Light components](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-components-configuring.html)
  * [Configuring lights with the Light Explorer](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingExplorer-landing.html)
  * Customize the Light Explorer


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingExplorer.html)
Light Explorer window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-ambient-light.html)
Add ambient light from the environment
# Customize the Light Explorer
The Light Explorer extension allows you to create your own version of the [Light Explorer window](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingExplorer.html). You can use this to adapt the functionality of the Light Explorer window so that it works with a custom Scriptable **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (SRP), or with the [High Definition Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?preview=1)’s custom [Lights](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Light-Component.html?).
The Light Explorer Window lets you see every [Light](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html) in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and edit their properties. With this extension, you can extend the current window in multiple ways. For example, you can:
  * Change the tabs, from simply changing the tab name to adding your own custom tabs that display lists of different types of **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). This is useful if you want to display property information for your own custom **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe), for example.
  * Change the columns on a tab, again from changing the name to adding your own custom columns. Adding columns is useful if you want to view extra Light properties.


## Extending the Light Explorer
To extend the Light Explorer, you can either inherit from the:
  * `ILightingExplorerExtension` interface and override the `GetContentTabs` method.
  * `DefaultLightingExplorerExtension` class, which inherits from `ILightingExplorerExtension`. This class provides you with all of the content that is already in the window. Use this if you only want to override the number of tabs, the titles of each tab, or which Lights to display. To find out how you can extend the Light Explorer this way, see the example below.


### Example code
The examples in this section show you how to extend the default Light Explorer class to only show the Name column for Lights, and change the number of tabs. In your own implementation, you can override as many or as few methods as you want.
The following example only shows the name column for Lights:
```
using UnityEngine;
using UnityEngine.Rendering;
using UnityEditor;

[SupportedOnRenderPipeline(typeof(ExampleRenderPipelineAsset))]
public class SimpleExplorerExtension : DefaultLightingExplorerExtension
{
    private static class Styles
    {
        public static readonly GUIContent Name = EditorGUIUtility.TrTextContent("Name");
    }
    
    protected override LightingExplorerTableColumn[] GetLightColumns()
    {
        return new[]
        {
            new LightingExplorerTableColumn(LightingExplorerTableColumn.DataType.Name, Styles.Name, null, 200), // 0: Name
        };
    }
}

```

The following example only shows the name and enabled status for Lights, and hides the Emissive Materials tab (only shows 3 tabs instead of 4)
```
using UnityEngine;
using UnityEngine.Rendering;
using UnityEditor;

[SupportedOnRenderPipeline(typeof(ExampleRenderPipelineAsset))]
public class ComplexLightExplorerExtension : DefaultLightingExplorerExtension
{
    private static class Styles
    {
        public static readonly GUIContent Name = EditorGUIUtility.TrTextContent("Name");
        public static readonly GUIContent Enabled = EditorGUIUtility.TrTextContent("Enabled");
    }
    
    protected override UnityEngine.Object[] GetLights()
    {
        return Resources.FindObjectsOfTypeAll<Light>();
    }

    protected override LightingExplorerTableColumn[] GetLightColumns()
    {
        return new[]
        {
            new LightingExplorerTableColumn(LightingExplorerTableColumn.DataType.Name, Styles.Name, null, 200), // 0: Name
            new LightingExplorerTableColumn(LightingExplorerTableColumn.DataType.Checkbox, Styles.Enabled, "m_Enabled", 25), // 1: Enabled
        };
    }

    public override LightingExplorerTab[] GetContentTabs()
    {
        return new[]
        {
            new LightingExplorerTab("Lights", GetLights, GetLightColumns, true),
            new LightingExplorerTab("2D Lights", Get2DLights, Get2DLightColumns, true),
            new LightingExplorerTab("Reflection Probes", GetReflectionProbes, GetReflectionProbeColumns, true),
            new LightingExplorerTab("Light Probes", GetLightProbes, GetLightProbeColumns, true),
            new LightingExplorerTab("Static Emissives", GetEmissives, GetEmissivesColumns, false),
        };
    }
}

```

### Useful classes and methods
Here is a list of classes and methods that you can use to extend the Light Explorer:
ILightingExplorerExtension:
```
public virtual LightingExplorerTab[] GetContentTabs();
public virtual void OnEnable() {}
public virtual void OnDisable() {}

```

DefaultLightingExplorerExtension (inherit from ILightingExplorerExtension):
```
public virtual LightingExplorerTab[] GetContentTabs();
public virtual void OnEnable() {}
public virtual void OnDisable() {}

protected virtual UnityEngine.Object[] GetLights();
protected virtual LightingExplorerTableColumn[] GetLightColumns();

protected virtual UnityEngine.Object[] GetReflectionProbes();
protected virtual LightingExplorerTableColumn[] GetReflectionProbeColumns();

protected virtual UnityEngine.Object[] GetLightProbes();
protected virtual LightingExplorerTableColumn[] GetLightProbeColumns();

protected virtual UnityEngine.Object[] GetEmissives();
protected virtual LightingExplorerTableColumn[] GetEmissivesColumns();

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingExplorer.html)
Light Explorer window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-ambient-light.html)
Add ambient light from the environment
