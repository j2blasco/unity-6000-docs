* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-GUIStyle.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [IMGUI (Immediate Mode GUI)](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html)
  * GUI Style (IMGUI System)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GUISkin.html)
GUI Skin (IMGUI System)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ExtendingTheEditor.html)
Extending the Editor with IMGUI
# GUI Style (IMGUI System)
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html "Go to GUIStyle page in the Scripting Reference")
**GUI Styles** are a collection of custom attributes for use with **IMGUI**. A single GUI Style defines the appearance of a single IMGUI **Control**.
![A GUI Style in the Inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/imgui/GuiStyleInspector.png) A GUI Style in the Inspector
If you want to add style to more than one control, use a [GUI Skin](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GUISkin.html) instead of a GUI Style. For more information about IMGUI, please read the [GUI Scripting Guide](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html).
**Please Note** : This page refers to part of the [IMGUI](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html) system, which is a _scripting-only_ UI system. Unity has a full GameObject-based UI system which you may prefer to use. It allows you to design and edit user interface elements as visible objects in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view. See the [UI System Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.ugui.html) for more information.
## Properties
**_Property:_** | **_Function:_**  
---|---  
**Name** | The text string that can be used to refer to this specific Style  
**Normal** The direction perpendicular to the surface of a mesh, represented by a Vector. Unity uses normals to determine object orientation and apply shading. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normal) | Background image & Text Color of the Control in default state  
**Hover** | Background image & Text Color when the mouse is positioned over the Control  
**Active** | Background image & Text Color when the mouse is actively clicking the Control  
**Focused** | Background image & Text Color when the Control has keyboard focus  
**On Normal** | Background image & Text Color of the Control in enabled state  
**On Hover** | Background image & Text Color when the mouse is positioned over the enabled Control  
**On Active** | Properties when the mouse is actively clicking the enabled Control  
**On Focused** | Background image & Text Color when the enabled Control has keyboard focus  
**Border** | Number of **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) on each side of the **Background** image that are not affected by the scale of the Control’ shape  
**Padding** | Space in pixels from each edge of the Control to the start of its contents.  
**Margin** | The margins between elements rendered in this style and any other GUI Controls.  
**Overflow** | Extra space to be added to the background image.  
**Font** | The Font used for all text in this style  
**Image Position** | The way the background image and text are combined.  
**Alignment** | Standard text alignment options.  
**Word Wrap** | If enabled, text that reaches the boundaries of the Control will wrap around to the next line  
**Text Clipping** | If **Word Wrap** is enabled, choose how to handle text that exceeds the boundaries of the Control  
**Overflow** | Any text that exceeds the Control boundaries will continue beyond the boundaries  
**Clip** | Any text that exceeds the Control boundaries will be hidden  
**Content Offset** | Number of pixels along X and Y axes that the Content will be displaced in addition to all other properties  
**X** | Left/Right Offset  
**Y** | Up/Down Offset  
**Fixed Width** | Number of pixels for the width of the Control, which will override any provided **Rect()** value  
**Fixed Height** | Number of pixels for the height of the Control, which will override any provided **Rect()** value  
**Stretch Width** | If enabled, Controls using this style can be stretched horizontally for a better layout.  
**Stretch Height** | If enabled, Controls using this style can be stretched vertically for a better layout.  
## Details
GUIStyles are declared from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) and modified on a per-instance basis. If you want to use a single or few Controls with a custom Style, you can declare this custom Style in the script and provide the Style as an argument of the Control function. This will make these Controls appear with the Style that you define.
First, you must declare a GUI Style from within a script.
```
/* Declare a GUI Style */
var customGuiStyle : GUIStyle;

...



```

When you attach this script to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), you will see the custom Style available to modify in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
![A Style declared in a script can be modified in each instance of the script](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ModifyingStyleInInspector.png) A Style declared in a script can be modified in each instance of the script
Now, when you want to tell a particular Control to use this Style, you provide the name of the Style as the last argument in the Control function.
```
...

function OnGUI () {
    // Provide the name of the Style as the final argument to use it
    GUILayout.Button ("I am a custom-styled Button", customGuiStyle);

    // If you do not want to apply the Style, do not provide the name
    GUILayout.Button ("I am a normal IMGUI Button without custom style");
}



```
![Two Buttons, one with Style, as created by the code example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/imgui/guiStyle-TwoButtonsOneIsStyled.png) Two Buttons, one with Style, as created by the code example
For more information about using IMGUI, please read the [GUI Scripting Guide](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html).
GUIStyle
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GUISkin.html)
GUI Skin (IMGUI System)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ExtendingTheEditor.html)
Extending the Editor with IMGUI
