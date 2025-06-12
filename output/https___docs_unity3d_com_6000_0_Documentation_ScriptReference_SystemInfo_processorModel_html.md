* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorModel.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).processorModel
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
processorModel; 
### Description
Specifies the model name of the processor in the user's device (Read Only).
With `SystemInfo.processorModel` and [SystemInfo.processorManufacturer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorManufacturer.html) values, you can categorize the devices running Unity applications to gather accurate performance metrics. You can use this data to test and optimize your application for improved performance.  
  
Returns `unknown` on WebGL platforms and IOS platforms platforms which don't support this property.  
  
Additional resources: [SystemInfo.processorManufacturer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorManufacturer.html)
```
using UnityEngine;
using TMPro;
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public TMP_Text DisplayText;
    private string _processorModel;  
  
    void Start()
    {
        _processorModel = SystemInfo.processorModel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorModel.html);
        DisplayText.text = _processorModel;
    }
}

```

* * *
