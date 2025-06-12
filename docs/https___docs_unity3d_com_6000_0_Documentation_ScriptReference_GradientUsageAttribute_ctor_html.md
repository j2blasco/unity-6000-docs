* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute-ctor.html

# GradientUsageAttribute Constructor
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
public GradientUsageAttribute(bool hdr); 
## Declaration
public GradientUsageAttribute(bool hdr, [ColorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorSpace.html) colorSpace); 
### Parameters
Parameter | Description  
---|---  
hdr | Set to true if the colors should be treated as HDR colors (default value: false).  
colorSpace | The colors should be treated as from this color space (default value: ColorSpace.Gamma).  
### Description
Attribute for gradient fields. Used to configure the GUI for the Gradient Editor.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Inspector editor for this gradient
    // allows to setup regular low dynamic range
    // colors.
    public Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) defaultGradient;  
  
    // Inspector editor for this gradient allows
    // to setup HDR colors.
    [GradientUsage(true)]
    public Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) hdrGradient;
}

```

* * *
