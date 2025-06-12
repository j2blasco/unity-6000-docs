* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.AreaScope-ctor.html

# GUILayout.AreaScope Constructor
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
public GUILayout.AreaScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect); 
## Declaration
public GUILayout.AreaScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, string text); 
## Declaration
public GUILayout.AreaScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public GUILayout.AreaScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public GUILayout.AreaScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public GUILayout.AreaScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public GUILayout.AreaScope([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
text | Optional text to display in the area.  
image | Optional texture to display in the area.  
content | Optional text, image and tooltip top display for this area.  
style | The style to use. If left out, the empty [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) ([GUIStyle.none](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-none.html)) is used, giving a transparent background.  
### Description
Create a new AreaScope and begin the corresponding Area.
* * *
