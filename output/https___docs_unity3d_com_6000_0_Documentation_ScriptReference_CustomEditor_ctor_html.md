* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor-ctor.html

# CustomEditor Constructor
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
public CustomEditor(Type inspectedType); 
## Declaration
public CustomEditor(Type inspectedType, bool editorForChildClasses); 
### Parameters
Parameter | Description  
---|---  
inspectedType | Type that this editor can edit.  
editorForChildClasses | If true, child classes of inspectedType will also show this editor. Defaults to false.  
### Description
Defines which object type the custom editor class can edit.
Additional resources: [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class.
* * *
