* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.TrTextContentWithIcon.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).TrTextContentWithIcon
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
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContentWithIcon(string text, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) icon); 
## Declaration
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContentWithIcon(string text, string iconName); 
## Declaration
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContentWithIcon(string text, string tooltip, string iconName); 
## Declaration
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContentWithIcon(string text, string tooltip, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) icon); 
## Declaration
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContentWithIcon(string text, string tooltip, [MessageType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MessageType.html) messageType); 
## Declaration
public static [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) TrTextContentWithIcon(string text, [MessageType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MessageType.html) messageType); 
### Parameters
Parameter | Description  
---|---  
text | The text associated with the [GUIContent.text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-text.html).  
icon | The icon associated with the [GUIContent.image](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-image.html).  
iconName | The name of the icon.  
tooltip | The tooltip to display when the cursor hovers over the icon.  
messageType | The type of the message to fetch the icon for.  
### Description
Gets the [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) from Unity built-in resources with the given information or creates a [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) for a GUI element.  
  
The text and the tooltip are localized and loaded with an icon.  
  
Typically, the icon from `Assets/Editor Default Resources/Icons` is fetched using the icon name. Only the name of the icon, without the .png extension is needed.  
  
If a message type is specified instead of an icon or an icon name, the [GUIContent.image](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-image.html) is the icon associated with that message type.
* * *
