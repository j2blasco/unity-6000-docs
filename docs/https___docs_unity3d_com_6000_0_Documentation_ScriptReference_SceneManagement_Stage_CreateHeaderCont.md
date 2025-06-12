* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.CreateHeaderContent.html

#  [Stage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.html).CreateHeaderContent
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
protected [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) CreateHeaderContent(); 
### Returns
**GUIContent** The header content for this Stage. 
### Description
Creates the header content for this Stage. Both the Hierarchy window header and Scene view breadcrumb bar use this content.
Classes inheriting from Stage should implement this method and return a GUIContent with an appropriate icon and label for the Stage.  
  
The icon should match the icon for the type of object you can edit in this stage. The label should match the name of the object you can edit in this stage (excluding extention) or the type of editing operation that you can do in this stage.
* * *
