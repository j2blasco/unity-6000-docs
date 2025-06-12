* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).Box
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
public static void Box([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text); 
## Declaration
public static void Box([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public static void Box([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public static void Box([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void Box([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void Box([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the box.  
text | Text to display on the box.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display on the box.  
content | Text, image and tooltip for this box.  
style | The style to use. If left out, the `box` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
### Description
Create a Box on the GUI Layer.
A Box can contain text, an image, or a combination of these along with an optional tooltip, through using a [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) parameter. You may also use a [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) to adjust the layout of items in a box, text colour and other properties.  
  
Here is an example of a Box containing Text:
```
using UnityEngine;  
  
public class BoxExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html)), "This is a box");
    }
}

```

Here is an example of a Box containing a Texture:
```
using UnityEngine;  
  
public class BoxWithTextureExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) BoxTexture;      // Drag a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) onto this item in the Inspector  
  
    void OnGUI()
    {
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html)), BoxTexture);
    }
}

```

Here is an example of a Box containing a GUIContent, combining Text, Texture and Tooltip:
```
using UnityEngine;  
  
public class BoxWithContentExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) BoxTexture;      // Drag a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) onto this item in the Inspector  
  
    GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content;  
  
    void Start()
    {
        content = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("This is a box", BoxTexture, "This is a tooltip");
    }  
  
    void OnGUI()
    {
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html)), content);
    }
}

```

Here is an example of a Box containing Text, with options set in a GUIStyle to position the Text in the center of the Box.
```
using UnityEngine;  
  
public class BoxWithTextStyleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)();  
  
    void Start()
    {
        // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) the Text in the center of the Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html)
        style.alignment = TextAnchor.MiddleCenter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAnchor.MiddleCenter.html);
    }  
  
    void OnGUI()
    {
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html)), "This is a box", style);
    }
}

```

Here is an example of a Box containing a Texture, with options set in a GUIStyle to position the Texture in the center of the Box.
```
using UnityEngine;  
  
public class BoxWithTextureStyleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) BoxTexture;              // Drag a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) onto this item in the Inspector  
  
    GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)();  
  

    void Start()
    {
        // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) in the center of the Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html)
        style.alignment = TextAnchor.MiddleCenter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAnchor.MiddleCenter.html);
    }  
  
    void OnGUI()
    {
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html)), BoxTexture, style);
    }
}

```

Finally, here is an example of a Box containing a GUIContent, combining Text, Texture and Tooltip, with positional information contained in the GUIStyle parameter:
```
using UnityEngine;  
  
public class BoxWithContentStyleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) BoxTexture;              // Drag a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) onto this item in the Inspector  
  
    GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content;
    GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)();  
  
    void Start()
    {
        content = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("This is a box", BoxTexture, "This is a tooltip");  
  
        // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) the Text and Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) in the center of the box
        style.alignment = TextAnchor.MiddleCenter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAnchor.MiddleCenter.html);  
  
        // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) the Text below the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) (rather than to the right of it)
        style.imagePosition = ImagePosition.ImageAbove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImagePosition.ImageAbove.html);
    }  
  
    void OnGUI()
    {
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html)), content, style);
    }
}

```

* * *
