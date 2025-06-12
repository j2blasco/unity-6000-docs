* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gui-Customization.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [IMGUI (Immediate Mode GUI)](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html)
  * Customize IMGUI controls


[](https://docs.unity3d.com/6000.0/Documentation/Manual/gui-Controls.html)
IMGUI Controls
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gui-Layout.html)
IMGUI Layout Modes
# Customize IMGUI controls
Although Unity’s IMGUI system is mainly intended for creating developer tools and debugging interfaces, you can still customize and style them in many ways. In Unity’s IMGUI system, you can fine-tune the appearance of your Controls with many details. Control appearances are dictated with **GUIStyles**. By default, when you create a Control without defining a GUIStyle, Unity’s default GUIStyle is applied. This style is internal in Unity and can be used in published games for quick prototyping, or if you choose not to stylize your Controls.
When you have a large number of different GUIStyles to work with, you can define them all within a single **GUISkin**. A GUISkin is no more than a collection of GUIStyles.
## How styles change the look of your GUI Controls
GUIStyles are designed to mimic Cascading Style Sheets (CSS) for web browsers. Many different CSS methodologies have been adapted, including differentiation of individual state properties for styling, and separation between the content and the appearance.
Where the Control defines the content, the Style defines the appearance. This allows you to create combinations like a functional **Toggle** A checkbox that allows the user to switch an option on or off. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Toggle.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toggle) which looks like a normal **Button**.
![Two Toggle Controls styled differently](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/gsg-ToggleStyles.png) Two Toggle Controls styled differently
### The difference between skins and styles
As stated earlier, GUISkins are a collection of GUIStyles. Styles define the appearance of a GUI Control. You do not have to use a Skin if you want to use a Style.
![A single GUIStyle shown in the Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/imgui/GuiStyleInspector.png) A single GUIStyle shown in the Inspector ![A single GUISkin shown in the Inspector with multiple GUIStyles](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Inspector-GUISkin.png) A single GUISkin shown in the Inspector with multiple GUIStyles
## Working with styles
All GUI Control functions have an optional last parameter: the GUIStyle to use for displaying the Control. If this is omitted, Unity’s default GUIStyle will be used. This works internally by applying the name of the control type as a string, so **GUI.Button()** uses the “button” style, **GUI.Toggle()** uses the “toggle” style, etc. You can override the default GUIStyle for a control by specifying it as the last parameter.
```
/* Override the default Control Style with a different style in the UnityGUI default Styles */

using UnityEngine;
using System.Collections;

public class GUITest : MonoBehaviour {
                    
    void OnGUI () {
        // Make a label that uses the "box" GUIStyle.
        GUI.Label (new Rect (0,0,200,100), "Hi - I'm a label looking like a box", "box");
    
        // Make a button that uses the "toggle" GUIStyle
        GUI.Button (new Rect (10,140,180,20), "This is a button", "toggle");
    }

}

```
![The controls created by the code example above](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/gsg-DifferentDefaultStyles.png) The controls created by the code example above
### Making a public variable GUIStyle
When you declare a public GUIStyle variable, all elements of the Style will show up in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector). You can edit all of the different values there.
```
/* Overriding the default Control Style with one you've defined yourself */

using UnityEngine;
using System.Collections;

public class GUITest : MonoBehaviour {
                    
    public GUIStyle customButton;
    
    void OnGUI () {
        // Make a button. We pass in the GUIStyle defined above as the style to use
        GUI.Button (new Rect (10,10,150,20), "I am a Custom Button", customButton);
    }
    
}

```

### Changing the different style elements
When you have declared a GUIStyle, you can modify that style in the Inspector. There are a great number of States you can define, and apply to any type of Control.
![Styles are modified on a per-script, per-GameObject basis](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ModifyingStyleInInspector.png) Styles are modified on a per-script, per-GameObject basis
Any Control State must be assigned a **Background** Color before the specified **Text Color** will be applied.
For more information about individual GUIStyles, please read the [GUIStyle Component Reference page](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GUIStyle.html).
## Working with skins
For more complicated GUI systems, it makes sense to keep a collection of styles in one place. This is what a GUISkin does. A GUISkin contains multiple different Styles, essentially providing a complete face-lift to all GUI Controls. 
### Creating a new GUISkin
To create a GUISkin, select **Assets- >Create->GUI Skin** from the menu bar. This will create a GUI Skin in your Project Folder. Select it to see all GUIStyles defined by the Skin in the Inspector.
### Applying the skin to a GUI
To use a skin you’ve created, assign it to **GUI.skin** in your **OnGUI()** function.
```
/* Make a property containing a reference to the skin you want to use */

using UnityEngine;
using System.Collections;

public class GUITest : MonoBehaviour {
                    
    public GUISkin mySkin;
    
    void OnGUI () {
        // Assign the skin to be the one currently used.
        GUI.skin = mySkin;
    
        // Make a button. This will get the default "button" style from the skin assigned to mySkin.
        GUI.Button (new Rect (10,10,150,20), "Skinned Button");
    }
        
}

```

You can switch skins as much as you like throughout a single **OnGUI()** call.
```
/* Example of switching skins in the same OnGUI() call */

using UnityEngine;
using System.Collections;

public class GUITest : MonoBehaviour {
                    
    public GUISkin mySkin;
    private bool toggle = true;
    
    void OnGUI () {
        // Assign the skin to be the one currently used.
        GUI.skin = mySkin;
    
        // Make a toggle. This will get the "button" style from the skin assigned to mySkin.
        toggle = GUI.Toggle (new Rect (10,10,150,20), toggle, "Skinned Button", "button");
    
        // Assign the currently skin to be Unity's default.
        GUI.skin = null;
    
        // Make a button. This will get the default "button" style from the built-in skin.
        GUI.Button (new Rect (10,35,150,20), "Built-in Button");
    }
        
}

```

### Changing GUI font size
This example will show you how to dynamically change the font size through code. 
First create a new project in Unity. Then make a C# script called Fontsize.cs and paste the following code in:
```
using UnityEngine;
using System.Collections;
    
public class Fontsize : MonoBehaviour
{
    void OnGUI ()
    {
        //Set the GUIStyle style to be label
        GUIStyle style = GUI.skin.GetStyle ("label");
        
        //Set the style font size to increase and decrease over time
        style.fontSize = (int)(20.0f + 10.0f * Mathf.Sin (Time.time));
        
        //Create a label and display with the current settings
        GUI.Label (new Rect (10, 10, 200, 80), "Hello World!");
    }
        
}

```

Save the script and attach it to an empty **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), click play to see the font loop through increasing and decreasing in size over time. You may notice that the font does not smoothly change size, this is becauses there is not an infinite number of font sizes.
This specific example requires that the default font (Arial) is loaded and marked as dynamic. You cannot change the size of any font that is not marked as dynamic.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gui-Controls.html)
IMGUI Controls
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gui-Layout.html)
IMGUI Layout Modes
