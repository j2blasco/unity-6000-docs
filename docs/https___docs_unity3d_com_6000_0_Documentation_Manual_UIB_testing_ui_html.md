* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * Test UI


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-using-uss-variables.html)
Assign USS variables in UI Builder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
Structure UI
# Test UI
You can test your UI inside the UI Builder, and use debugging tools to investigate styles.
## Test UI in Preview mode
To test your UI inside the UI Builder, directly inside the **Canvas** , you can enable **Preview** mode, found in the ****Viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport)**’s **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar). **Preview** mode removes the UI Builder-specific picking overlay and handles from the **Canvas**. You can tell if you have **Preview** mode enabled by looking for an orange border around the entire **Viewport** :
![PreviewMode](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/PreviewMode.png) PreviewMode
With **Preview** mode enabled, you can test the following:
  * State-based controls like `Foldout`, which you can click on to expand and see how the rest of the UI reacts.
  * Input fields like `IntegerField`, where you can test input validation.
  * Large containers like `ScrollView`, where you can test scrolling up and down.
  * `:hover` pseudo states to check hover-only styles.


In **Preview** mode, you can still work on your UI. However, **Canvas** picking and manipulators are turned off in **Preview** mode.
## Debug styles
If you don’t know where a style comes from, you can find the styles for an element in the **Matching Selectors** section in the UI Builder’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
  1. In the **Canvas** of the UI Builder, select the element.
  2. In the Inspector window, expand **StyleSheet** > **Matching Selectors**.


![An example of Matching Selectors](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/MatchingSelectorsFoldout.png)
The **Matching Selectors** section displays the following:
  * USS selectors from your own style sheets
  * USS selectors from the default Unity theme


**Note** : USS selectors that appear lower in the list always override the same style properties in higher USS selectors.
If the **Matching Selectors** section doesn’t provide enough information, you can use the [UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ui-debugger.html). The UI Toolkit Debugger is a tool that you can use to inspect and debug your UI elements in real-time. It provides a visual representation of your UI hierarchy. You use it to examine the state and properties of each UI element.
## Additional resources
  * [Style UI with USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [USS selectors](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors.html)
  * [UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ui-debugger.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-styling-ui-using-uss-variables.html)
Assign USS variables in UI Builder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
Structure UI
