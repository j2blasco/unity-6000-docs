* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-conditional-ui.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Structure UI examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-examples.html)
  * Use Toggle to create a conditional UI


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-popup-window.html)
Create a pop-up window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-structuring-ui-custom-elements.html)
Create a custom control with two attributes
# Use Toggle to create a conditional UI
This example uses a Toggle to create a conditional UI. 
## Example overview
The example creates a custom Editor window with two toggles. You can use the toggles to do the following:
  * Show or hide a label
  * Activate or deactivate a button


You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/ToggleExample).
## Create the example
To create the example:
  1. Create a Unity project with any template.
  2. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `Editor`.
  3. In the `Editor` folder, create a C# script file named `ToggleExample` with the following content:
```
using UnityEngine;
using UnityEditor;
using UnityEngine.UIElements;
namespace Samples.Editor.Controls
{
    public class ToggleExample : EditorWindow
    {
        private Toggle showToggle;
        private Toggle activateToggle;
        private Label labelToShow;
        private Button buttonToActivate;
        [MenuItem("Window/ToggleExample")]
        public static void OpenWindow()
        {
            var window = GetWindow<ToggleExample>("Controls: Toggle Sample");
            window.minSize = new Vector2(200, 170);
        }
        public void CreateGUI()
        {
            showToggle = new Toggle("Show label")
            {
                value = true
            };
            activateToggle = new Toggle("Active button")
            {
                value = true
            };
            labelToShow = new Label("This label is shown when the above toggle is set to On");
            buttonToActivate = new Button(() => Debug.Log("Button pressed!"))
            {
                text = "Active if above toggle is On"
            };
            rootVisualElement.Add(showToggle);
            rootVisualElement.Add(labelToShow);
            rootVisualElement.Add(activateToggle);
            rootVisualElement.Add(buttonToActivate);
            showToggle.RegisterValueChangedCallback(evt => labelToShow.visible = evt.newValue);
            activateToggle.RegisterValueChangedCallback(evt => buttonToActivate.SetEnabled(evt.newValue));
        }
    }
}

```

  4. To try the example, from the menu, select **Window** > **ToggleExample**.


## Additional resources
  * [Toggle](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html)A checkbox that allows the user to switch an option on or off. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toggle)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-popup-window.html)
Create a pop-up window
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-structuring-ui-custom-elements.html)
Create a custom control with two attributes
