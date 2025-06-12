* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-manage-asset-reference.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Structure UI with UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * Load UXML and USS C# scripts


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-reference-other-files-from-uxml.html)
Reference other files from UXML
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-LoadingUXMLcsharp.html)
Instantiate UXML from C# scripts
# Load UXML and USS C# scripts
Unity represents UXML files as `VisualTreeAsset` objects in C# and represents USS files as `StyleSheet` objects in C#. Since `VisualTreeAsset` and `StyleSheet` are regular Unity assets, you can use Unity’s standard workflows to load them.
## Use serialization references
Unity automatically detect fields from your C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) which are of type `VisualTreeAsset` or `StyleSheet`. You can use the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) to set references to specific UXML or USS files imported in your project. Such references remain valid even when the location of your assets change in your project.
There are three ways to use this in your scripts:
**Description** | **How to display the Inspector** | **Reference save location**  
---|---|---  
Instances of custom scripts (such as `MonoBehaviour`) | Select the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) holding the instance of the script | Inside the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)  
Default references for a script that derives from `EditorWindow` or `Editor` | Select the actual C# file in the Project Browser | Inside the meta file associated with the script  
Custom assets in your project that derive from `ScriptableObject` | Select the asset in the Project browser | Inside the serialized data of the asset itself  
**Note** : The default references works for all scripts that derive from `MonoBehaviour` or `ScriptableObject`. It provides a way to populate default values for serialized fields of scripts.
The following example `MonoBehaviour` class receives a UXML file and a list of USS files from the Inspector:
```
using UnityEngine;
using UnityEngine.UIElements;

public class MyBehaviour : MonoBehaviour
{
  // Note that public fields are automatically exposed in the Inspector
  public VisualTreeAsset mainUI;
  [Reorderable]
  public StyleSheet[] seasonalThemes;
}

```
![The Inspector window shows a single reference picker and a list of seasonal themes \(the list is empty\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/managing-asset-ref-mb.png) The Inspector window shows a single reference picker and a list of seasonal themes (the list is empty)
The following example `EditorWindow` class receives default references from the Inspector:
```
using UnityEditor;
using UnityEngine.UIElements;

public class MyWindow : EditorWindow
{
  [SerializeField]
  private VisualTreeAsset uxml;
  [SerializeField]
  private StyleSheet uss;
}

```
![The Inspector window shows three reference fields: View Data Dictionary, Uxml, and Uss](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/managing-asset-ref-window.png) The Inspector window shows three reference fields: View Data Dictionary, Uxml, and Uss
## Use the Asset Database (Editor only)
You can load your UI Assets by path or GUID with the [`AssetDatabase`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html) class. 
The following example shows how to locate an asset by path:
```
VisualTreeAsset uxml = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Assets/Editor/main_window.uxml");
StyleSheet uss = AssetDatabase.LoadAssetAtPath<StyleSheet>("Assets/Editor/main_styles.uss");

```

The following example shows how to locate an asset by path from a package:
```
VisualTreeAsset uxml = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Packages/<name-of-the-package>/main_window.uxml");
StyleSheet uss = AssetDatabase.LoadAssetAtPath<StyleSheet>("Packages/<name-of-the-package>/main_styles.uss");

```

## Use Addressables
The Addressables system provides tools and scripts to organize and package content for your application and an API to load and release assets at runtime.
You can use UXML and USS assets with the Addressable system.
For information about how to set up Addressables for any assets in Unity, see [Getting started with Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@1.19/manual/AddressableAssetsGettingStarted.html).
## Use a Resources folder
If you add a `Resources` folder in your project and place your UI assets in it, you can use the [`Resources.Load`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html) method to load your assets. 
The following examples shows how to load an asset in the `Resources` folder:
```
VisualTreeAsset uxml = Resources.Load<VisualTreeAsset>("main_window");
StyleSheet uss = Resources.Load<StyleSheet>("main_styles");

```

**Note** : This method increases the final build size significantly. If you are concerned with the build size, use [`Addressables`](https://docs.unity3d.com/Packages/com.unity.addressables@1.19/manual/AddressableAssetsGettingStarted.html) instead.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-reference-other-files-from-uxml.html)
Reference other files from UXML
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-LoadingUXMLcsharp.html)
Instantiate UXML from C# scripts
