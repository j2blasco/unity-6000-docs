* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUtility.TryParseHtmlString.html

#  [ColorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUtility.html).TryParseHtmlString
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
## Declaration
public static bool TryParseHtmlString(string htmlString, out [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color); 
### Parameters
Parameter | Description  
---|---  
htmlString | Case insensitive html string to be converted into a color.  
color | The converted color.  
### Returns
**bool** True if the string was successfully converted else false. 
### Description
Attempts to convert a html color string.
**Strings that begin with '#' will be parsed as hexadecimal in the following way:**   
#RGB (becomes RRGGBB)  
#RRGGBB  
#RGBA (becomes RRGGBBAA)  
#RRGGBBAA  
  
When not specified alpha will default to FF.   
**Strings that do not begin with '#' will be parsed as literal colors, with the following supported:**  
red, cyan, blue, darkblue, lightblue, purple, yellow, lime, fuchsia, white, silver, grey, black, orange, brown, maroon, green, olive, navy, teal, aqua, magenta..  
  
The following example creates a custom PropertyDrawer that allows the user to input html colors. This property drawer can be shown in the inspector when a color property has the attribute ColorHtmlProperty.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/HexColorPropertyDrawer.png)  
_our custom property drawer._
```
// This is not an editor script.
using UnityEngine;  
  
public class ColorHtmlPropertyAttribute : PropertyAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html)
{
}

```

```
// This is an editor script and should be placed in an 'Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)' directory.
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomPropertyDrawer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomPropertyDrawer.html)(typeof(ColorHtmlPropertyAttribute))]
public class ColorHtmlPropertyDrawer : PropertyDrawer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html)
{
    public override void OnGUI(Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label)
    {
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) htmlField = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(position.x, position.y, position.width - 100, position.height);
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) colorField = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(position.x + htmlField.width, position.y, position.width - htmlField.width, position.height);  
  
        string htmlValue = EditorGUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextField.html)(htmlField, label, "#" + ColorUtility.ToHtmlStringRGBA[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUtility.ToHtmlStringRGBA.html)(property.colorValue));  
  
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) newCol;
        if (ColorUtility.TryParseHtmlString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUtility.TryParseHtmlString.html)(htmlValue, out newCol))
            property.colorValue = newCol;  
  
        property.colorValue = EditorGUI.ColorField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ColorField.html)(colorField, property.colorValue);
    }
}

```

```
// This shows how we would use the PropertyDrawer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html).
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [ColorHtmlProperty]
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) htmlColor = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);  
  
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) standardColor = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
}

```

* * *
