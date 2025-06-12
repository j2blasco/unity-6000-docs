* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SaveModifiedScenesIfUserWantsTo.html

#  [EditorSceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.html).SaveModifiedScenesIfUserWantsTo
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
public static bool SaveModifiedScenesIfUserWantsTo(Scene[] scenes); 
### Parameters
Parameter | Description  
---|---  
scenes | Scenes that should be saved if they are modified.  
### Returns
**bool** Returns true if the user clicked **Save** or **Don't Save** to indicate that that it is ok to close the input scenes after the dialog closes. Returns false if the user clicked **Cancel** to abort. 
### Description
Asks whether the modfied input Scenes should be saved.
In some cases, you might want to call this before opening another Scene or creating a new Scene. A return value of true indicates that you may continue. A return value of false indicates that the user cancelled the operation and you should not Open another Scene.
* * *
