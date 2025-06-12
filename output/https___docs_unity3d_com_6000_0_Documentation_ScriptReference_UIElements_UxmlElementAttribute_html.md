* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlElementAttribute.html

# UxmlElementAttribute
class in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Declares a custom control. 
To create a custom control, you must add the UxmlElement attribute to the custom control class definition. You must declare the custom control class as a partial class and inherit it from [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) or one of its derived classes. When an element is marked with the UxmlElement attribute, a corresponding [UxmlSerializedData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.UxmlSerializedData.html) class is generated in the partial class. This data class contains a [SerializeField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html) for each field or property that was marked with the [UxmlAttributeAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeAttribute.html) attribute. This serialized data allows for the element to be serialized from UXML and supports editing in the Attributes field of the Inspector window in the UI Builder. By default, the custom control appears in the Library tab in UI Builder. To hide it from the Library tab, provide the [HideInInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html) attribute.  
  
For an example of migrating a custom control from `UxmlFactory` and `UxmlTraits` to the `UxmlElement` and `UxmlAttributes` system, refer to [Enhanced custom controls creation with UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuideUnity6#enhanced-custom-controls-creation-with-uxml.html).   
  
The following example creates a custom control with multiple attributes: 
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;  
  
[UxmlElement]
public partial class ExampleVisualElement : VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
{
    [UxmlAttribute]
    public string myStringValue { get; set; }  
  
    [UxmlAttribute]
    public int myIntValue { get; set; }  
  
    [UxmlAttribute]
    public float myFloatValue { get; set; }  
  
    [UxmlAttribute]
    public List<int> myListOfInts { get; set; }  
  
    [UxmlAttribute, UxmlTypeReference(typeof(VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)))]
    public Type myType { get; set; }  
  
    [UxmlAttribute]
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) myTexture { get; set; }  
  
    [UxmlAttribute]
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) myColor { get; set; }
}

```

The following UXML document uses the custom control: 
```
<ui:UXML xmlns:ui="UnityEngine.UIElements">
    <ExampleElement my-string-value="Hello World" my-int-value="123" />
    <ExampleElement my-float-value="3.14" my-list-of-ints="1,2,3" />
    <ExampleElement my-string-value="Hello World" my-int-value="123" />
    <ExampleElement my-texture="project://database/Assets/MyTexture.png" />
    <ExampleElement my-color="#FF0000FF" />
    <ExampleElement my-type="UnityEngine.UIElements.Button, UnityEngine.UIElementsModule[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)" />
</ui:UXML>

```

When you create a custom control, the default name used in UXML and UI Builder is the element type name (C# class name). However, you can customize the name to make it easier to refer to the element.   
  
**Note** : You are still required to reference the classes' namespace in UXML. To create a custom name for an element, provide a value to the `name` property.   
For example, if you create the following custom button: 
```
using UnityEngine.UIElements;  
  
[UxmlElement("MyButton")]
public partial class CustomButtonElement : Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
{
}

```

You can then reference the custom button in UXML with the custom name or its type: 
```
<ui:UXML xmlns:ui="UnityEngine.UIElements">
    <MyButton />
    <CustomButtonElement />
</ui:UXML>

```

### Properties
Property | Description  
---|---  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlElementAttribute-name.html) |  Provides a custom name for an element.   
### Constructors
Constructor | Description  
---|---  
[UxmlElementAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlElementAttribute-ctor.html) |  Exposes a type of VisualElement to UXML and UI Builder   
* * *
