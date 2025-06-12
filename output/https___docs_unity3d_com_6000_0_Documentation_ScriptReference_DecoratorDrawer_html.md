* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.html

# DecoratorDrawer
class in UnityEditor
/
Inherits from:[GUIDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIDrawer.html)
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
Base class to derive custom decorator drawers from.
A DecoratorDrawer is similar to a [PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html), except that it doesn't draw a property but rather draws decorative elements based purely on the data it gets from its corresponding [PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html).  
  
Unity uses builtin DecoratorDrawers for the [SpaceAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpaceAttribute.html) and [HeaderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HeaderAttribute.html). You can also create your own DecoratorDrawers with matching PropertyAttributes.  
  
Although a DecoratorDrawer conceptually is not meant to be associated with a specific field, its attribute still needs to be placed above a field in the script. However, unlike PropertyDrawer attributes, there can be multiple DecoratorDrawers attributes above the same field. Also unlike PropertyDrawers, if a DecoratorDrawer attribute is placed above a field that is a List or an array, the decorator will only show up once before the array; not for every array element.  
  
**Note** : If you need your decorator drawer to perform cleanup tasks, such as detaching itself from editor events, you can implement the [IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable) interface. This interface allows you to define a method that will be invoked when the Editor is being destroyed, giving you the opportunity to handle any necessary cleanup operations.  
  
The example below comes in two scripts.  
  
The first script defines the an example attribute called "ColorSpacer", and then defines a DecoratorDrawer which determines how it should be drawn in the inspector.  
  
The second script is an example MonoBehaviour which uses the ColorSpacer attribute to visually separate two groups of public properties in the inspector.
```
// Name this script "ColorSpacerExample"  
  
using UnityEngine;
using System.Collections;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// This class defines the ColorSpacer attribute, so that
// it can be used in your regular MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) scripts:  
  
public class ColorSpacer : PropertyAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html)
{
    public float spaceHeight;
    public float lineHeight;
    public float lineWidth;
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) lineColor = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);  
  
    public ColorSpacer(float spaceHeight, float lineHeight, float lineWidth, float r, float g, float b)
    {
        this.spaceHeight = spaceHeight;
        this.lineHeight = lineHeight;
        this.lineWidth = lineWidth;  
  
        // unfortunately we can't pass a color through as a Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) object
        // so we pass as 3 floats and make the object here
        this.lineColor = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(r, g, b);
    }
}  
  

// This defines how the ColorSpacer should be drawn
// in the inspector, when inspecting a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with
// a MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) which uses the ColorSpacer attribute  
  
[CustomPropertyDrawer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomPropertyDrawer.html)(typeof(ColorSpacer))]
public class ColorSpacerDrawer : DecoratorDrawer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.html)
{
    ColorSpacer colorSpacer
    {
        get { return ((ColorSpacer)attribute); }
    }  
  
    public override float GetHeight()
    {
        return base.GetHeight() + colorSpacer.spaceHeight;
    }  
  
    public override void OnGUI(Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position)
    {
        // calculate the rect values for where to draw the line in the inspector
        float lineX = (position.x + (position.width / 2)) - colorSpacer.lineWidth / 2;
        float lineY = position.y + (colorSpacer.spaceHeight / 2);
        float lineWidth = colorSpacer.lineWidth;
        float lineHeight = colorSpacer.lineHeight;  
  
        // Draw the line in the calculated place in the inspector
        EditorGUI.DrawRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawRect.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(lineX, lineY, lineWidth, lineHeight), colorSpacer.lineColor);
    }
}

```

And this second script is the one which makes use of the ColorSpacer attribute defined above:
```
using UnityEngine;
using System.Collections;  
  
public class ShowDecoratorDrawerExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int a = 1;
    public int b = 2;
    public int c = 3;  
  
    // this shows our custom Decorator Drawer between the groups of properties
    [ColorSpacer(30, 3, 100, 1, 0, 0)]  
  
    public string d = "d";
    public string e = "e";
    public string f = "f";
}

```

### Properties
Property | Description  
---|---  
[attribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer-attribute.html) | The PropertyAttribute for the decorator. (Read Only)  
### Public Methods
Method | Description  
---|---  
[CreatePropertyGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.CreatePropertyGUI.html) | Override this method to make your own GUI for the property based on UIElements.  
[GetHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.GetHeight.html) | Override this method to specify how tall the GUI for this decorator is in pixels.  
[OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.OnGUI.html) | Override this method to make your own GUI for the decorator. See DecoratorDrawer for an example of how to use this.  
### Inherited Members
* * *
