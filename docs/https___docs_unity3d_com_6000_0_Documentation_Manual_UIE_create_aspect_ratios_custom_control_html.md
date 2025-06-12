* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-aspect-ratios-custom-control.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Structure UI examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-examples.html)
  * Create an aspect ratio custom control


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-list-treeview-between-windows.html)
Create a drag-and-drop list and tree views between windows
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/example-create-custom-inventory-property-drawer.html)
Create a custom inventory property drawer
# Create an aspect ratio custom control
The **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio) is the ratio between the width and height of the display. The aspect ratio is used to maintain the proportions of the display. For example, if you have a `4:3` aspect ratio, then the display is `4` **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) wide for every `3` pixels in height. If you have a `16:9` aspect ratio, then the display is `16` pixels wide for every `9` pixels in height.
## Example overview
This example creates a custom control that maintains a specified aspect ratio of its child elements. For demonstration purposes, the custom control adds paddings to the left and right if the display ratio is wider, or the top and bottom if the display ratio is higher, pushing the “central” items to fit into the aspect ratio.
![Aspect ratio example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uxml/aspect-ratio.png) Aspect ratio example
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/2023.2/create-aspect-ratios-custom-control).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [Custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-custom-controls.html)


## Create the custom control class
Create a C# class that inherits from `VisualElement` with two attributes: `width` and `height`. The `width` and `height` attributes are used to calculate the aspect ratio.
  1. Create a Unity project with any template.
  2. Create a C# script named `AspectRatio.cs` with the following content:
```
using UnityEngine;
using UnityEngine.UIElements;
    
// Custom element that lays out its contents following a specific aspect ratio.
[UxmlElement]
public partial class AspectRatioElement : VisualElement
{
    // The ratio of width.
    [UxmlAttribute("width")]
    public int RatioWidth
    {
        get => _ratioWidth;
        set
        {
            _ratioWidth = value;
            UpdateAspect();
        }
    }
    
    // The ratio of height.
    [UxmlAttribute("height")]
    public int RatioHeight
    {
        get => _ratioHeight;
        set
        {
            _ratioHeight = value;
            UpdateAspect();
        }
    }
    
    // Padding elements to keep the aspect ratio.
    private int _ratioWidth = 16;
    private int _ratioHeight = 9;
    
    public AspectRatioElement()
    {
        // Update the padding elements when the geometry changes.
        RegisterCallback<GeometryChangedEvent>(UpdateAspectAfterEvent);
        // Update the padding elements when the element is attached to a panel.
        RegisterCallback<AttachToPanelEvent>(UpdateAspectAfterEvent);
    }
    
    static void UpdateAspectAfterEvent(EventBase evt)
    {
        var element = evt.target as AspectRatioElement;
        element?.UpdateAspect();
    }
    
    private void ClearPadding()
    {
        style.paddingLeft = 0;
        style.paddingRight = 0;
        style.paddingBottom = 0;
        style.paddingTop = 0;
    }
        
    // Update the padding.
    private void UpdateAspect()
    {
        var designRatio = (float)RatioWidth / RatioHeight;
        var currRatio = resolvedStyle.width / resolvedStyle.height;
        var diff = currRatio - designRatio;
            
        if (RatioWidth <= 0.0f || RatioHeight <= 0.0f)
        {
            ClearPadding();
            Debug.LogError($"[AspectRatio] Invalid width:{RatioWidth} or height:{RatioHeight}");
            return;
        }
    
        if (float.IsNaN(resolvedStyle.width) || float.IsNaN(resolvedStyle.height))
        {
            return;
        }
            
        if (diff > 0.01f)
        {
            var w = (resolvedStyle.width - (resolvedStyle.height * designRatio)) * 0.5f;
            style.paddingLeft = w;
            style.paddingRight = w;
            style.paddingTop = 0;
            style.paddingBottom = 0;
        }
        else if (diff < -0.01f)
        {
            var h = (resolvedStyle.height - (resolvedStyle.width * (1/designRatio))) * 0.5f;
            style.paddingLeft= 0;
            style.paddingRight = 0;
            style.paddingTop = h;
            style.paddingBottom = h;
        }
        else
        {
            ClearPadding();
        }
    }
}

```



## Use the custom control
Create a custom Editor window that uses the custom control. Test the custom control to see how it behaves when you change the aspect ratio.
  1. Create a C# script named `AspectRatioDemo.cs` with the following content:
```
using UnityEditor;
using UnityEngine;
using UnityEngine.UIElements;
    
public class AspectRatioDemo : EditorWindow
{
    [SerializeField]
    private VisualTreeAsset m_VisualTreeAsset = default;
    
    [MenuItem("Test/AspectRatioDemo")]
    public static void ShowExample()
    {
        AspectRatioDemo wnd = GetWindow<AspectRatioDemo>();
        wnd.titleContent = new GUIContent("AspectRatioDemo");
    }
    
    public void CreateGUI()
    {
        // Each editor window contains a root VisualElement object.
        VisualElement root = rootVisualElement;
    
        var aspectRatio = new AspectRatioElement();
        aspectRatio.style.flexGrow = 1;
    
        var widthField = new IntegerField() { value = aspectRatio.RatioWidth, label = "W"};
        var heightField = new IntegerField() { value = aspectRatio.RatioHeight, label = "H" };
    
        root.Add(widthField);
        root.Add(heightField);
        root.Add(aspectRatio);
    
        var contents = new VisualElement();
        aspectRatio.Add(contents);
    
        aspectRatio.style.backgroundColor = Color.black;
    
        contents.style.backgroundColor = Color.green;
    
        widthField.RegisterValueChangedCallback((evt) =>aspectRatio.RatioWidth = evt.newValue);
        heightField.RegisterValueChangedCallback((evt) => aspectRatio.RatioHeight = evt.newValue);
            
        contents.style.width = new Length(100, LengthUnit.Percent);
        contents.style.height = new Length(100, LengthUnit.Percent);
            
        contents.RegisterCallback<GeometryChangedEvent>((evt) =>
        {
            Debug.Log($"Content ratio: {evt.newRect.width} x {evt.newRect.height} : {evt.newRect.width/evt.newRect.height}");
        });
    
    }
}

```

  2. From the menu, select **Test** > **Aspect Ratio Demo**.
  3. Change the aspect ratios to different values. The custom control adds padding to the left and right, or top and bottom depending on the size of your Editor window.


## Additional resources
  * [Support for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-runtime-ui.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-list-treeview-between-windows.html)
Create a drag-and-drop list and tree views between windows
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/example-create-custom-inventory-property-drawer.html)
Create a custom inventory property drawer
