* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.IMGUIModule.html

# UnityEngine.IMGUIModule
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
The IMGUI module provides Unity's immediate mode GUI solution for creating in-game and editor user interfaces.
  
Additional resources: [GUI tutorial](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html).
### Classes
Class | Description  
---|---  
[Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) | A UnityGUI event.  
[ExitGUIException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExitGUIException.html) | An exception that will prevent all subsequent immediate mode GUI functions from evaluating for the remainder of the GUI loop.  
[GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) | The GUI class is the interface for Unity's GUI with manual positioning.  
[GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) | The contents of a GUI element.  
[GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html) | The GUILayout class is the interface for Unity gui with automatic layout.  
[GUILayoutOption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutOption.html) | Class internally used to pass layout options into GUILayout functions. You don't use these directly, but construct them with the layouting functions in the GUILayout class.  
[GUILayoutUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutUtility.html) | Utility functions for implementing and extending the GUILayout class.  
[GUISettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISettings.html) | General settings for how the GUI behaves.  
[GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) | Defines how GUI looks and behaves.  
[GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) | Styling information for GUI elements.  
[GUIStyleState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyleState.html) | Specialized values for the given states used by GUIStyle objects.  
[GUITargetAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUITargetAttribute.html) | Allows to control for which display the OnGUI is called.  
[GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html) | Utility class for making new GUI controls.  
### Enumerations
Enumeration | Description  
---|---  
[EventModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventModifiers.html) | Types of modifier key that can be active during a keystroke event.  
[EventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html) | Types of UnityGUI input and processing events.  
[FocusType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.html) | Used by GUIUtility.GetControlID to inform the IMGUI system if a given control can get keyboard focus. This allows the IMGUI system to give focus appropriately when a user presses tab for cycling between controls.  
[ImagePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImagePosition.html) | How image and text is placed inside GUIStyle.  
[PointerType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PointerType.html) | Pointer types.  
[ScaleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.html) | Scaling mode to draw textures with.  
[TextClipping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextClipping.html) | Different methods for how the GUI system handles text being too large to fit the rectangle allocated.  
* * *
