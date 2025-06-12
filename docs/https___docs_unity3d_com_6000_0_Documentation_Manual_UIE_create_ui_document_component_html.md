* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-ui-document-component.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Support for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-runtime-ui.html)
  * [Configure runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-render-runtime-ui.html)
  * UI Document component


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html)
Panel Settings properties reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Event-System.html)
Runtime UI event system and input handling
# UI Document component
A UI Document component references a UXML document and a Panel Settings asset. It serves as a bridge between the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and a UXML document. The UXML document specifies the UI structure, while the Panel Settings asset handles rendering.
## Create a UI Document component
To create a UI Document component, do one of the following:
  * To add a UI Document component to an existing GameObject in your scene, select **Component** > **UI Toolkit** > **UI Document**.
  * To create a new GameObject with a preconfigured UI Document component, select **GameObject** > **UI Toolkit** > **UI Document**.


## Connect the UI to a panel
To Connect the UI to a panel, in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window of the UI Document component, configure UI Document component.
![UI Document component](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uitk/ui-document.png) UI Document component
  * **Panel Settings** : The Panel Settings asset that renders the UI.
  * **Source Asset** : The UXML document that contains the UI to display.
  * **Sort Order** : The rendering order of the UI Document component. The lower the value, the earlier the UI Document component renders.


## Render multiple UXML Documents on the same panel
A panel can display UI from more than one UXML Document component. This allows you to break complex UIs into smaller, more manageable parts. Each UXML Document component references a different UXML document and the same Panel Settings asset. 
Each UI Document component has a **Sort Order** property that controls rendering order. Child UI Document components render on top of their parent UI Document components. Sibling UI Document components (at the same hierarchy level) render in ascending order based on their **Sort Order** value. The lower the **Sort Order** value, the earlier the UI Document component renders.
**Note** : If there are multiple UI document components attached to the same Panel Settings, all these documents have a common focus navigation context. If they have distinct Panel Settings, navigation won’t jump automatically from one to the other even if you arrange them side by side. To make navigation jump from one to the other, you must set the `focusController` of the Panel Settings to the `FocusController` of the UI Document component you want to jump to.
## Lifecycle of UI Document components
Unity loads a UI Document component’s source UXML documents when it calls the `OnEnable()` method on the component. To ensure the **visual tree** An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree) loads correctly, add logic to interact with the controls inside the `OnEnable()` method. This means your script must respond to `OnEnable()` and `OnDisable()` to safely reference **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) from your UXML documents.
A UI Document component clears its contents when it responds to the `OnEnable()` and `OnDisable()` methods. This approach removes UI elements that the UI Document won’t reuse soon and effectively clears the associated resources. Additionally, if a UI Document component isn’t assigned with a [Panel Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html) asset, it automatically clears its contents.
To hide a UI element that’s likely to be reused soon or needs to appear quickly to avoid an initialization penalty, [set the `display` of the `UIDocument.rootVisualElement` to `none`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-SupportedProperties.html#appearance). You can also use this to hide a UI element component that’s part of a larger UI hierarchy.
## Additional resources
  * [Create a panel](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-panel.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Panel-Settings.html)
Panel Settings properties reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Runtime-Event-System.html)
Runtime UI event system and input handling
