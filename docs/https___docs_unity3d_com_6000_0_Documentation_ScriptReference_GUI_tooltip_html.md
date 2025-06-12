* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).tooltip
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
tooltip; 
### Description
The tooltip of the control the mouse is currently over, or which has keyboard focus. (Read Only).
When you create GUI controls, you can pass in a tooltip for them. This is done by changing the content parameter to take a custom-made [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) object, rather than just passing in a string to display.  
  
When the mouse is over a control with a tooltip, it sets the global [GUI.tooltip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html) value to the tooltip you pass in. If the mouse is not hovering over any control, the value is set to the control which has keyboard focus. At the end of the OnGUI code, you can make a label showing the value of [GUI.tooltip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUITooltip.png)  
_GUI Tooltip on the Game view appears when the mouse is over the button._
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        // Make a button using a custom GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) parameter to pass in the tooltip.
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 20), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Click me", "This is the tooltip"));  
  
        // Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the tooltip from the element that has mouseover or keyboard focus
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 40, 100, 40), GUI.tooltip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html));
    }
}

```

You can use the ordering of elements to create 'hierarchical' tooltips:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        // This box is larger than many elements following it, and it has a tooltip.
        GUI.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(5, 35, 110, 75), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html)", "this box has a tooltip"));  
  
        // This button is inside the box, but has no tooltip so it does not
        // override the box's tooltip.
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 55, 100, 20), "No tooltip here");  
  
        // This button is inside the box, and HAS a tooltip so it overrides
        // the tooltip from the box.
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 80, 100, 20), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("I have a tooltip", "The button overrides the box"));  
  
        // finally, display the tooltip from the element that has
        // mouseover or keyboard focus
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 40, 100, 40), GUI.tooltip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html));
    }
}

```

Tooltips can also be used to implement an OnMouseOver / OnMouseOut messaging system:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string lastTooltip = " ";  
  
    void OnGUI()
    {
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Play Game", "Button1"));
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Quit", "Button2"));  
  
        if (Event.current.type == EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html) && GUI.tooltip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html) != lastTooltip)
        {
            if (lastTooltip != "")
            {
                SendMessage(lastTooltip + "OnMouseOut", SendMessageOptions.DontRequireReceiver[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.DontRequireReceiver.html));
            }  
  
            if (GUI.tooltip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html) != "")
            {
                SendMessage(GUI.tooltip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html) + "OnMouseOver", SendMessageOptions.DontRequireReceiver[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.DontRequireReceiver.html));
            }  
  
            lastTooltip = GUI.tooltip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html);
        }
    }  
  
    void Button1OnMouseOver()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Play game got focus");
    }  
  
    void Button2OnMouseOut()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Quit lost focus");
    }
}

```

* * *
