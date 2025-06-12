* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html

# GUI
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
### Description
The GUI class is the interface for Unity's GUI with manual positioning.
  
Additional resources: [GUI tutorial](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html).
### Static Properties
Property | Description  
---|---  
[backgroundColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-backgroundColor.html) | Global tinting color for all background elements rendered by the GUI.  
[changed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html) | Returns true if any controls changed the value of the input data.  
[color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) | Applies a global tint to the GUI. The tint affects backgrounds and text colors.  
[contentColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-contentColor.html) | Tinting color for all text rendered by the GUI.  
[depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-depth.html) | The sorting depth of the currently executing GUI behaviour.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-enabled.html) | Is the GUI enabled?  
[matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-matrix.html) | The GUI transform matrix.  
[skin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-skin.html) | The global skin to use.  
[tooltip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-tooltip.html) | The tooltip of the control the mouse is currently over, or which has keyboard focus. (Read Only).  
### Static Methods
Method | Description  
---|---  
[BeginGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html) | Begin a group. Must be matched with a call to EndGroup.  
[BeginScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginScrollView.html) | Begin a scrolling view inside your GUI.  
[Box](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html) | Create a Box on the GUI Layer.  
[BringWindowToBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToBack.html) | Bring a specific window to back of the floating windows.  
[BringWindowToFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToFront.html) | Bring a specific window to front of the floating windows.  
[Button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html) | Make a single press button. The user clicks them and something happens immediately.  
[DragWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html) | Make a window draggable.  
[DrawTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTexture.html) | Draw a texture within a rectangle.  
[DrawTextureWithTexCoords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTextureWithTexCoords.html) | Draw a texture within a rectangle with the given texture coordinates.  
[EndGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndGroup.html) | End a group.  
[EndScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndScrollView.html) | Ends a scrollview started with a call to BeginScrollView.  
[FocusControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.FocusControl.html) | Move keyboard focus to a named control.  
[FocusWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.FocusWindow.html) | Make a window become the active window.  
[GetNameOfFocusedControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.GetNameOfFocusedControl.html) | Get the name of named control that has focus.  
[HorizontalScrollbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalScrollbar.html) | Make a horizontal scrollbar. Scrollbars are what you use to scroll through a document. Most likely, you want to use scrollViews instead.  
[HorizontalSlider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html) | A horizontal slider the user can drag to change a value between a min and a max.  
[Label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html) | Make a text or texture label on screen.  
[ModalWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ModalWindow.html) | Show a Modal Window.  
[PasswordField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.PasswordField.html) | Make a text field where the user can enter a password.  
[RepeatButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.RepeatButton.html) | Make a button that is active as long as the user holds it down.  
[ScrollTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ScrollTo.html) | Scrolls all enclosing scrollviews so they try to make position visible.  
[SelectionGrid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SelectionGrid.html) | Make a grid of buttons.  
[SetNextControlName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html) | Set the name of the next control.  
[TextArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextArea.html) | Make a Multi-line text area where the user can edit a string.  
[TextField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html) | Make a single-line text field where the user can edit a string.  
[Toggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html) | Make an on/off toggle button.  
[Toolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toolbar.html) | Make a toolbar.  
[UnfocusWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.UnfocusWindow.html) | Remove focus from all windows.  
[VerticalScrollbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalScrollbar.html) | Make a vertical scrollbar. Scrollbars are what you use to scroll through a document. Most likely, you want to use scrollViews instead.  
[VerticalSlider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalSlider.html) | A vertical slider the user can drag to change a value between a min and a max.  
[Window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html) | Make a popup window.  
### Delegates
Delegate | Description  
---|---  
[WindowFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.WindowFunction.html) | Callback to draw GUI within a window (used with GUI.Window).  
* * *
