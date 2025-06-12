* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HelpBox.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).HelpBox
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
public static void HelpBox(string message, [MessageType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MessageType.html) type); 
## Declaration
public static void HelpBox([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, bool wide); 
## Declaration
public static void HelpBox(string message, [MessageType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MessageType.html) type, bool wide); 
### Parameters
Parameter | Description  
---|---  
message | The message text.  
type | The type of message.  
wide | If true, the box will cover the whole width of the window; otherwise it will cover the controls part only.  
content | The message contents. If an image is provided, it will be displayed to the left of the message. The expect image size is 32x32 pixels.  
### Description
Make a help box with a message to the user.
* * *
