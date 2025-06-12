* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.GroupScope-ctor.html

# GUI.GroupScope Constructor
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
public GUI.GroupScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position); 
## Declaration
public GUI.GroupScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text); 
## Declaration
public GUI.GroupScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public GUI.GroupScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public GUI.GroupScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public GUI.GroupScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public GUI.GroupScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the group.  
text | Text to display on the group.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display on the group.  
content | Text, image and tooltip for this group. If supplied, any mouse clicks are "captured" by the group and not If left out, no background is rendered, and mouse clicks are passed.  
style | The style to use for the background.  
### Description
Create a new GroupScope and begin the corresponding group.
* * *
