* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.SetTemporaryProjectKeepPath.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).SetTemporaryProjectKeepPath
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
public static void SetTemporaryProjectKeepPath(string path); 
### Parameters
Parameter | Description  
---|---  
path | The path that the current temporary project should be relocated to when closing it.  
### Description
Sets the path that Unity should store the current temporary project at, when the project is closed.
Usually, when the user closes a temporary project (by opening another project, or exiting Unity), they are prompted to keep the project by selecting a permanent location for it. If you pass a non-empty path to this function, the prompt will be bypassed and the temporary project will be automatically relocated to the provided path.  
  
It is an error to call this API if [EditorApplication.isTemporaryProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isTemporaryProject.html) is not true.
* * *
