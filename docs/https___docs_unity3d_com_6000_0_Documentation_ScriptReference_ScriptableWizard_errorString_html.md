* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard-errorString.html

#  [ScriptableWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html).errorString
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
errorString; 
### Description
Allows you to set the error text of the wizard.
Additional resources: [ScriptableWizard.OnWizardUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.OnWizardUpdate.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ErrorString.png)  
_Error String on a ScriptableWizard window._
```
// Creates a simple Wizard window and prints an error
// string until you set the number to 5  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ErrorString : ScriptableWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html)
{
    public int number = 0;
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Show Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html) String")]
    static void CreateWindow()
    {
        ScriptableWizard.DisplayWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DisplayWizard.html)("Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html) String example", typeof(ErrorString), "Close");
    }  
  
    void OnWizardUpdate()
    {
        helpString = "Set The number to 5";
        if (number != 5)
            errorString = "The number has to be set to 5!";
        else
            errorString = "";
    }
}

```

* * *
