* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.EnsureUntitledSceneHasBeenSaved.html

#  [EditorSceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.html).EnsureUntitledSceneHasBeenSaved
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
public static bool EnsureUntitledSceneHasBeenSaved(string dialogContent); 
### Parameters
Parameter | Description  
---|---  
dialogContent | Text shown in the save dialog.  
### Returns
**bool** True if the Scene is saved or if there is no Untitled Scene. 
### Description
Shows a save dialog if an Untitled Scene exists in the current Scene manager setup.
Call this method if a process in your Editor code requires that the Untitled Scene is saved. If the user selects Cancel then the process can be aborted. Returns true if the Scene is saved or if there is no Untitled Scene. Returns false if the user cancels the save dialog.
* * *
