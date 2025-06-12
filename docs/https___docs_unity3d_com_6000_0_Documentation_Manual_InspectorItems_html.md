* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorItems.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)
  * Inspect items


[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorOptions.html)
Manage the Inspector window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorFocused.html)
Focused Inspectors
# Inspect items
What you can view and edit in an **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window depends on the type of item you’re inspecting. This section describes what an Inspector window displays for different types of items you can select.
Item type | Description  
---|---  
**Single GameObject** | The GameObject’s components and materials. For more information, refer to [Manage components and their values](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorManageComponents.html).  
**Multiple GameObjects** | The components that the selected GameObjects have in common, and a message if:   
- Any components are hidden because one or more GameObjects don’t have those components.   
- Any components don’t support editing across multiple GameObjects.   
- If a component’s values are the same across all selected GamedObjects, the Inspector shows the value. If the values are different across two or more selected GameObjects, the Inspector displays a dash (**-**). To apply a property value from one selected GameObject to all selected GameObjects, right-click the property name and select **Set to Value of`[Name of GameObject]`** from the context menu.  
**Single Prefab** | Similar to other GameObjects, but with additional actions: When you [Edit a Prefab Instance](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingPrefabViaInstance.html), the Inspector window displays options for working with the Prefab Asset and [applying overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html). The Inspector window displays the names of properties you override in bold.  
**Multiple Prefabs** | You can inspect multiple Prefab instances like you would with multiple GameObjects, but the Inspector hides the **Select** , **Revert** , and **Apply** buttons. Refer to [Editing a Prefab via its instances](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingPrefabViaInstance.html) to learn more.  
**Single Assets** | The asset’s import settings and runtime properties. Each type of asset has its own settings, for example the [Model Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-FBXImporter.html), [Audio Clip Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), and the [Texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).  
**Multiple Assets** | The properties that the selected assets have in common. If a property’s values are the same across all selected assets, the Inspector shows the value. If the values are different across two or more selected assets, the Inspector displays a dash (**-**). Properties you can’t edit for all assets at once are grayed out.  
**Script** | The Inspector displays the script’s public variables, and private fields with the [SerializeField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html) attribute. Use these to set parameters and default values without modifying the script’s code. To hide these variables, use [HideInInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html).  
**Tip:** You can use the **Inspector** window to locate an item in the **Hierarchy** window. From the Inspector window’s **More Items** (**⋮**) menu, select **Ping**. 
## Additional resources
  * [Inspecting scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/inspecting-scripts.html)
  * [GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)
  * [Components](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-components.html)A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#component)
  * [Prefabs](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab)
  * [The Hierarchy window](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorOptions.html)
Manage the Inspector window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InspectorFocused.html)
Focused Inspectors
