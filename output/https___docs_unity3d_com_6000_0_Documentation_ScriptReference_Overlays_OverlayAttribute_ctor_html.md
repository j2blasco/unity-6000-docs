* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayAttribute-ctor.html

# OverlayAttribute Constructor
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
public OverlayAttribute(Type editorWindowType, string id, string displayName, string ussName, bool defaultDisplay); 
## Declaration
public OverlayAttribute(Type editorWindowType, string id, string displayName, bool defaultDisplay); 
## Declaration
public OverlayAttribute(Type editorWindowType, string displayName, bool defaultDisplay); 
## Declaration
public OverlayAttribute(); 
### Parameters
Parameter | Description  
---|---  
id | Defines the unique identifier used to identify the overlay.  
ussName | Name of the overlay's root visual element.  
editorWindowType | Defines which EditorWindow type the overlay will be used in.  
displayName | Defines what the display name of the overlay will be.  
defaultDisplay | True if this [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) is enabled by default in new windows.  
### Description
Attribute used to register a class as an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html).
Overlays are not directly instantiated in code. The Editor will use reflection on startup to identify [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) classes with an [OverlayAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayAttribute.html) to populate the available Overlays in an Editor Window.
* * *
