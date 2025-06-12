* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard-helpString.html

#  [ScriptableWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html).helpString
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
helpString; 
### Description
Allows you to set the help text of the wizard.
Additional resources: [ScriptableWizard.OnWizardUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.OnWizardUpdate.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/HelpString.png)  
_Help string on a ScriptableWizard window._
```
// Creates a simple Wizard window and prints the HelpString
// in the Wizard window.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class HelpString : ScriptableWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Show Help[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.html) String")]
    static void CreateWindow()
    {
        ScriptableWizard.DisplayWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DisplayWizard.html)("", typeof(HelpString), "Finish");
    }  
  
    void OnWizardUpdate()
    {
        helpString = "This string describes what the Scriptable Wizard does.";
    }
}

```

* * *
