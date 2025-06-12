* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-list-view.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * [Runtime data binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-examples.html)
  * Bind ListView to a list with runtime binding


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-custom-binding-bind-uss.html)
Create a custom binding to bind USS selectors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
SerializedObject data binding
# Bind ListView to a list with runtime binding
**Version** : 6000+
The ListView control is the most efficient way to create lists. This example demonstrates how to use runtime binding to bind a ListView to a list. Runtime binding supports both runtime and Editor UI. For demonstration purposes, this example displays the ListView in an Editor window.
## Example overview
The example creates a ListView and a list. To bind the ListView to the list, set the binding data source of the ListView to the property that contains the list.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/2023/runtime-binding-listview).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [Runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html)
  * [UXML element ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ListView.html)


## Create an object with a list
Create an example `List` object that has a list of `Item` objects. Each `Item` contains a `name` and an `enabled` property.
  1. Create a Unity project with any template.
  2. In your **Project** window, create a folder named `runtime-binding-listview` to store all your files.
  3. In the `runtime-binding-listview` folder, create a folder named `Scripts` to store all your C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
  4. In the `Scripts` folder, create a C# script named `ExampleItemObject.cs` with the following contents:

```
   using System;
   using System.Collections.Generic;
   using UnityEngine;
   
   public class ExampleItemObject  
   {
       public List<Item> items = new();
   
       public void Reset()
       {
           items = new List<Item>{
               new() { name = "Use Local Serverdfsdfsd", enabled = false },
               new() { name = "Show Debug Menu", enabled = false },
               new() { name = "Show FPS Counter", enabled = true },
           };
       }
   
       // Use a struct instead of a class to ensure that the ListView can create items 
       // when the + button is clicked.
       public struct Item
       {
           public bool enabled;
           public string name;
       }
   }

```

## Create the ListView item template in UI Builder
Create the template of the list item in UI Builder. Each item contains a Toggle and a TextField. Bind them to the `enabled` and `name` properties of the `Item` object.
  1. In the `runtime-binding-listview` folder, create a folder named `UXML`.
  2. In the `UXML` folder, create a UXML file named `ListViewItem.uxml`.
  3. Double-click the `ListViewItem.uxml` file to open it in UI Builder.
  4. In the **Hierarchy** panel, add a **VisualElement**.
  5. Add a **Toggle** as a child of **VisualElement**.
  6. Add a **TextField** as a child **VisualElement**.
  7. Remove the label text for the **Toggle** and **TextField**.
  8. Set the **Flex direction** of the **VisualElement** to `Row`.
  9. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** panel of the **Toggle** , do the following:
  10. Right-click **Value** and select **Add binding**.
  11. In the **Add Binding** window, set **Data Source Path** to `enabled`.
  12. In the **Inspector** panel of the **TextField** , do the following:
     * Right-click **Value** and select **Add binding**.
     * In the **Add Binding** window, set **Data Source Path** to `name`.
  13. Save the UXML file. The finished UXML file looks like the following:

```
   <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xsi="http://www.w3.org/2001/XMLSchema-instance" engine="UnityEngine.UIElements" editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../../UIElementsSchema/UIElements.xsd" editor-extension-mode="False">
       <ui:VisualElement name="VisualElement" style="flex-direction: row;">
           <ui:Toggle>
               <Bindings>
                   <ui:DataBinding property="value" data-source-path="enabled"  />
               </Bindings>
           </ui:Toggle>
           <ui:TextField placeholder-text="filler text">
               <Bindings>
                   <ui:DataBinding property="value" data-source-path="name"  />
               </Bindings>
           </ui:TextField>
       </ui:VisualElement>
   </ui:UXML>

```

## Create the ListView UI in UI Builder
Create the ListView UI in UI Builder, and set the item template to `ListViewItem.uxml`.
  1. In the `UXML` folder, create a UXML file named `UIListView.uxml`.
  2. Double-click the `UIListView.uxml` file to open it in UI Builder.
  3. In the **Hierarchy** panel, add a **ListView**. 
  4. In the **Inspector** panel of the **ListView** , do the following:
  5. Set **Virtualization Method** to **Dynamic Height**.
  6. Set **Reorder Mode** to **Animated**.
  7. Set **Item Template** to `ListViewItem.uxml`.
  8. Set **Binding Source Selection Mode** to **Auto Assign**.
  9. Select the **Reorderable** checkbox.
  10. Select the **Show Add Remove Footer** checkbox.
  11. Set **Header Title** to `Items`.
  12. Select the **Show Foldout Header** checkbox.
  13. Save the UXML file. The finished UXML file looks like the following:

```
   <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xmlns="UnityEngine.UIElements" ue="UnityEditor.UIElements" editor-extension-mode="False">
       <ui:ListView virtualization-method="DynamicHeight" reorder-mode="Animated" binding-source-selection-mode="AutoAssign" show-add-remove-footer="true" header-title="Items" reorderable="true" show-border="false" show-foldout-header="true" item-template="ListViewItem.uxml" show-bound-collection-size="false" />
   </ui:UXML>

```

## Create a custom Editor window and set the binding
Create a custom Editor window that contains the ListView and bind it to the `items` property of `List`. This example sets the binding source in the C# script. You can also manually set the binding source in the UXML file inside the ListView element like this:
```
<ui:ListView>
    <Bindings>
        <ui:DataBinding property="itemsSource" data-source-path="items" />
    </Bindings>
</ui:ListView>

```

  1. In the `Scripts` folder, create a folder named `Editor`.
  2. In the `Editor` folder, create a C# script named `ListViewTestWindow.cs` with the following contents:

```
   using UnityEngine;
   using UnityEngine.UIElements;
   using UnityEditor;
   using UnityEditor.UIElements;
   using System.Collections.Generic;
   using Unity.Properties;
   
   internal class ListViewTestWindow : EditorWindow
   {
       [SerializeField] private VisualTreeAsset itemLayout;
       [SerializeField] private VisualTreeAsset editorLayout;
   
       ExampleItemObject m_ExampleItemObject;
       
       [MenuItem("Window/ListViewTestWindow")]
       static void Init()
       {
           ListViewTestWindow window = EditorWindow.GetWindow<ListViewTestWindow>();
           window.Show();
       }
   
       void CreateGUI()
       {
           m_ExampleItemObject = new();
   
           editorLayout.CloneTree(rootVisualElement);
           var listView = rootVisualElement.Q<ListView>();
           
           // This example sets the itemTemplate and bindingSourceSelectionMode in the UXML file.
           // You can also set them in the C# script like the following:
           //listView.itemTemplate = itemLayout;
           //listView.bindingSourceSelectionMode = BindingSourceSelectionMode.AutoAssign;
   
           // Set the binding source to the ExampleItemObject instance.
           listView.dataSource = m_ExampleItemObject;
   
           // Set the itemsSource binding to the items property of the List object.
           listView.SetBinding("itemsSource", new DataBinding() {dataSourcePath = new PropertyPath("items")});
           
           m_ExampleItemObject.Reset();
       }
   }
   

```

## Test the binding
  * From the menu, select **Window** > **ListViewTestWindow**.


The Editor window displays a ListView bound to the items defined in the `ExampleItemObject.cs`. If you update the values of the `enabled` or `name` properties for the `Item` in `ExampleItemObject.cs`, the changes are automatically reflected in the ListView.
## Additional resources
  * [`ListView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html)
  * [Bind to a list](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list.html)
  * [Create a custom Editor window with C# script](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateEditorWindow.html)
  * [Create custom binding to bind USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-custom-binding-bind-uss.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-custom-binding-bind-uss.html)
Create a custom binding to bind USS selectors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
SerializedObject data binding
