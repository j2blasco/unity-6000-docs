* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard-isValid.html

#  [ScriptableWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html).isValid
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
isValid; 
### Description
Allows you to enable and disable the wizard create button, so that the user can not click it.
Additional resources: [ScriptableWizard.OnWizardUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.OnWizardUpdate.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/isValidScriptableWizard.png)  
_The finish button gets disabled until the user sets the number to 5._
```
// Asks the user to set the var "Number" to 5, if is not set to 5
// the "Finish" button will not be reachable  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class isValidScriptableWizard : ScriptableWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html)
{
    public int number = 0;
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Show isValid Usage")]
    static void CreateWindow()
    {
        ScriptableWizard.DisplayWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DisplayWizard.html)(
            "isValid boolean example",
            typeof(isValidScriptableWizard),
            "Finish");
    }  
  
    void OnWizardUpdate()
    {
        helpString = "Set The number to 5 and press finish";
        if (number != 5)
        {
            errorString = "The number has to be set to 5!";
            isValid = false;
        }
        else
        {
            errorString = "";
            isValid = true;
        }
    }
}

```

* * *
