* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.FocusWindowIfItsOpen.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).FocusWindowIfItsOpen
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
public static void FocusWindowIfItsOpen(Type t); 
### Parameters
Parameter | Description  
---|---  
windowType | The type of the window. Must derive from EditorWindow.  
### Description
Focuses the first found EditorWindow of specified type if it is open.
If there is no open window of such type, nothing happens.
* * *
## Declaration
public static void FocusWindowIfItsOpen(); 
### Parameters
Parameter | Description  
---|---  
T | The type of the window. Must derive from EditorWindow.  
### Description
Focuses the first found EditorWindow of type `T` if it is open.
If there is no open window of such type, nothing happens.
* * *
