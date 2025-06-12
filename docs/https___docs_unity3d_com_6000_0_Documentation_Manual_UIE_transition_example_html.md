* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-transition-example.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Control behavior with events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events.html)
  * [Event examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-event-examples.html)
  * Create a simple transition with UI Builder and C# scripts


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-event-examples.html)
Event examples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-ui.html)
Create a drag-and-drop UI inside a custom Editor window
# Create a simple transition with UI Builder and C# scripts
Version: 2021.3+
This example demonstrates how to create simple transitions that are triggered by pseudo-classes and C# events.
## Example overview
The example creates a custom Editor window with three labels that rotate and scale when you hover over them. The transition lasts for three seconds.
![A Unity Editor window with text that rotates when the mouse cursor hovers over it.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/transition-example.gif) A Unity Editor window with text that rotates when the mouse cursor hovers over it.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/create-a-transition).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * [USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [Pseudo-classes](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors-Pseudo-Classes.html)
  * [Handle events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Events-Handling.html)


## Create the Editor window files
Use the menu to create the Editor window files with three default labels.
  1. Create a Unity project with any template.
  2. Create a folder named `create-a-transition` to store the files for this example.
  3. In that folder, right-click in the Project window and select **Create** > **UI Toolkit** > **Editor Window**.
  4. In the **C#** box, enter `TransitionExample`. This creates the following files:
     * `TransitionExample.cs`
     * `TransitionExample.uss`
     * `TransitionExample.uxml`


## Create the transition with UI Builder
In UI Builder, use the **StyleSheets** window to create a hover style for the label, which triggers the transition. Set the transition on the label rather than the hover. If you set the transition on the hover, the transition doesn’t work if the cursor leaves the label.
  1. Open `TransitionExample.uxml` in the UI Builder.
  2. In the **StyleSheets** window, click **Add new selector** and enter `Label:hover` to add a hover style for the label.
  3. Press Enter and select **Label:hover** in the list of USS selectors.
  4. In the **Transform** section of the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), do the following to scale and rotate the labels: 
     * In the **Scale** row, change the **X** value to `1.1`.
     * In the **Rotate** row, enter `10`.
  5. In the **StyleSheets** window, click **Add new selector** and enter `Label` to add a style for the label. 
  6. Press Enter and select **Label** in the list of USS selectors.
  7. In the **Transition Animations** section, enter `3` in the **Duration** row.
  8. Save and close the UI Builder. Your `TransitionExample.uss` file looks like the following:
```
.custom-label {
    font-size: 20px;
    -unity-font-style: bold;
    color: rgb(68, 138, 255);
}
    
Label:hover {
    scale: 1.1 1;
    rotate: 10deg;
}
    
Label {
    transition-duration: 3s;
}

```

  9. In Unity, select **Window** > **UI Toolkit** > **Transition Example**.
  10. Hover over the second and third labels. The labels rotate and increase in size over three seconds. 


## Create the transition with C# scripts
In C#, create the same transition you did in the previous section for the first label. Use the pointer events to trigger the transition.
  1. Open `TransitionExample.cs` in a text editor.
  2. Replace the contents of `TransitionExample.cs` with the following:
```
using UnityEditor;
using UnityEngine;
using UnityEngine.UIElements;
using System.Collections.Generic;

public class TransitionExample : EditorWindow
{
    [SerializeField]
    VisualTreeAsset m_VisualTreeAsset;

    [MenuItem("Window/UI Toolkit/TransitionExample")]
    public static void ShowExample()
    {
        TransitionExample wnd = GetWindow<TransitionExample>();
        wnd.titleContent = new GUIContent("Transition Example");
    }

    public void CreateGUI()
    {
        // Each editor window contains a root VisualElement object.
        VisualElement root = rootVisualElement;

        // VisualElements objects can contain other VisualElement following a tree hierarchy.
        cSharpLabel = new Label("Hello World! From C#");
        root.Add(cSharpLabel);

        // Create transition on the new Label.
        cSharpLabel.style.transitionDuration = new List<TimeValue>{ new TimeValue(3) };

        // Record default rotate and scale values.
        defaultRotate = cSharpLabel.resolvedStyle.rotate;
        defaultScale = cSharpLabel.resolvedStyle.scale;

        // Set up event handlers to simulate the use of the :hover pseudo-class.
        cSharpLabel.RegisterCallback<PointerOverEvent>(OnPointerOver);
        cSharpLabel.RegisterCallback<PointerOutEvent>(OnPointerOut);

        // Instantiate UXML
        VisualElement labelFromUXML = m_VisualTreeAsset.Instantiate();
        root.Add(labelFromUXML);
    }

    // The Label created with C#.
    VisualElement cSharpLabel;

    // The default rotate and scale values for the new Label.
    Rotate defaultRotate;
    Scale defaultScale;

    void OnPointerOver(PointerOverEvent evt)
    {
        SetHover(evt.currentTarget as VisualElement, true);
    }

    void OnPointerOut(PointerOutEvent evt)
    {
        SetHover(evt.currentTarget as VisualElement, false);
    }

    // When the user enters or exits the Label, set the rotate and scale.
    void SetHover(VisualElement label, bool hover)
    {
        label.style.rotate = hover ? new(Angle.Degrees(10)) : defaultRotate;
        label.style.scale = hover ? new Vector2(1.1f, 1) : defaultScale;
    }

    // Unregister all event callbacks.
    void OnDisable()
    {
        cSharpLabel.UnregisterCallback<PointerOverEvent>(OnPointerOver);
        cSharpLabel.UnregisterCallback<PointerOutEvent>(OnPointerOut);
    }
}

```

  3. In Unity, select **Window** > **UI Toolkit** > **Transition Example**.
  4. Hover over the first label. The label rotates and increases in size over three seconds.


## Additional resources
  * [USS transition](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transitions.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-event-examples.html)
Event examples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-ui.html)
Create a drag-and-drop UI inside a custom Editor window
