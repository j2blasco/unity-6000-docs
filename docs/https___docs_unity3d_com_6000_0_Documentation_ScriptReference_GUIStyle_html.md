* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html

# GUIStyle
class in UnityEngine
/
Implemented in:[UnityEngine.IMGUIModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.IMGUIModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GUIStyle.html "Go to GUIStyle Component in the Manual")
### Description
Styling information for GUI elements.
Most GUI functions accept an optional GUIStyle parameter to override the default style. This allows coloring, fonts and other details to be changed and switched for different states (eg, when the mouse is hovering over the control). Where a consistent look-and-feel is required over a whole GUI design, the GUISkin class is a useful way to collect a set of GUIStyle settings and apply them all at once.
### Static Properties
Property | Description  
---|---  
[none](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-none.html) | Shortcut for an empty GUIStyle.  
### Properties
Property | Description  
---|---  
[active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-active.html) | Rendering settings for when the control is pressed down.  
[alignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-alignment.html) | Text alignment.  
[border](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-border.html) | The borders of all background images.  
[clipping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-clipping.html) | What to do when the contents to be rendered is too large to fit within the area given.  
[contentOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-contentOffset.html) | Pixel offset to apply to the content of this GUIstyle.  
[fixedHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-fixedHeight.html) | If non-0, any GUI elements rendered with this style will have the height specified here.  
[fixedWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-fixedWidth.html) | If non-0, any GUI elements rendered with this style will have the width specified here.  
[focused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-focused.html) | Rendering settings for when the element has keyboard focus.  
[font](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-font.html) | The font to use for rendering. If null, the default font for the current GUISkin is used instead.  
[fontSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-fontSize.html) | The font size to use (for dynamic fonts).  
[fontStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-fontStyle.html) | The font style to use (for dynamic fonts).  
[hover](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-hover.html) | Rendering settings for when the mouse is hovering over the control.  
[imagePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-imagePosition.html) | How image and text of the GUIContent is combined.  
[lineHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-lineHeight.html) | The height of one line of text with this style, measured in pixels. (Read Only)  
[margin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-margin.html) | The margins between elements rendered in this style and any other GUI elements.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-name.html) | The name of this GUIStyle. Used for getting them based on name.  
[normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-normal.html) | Rendering settings for when the component is displayed normally.  
[onActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-onActive.html) | Rendering settings for when the element is turned on and pressed down.  
[onFocused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-onFocused.html) | Rendering settings for when the element has keyboard and is turned on.  
[onHover](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-onHover.html) | Rendering settings for when the control is turned on and the mouse is hovering it.  
[onNormal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-onNormal.html) | Rendering settings for when the control is turned on.  
[overflow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-overflow.html) | Extra space to be added to the background image.  
[padding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-padding.html) | Space from the edge of GUIStyle to the start of the contents.  
[richText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-richText.html) | Enable HTML-style tags for Text Formatting Markup.  
[stretchHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-stretchHeight.html) | Can GUI elements of this style be stretched vertically for better layout?  
[stretchWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-stretchWidth.html) | Can GUI elements of this style be stretched horizontally for better layouting?  
[wordWrap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-wordWrap.html) | Should the text be wordwrapped?  
### Constructors
Constructor | Description  
---|---  
[GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-ctor.html) | Constructor for empty GUIStyle.  
### Public Methods
Method | Description  
---|---  
[CalcHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.CalcHeight.html) | How tall this element will be when rendered with content and a specific width.  
[CalcMinMaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.CalcMinMaxWidth.html) | Calculate the minimum and maximum widths for this style rendered with content.  
[CalcScreenSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.CalcScreenSize.html) | Calculate the size of an element formatted with this style, and a given space to content.  
[CalcSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.CalcSize.html) | Calculate the size of some content if it is rendered with this style.  
[Draw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.Draw.html) | Draw this GUIStyle on to the screen, internal version.  
[DrawCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.DrawCursor.html) | Draw this GUIStyle with selected content.  
[DrawWithTextSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.DrawWithTextSelection.html) | Draw this GUIStyle with selected content.  
[GetCursorPixelPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.GetCursorPixelPosition.html) | Get the pixel position of a given string index.  
[GetCursorStringIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.GetCursorStringIndex.html) | Get the cursor position (indexing into contents.text) when the user clicked at cursorPixelPosition.  
### Operators
Operator | Description  
---|---  
[GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-operator_string.html) | Get a named GUI style from the current skin.  
* * *
