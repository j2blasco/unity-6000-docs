* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-radial-progress-use-vector-api.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [UI Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ui-renderer.html)
  * Use Vector API to create a radial progress indicator


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-pie-chart.html)
Create a pie chart in the Editor and runtime UI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-radial-progress.html)
Use Mesh API to create a radial progress indicator
# Use Vector API to create a radial progress indicator
**Version** : 2023.2+
This example demonstrates how to create custom controls and use the Vector API to draw visual content onto a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement).
## Example overview
This example creates a custom control that displays progress, as an alternative to a loading bar. The progress indicator displays a progress value in a partially filled ring around a label that displays the percentage. It supports a value between 0 and 100, which determines how much of the ring is filled.
![A radial control with progress highlighted in green, and the number 87% displayed in the center of the radial control.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/radial-progress-finished.png) A radial control with progress highlighted in green, and the number 87% displayed in the center of the radial control.
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/2023.2/radial-progress-vector-api).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * [UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [Generate 2D visual content](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-generate-2d-visual-content.html)
  * [`MeshGenerationContext`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.html)


## Create the radial progress control and its custom mesh
Create a C# script to define a `RadialProgress` visual element and a C# script to define the custom **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh). Style the visual element with a USS file.
  1. Create a Unity project with any template.
  2. Create a folder named `radial-progress` to store your files.
  3. In the `radial-progress` folder, create a C# script named `RadialProgress.cs` with the following content:

```
using Unity.Collections;
using UnityEngine;
using UnityEngine.UIElements;

namespace MyGameUILibrary
{

    // An element that displays progress inside a partially filled circle
    [UxmlElement]
    public partial class RadialProgress : VisualElement
    {

        // These are USS class names for the control overall and the label.
        public static readonly string ussClassName = "radial-progress";
        public static readonly string ussLabelClassName = "radial-progress__label";

        // These objects allow C# code to access custom USS properties.
        static CustomStyleProperty<Color> s_TrackColor = new CustomStyleProperty<Color>("--track-color");
        static CustomStyleProperty<Color> s_ProgressColor = new CustomStyleProperty<Color>("--progress-color");

        Color m_TrackColor = Color.gray;
        Color m_ProgressColor = Color.red;

        // This is the label that displays the percentage.
        Label m_Label;

        // This is the number that the Label displays as a percentage.
        float m_Progress;

        // A value between 0 and 100
        [UxmlAttribute]
        public float progress
        {
            // The progress property is exposed in C#.
            get => m_Progress;
            set
            {
                // Whenever the progress property changes, MarkDirtyRepaint() is named. This causes a call to the
                // generateVisualContents callback.
                m_Progress = value;
                m_Label.text = Mathf.Clamp(Mathf.Round(value), 0, 100) + "%";
                MarkDirtyRepaint();
            }
        }

        // This default constructor is RadialProgress's only constructor.
        public RadialProgress()
        {
            // Create a Label, add a USS class name, and add it to this visual tree.
            m_Label = new Label();
            m_Label.AddToClassList(ussLabelClassName);
            Add(m_Label);

            // Add the USS class name for the overall control.
            AddToClassList(ussClassName);

            // Register a callback after custom style resolution.
            RegisterCallback<CustomStyleResolvedEvent>(evt => CustomStylesResolved(evt));

            // Register a callback to generate the visual content of the control.
            generateVisualContent += GenerateVisualContent;

            progress = 0.0f;
        }

        static void CustomStylesResolved(CustomStyleResolvedEvent evt)
        {
            RadialProgress element = (RadialProgress)evt.currentTarget;
            element.UpdateCustomStyles();
        }

        // After the custom colors are resolved, this method uses them to color the meshes and (if necessary) repaint
        // the control.
        void UpdateCustomStyles()
        {
            bool repaint = false;
            if (customStyle.TryGetValue(s_ProgressColor, out m_ProgressColor))
                repaint = true;

            if (customStyle.TryGetValue(s_TrackColor, out m_TrackColor))
                repaint = true;

            if (repaint)
                MarkDirtyRepaint();
        }

        void GenerateVisualContent(MeshGenerationContext context)
        {
            float width = contentRect.width;
            float height = contentRect.height;

            var painter = context.painter2D;
            painter.lineWidth = 10.0f;
            painter.lineCap = LineCap.Butt;

            // Draw the track
            painter.strokeColor = m_TrackColor;
            painter.BeginPath();
            painter.Arc(new Vector2(width * 0.5f, height * 0.5f), width * 0.5f, 0.0f, 360.0f);
            painter.Stroke();

            // Draw the progress
            painter.strokeColor = m_ProgressColor;
            painter.BeginPath();
            painter.Arc(new Vector2(width * 0.5f, height * 0.5f), width * 0.5f, -90.0f, 360.0f * (progress / 100.0f) - 90.0f);
            painter.Stroke();
        }
    }
}

```

## Style the custom control
Create a USS file named `RadialProgress.uss` with the following content:
```
.radial-progress {
        min-width: 26px;
        min-height: 20px;
        --track-color: rgb(130, 130, 130);
        --progress-color: rgb(46, 132, 24);
        --percentage-color: white;
        margin-left: 5px;
        margin-right: 5px;
        margin-top: 5px;
        margin-bottom: 5px;
        flex-direction: row;
        justify-content: center;
        width: 100px; 
        height: 100px;
    }

    .radial-progress__label {
        -unity-text-align: middle-left;
        color: var(--percentage-color);
    }

```

## Use the custom control in a UI Document and test
Use UI Builder to add the control and apply the USS stylesheet. Test the control with different `Progress` values.
  1. Create a UI Document named `RadialProgressExample.uxml`.
  2. Double-click `RadialProgressExample.uxml` to open it in the UI Builder.
  3. In the Library window, select **Project** > **Custom Controls** > **MyUILibrary**.
  4. Drag **RadialProgress** to the Hierarchy window.
  5. In the **StyleSheets** section of the UI Builder, add `RadialProgress.uss` as the existing USS.
  6. In the Hierarchy window, select **RadialProgress**.
  7. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, enter `radial-progress` in the **Name** box.
  8. In the Inspector window, enter different values in the **Progress** box. The percentage in the ****Viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport)** changes, and the green progress ring resizes.


## Create logic to update the progress with dynamic values
Create a C# MonoBehaviour script to update the `Progress` property of the control with dynamic values for demo purposes. In the `radial-progress` folder, create a C# MonoBehaviour named `RadialProgressComponent.cs` with the following content:
```
using MyUILibrary;
using UnityEngine;
using UnityEngine.UIElements;

[RequireComponent(typeof(UIDocument))]
public class RadialProgressComponent : MonoBehaviour
{
    RadialProgress m_RadialProgress;

    void Start()
    {
        var root = GetComponent<UIDocument>().rootVisualElement;

       m_RadialProgress = new RadialProgress() {
            style = {
                position = Position.Absolute,
                left = 20, top = 20, width = 200, height = 200
            }
        };

        root.Add(m_RadialProgress);
    }

    void Update()
    {
        m_RadialProgress.progress = ((Mathf.Sin(Time.time) + 1.0f) / 2.0f) * 60.0f + 10.0f;
    }
}

```

## Test the progress indicator in runtime
  1. In Unity, select **GameObject** > **UI Toolkit** > **UI Document**.
  2. Select the **UIDocument** in the Hierarchy window.
  3. Add **RadialProgressComponent.cs** as a component of the UIDocument **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).
  4. Enter play mode. The progress indicator appears in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), and the progress ring and value change dynamically.


## Additional resources
  * [Create custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html)
  * [Use Mesh API to create a radial progress indicator](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-radial-progress.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-pie-chart.html)
Create a pie chart in the Editor and runtime UI
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-radial-progress.html)
Use Mesh API to create a radial progress indicator
