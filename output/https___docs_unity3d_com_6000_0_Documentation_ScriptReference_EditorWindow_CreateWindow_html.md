* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateWindow.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).CreateWindow
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
public static T CreateWindow(params Type[] desiredDockNextTo); 
## Declaration
public static T CreateWindow(string title, params Type[] desiredDockNextTo); 
### Parameters
Parameter | Description  
---|---  
T | The type of the window. Must derive from EditorWindow.  
title | The title of the created window. If this value is null, use the class name as title.  
desiredDockNextTo | An array of EditorWindow types that the window will attempt to dock onto.  
### Description
Creates an EditorWindow of type `T`.
Creates and shows a new window and returns the instance of it.
* * *
