* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)
  * Bind to a list with ListView


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-callback-any-properties.html)
Receive callbacks when any bound properties change
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list-without-listview.html)
Bind to a list without ListView
# Bind to a list with ListView
**Version** : 2021.3+
The ListView control is the most efficient way to create lists. To bind to a list with ListView, set the binding path of the ListView to the name of the property that contains the list.
This example demonstrates how to bind to a list with ListView. 
## Example overview
The example creates a list of toggles and binds the list to an underlying list of `GameSwitch` objects.
![A list of custom switches, displayed in the Unity Editor.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uie_binding_listview.png) A list of custom switches, displayed in the Unity Editor.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/bind-to-list).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [Visual Tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree)
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [`ListView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html)


## Create an object with a list
Create a `GameSwitch` object and a serialized object that has a list of `GameSwitch` objects as a property.
  1. Create a Unity project with any template.
  2. In your **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `bind-to-list` to store all your files.
  3. Create a C# script named `GameSwitch.cs` and replace its content with the following:
```
using System;

[Serializable]
public struct GameSwitch
{
    public string name;
    public bool enabled;
}

```

  4. Create a UI Document named `game_switch.uxml` and replace its contents with the following:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:ue="UnityEditor.UIElements">
    <Box style="flex-direction: row;">
        <Toggle binding-path="enabled" />
        <TextField binding-path="name" readonly="true" style="flex-grow: 1;"/>
    </Box>
</UXML>

```

  5. Create a C# script named `GameSwitchListAsset.cs` and replace its contents with the following:
```
using System.Collections.Generic;
using UnityEngine;

namespace UIToolkitExamples
{
    [CreateAssetMenu(menuName = "UIToolkitExamples/GameSwitchList")]
    public class GameSwitchListAsset : ScriptableObject
    {
        public List<GameSwitch> switches;

        public void Reset()
        {
            switches = new()
            {
                new() { name = "Use Local Server", enabled = false },
                new() { name = "Show Debug Menu", enabled = false },
                new() { name = "Show FPS Counter", enabled = true },
            };
        }

        public bool IsSwitchEnabled(string switchName) => switches.Find(s => s.name == switchName).enabled;
    }
}

```



## Create a custom Editor and set the binding
Create a custom Editor that can create an asset with a list of toggles. Bind the toggle list to the `GameSwitch` list by setting the `binding-path` attribute of the UI Document to the property name of the `GameSwitch` list, which is `switches`.
  1. Create a folder named `Editor`.
  2. In the **Editor** folder, create a C# script named `GameSwitchListEditor.cs` and replace its contents with the following:
```
using UnityEditor;
using UnityEngine;
using UnityEngine.UIElements;

namespace UIToolkitExamples
{
    [CustomEditor(typeof(GameSwitchListAsset))]
    public class GameSwitchListEditor : Editor
    {
        [SerializeField]
        VisualTreeAsset m_ItemAsset;

        [SerializeField]
        VisualTreeAsset m_EditorAsset;

        public override VisualElement CreateInspectorGUI()
        {
            var root = m_EditorAsset.CloneTree();
            var listView = root.Q<ListView>();
            listView.makeItem = m_ItemAsset.CloneTree;
            return root;
        }
    }
}

```

  3. Create a UI Document named `game_switch_list_editor.uxml` and replace its contents with the following:
```
<UXML xmlns="UnityEngine.UIElements" xmlns:ue="UnityEditor.UIElements">
    <ListView virtualization-method="DynamicHeight"
              reorder-mode="Animated"
              binding-path="switches"
              show-add-remove-footer="true"
              show-border="true"
              show-foldout-header="true"
              header-title="Switches"
    />
</UXML>

```

  4. In the Project window, select **GameSwitchListEditor.cs**.
  5. Drag **game_switch.uxml** to **Item Asset** in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
  6. Drag **game_switch_list_editor.uxml** to **Editor Asset** in the Inspector.


## Test the binding
  1. From the menu, select **Assets** > **Create** > **UIToolkitExamples** > **GameSwitchList**. This creates an asset named **New Game Switch List Asset**.
  2. In the Project window, select **New Game Switch List Asset**. This shows a list of toggles in the Inspector. You can reorder the list, collapse it, add entries to or remove entries from the list, and change the number of entries in the list. If you make changes in the Inspector UI, the `switches` property of the `GameSwitchListAsset` object changes.


## Additional resources
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)
  * [Bindable elements](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bindable-elements.html)
  * [Binding data type conversion](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-data-type-conversion.html)
  * [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-implementation-details.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-callback-any-properties.html)
Receive callbacks when any bound properties change
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list-without-listview.html)
Bind to a list without ListView
