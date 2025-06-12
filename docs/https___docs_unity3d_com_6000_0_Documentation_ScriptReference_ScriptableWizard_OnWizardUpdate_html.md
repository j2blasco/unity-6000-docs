* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.OnWizardUpdate.html

#  [ScriptableWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html).OnWizardUpdate()
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
### Description
This is called when the wizard is opened or whenever the user changes something in the wizard.
This allows you to set the [helpString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard-helpString.html), [errorString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard-errorString.html) and enable/disable the Create button via [isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard-isValid.html). Also it lets you change labels (for timers i.e.) or buttons when the wizard is being shown  
  
Additional resources: [ScriptableWizard.DisplayWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DisplayWizard.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/CloneObjects.png)  
_ScriptableWizard window for cloning a Game Object._
```
// Simple Wizard that clones an object several times.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Collections;  
  
public class CloneObjects : ScriptableWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) objectToCopy = null;
    public int numberOfCopies = 2;
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Clone objects")]
    static void CreateWindow()
    {
        // Creates the wizard for display
        ScriptableWizard.DisplayWizard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.DisplayWizard.html)("Clone an object.", typeof(CloneObjects), "Clone!");
    }  
  
    void OnWizardUpdate()
    {
        helpString = "Clones an object a number of times and move the cloned objects to the origin";
        if (!objectToCopy)
        {
            errorString = "Please assign an object";
            isValid = false;
        }
        else
        {
            errorString = "";
            isValid = true;
        }
    }  
  
    void OnWizardCreate()
    {
        for (int i = 0; i < numberOfCopies; i++)
            Instantiate(objectToCopy, Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
    }
}

```

* * *
