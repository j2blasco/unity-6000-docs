* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorManufacturer.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).processorManufacturer
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
processorManufacturer; 
### Description
Specifies the manufacturer name of the processor in the user's device (Read Only).
With `SystemInfo.processorManufacturer` and [SystemInfo.processorModel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorModel.html) values, you can categorize the devices running Unity applications to gather accurate performance metrics. You can use this data to test and optimize your application for improved performance.   
  
Returns `unknown` on WebGL platforms which don't support this property.  
  
Additional resources: [SystemInfo.processorModel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorModel.html)
```
using UnityEngine;
using TMPro;
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public TMP_Text DisplayText;
    private string _processorManufacturer;  
  
    void Start()
    {
        _processorManufacturer = SystemInfo.processorManufacturer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorManufacturer.html);
        DisplayText.text = _processorManufacturer;
    }
}

```

* * *
