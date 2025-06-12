* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DrawWizardGUI.html

#  [ScriptableWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html).DrawWizardGUI
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
protected bool DrawWizardGUI(); 
### Returns
**bool** Returns true if any property has been modified. 
### Description
Will be called for drawing contents when the ScriptableWizard needs to update its GUI.
Derived class may override this function to provide customized behaviour for GUI drawing. The default behaviour is to draw property fields for all public properties on the wizard, arranged vertically.
* * *
