* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.LicenseInformation.PurchaseApp.html

#  [LicenseInformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.LicenseInformation.html).PurchaseApp
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
public static string PurchaseApp(); 
### Returns
**string** Purchase receipt. 
### Description
Attempts to purchase the app if it is in installed in trial mode.
Calling this pops up a dialog for the user asking whether they want to buy the application. If the user buys the application, returns a valid purchase receipt string. Otherwise, returns an empty string.
```
using UnityEngine;
using UnityEngine.Windows;  
  
class MyMonoBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string m_Receipt;  
  
    void OnGUI()
    {
        if (LicenseInformation.isOnAppTrial[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.LicenseInformation-isOnAppTrial.html))
        {
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 40), "Buy full version"))
            {
                m_Receipt = LicenseInformation.PurchaseApp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.LicenseInformation.PurchaseApp.html)();
            }
        }
        else
        {
            GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 40), "You have full application version installed");
        }
    }
}

```

* * *
